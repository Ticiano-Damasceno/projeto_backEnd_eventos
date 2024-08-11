from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class Attendees(Base):
    __tablename__ = "tbl_attendees"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey('tbl_events.id'))
    create_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f'Attendees [name={Attendees.name}, email={Attendees.email}, event_id={Attendees.event_id}]'