from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.schema import TaskCreate,TaskOut,TaskUpdate
from models.task import Task
from sqlalchemy import select
router=APIRouter()

@router.post("/tasks",response_model=TaskOut,status_code=201)
def create_task(task:TaskCreate,db:Session=Depends(get_db)):

    new_task=Task(
        title=task.title,
        description=task.description,
        status=task.status,
        due_date=task.due_date

    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/tasks",response_model=list[TaskOut])
def get_tasks(db:Session=Depends(get_db)):
    result=db.execute(select(Task))
    tasks=result.scalars().all()

    return tasks

@router.get("/tasks/{task_id}",response_model=TaskOut)
def getby_id(task_id:int,db:Session=Depends(get_db)):
    result=db.execute(
        select(Task).where(Task.id == task_id)
    )
    task=result.scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404,detail="Not found")

    return task

@router.put("/tasks/{task_id}",response_model=TaskOut)
def update_task(
    task_id:int,
    task_data:TaskUpdate,
    db:Session=Depends(get_db)
):
    result=db.execute(select(Task).where(Task.id == task_id))
    task=result.scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404,detail="Not foumd")

    update_data=task_data.model_dump(exclude_unset=True)

    for field,value in update_data.items():
        setattr(task,field,value)

    db.commit()
    db.refresh(task)

    return task


@router.delete("/tasks/{task_id}",status_code=204)
def del_task(task_id:int,db:Session=Depends(get_db)):
    result=db.execute(select(Task).where(Task.id==task_id))
    task=result.scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404,detail="Not found")
    db.delete(task)
    db.commit()
