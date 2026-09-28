from datetime import date

from sqlalchemy import String,Date
from sqlalchemy.orm import Mapped,mapped_column

from model import Base

class Task(Base):
    __tablename__="tasks"

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(255))
    description:Mapped[str]=mapped_column(String(1000))
    status:Mapped[str]=mapped_column(String(50))
    due_date:Mapped[date]=mapped_column(Date)

