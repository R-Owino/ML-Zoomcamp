FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

COPY ["Q5.py", "./"]

EXPOSE 4545

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:4545", "Q5:app"]
