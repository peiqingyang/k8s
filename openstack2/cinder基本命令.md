#### 查看cinder服务

```
openstack volume service list
```

#### 创建块存储

```shell
#通过命令创建块存储，大小为2G，名称为“volume”。
openstack volume create --size 2 volume
```

#### 查看块存储

```shell
openstack volume list
#查看某一块存储的详细信息
openstack volume show volume
```

#### 挂载云硬盘

```shell
#使用命令将创建的“volume”块存储添加至云主机“cirros-test”上
openstack server add volume cirros-test vilume
```

#### 扩展卷

```shell
#分离卷，通过命令将“volume”卷大小从2G扩容至3G，使用–size参数可修改已创建好的卷大小
openstack server remove volume cirros-test vilume
openstack volume set --size 3 volume 
openstack server add volume cirros-test vilume
```

#### 验证卷大小

```shell
openstack volume list
#可以看到卷“volume”挂载至云主机“cirros-test”上盘符的名称为/dev/vdb，使用virsh工具登录云主机，输入命令“lsblk”查看云硬盘大小是否为3G
virsh list --all
virsh console instance-00000001
Connected to domain instance-00000001 
```

