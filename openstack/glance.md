使用自己搭建的openstack云平台，使用http:///cirros-0.3.4-x86_64-disk.img镜像，使用命令创建一个名为cirros的镜像。完成后提交提交过程中所用到的命令以及查询结果。

```shell
[root@controller ~]# glance image-create --name "cirros" --disk-format qcow2 --container-format bare --progress < cirros-0.3.3-x86_64-disk.img

[=============================>] 100%
+------------------+----------------------------------------------------------------------------------+
| Property         | Value                                                                            |
+------------------+----------------------------------------------------------------------------------+
| checksum         | ee1eca47dc88f4879d8a229cc70a07c6                                                 |
| container_format | bare                                                                             |
| created_at       | 2022-06-14T17:10:50Z                                                             |
| disk_format      | qcow2                                                                            |
| id               | 7fbdf8c3-8b48-4c9d-9046-119f2a534ad5                                             |
| min_disk         | 0                                                                                |
| min_ram          | 0                                                                                |
| name             | cirros                                                                           |
| os_hash_algo     | sha512                                                                           |
| os_hash_value    | 1b03ca1bc3fafe448b90583c12f367949f8b0e665685979d95b004e48574b953316799e23240f4f7 |
|                  | 39d1b5eb4c4ca24d38fdc6f4f9d8247a2bc64db25d6bbdb2                                 |
| os_hidden        | False                                                                            |
| owner            | be793ced7c41434d93863df5e65fd8aa                                                 |
| protected        | False                                                                            |
| size             | 13287936                                                                         |
| status           | active                                                                           |
| tags             | []                                                                               |
| updated_at       | 2022-06-14T17:11:01Z                                                             |
| virtual_size     | Not available                                                                    |
| visibility       | shared                                                                           |
+------------------+----------------------------------------------------------------------------------+
[root@controller ~]#
[root@controller ~]# glance image-list
+--------------------------------------+--------+
| ID                                   | Name   |
+--------------------------------------+--------+
| 7fbdf8c3-8b48-4c9d-9046-119f2a534ad5 | cirros |
+--------------------------------------+--------+

```

使用自己搭建的openstack云平台，将云主机VM1保存为qcow2格式的快照并保存到controller节点/root/cloudsave目录下，保存名字为csccvm.qcow2。完成后提交云主机的用户名、密码和IP地址到答题框。

```shell
[root@controller glance]# glance image-list
+--------------------------------------+---------+
| ID                                   | Name    |
+--------------------------------------+---------+
| 6fcec4ad-0cf9-4855-8dc6-dce1817b22c6 | cen2009 |
| 48a18f87-1954-4730-bc07-ade960a6603b | cirros  |
| f7fb1d74-ec1e-45e0-a738-1094f222332f | csccvm  |
+--------------------------------------+---------+
[root@controller glance]# glance image-download --file /root/cloudsave/csccvm.qcow2 f7fb1d74-ec1e-45e0-a738-1094f222332f
```

