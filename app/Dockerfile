FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir boto3
RUN apt-get update && apt-get install -y dnsutils curl
COPY . .
EXPOSE 3000
CMD ["python", "app.py"]