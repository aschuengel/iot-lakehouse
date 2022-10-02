FROM amazoncorretto:11-alpine

ENV JAVA_HOME=/usr/lib/jvm/default-jvm
ENV HIVE_VERSION=3.1.3
ENV HADOOP_VERSION=3.3.4
ENV POSTGRESQL_VERSION=42.5.0
ENV HADOOP_HOME=/app/hadoop

WORKDIR /app
RUN wget https://repo1.maven.org/maven2/org/apache/hive/hive-standalone-metastore/${HIVE_VERSION}/hive-standalone-metastore-${HIVE_VERSION}-bin.tar.gz
RUN tar xzf hive-standalone-metastore-${HIVE_VERSION}-bin.tar.gz
RUN rm -f hive-standalone-metastore-${HIVE_VERSION}-bin.tar.gz
RUN ln -sf apache-hive-metastore-${HIVE_VERSION}-bin apache-hive-metastore-bin
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
RUN tar xzf hadoop-${HADOOP_VERSION}.tar.gz
RUN rm -f hadoop-${HADOOP_VERSION}.tar.gz
RUN ln -sf hadoop-${HADOOP_VERSION} hadoop
RUN apk update
RUN apk upgrade
RUN apk add bash
RUN wget https://repo1.maven.org/maven2/org/postgresql/postgresql/${POSTGRESQL_VERSION}/postgresql-${POSTGRESQL_VERSION}.jar 
RUN mv -f postgresql-${POSTGRESQL_VERSION}.jar /app/apache-hive-metastore-bin/lib/
RUN find /app/hadoop/ -name '*aws*.jar' -print -exec cp -fv {} /app/apache-hive-metastore-bin/lib/ \;
COPY metastore-site.xml /app/apache-hive-metastore-bin/conf/
COPY entrypoint.sh /app/

ENTRYPOINT [ "/bin/bash", "/app/entrypoint.sh" ]
