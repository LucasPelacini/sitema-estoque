FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["fastapi", "dev", "main.py", "--port", "80", "--host", "0.0.0.0"]