# event-driven-example
Demo de arquitectura basada en eventos usando Docker Compose y Redis

# Event-Driven Architecture Demo

Este proyecto demuestra una arquitectura basada en eventos usando Docker, Redis y Python. Incluye un **Producer** que publica eventos en un canal de Redis y dos servicios (**Notification** y **Logistics**) que procesan los eventos.

## Requisitos

- Docker y Docker Compose instalados en tu máquina.
- Python 3.9+ si deseas ejecutar los servicios manualmente.

## Configuración

1. Clona este repositorio:
   ```bash

   git clone https://github.com/<TU-USUARIO>/event-driven-example.git
   cd event-driven-example

2. Levanta los contenedores usando Docker Compose:

bash
Copiar
Editar
docker compose up --build

3. Verifica que los servicios estén funcionando:

Logs del Producer:
bash
Copiar
Editar
docker compose logs -f producer

Logs del Notification Service:
bash
Copiar
Editar
docker compose logs -f notification

Logs del Logistics Service:
bash
Copiar
Editar
docker compose logs -f logistics