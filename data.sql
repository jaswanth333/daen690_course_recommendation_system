create database student_course_data;
use student_course_data;


create table sc_data(
   student_name varchar(100),
   course_name varchar(200),
   nationality varchar(100),
   school varchar(100),
   gender varchar(100),
   age varchar(200),
   modes_of_learning varchar(200),
   session int,
   field_of_interest varchar(100),
   difficulty_level varchar(200),
   course_recommended varchar(200),
   course_rating int );   
   
   
describe sc_data;
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/student_course_data.csv'
INTO TABLE sc_data 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from sc_data;
