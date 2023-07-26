from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import request
import db
 
 #Instancionamos fastapi
app = FastAPI()


# entidad user
# El base model da la capacidad de crear una entidad
class Todo(BaseModel):
    id: int
    message: str
    label: str
    dueDate: str


tasks_list = [Todo(id=1, message="Brais", label="Moure", dueDate="22"),
              Todo(id=2, message="oli", label="caracoli", dueDate="15")]


db.connect_db()

# Para obtener un listado de todas las labels
@app.get("/labels")
async def labels():
    labels_list = request.request_labels()
    return labels_list


# Para obtener una label en concreto
@app.get("/labels/{id}")
async def labels(id: str):
    labels_list = request.request_one_label(id)
    return labels_list

#Para hacer el get de los TODOS
@app.get("/tasks")
async def tasks():
    #Hacer conexion a la BD y devolver la lista de todos los TODOS
    return tasks_list

#Para hacer el get de un Todo
@app.get("/task/{id}")
async def task(id: int):
    return search_task(id)


#añadir todos
@app.post("/task/", response_model=Todo, status_code=201)
async def task(task: Todo):
    if type(search_task(task.id)) == Todo:
        raise HTTPException(status_code=404, detail="El Todo ya existe")
    else:
        tasks_list.append(task)
        return task


#Actualizar labels
@app.put("/task/")
async def task(task: Todo):

    found =  False

    for index, saved_task in enumerate(tasks_list):
        if saved_task.id == task.id:
            tasks_list[index] = task
            found = True
    if not found:
        return {"error":"No se ha actualizado el Todo"}
    else:
        return task


#Borramos labels
@app.delete("/task/{id}")
async def task(id: int):

    found = False

    for index, saved_task in enumerate(tasks_list):
        if saved_task.id == id:
            del tasks_list[index] 
            found = True
    if not found:
        return {"error": "No se ha eliminado el Todo"}


def search_task(id: int):
    tasks = filter(lambda task: task.id == id, tasks_list)
    try:
        return list(tasks)[0]
    except:
        return {"error": "No se ha encontrado el Todo"}
    



    









# Inicia el servidor con: uvicorn users:app --reload