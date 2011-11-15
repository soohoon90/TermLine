drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title string not null,
  text string not null
);

drop table if exists jsons;
create tables jsons (
  id integer primary key autoincrement,
  text string not null
);

