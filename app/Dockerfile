FROM python:3.9

WORKDIR /

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

WORKDIR /usr/src/app/api_biblioteca

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]