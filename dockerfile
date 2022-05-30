FROM python:3.9

COPY requirements.txt .

WORKDIR .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]