FROM python:3.11-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto donde corre FastAPI
EXPOSE 8000

# Comando para correr FastAPI
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
