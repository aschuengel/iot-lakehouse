from datetime import datetime, timedelta
import math
from os import times
import random
import psycopg2
import uuid

# Connect to your postgres DB
with psycopg2.connect('dbname=iot user=iot password=iot12345 host=localhost') as connection:

    # Open a cursor to perform database operations
    with connection.cursor() as cursor:

        cursor.execute('''delete from measurements''')

        timestamp = datetime.now() - timedelta(days=7)

        while timestamp < datetime.now():
            phi = ((timestamp.hour - 8) / 12) * math.pi
            print(timestamp, phi)
            temperature = random.random() * 2 + 10 + math.sin(phi) * 5
            pressure = random.random() * 100 - 50 + 1013
            cursor.execute('''insert into measurements (id, timestamp, temperature, pressure) values (%s, %s, %s, %s)''',
                        (str(uuid.uuid4()), timestamp, temperature, pressure))
            timestamp = timestamp + timedelta(minutes=5)

