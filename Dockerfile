FROM python:3.8-alpine

WORKDIR /dockermonitor

COPY . .

RUN pip install -r documentation/requirements.txt

CMD ["python3", "src/main.py"]
