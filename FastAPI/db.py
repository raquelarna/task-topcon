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
    curs = conn.cursor()
    return conn, curs

def create_todo(con, cur, task_dct):
    sql_insert ="INSERT INTO public.todos (message, label_id, dueDate) VALUES('" + str(task_dct["message"]) + "','" + str(task_dct["label"]) + "','" + str(task_dct["dueDate"]) + "');"
    cur.execute(sql_insert)
    con.commit()


def update_todo(con, cur, task_dct):
    sql_update ="UPDATE public.todos set message ='" + str(task_dct["message"]) + "', label_id = '" + str(task_dct["label"]) + "', dueDate = '" + str(task_dct["dueDate"])  + "' WHERE id_todo = " + str(task_dct["id"]) +" ;"
    cur.execute(sql_update)
    con.commit()

def delete_todo(con, cur, id_task):
    sql_delete ="DELETE FROM public.todos where id_todo = " + str(id_task) + ";"
    cur.execute(sql_delete)
    con.commit()
        
def select_todo(cur):
    try:
        cur.execute("SELECT * FROM public.todos;")
        results = cur.fetchall()
        return results
    except:
        print("I can't select the data")

def select_only_one_todo(cur, id_todo):
    try:
        sql_select ="SELECT * FROM public.todos where id_todo = " + str(id_todo) + ";"
        cur.execute(sql_select)
        results = cur.fetchall()
        return results
    except:
        print("I can't select the data")