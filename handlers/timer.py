import logging
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, Router, types
from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from base import projects, time

logger = logging.getLogger("__name__")
rt = Router()


class TimerState(StatesGroup):
    timer_on = State()


@rt.message(TimerState.timer_on, F.text.lower() == "старт")
async def restart_timer(msg: types.Message, state: FSMContext):
    await stop_timer(msg, state)
    await start_timer(msg, state)


@rt.message(F.text.lower() == "старт")
async def start_timer(msg: types.Message, state: FSMContext):
    _state = await state.get_state()
    if _state:
        await state_warning(msg, _state) 
        return
    project, stage = projects.get_project(msg.from_user.id)
    if not project:
        await msg.answer("Ошибка! Текущий проект не выбран")
        return
    await state.set_state(TimerState.timer_on)
    await state.set_data({"time": datetime.now()})
    await msg.answer(f"Таймер запущен\nТекущий проект - {project}\nЭтап - {stage}")


@rt.message(TimerState.timer_on, F.text.lower() == "стоп")
async def stop_timer(msg: types.Message, state: FSMContext):
    delta_time = datetime.now() - (await state.get_data())["time"]
    await state.clear()
    seconds = time.save_time(msg.from_user.id, delta_time)
    project, stage = projects.get_project(msg.from_user.id)
    await msg.answer(
        f"Таймер остановлен.   {str(delta_time).split('.')[0]}\n"
        f"Текущий проект - {project}\nЭтап - {stage}\n"
        f"Суммарное время - {str(timedelta(seconds = int(seconds)))}"
    )


@rt.message(TimerState.timer_on, F.text.lower() == "отмена")
async def cancel_timer(msg: types.Message, state: FSMContext):
    delta_time = datetime.now() - (await state.get_data())["time"]
    await state.clear()
    project, stage = projects.get_project(msg.from_user.id)
    await msg.answer(
        f"Таймер отменен.  {str(delta_time).split('.')[0]}\nТекущий проект - {project}\nЭтап - {stage}"
    )


@rt.message((F.text.lower() == "стоп") | (F.text.lower() == "отмена"))
async def wrong_timer(msg: types.Message):
    await msg.answer("Ошибка! Таймер не был запущен.")


async def state_warning(msg: types.Message, state: str):
    match state:
        case "ChoiceState:project":
            await msg.answer("Ошибка! Завершите выбор проекта")
        case "ChoiceState:stage":
            await msg.answer("Ошибка! Завершите выбор этапа")
