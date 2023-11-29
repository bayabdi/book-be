from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    duration = Column(Integer)
    reason = Column(String)
    start_time = Column(DateTime)
    status = Column(Integer)

    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship('User', back_populates='appointments')
