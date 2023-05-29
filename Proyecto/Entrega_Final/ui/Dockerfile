FROM python:3.9
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install psycopg2 mlflow awscli boto3
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

