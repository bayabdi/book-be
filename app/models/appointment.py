from app.db.base_class import Base
from sqlalchemy import Column, Integer, String


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    duration = Column(Integer)
    reason = Column(String)
    status = Column(Integer)
