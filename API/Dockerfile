FROM python:3.6-slim

COPY . /app

RUN apt-get update
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

ENV PYTHONPATH "${PYTONPATH}:/app/TwitterData"

CMD ["python", "/app/API/api.py"]
