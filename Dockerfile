FROM python:3.6.10-slim

WORKDIR /app

COPY . .

CMD ["python", "app.py"]  