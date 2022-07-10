### 对象存储

#### 创建容器

```
openstack container create swift-test
```

#### 查看容器

```shell
openstack container list
```

#### 查询详细信息

```shell
openstack container show swift-test
```

#### 创建对象

在使用命令创建对象前，需要将上传后的目录结构在本地创建。在本地创建名为“test”的目录“/root/test”，将/root/anaconda-ks.cfg文件复制至“/root/test”目录中。命令代码如下所示：

```
[root@controller ~]# mkdir test
[root@controller ~]# cp anaconda-ks.cfg test/
```

创建对象的过程也是向容器中上传文件，使用命令创建“test/anaconda-ks.cfg”和“anaconda-ks.cfg”对象。操作命令如下所示：

```
[root@controller ~]# openstack object create swift-test test/anaconda-ks.cfg 
+----------------------+------------+----------------------------------+
| object               | container  | etag                             |
+----------------------+------------+----------------------------------+
| test/anaconda-ks.cfg | swift-test | 41656296ae6768ae924a5b5f3fe15bf0 |
+----------------------+------------+----------------------------------+
```

#### 查看对象

```shell
#查看容器“swift-test”中所有对象信息
openstack object list swift-test
#查询详细信息
opensatck object show swift-test/an**.cfg
```

#### 下载对象

```shell
opensatck object save swift-test test/anaconda-ks.cfg
```

#### 删除对象

```shewll
opensatck object delete swift-test test/an**.cfg
```

#### 删除容器

```shell
openstack container delete swift-test
```

---

### 分片存储

#### 创建容器

```shell
#创建一个容器test并查看容器的状态信息
swift post test
swift stat test
```

#### 上传镜像并分片存储

```shell
swift upload test -S 10000000 cirros***.img
#查看cirros镜像的存储路径
swift stat test cirros-0.3.4-x86_64-disk.img 
#查看存储路径中的数据片
swift list test_segments
```

