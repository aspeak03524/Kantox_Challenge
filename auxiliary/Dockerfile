FROM python:3.9-slim-buster
WORKDIR /Auxiliary
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir boto3
COPY . .
CMD ["python", "background.py"]
EXPOSE 4000