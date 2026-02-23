from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import ToDo  

router = APIRouter()


class ToDoCreate(BaseModel):
    title: str
    description: str
    completed: bool  


class ToDoResponse(ToDoCreate):
    id: int

    class Config:orm_mode = True 



@router.get('/get', response_model=List[ToDoResponse])
def show_todos(db: Session = Depends(get_db)):
    todos = db.query(ToDo).all()
    return todos  



@router.post("/create", response_model=ToDoResponse)
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    new_todo = ToDo(
        title = todo.title,description=todo.description,completed=todo.completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.put('/update/{todo_id}', response_model=ToDoResponse)
def update_todo(todo_id: int, todo: ToDoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")

    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.completed = todo.completed

    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete('/delete/{todo_id}')
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo Not Found")

    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
