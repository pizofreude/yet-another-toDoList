"""
Project Structures:
1. Create Database mysql
2. Create main.py: delete, update & mainloop()
3. Create addTask.py
"""

# 3. Create addTask.py

## Import necessary libraries
from tkinter import *
from tkinter import messagebox
import mysql.connector

## Define add database function
def add_db():
    
    global id
    global task
 
    tid = id.get()
    ttask = task.get()
    
    db = mysql.connector.connect(host = "localhost",
                                 user = "root",
                                 password = 'password',
                                 database='db')
    cursor = db.cursor()
 
    sqlquery = "insert into ToDoList values('" + tid + "','" + ttask + "','NO');"
    print(sqlquery)
 
    try:
        cursor.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success','Task added!')
    except:
        messagebox.showinfo('Error', 'Database Access Denied')

## Define add task function
def add():
 
    global id
    global task
    
    window = Tk()
    window.title("YaTL - Yet another ToDoList")
 
    greet = Label(window, font = ('arial 20'), text = "Add a Task!")
    greet.grid(row = 0, columnspan = 3)
 
    #----------id-------------------
    L = Label(window, font = ('arial 15 bold'), text = "Enter Task id: ")
    L.grid(row = 2, column = 1)
 
    L = Label(window, font = ('arial 15'), text = "   ")
    L.grid(row = 2, column = 2)
 
    id = Entry(window, width=5, font =('arial 15'))
    id.grid(row = 2, column = 3)
 
    #------------------task---------------------
 
    L = Label(window, font = ('arial 15 bold'), text = "Enter task: ")
    L.grid(row = 3, column = 1)
 
    L = Label(window, font = ('arial 15'), text = "   ")
    L.grid(row = 3, column = 2)
 
    task = Entry(window, width=5, font =('arial 15'))
    task.grid(row = 3, column = 3)
 
    submitbtn = Button(window, text="Submit", command=add_db, bg="#1E90FF", fg="white", font = ('arial 15 bold'))
    submitbtn.grid(row = 5, columnspan = 3)
        
    pass