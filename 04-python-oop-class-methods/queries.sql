-- SQLite
-- create table contact_info (
--   id INTEGER PRIMARY KEY,
--   phone varchar(25),
--   employeeId INTEGER NOT NULL,
--   FOREIGN KEY (employeeId) REFERENCES employees(EmployeeId)
-- );

-- insert into contact_info (phone, employeeId)
-- VALUES
-- ('555-555-5555', 1);

-- one-to-one
-- select FirstName, LastName, contact_info.phone
-- from employees
-- JOIN contact_info 
--   on employees.EmployeeId = contact_info.employeeId
-- ;

-- one-to-many
-- select *
-- from albums
-- join artists on artists.ArtistId = albums.ArtistId
-- order by artists.Name
-- ;

-- many-to-many
create table bars (
  id integer PRIMARY key,
  name varchar (25)
);

create table drinks (
  id integer PRIMARY key,
  name varchar(25)
)
;

create table bars_drinks (
  id integer PRIMARY key,
  barId integer not null,
  drinkId integer not NULL,
  FOREIGN KEY (barId) REFERENCES bars(id),
  FOREIGN KEY (drinkId) REFERENCES drinks(id)
);

insert into bars (name)
values ("white horse"), ("my bar");

insert into drinks (name)
values ("whiskey"), ("gin");

insert into bars_drinks (barId, drinkId)
VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2);


-- many-to-many
select *
from bars
join bars_drinks on bars.id = bars_drinks.barId
join drinks on drinks.id = bars_drinks.drinkId
;