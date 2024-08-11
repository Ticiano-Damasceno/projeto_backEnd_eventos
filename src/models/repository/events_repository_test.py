import pytest
from src.models.settings.connection import db_connection_handler  
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo registro em banco de dados')
def test_insert_event():
    event_random = {
        'uuid': 'meu-uuid-testando',
        'title': 'meu titulo',
        'slug': 'meu slug', 
        'maximum_attendees': 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event_random)
    print(response)

@pytest.mark.skip(reason="já testado e funcionou!")
def test_get_event_by_id():
    event_id = 'meu-uuid-testando12321'
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id=event_id)
    print(response)

