## FastAPI, SQLAlchemy 2, aio_pika, RabbitMQ boilerplate

### Features:

1. [x] _Project fully async_
2. [x] _SqlAlchemy async session_
3. [x] _docker-compose and Dockerfiles_
4. [x] _`RabbitConnection` class. Path: `src/config/rabbit_connection_py`_
5. [x] _Base logging configuration_
6. [x] _FastAPI Cors base configuration_
7. [x] _FastAPI lifespan feature_
8. [x] _Poetry package manager_
9. [x] _Used hypercorn_
10. [x] _Configurated default BaseSettings instance_


### Dependencies:

```python
python = "^3.11"
fastapi = "^0.95.0"
hypercorn = "^0.14.3"
aio-pika = "^9.0.5"
sqlalchemy = "^2.0.8"
asyncpg = "^0.27.0"
```

### Setup

1. _Install Docker if not installed_
2. _Rename `.env.dev-example` to `.env.dev`_
3. _Run `docker compose up -d --build` command_
4. _Open `http://localhost:8000/docs` in your browser_


### Tips:

* Logs you can find by path `src/logs`
* Also you can run command `docker compose logs` to check logs
* You can disable logging to the files by removing/commenting this code in the `consumer.py` and `main.py`:
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("logs/fastapi.log"),
        logging.StreamHandler()
    ]
)
```
