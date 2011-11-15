drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    title string not null,
    text string not null
);

drop table if exists jsons;
create table jsons (
    id integer primary key autoincrement,
    text string not null
);

drop table if exists images;
create table images (
    id integer primary key autoincrement,
    title string not null,
    text string not null,
    tag string not null,
    image blob not null
);

drop table if exists users;
create table users (
    uid integer primary key autoincrement,
    username string not null,
    password string not null
);

insert into users (username, password) values (admin, admin);

