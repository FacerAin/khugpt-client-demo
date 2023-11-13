FROM python:3.11

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir -r /src/requirements.txt

COPY ./src /src/app

EXPOSE 1008

HEALTHCHECK CMD curl --fail http://localhost:1008/_stcore/health

ENTRYPOINT ["streamlit", "run", "app/app.py", "--server.port=1008", "--server.address=0.0.0.0"]
