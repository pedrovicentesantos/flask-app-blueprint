FROM python:alpine

WORKDIR /app
ENV PYTHONPATH=/app
COPY requirements.txt ./
RUN pip install -r requirements.txt && mkdir log
COPY . .
COPY .env* ./

CMD ["python3",  "app/app.py"]
