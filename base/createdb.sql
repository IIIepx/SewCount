
create table users(
  id integer primary key,
  name varchar(255) not null,
);

create table projects(
  id integer primary key autoincrement,
  name varchar(255) unique
  user integer not null,
  FOREIGN KEY(user) REFERENCES users(id)
);

create table stages(
  id integer primary key autoincrement,
  name varchar(255)
  project integer not null,
  FOREIGN KEY(project) REFERENCES projects(id),
);

create table timerecords(
  id integer primary key autoincrement,
  user integer not null,
  project integer not null,
  hours varchar(8)
  FOREIGN KEY(user) REFERENCES users(id)
  FOREIGN KEY(project) REFERENCES projects(id),
)
