FROM python:3.12-slim

WORKDIR /app
COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt

COPY . .

# Render define PORT; usamos env var para ser cloud-ready.
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]