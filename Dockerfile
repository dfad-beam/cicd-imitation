FROM alpine:latest
COPY motd /etc/
RUN cat /etc/passwd
ENTRYPOINT sleep 900
