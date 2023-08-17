FROM python:3.10-slim

RUN mkdir /osa_expert_bot

COPY requirements.txt /osa_expert_bot/

RUN python -m pip install -r /osa_expert_bot/requirements.txt

COPY . /osa_expert_bot/

WORKDIR /osa_expert_bot

RUN ["python", "bot_authorization.py"]

ENTRYPOINT ["python", "main.py"]
