# Bucket of Bolts API

* Flask
* MySql 8.0.13
    * MySql 8.0.0 has an issue with `tx_isolation` still being used and not `transaction_isolation` causing SqlAlchemy errors. Upgrading to 8.0.13 resolved the issue.

# Docker

Could not mount a volume via `c:/host/dir/to/mount:container/path`. MySql was failing to
allocate resources and perform I/O. Instead, I used `docker volume create mysql_data` and mounted that in the `docker-compose.yaml`. This seems to be a Windows only issue.