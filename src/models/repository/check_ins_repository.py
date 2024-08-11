from sqlalchemy.exc import IntegrityError
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns

class CheckInRepository:
    def insert_check_in(self, attendee_id):
        with db_connection_handler as database:
            try:
                check_in = CheckIns(attendee_id = attendee_id)
                database.session.add(check_in)
                database.session.commit()

                return attendee_id
            
            except IntegrityError:
                raise Exception('Check In já cadastrado.')

            except Exception as exception:
                database.session.rollback()
                raise exception