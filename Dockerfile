FROM alpine:3.18
COPY motd /etc/
RUN addgroup -S admin && adduser -S admin -G admin
RUN cat /etc/passwd
USER admin
ENTRYPOINT sleep 900
