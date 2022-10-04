docker compose exec superset superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin

docker compose exec superset superset db upgrade    

docker compose exec superset superset load_examples

docker compose exec superset superset init

docker compose exec superset pip install trino