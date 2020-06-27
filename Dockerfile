FROM python:3.8

WORKDIR /app

RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml /app
COPY boilerplateapp/ /app/boilerplateapp
COPY app.py /app

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-ansi

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=5000"]
