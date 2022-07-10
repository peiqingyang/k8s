创建test容器

```shell
[root@controller ~]# swift post test
[root@controller ~]# swift list -l
    0            0 2022-06-14 17:01:20 test
    0            0
[root@controller ~]# swift list
test
```

使用自己搭建的openstack云平台，自行安装Swift服务，新建名为chinaskill的容器，将cirros-0.3.4-x86_64-disk.img镜像上传到chinaskill容器中，并设置分段存放，每一段大小为10M。完成后提交提交过程中所用到的命令以及查询结果。

```shell
[root@controller ~]# swift post chinaskill
[root@controller ~]# swift list
chinaskill
name
[root@controller ~]# swift list chinaskill
[root@controller ~]# mkdir file
[root@controller ~]# swift upload chinaskill file/
file/
[root@controller ~]# swift upload chinaskill -S 10485760 image/cirros-0.3.4-x86_64-disk.img
image/cirros-0.3.4-x86_64-disk.img segment 1
image/cirros-0.3.4-x86_64-disk.img segment 0
image/cirros-0.3.4-x86_64-disk.img
[root@controller ~]# swift list chinaskill
file/
image/cirros-0.3.4-x86_64-disk.img
[root@controller ~]# swift list chinaskill_segments
image/cirros-0.3.4-x86_64-disk.img/1655339961.186344/13287936/10485760/00000000
image/cirros-0.3.4-x86_64-disk.img/1655339961.186344/13287936/10485760/00000001
[root@controller ~]#

```

