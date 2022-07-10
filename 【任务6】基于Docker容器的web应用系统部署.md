## 【任务6】基于Docker容器的web应用系统部署

### 【题目1】容器化部署Redis[3分]

在master节点上编写/root/redis/Dockerfile文件构建chinaskill-redis:v1.1镜像，具体要求如下：（需要用到的软件包在/桌面/附件/容器云附件/gpmall-single.tar.gz）

（1）基础镜像：centos:centos7.5.1804；

（2）作者：Chinaskill；

（3）修改配置文件中的bind 127.0.0.1为bind 0.0.0.0；

（4）设置Redis免密，并关闭保护模式；

（5）开放端口：6379；

（6）设置服务开机自启。

```bash
[root@master redis]# cat Dockerfile
FROM centos:centos7.5.1804
MAINTAINER Chinaskill
COPY local.repo /etc/yum.repos.d/
RUN rm -rf /etc/yum.repos.d/C* && yum clean all && yum -y install redis*
RUN sed -i 's/bind 127.0.0.1/bind 0.0.0.0/g' /etc/redis.conf && sed -i 's/protected-mode yes/protected-mode no/g' /etc/redis.conf
EXPOSE 6379
CMD ["redis-server","/etc/redis.conf"]
```

```bash

## yum 源配置文件
[root@master redis]# cat local.repo
[k8s]
name=k8s
## 此处的IP地址为 master 节点的IP
baseurl=ftp://192.168.92.35/kubernetes-repo
gpgcheck=0
enabled=1

[Centos]
name=centos
## 此处的IP地址为 controller 节点的IP，要解决依赖关系
baseurl=ftp://192.168.5.235/centos
gpgcheck=0
enabled=1

## 构建镜像
[root@master redis]# docker build -t chinaskill-redis:v1.1 .

## 查看镜像的详细信息
[root@master redis]# docker inspect chinaskill-redis:v1.1
```



### 【题目2】容器化部署MariaDB

在master节点上编写/root/mariadb/Dockerfile文件构建chinaskill-mariadb:v1.1镜像，具体要求如下：（需要用到的软件包在/桌面/附件/容器云附件/gpmall-single.tar.gz）

（1）基础镜像：centos:centos7.5.1804；

（2）作者：Chinaskill；

（3）设置数据库密码：123456；

（4）创建数据库gpmall并导入数据库文件gpmall.sql；

（5）设置字符编码：UTF-8；

（6）开放端口：3306；

（7）设置服务开机自启。

完成后构建镜像，并提交master节点的用户名、密码和IP到答题框。

```bash
[root@master mariadb]# ll
total 72
-rw-r--r-- 1 root root   281 Oct 12 21:53 Dockerfile
-r-xr-xr-x 1 root root 59239 Oct 12 22:09 gpmall.sql
-rw-r--r-- 1 root root    91 Oct 12 21:52 local.repo
-rw-r--r-- 1 root root   279 Oct 12 22:06 start.sh

```

```bash
[root@master mariadb]# cat Dockerfile
FROM centos:centos7.5.1804
MAINTAINER chinaskill
RUN rm -rf /etc/yum.repos.d/*
ADD local.repo /etc/yum.repos.d/
ADD gpmall.sql /opt/
ADD start.sh /opt/
RUN yum -y install mariadb-server && chmod +x /opt/start.sh  && /opt/start.sh
EXPOSE 3306
ENV LC_ALL en_US.UTF-8
CMD mysqld_safe
[root@master mariadb]# cat local.repo
[db]
name=db
baseurl=ftp://192.168.92.35/ChinaskillMall/gpmall-repo/
gpgcheck=0
enabled=1
[Centos]
name=centos
baseurl=ftp://192.168.5.235/centos
gpgcheck=0
enabled=1
[root@master mariadb]# cat start.sh
#!/bin/bash
mysql_install_db --user=mysql
mysqld_safe &
sleep 3
mysqladmin -u root password '123456'
mysql -uroot -p123456 -e "grant all privileges on *.* to 'root'@'%' identified by '123456';"
mysql -uroot -p123456 -e "create database gpmall;use gpmall;source /opt/gpmall.sql;"

[root@master mariadb]# docker build -t chinaskill-mariadb:v1.1 .

```

### 【题目3】容器化部署Zookeeper

在master节点上编写/root/zookeeper/Dockerfile文件构建chinaskill-zookeeper:v1.1镜像，具体要求如下：（需要用到的软件包在/桌面/附件/容器云附件/gpmall-single.tar.gz）

（1）基础镜像：centos:centos7.5.1804；

（2）作者：Chinaskill；

（3）开放端口：2181；

（4）设置服务开机自启。

完成后构建镜像，使用构建的镜像运行容器myzookeeper，并提交master节点的用户名、密码和IP到答题框。

```bash
[root@master zookeeper]# ll
total 36804
-rw-r--r-- 1 root root      402 Oct 13 02:00 Dockerfile
-rw-r--r-- 1 root root      167 Oct 13 01:20 local.repo
-r-xr-xr-x 1 root root 37676320 Oct 13 01:19 zookeeper-3.4.14.tar.gz

```

```bash
[root@master zookeeper]# cat Dockerfile
FROM centos:centos7.5.1804
MAINTAINER Chinaskill
RUN rm -rf /etc/yum.repos.d/*
COPY local.repo /etc/yum.repos.d/local.repo
ADD zookeeper-3.4.14.tar.gz /opt
RUN yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel  && mv /opt/zookeeper-3.4.14/conf/zoo_sample.cfg /opt/zookeeper-3.4.14/conf/zoo.cfg
EXPOSE 2181
CMD ["sh","-c","/opt/zookeeper-3.4.14/bin/zkServer.sh start && tail -f /etc/hosts"]

[root@master zookeeper]# cat local.repo
[db]
name=db
baseurl=ftp://192.168.92.35/ChinaskillMall/gpmall-repo/
gpgcheck=0
enabled=1
[Centos]
name=centos
baseurl=ftp://192.168.5.235/centos
gpgcheck=0
enabled=1

[root@master zookeeper]#  docker build -t chinaskill-zookeeper:v1.1 .

[root@master zookeeper]#  docker run -itd --name myzookeeper chinaskill-zookeeper:v1.1


```

### 【练习4】容器化部署Kafka

在master节点上编写/root/kafka/Dockerfile文件构建chinaskill-kafka:v1.1镜像，具体要求如下：（需要用到的软件包在/桌面/附件/容器云附件/gpmall-single.tar.gz）
（1）基础镜像：centos:centos7.5.1804；
（2）作者：Chinaskill；
（3）开放端口：9092；
（4）设置服务开机自启。
完成后构建镜像，并提交master节点的用户名、密码和IP到答题框。

> **kafka 的运行要依赖于 zookeeper 所以要同时安装两个组件，zookeeper 和 kafka**

```bash
[root@master kafka]# ll
total 92932
-rw-r--r-- 1 root root      496 Oct 14 03:39 Dockerfile
-r-xr-xr-x 1 root root 57471165 Oct 14 03:10 kafka_2.11-1.1.1.tgz
-rw-r--r-- 1 root root      167 Oct 14 03:11 local.repo
-r-xr-xr-x 1 root root 37676320 Oct 14 03:39 zookeeper-3.4.14.tar.gz

```

```bash
[root@master kafka]# cat Dockerfile
FROM centos:centos7.5.1804
MAINTAINER chinaskill
RUN rm -rf /etc/yum.repos.d/*
ADD local.repo /etc/yum.repos.d/
ADD zookeeper-3.4.14.tar.gz /opt/
ADD kafka_2.11-1.1.1.tgz /opt/
RUN yum -y install java-1.8.0-openjdk java-1.8.0-openjdk-devel && mv /opt/zookeeper-3.4.14/conf/zoo_sample.cfg /opt/zookeeper-3.4.14/conf/zoo.cfg
EXPOSE 9092
CMD ["sh","-c","/opt/zookeeper-3.4.14/bin/zkServer.sh start && /opt/kafka_2.11-1.1.1/bin/kafka-server-start.sh /opt/kafka_2.11-1.1.1/config/server.properties"]
[root@master kafka]# cat local.repo
[db]
name=db
baseurl=ftp://192.168.92.35/ChinaskillMall/gpmall-repo/
gpgcheck=0
enabled=1
[Centos]
name=centos
baseurl=ftp://192.168.5.235/centos
gpgcheck=0
enabled=1

```

### 【练习5】容器化部署Nginx

在master节点上编写/root/nginx/Dockerfile文件构建chinaskill-nginx:v1.1镜像，具体要求如下：（需要用到的软件包路径http://<IP>/gpmall-single.tar.gz）

（1）基础镜像：centos:centos7.5.1804；

（2）作者：Chinaskill；

（3）编写/etc/nginx/conf.d/default.conf文件，配置反向代理，将80端口请求转发到8081、8082和8083；

（4）将dist中的文件复制到/usr/share/nginx/html/目录下；

（5）复制所有的jar包到镜像中；

（6）开放端口：80、443、8081、8082、8083；

（7）设置服务开机自启。

完成后构建镜像。

```
[root@master nginx]# ll
total 196772
dr-xr-xr-x 3 root root       38 Oct 19 06:53 dist
-rw-r--r-- 1 root root      692 Oct 19 06:49 Dockerfile
-r-xr-xr-x 1 root root 47765234 Oct 19 06:47 gpmall-shopping-0.0.1-SNAPSHOT.jar
-r-xr-xr-x 1 root root 39005479 Oct 19 06:47 gpmall-user-0.0.1-SNAPSHOT.jar
-rw-r--r-- 1 root root      167 Oct 19 06:46 local.repo
-rw-r--r-- 1 root root      276 Oct 19 06:43 setup.sh
-r-xr-xr-x 1 root root 53627038 Oct 19 06:47 shopping-provider-0.0.1-SNAPSHOT.jar
-r-xr-xr-x 1 root root 61077919 Oct 19 06:47 user-provider-0.0.1-SNAPSHOT.jar

```



```bash
[root@master nginx]# cat Dockerfile
FROM centos:centos7.5.1804
MAINTAINER chinaskill
RUN rm -rf /etc/yum.repos.d/*
ADD local.repo /etc/yum.repos.d/
ADD *.jar /root/
ADD setup.sh /root/
RUN yum -y install nginx java-1.8.0-openjdk java-1.8.0-openjdk-devel \
 && sed -i '1a location /shopping { proxy_pass http://127.0.0.1:8081 ;}' /etc/nginx/conf.d/default.conf \
 && sed -i '2a location /user { proxy_pass http://127.0.0.1:8082 ;}' /etc/nginx/conf.d/default.conf \
 && sed -i '3a location /cashier { proxy_pass http://127.0.0.1:8083 ;}' /etc/nginx/conf.d/default.conf \
 && chmod +x /root/setup.sh \
 && rm -rf /usr/share/nginx/html/
EXPOSE 80 8081 8082 8083
ADD dist/ /usr/share/nginx/html/
CMD ["nginx","-g","daemon off;"]

[root@master nginx]# cat local.repo
[db]
name=db
baseurl=ftp://192.168.92.35/ChinaskillMall/gpmall-repo/
gpgcheck=0
enabled=1
[Centos]
name=centos
baseurl=ftp://192.168.5.235/centos
gpgcheck=0
enabled=1

[root@master nginx]# cat setup.sh
#!/bin/bash
nohup java -jar /root/shopping-provider-0.0.1-SNAPSHOT.jar &
sleep 5
nohup java -jar /root/user-provider-0.0.1-SNAPSHOT.jar &
sleep 5
nohup java -jar /root/gpmall-shopping-0.0.1-SNAPSHOT.jar &
sleep 5
nohup java -jar /root/gpmall-user-0.0.1-SNAPSHOT.jar &
sleep 5

[root@master nginx]# docker build -t chinaskill-nginx:v1.1 .
```

### 【练习6】编排部署商城

在master节点上编写/root/dockerchinaskillmall/docker-compose.yaml文件部署，具体要求如下：

（1）容器1名称：mall-mysql；镜像：chinaskill-mariadb:v1.1；端口映射：13306:3306；

（2）容器2名称：mall-redis；镜像：chinaskill-redis:v1.1；端口映射：16379:6379；

（3）容器3名称：mall-kafka；镜像：chinaskill-kafka:v1.1；端口映射：19092:9092；

（4）容器4名称：mall-zookeeper；镜像：chinaskill-zookeeper:v1.1；端口映射：12181:2181；

（5）容器5名称：mall-nginx；镜像：chinaskill-nginx:v1.1；端口映射：83:80，1443:443；自启动所有的jar包程序。

完成后编排部署商城，并能成功访问商城首页。

```bash
[root@master chinaskillmall]# cat docker-compose.yaml
version: '3.3'
services:
  mall-mysql:
    image: chinaskill-mariadb:v1.1
    ports:
      - 13306:3306

  mall-redis:
    image: chinaskill-redis:v1.1
    ports:
      - 16379:6379

  mall-kafka:
    image: chinaskill-kafka:v1.1
    ports:
      - 19092:9092
  mall-zookeeper:
    image: chinaskill-zookeeper:v1.1
    ports:
      - 12181:2181
  mall-nginx:
    image: chinaskill-nginx:v1.1
    depends_on:
      - mall-mysql
      - mall-redis
      - mall-zookeeper
      - mall-kafka
    links:
      - mall-mysql:mysql.mall
      - mall-redis:redis.mall
      - mall-zookeeper:zookeeper.mall
      - mall-kafka:kafka.mall
    ports:
      - 83:80
      - 1443:443
    command: ["sh","-c","/root/setup.sh && nginx && tail -f /etc/shadow"]
#启动
[root@master chinaskillmall]# docker-compose -f docker-compose.yaml up -d
#停止
[root@master chinaskillmall]# docker-compose -f docker-compose.yaml down

```

