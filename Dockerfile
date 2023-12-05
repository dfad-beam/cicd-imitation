FROM alpine:latest
COPY motd /etc/
RUN useradd admin
RUN cat /etc/passwd
USER admin
ENTRYPOINT sleep 900
