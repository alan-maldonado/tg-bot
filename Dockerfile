# Imagen base ligera
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Variable de entorno del token
ENV BOT_TOKEN=""

# Comando para ejecutar el bot
CMD ["python", "bot.py"]

