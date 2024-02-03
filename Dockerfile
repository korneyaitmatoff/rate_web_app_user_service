FROM python:3.11

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./src/ ./src/
COPY ./config.py ./config.py

ENV DB_USER=tavern
ENV DB_PASSWORD=tavern
ENV DB_HOST=45.9.43.40
ENV DB_PORT=5432
ENV DB_NAME=app
ENV API_HOST=http://127.0.0.1
ENV API_PORT=8080

CMD ["uvicorn", "src:server", "--port", "8080"]