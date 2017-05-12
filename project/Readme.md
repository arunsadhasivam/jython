pip install -r requirements.txt

db creation:
=============

create database
================
C:\softwares\sqllite>sqlite3 db/emp1.db,test,test
SQLite version 3.18.0 2017-03-28 18:48:43
Enter ".help" for usage hints.
sqlite> .open db/emp1.db
sqlite>

C:\softwares\sqllite>sqlite3 db/emp.db
SQLite version 3.18.0 2017-03-28 18:48:43
Enter ".help" for usage hints.
sqlite> show databases;
Error: near "show": syntax error
sqlite> .databases
main: C:\softwares\sqllite\db\emp.db
sqlite> use emp
   ...> ;
Error: near "use": syntax error
sqlite> create table employee(empid varchar(10), name varchar(30),
ar(50));
sqlite> insert into employee values('Arun','100','wipro');
