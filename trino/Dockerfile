FROM azul/zulu-openjdk-alpine:17-jre-headless-latest
WORKDIR /app
ENV TRINO_VERSION=398
RUN wget https://repo1.maven.org/maven2/io/trino/trino-server/${TRINO_VERSION}/trino-server-${TRINO_VERSION}.tar.gz
RUN tar xzvf trino-server-${TRINO_VERSION}.tar.gz
RUN rm -f trino-server-${TRINO_VERSION}.tar.gz
RUN ln -sf trino-server-${TRINO_VERSION} trino-server
RUN apk update
RUN apk upgrade
RUN apk add python3
RUN ln -sf /usr/bin/python3 /usr/bin/python
COPY config.properties /app/trino-server/etc/
COPY node.properties /app/trino-server/etc/
COPY jvm.config /app/trino-server/etc/
COPY hive.properties /app/trino-server/etc/catalog/
COPY postgresql.properties /app/trino-server/etc/catalog/

ENTRYPOINT [ "/app/trino-server/bin/launcher", "run" ]