
para correr el codigo: 
```docker-compose up --build```

para hacer migraciones: 
```docker exec -it pabellones_api alembic revision --autogenerate -m "nombre"```

para correr migraciones: 
```docker exec -it pabellones_api alembic upgrade head```
