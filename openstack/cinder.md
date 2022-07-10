使用cinder命令创建一个名字叫blockvolume，大小为2G的云硬盘。

```shell
[root@controller ~]# cinder create --name blockvolume 2
WARNING:cinderclient.shell:API version 3.59 requested,
WARNING:cinderclient.shell:downgrading to 3.50 based on server support.
+--------------------------------+--------------------------------------+
| Property                       | Value                                |
+--------------------------------+--------------------------------------+
| attachments                    | []                                   |
| availability_zone              | nova                                 |
| bootable                       | false                                |
| consistencygroup_id            | None                                 |
| created_at                     | 2022-06-14T17:04:24.000000           |
| description                    | None                                 |
| encrypted                      | False                                |
| group_id                       | None                                 |
| id                             | 64053acf-179e-473a-ad77-28742d893aa8 |
| metadata                       | {}                                   |
| migration_status               | None                                 |
| multiattach                    | False                                |
| name                           | blockvolume                          |
| os-vol-host-attr:host          | None                                 |
| os-vol-mig-status-attr:migstat | None                                 |
| os-vol-mig-status-attr:name_id | None                                 |
| os-vol-tenant-attr:tenant_id   | be793ced7c41434d93863df5e65fd8aa     |
| provider_id                    | None                                 |
| replication_status             | None                                 |
| service_uuid                   | None                                 |
| shared_targets                 | True                                 |
| size                           | 2                                    |
| snapshot_id                    | None                                 |
| source_volid                   | None                                 |
| status                         | creating                             |
| updated_at                     | None                                 |
| user_id                        | 65c9f5a2ea68440b86bc762aa65d1c2e     |
| volume_type                    | None                                 |
+--------------------------------+--------------------------------------+
[root@controller ~]# cinder list
WARNING:cinderclient.shell:API version 3.59 requested,
WARNING:cinderclient.shell:downgrading to 3.50 based on server support.
+--------------------------------------+-----------+-------------+------+-------------+----------+-------------+
| ID                                   | Status    | Name        | Size | Volume Type | Bootable | Attached to |
+--------------------------------------+-----------+-------------+------+-------------+----------+-------------+
| 64053acf-179e-473a-ad77-28742d893aa8 | available | blockvolume | 2    | -           | false    |             |
+--------------------------------------+-----------+-------------+------+-------------+----------+-------------+
[root@controller ~]#

```

