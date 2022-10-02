from multiprocessing import connection
from trino.dbapi import connect

connection = connect(
    host='localhost',
    port=8080,
    user='trino',
    catalog='hive',
    schema='default'
)
cursor = connection.cursor()
cursor.execute('drop table if exists hive.default.iot')
cursor.execute("""create table hive.default.iot (
    temperature double precision,
    pressure double precision)
with (
    format = 'parquet',
    external_location = 's3a://iot/measurements/'
)""")
cursor.execute('select * from hive.default.iot limit 10')
print(cursor.fetchall())
cursor.execute('show tables')
print(cursor.fetchall())
cursor.execute('describe iot')
print(cursor.fetchall())
cursor.close()
connection.close()