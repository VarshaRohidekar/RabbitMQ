FROM python:3.9

WORKDIR /CC Project

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "producer.py"]