# yet-another-toDoList

This is yet again another to-do list (YaTL) built with Python (3.11).

Installation of a SQL Database is a must. Any SQL software will do. In this project, [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) is applied.

## To-do List Features

- Add a task
- Delete a task
- Mark a task Complete
- Display all tasks

## Necessary Libraries

1. tkinter - `pip install tkinter`
2. mysql connector - `pip install mysql-connector-python`

### Project Structures:

1. Create Database via MySQL Command Line Client

   ```sql
    create database db;
 
    use db;
 
    create table ToDoList(
       id varchar(10),
       task varchar(100),
       status varchar(5));
    
    
    desc ToDoList;
   ```

   Output:

   ```sql
   Enter password: XXXXXXXXXXXXXXXXXX
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 8
   Server version: 8.0.31 MySQL Community Server - GPL

   Copyright (c) 2000, 2022, Oracle and/or its affiliates.

   Oracle is a registered trademark of Oracle Corporation and/or its
   affiliates. Other names may be trademarks of their respective
   owners.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   mysql> create database db;
   Query OK, 1 row affected (0.01 sec)

   mysql> use db;
   Database changed
   mysql> create table ToDoList(
       -> id varchar(10),
       -> task varchar(100),
       -> status varchar(5));
   Query OK, 0 rows affected (0.06 sec)

   mysql> desc ToDoList;
   +--------+--------------+------+-----+---------+-------+
   | Field  | Type         | Null | Key | Default | Extra |
   +--------+--------------+------+-----+---------+-------+
   | id     | varchar(10)  | YES  |     | NULL    |       |
   | task   | varchar(100) | YES  |     | NULL    |       |
   | status | varchar(5)   | YES  |     | NULL    |       |
   +--------+--------------+------+-----+---------+-------+
   3 rows in set (0.03 sec)
   ```

   These three attributes describes a task:
   - id: Acts as a primary key.
   - task: Description of task.
   - status: Indicates the task completion.

2. Create main.py: delete, update & mainloop()

3. Create addTask.py

## Bug

1. Auto-refresh window after each task still not yet solved. E.g.: adding new task will prompted as successfully but will not shown immediately. It will be shown after closing and restarting the main.py

## Contributing

Feel free to fork, git clone, git checkout -b feature-name, modify & battletesting, git remote add upstream, git push origin main and finally create pull request.
