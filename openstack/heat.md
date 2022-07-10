模板

```shell
[root@controller ~]# cat server.yaml
heat_template_version: 2014-10-16

description: Generated template

resources:
        nove_floar:
                type: OS::Nova::Flavor
                properties:
                        name: m1.flavor
                        disk: 20
                        is_public: True
                        ram: 1024
                        vcpus: 1
                        flavorid: 1234

[root@controller ~]# openstack stack create -t server.yaml test
+---------------------+--------------------------------------+
| Field               | Value                                |
+---------------------+--------------------------------------+
| id                  | 3b1bd647-48c4-41a1-8949-2c6c24c9fd24 |
| stack_name          | test                                 |
| description         | Generated template                   |
| creation_time       | 2022-06-14T18:12:19Z                 |
| updated_time        | None                                 |
| stack_status        | CREATE_IN_PROGRESS                   |
| stack_status_reason | Stack CREATE started                 |
+---------------------+--------------------------------------+

[root@controller ~]# openstack stack list
+--------------------------------------+------------+----------------------------------+-----------------+----------------------+--------------+
| ID                                   | Stack Name | Project                          | Stack Status    | Creation Time        | Updated Time |
+--------------------------------------+------------+----------------------------------+-----------------+----------------------+--------------+
| 3b1bd647-48c4-41a1-8949-2c6c24c9fd24 | test       | be793ced7c41434d93863df5e65fd8aa | CREATE_COMPLETE | 2022-06-14T18:12:19Z | None         |
+--------------------------------------+------------+----------------------------------+-----------------+----------------------+--------------+
[root@controller ~]# openstack flavor list
+------+-----------+------+------+-----------+-------+-----------+
| ID   | Name      |  RAM | Disk | Ephemeral | VCPUs | Is Public |
+------+-----------+------+------+-----------+-------+-----------+
| 1    | m1.tiny   |  512 |   10 |         0 |     1 | True      |
| 1234 | m1.flavor | 1024 |   20 |         0 |     1 | True      |
| 2    | m1.small  | 1024 |   20 |         0 |     1 | True      |
| 3    | m1.medium | 2048 |   40 |         0 |     2 | True      |
+------+-----------+------+------+-----------+-------+-----------+

```

hell

