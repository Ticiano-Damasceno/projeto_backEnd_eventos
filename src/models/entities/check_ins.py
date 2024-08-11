from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = 'tbl_check_ins'

    id = Column(String, primary_key=True)
    create_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey('tbl_attendees.id'))
    
    def __repr__(self):
        return f'CheckIns [attendeeId={CheckIns.attendeeId}]'