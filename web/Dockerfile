FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt /app

RUN python -m venv /opt/venv
ENV PATH="opt/venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /app

EXPOSE 8007


ENTRYPOINT ["sh","/app/entrypoint.sh"]