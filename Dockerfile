
FROM python:3.9-slim

WORKDIR /app


RUN apt-get update \
    && apt-get install -y postgresql-server-dev-all gcc \
    && which pg_config \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "FMS.wsgi:application", "--bind", "0.0.0.0:8000"]