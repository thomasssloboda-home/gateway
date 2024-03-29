FROM python:3.11.7
WORKDIR /app
COPY ./src /app
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
