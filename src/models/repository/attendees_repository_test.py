import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo registro em banco de dados')
def test_insert_attendees():
    event_id = 'meu-uuid-testando'
    attendee_info = {
        'uuid': 'meu-uuid-attendee',
        'name': 'attendee_avulso',
        'email': 'email@atendee.com',
        'event_id': event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendees(attendee_info)
    print(response)

@pytest.mark.skip(reason='já testado e funcionou!')
def test_get_attendee_badge_by_id():
    attendee_id = 'meu-uuid-attendee'
    attendee_repository = AttendeesRepository()
    attendee = attendee_repository.get_attendee_badge_by_id(attendee_id)

    print(attendee)