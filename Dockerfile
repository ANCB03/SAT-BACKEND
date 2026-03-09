# Usamos slim-bullseye: estable, ligero y compatible con la mayoría de librerías
FROM python:3.9-slim-bullseye

# Evitamos archivos .pyc y aseguramos logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Definimos el path para que Python encuentre tu carpeta src
ENV PYTHONPATH=/app/src

WORKDIR /app

# Dependencias mínimas del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario para no correr como root (Seguridad)
RUN useradd -ms /bin/bash appuser

# Instalación de librerías (Copiamos solo requirements primero para usar caché)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de la app
COPY . .

# Ajustamos permisos para el usuario
RUN chown -R appuser:appuser /app

USER appuser

# Puerto de escucha
EXPOSE 8080

# Entramos a la carpeta src para ejecutar la app
WORKDIR /app/src

# Comando para producción con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]