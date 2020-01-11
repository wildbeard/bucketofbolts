# Bucket of Bolts API

* Flask
* MySql 8

# Docker

Could not mount a volume via `c:/host/dir/to/mount:container/path`. MySql was failing to
allocate resources and perform I/O. Instead, I used `docker volume create mysql_data` and mounted that in the `docker-compose.yaml`. This seems to be a Windows only issue.