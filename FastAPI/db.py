# import the PostgreSQL client for Python

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


""" 
def create_db():
    # Connect to PostgreSQL 
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost', port='5432')
    cur = conn.cursor()

    cur.execute("CREATE TABLE todo (id_todo serial PRIMARY KEY, message varchar, label_id varchar, dueDate timestamp);")

    print("I can't create the todo table")

    conn.commit() # <--- makes sure the change is shown in the database
    conn.close()
    cur.close() """


def connect_db():
    try:
         conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "localhost", port = "5432")
    except:
        print("I am unable to connect to the database")
    cur = conn.cursor()
    return conn, cur

def create_todo(task):
    cur = connect_db()
    try:
        sql_insert ="INSERT INTO public.todo (message, label_id, dueDate) VALUES(%s, %s, %s);"
        cur.execute(sql_insert, (task))
    except:
        print("I can't insert the data")

def update_todo(task):
    cur = connect_db()
    try:
        sql_update =''
        cur.execute("UPDATE public.todo  set message = , label_id = , dueDate = ;")
    except:
        print("I can't update the data")

def delete_todo(task):
    cur = connect_db()
    try:
        sql_delete =''
        cur.execute("DELETE FROM public.todo where id_todo = ;")
    except:
        print("I can't update the data")
        
def select_todo(task):
    cur = connect_db()
    try:
        cur.execute("SELECT * FROM public.todo;")
    except:
        print("I can't select the data")

def select_only_one_todo(task):
    cur = connect_db()
    try:
        sql_select =''
        cur.execute("SELECT * FROM public.todo where id_todo =;")
    except:
        print("I can't select the data")