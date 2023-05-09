FROM python:3.10.9


WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app

ENV POSTGRES_USER=dagster
ENV POSTGRES_PASSWORD=dagster
ENV POSTGRES_DB=dagster
ENV POSTGRES_HOST=postgres
ENV POSTGRES_PORT=5432

COPY dagster.yaml ./dagster.yaml
COPY requirements.txt ./requirements.txt
COPY Giveways ./Giveways
COPY Giveways_tests ./Giveways_tests
COPY workspace.yaml ./workspace.yaml

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt


CMD ["sh","-c","dagster dev -h 0.0.0.0 -p 3000"]

EXPOSE 3000