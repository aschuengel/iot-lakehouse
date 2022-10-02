#!/bin/bash
/app/apache-hive-metastore-bin/bin/schematool -dbType postgres -initSchema --verbose
/app/apache-hive-metastore-bin/bin/start-metastore --verbose
# EOF