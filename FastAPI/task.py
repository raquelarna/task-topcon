from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import request
import db
import json
 
 #Instancionamos fastapi
app = FastAPI()

# entidad todo
# El basemodel da la capacidad de crear una entidad
class Todo(BaseModel):
    id: int
    message: str
    label: str
    dueDate: str


# cursor = db.connect_db()
# task_list = db.select_only_one_todo(cursor, 1)
# res_todo = [Todo(id=task_list[0][0], message=str(task_list[0][1]), label=str(task_list[0][2]), dueDate=str(task_list[0][3]))]


# tasks_list = [Todo(id=1, message="Brais", label="Moure", dueDate="22"),Todo(id=2, message="oli", label="caracoli", dueDate="15")]

#Conexion a la bd
con, cur = db.connect_db()

# Para obtener un listado de todas las labels
@app.get("/labels")
async def labels():
    labels_list = request.request_labels()
    return labels_list


# Para obtener una label en concreto
@app.get("/label/{id}")
async def labels(id: str):
    labels_list = request.request_one_label(id)
    return labels_list

#Obtener todos los todo de la bd
@app.get("/tasks")
async def tasks():
    task_list = db.select_todo(cur)
    todo_res= []
    for res in task_list:
        res_json = Todo(id=res[0], message=str(res[1]), label=str(res[2]), dueDate=str(res[3]))
        todo_res.append(res_json)
    return todo_res

#Obtener un Todo de la bd pr el id
@app.get("/task/{id}")
async def task(id: str):
    task_list = db.select_only_one_todo(cur, id)
    res_todo = [Todo(id=task_list[0][0], message=str(task_list[0][1]), label=str(task_list[0][2]), dueDate=str(task_list[0][3]))]
    return res_todo


#añadir un todo a la bd
@app.post("/task/", response_model=Todo, status_code=201)
async def task(task: Todo):
    task_dict = dict(task)
    db.create_todo(con, cur, task_dict)
    return task


#Actualizar todo de la bd
@app.put("/task/")
async def task(task: Todo):
    task_dict = dict(task)
    db.update_todo(con, cur, task_dict)
    return task


#Borrar todo de la bd
@app.delete("/task/{id}")
async def task(id: int):
    db.delete_todo(con, cur, id)
    return task
