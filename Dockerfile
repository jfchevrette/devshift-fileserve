FROM centos:7

COPY fileserve.py /

ENTRYPOINT ["/fileserve.py"]
CMD ["/etc/motd"]

