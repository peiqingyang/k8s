#### 创建镜像

通过命令创建镜像，命令的格式如下：

> ```shell
> [root@controller ~]# glance help image-create 
> usage: glance image-create[--architecture <ARCHITECTURE>]
>                            [--protected [True|False]] [--name <NAME>]##受保护
>                            [--instance-uuid <INSTANCE_UUID>]##事例UID
>                            [--min-disk <MIN_DISK>] [--visibility <VISIBILITY>]##最小磁盘 && 可见性
>                            [--kernel-id <KERNEL_ID>]##内核ID
>                            [--tags <TAGS> [<TAGS> ...]]##标签
>                            [--os-version <OS_VERSION>]##操作系统版本
>                            [--disk-format <DISK_FORMAT>]##磁盘格式
>                            [--os-distro <OS_DISTRO>] [--id <ID>]
>                            [--owner <OWNER>] [--ramdisk-id <RAMDISK_ID>]
>                            [--min-ram <MIN_RAM>]##最小ram
>                            [--container-format <CONTAINER_FORMAT>]##容器格式
>                            [--property <key=value>] [--file <FILE>] ##属性&&文件
>                            [--progress]##进度条
> 
> ```
>

参数说明：

● --disk-format：镜像格式。

● --container-format：镜像在其他项目中可见性。

● --progress：显示上传镜像的进度。

● --file：选择本地镜像文件。

● --name：上传后镜像的名称。

```shell
glance image-create  --name cirros --disk-format qcow2 --container-format bare --progress < image
```

---

#### 查看镜像

```shell
glance image-list
```

#### 修改镜像

可以使用glance image-update更新镜像信息，命令的格式如下：

```
[root@controller ~]# glance help image-update 
usage: glance image-update [--architecture <ARCHITECTURE>]
                           [--protected [True|False]] [--name <NAME>]
                           [--instance-uuid <INSTANCE_UUID>]
                           [--min-disk <MIN_DISK>] [--visibility <VISIBILITY>]
                           [--kernel-id <KERNEL_ID>]
                           [--os-version <OS_VERSION>]
                           [--disk-format <DISK_FORMAT>]
                           [--os-distro <OS_DISTRO>] [--owner <OWNER>]
                           [--ramdisk-id <RAMDISK_ID>] [--min-ram <MIN_RAM>]
                           [--container-format <CONTAINER_FORMAT>]
                           [--property <key=value>] [--remove-property key]
                           <IMAGE_ID>
```

参数说明：

● --min-disk：镜像启动最小硬盘大小。

● --name：镜像名称。

● --disk-format：镜像格式。

● --min-ram：镜像启动最小内存大小。

● --container-format：镜像在项目中可见性。

```shell
# 如果需要改变镜像启动硬盘最低要求值（min-disk）1G，min-disk默认单位为G。使用glance image-update更新镜像信息操作如下：
glance image-update --min-disk=1 ID
# 也可以使用命令更新镜像启动内存最低要求值（min-ram）为1G，min-ram默认单位为M。使用glance image-update更新镜像信息操作如下：
glance image-update --min-ram=1024 ID
```

#### 删除镜像

可以使用glance image-delete删除上传至OpenStack平台中的镜像，使用命令格式如下：

```shel
[root@controller ~]# glance help image-delete
usage: glance image-delete <IMAGE_ID> [<IMAGE_ID> ...]

Delete specified image.

Positional arguments:
  <IMAGE_ID>  ID of image(s) to delete.

Run `glance --os-image-api-version 1 help image-delete` for v1 help
```

只需要在命令后跟上镜像ID即可。命令如下：

```
[root@controller ~]# glance image-delete 32a2513c-e5ba-438b-a5ee-63c35c03b284
```