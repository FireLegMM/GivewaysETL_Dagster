FROM postgres:latest

ENV POSTGRES_USER=dagster
ENV POSTGRES_PASSWORD=dagster
ENV POSTGRES_DB=dagster

COPY ./Docker/init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

# Start the PostgreSQL service
CMD ["postgres"]