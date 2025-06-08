FROM astrocrpublic.azurecr.io/runtime:3.0-2

RUN pip install dbt-postgres

RUN mkdir -p /home/astro/.dbt
COPY include/.dbt/profiles.yml /home/astro/.dbt/profiles.yml
