import numpy as np
import pandas as pd
import s3fs

record_count = 100_000

fs = s3fs.S3FileSystem(
    anon=False,
    use_ssl=False,
    client_kwargs={
        'endpoint_url': 'http://localhost:9000/',
        'aws_access_key_id': 'minio',
        'aws_secret_access_key': 'minio1234',
        'verify': True,
    }
)

if not fs.isdir('iot'):
    fs.mkdir('iot')

for i in range(10):
    temperature = np.random.random(record_count) * 20 + 10
    pressure = (np.random.random(record_count) * 100 - 50 + 1013)
    df = pd.DataFrame({'temperature': temperature, 'pressure': pressure})
    filename = f'iot/measurements/iot-{i:02d}.parquet'
    print(filename)
    with fs.open(filename, 'wb') as stream:
        df.to_parquet(stream)
