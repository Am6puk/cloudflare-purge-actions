FROM python:3.11.0-alpine

RUN pip3 install requests

COPY app.py /app/app.py
ENTRYPOINT ["python", "/app/app.py"]