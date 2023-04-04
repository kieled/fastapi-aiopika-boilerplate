from fastapi import APIRouter

from config import rabbit_connection

test_router = APIRouter(prefix='/test', tags=['Test routes'])


@test_router.get('/')
async def process():
    message = {
        'type': 'test_message',
        'message': 'Test message text'
    }
    await rabbit_connection.send_messages(
        messages=message
    )
