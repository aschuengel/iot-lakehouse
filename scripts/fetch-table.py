from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text
from pprint import pprint

engine = create_engine('trino://trino@localhost:8080/hive/default')
connection = engine.connect()

rows = connection.execute(text('select  * from iot limit 10')).mappings().all()
pprint(rows)

rows = connection.execute(text(
    'select max(temperature) as max, min(temperature) as min, avg(temperature) as average from iot')).mappings().one()
pprint(rows)
