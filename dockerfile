FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt requirements.txt

ENV telegram_token 5285906181:AAFyBecEjJV9_Y802Gvtk9boTuZ2UzKREUc

RUN python3 -m venv venv
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN source /app/venv/bin/activate
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . .

CMD ["python3", "bot_telegram.py"]

