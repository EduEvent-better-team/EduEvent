# Używamy oficjalnego obrazu Pythona
FROM python:3.11-slim

# Wyłączamy buforowanie wyjścia konsoli w Pythonie
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Ustawiamy katalog roboczy
WORKDIR /app

# Instalujemy zależności systemowe dla PostgreSQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Kopiujemy z głównego katalogu listę wymagań i instalujemy paczki
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Kopiujemy całą zawartość głównego katalogu do /app/ w kontenerze
COPY . /app/

# Ustawiamy Python PATH, aby Django poprawnie widziało folder backend
ENV PYTHONPATH=/app/backend:$PYTHONPATH
