# Usa una imagen base de Python
FROM python:3.9-slim

# Instala redis-py
RUN pip install redis

# Copia el código fuente al contenedor
WORKDIR /app
COPY . /app

# Define el comando por defecto
CMD ["python", "producer.py"]