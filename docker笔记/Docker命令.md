# Docker命令

---

### 镜像

##### 上传基础镜像

```shell
docker load -i name.tar
```



##### 列出本地主机的镜像

```shell
docker images
```

##### 获取镜像

[Docker pull 命令 | 菜鸟教程 (runoob.com)](https://www.runoob.com/docker/docker-pull-command.html)

```shell
docekr pull {docker_image_name}
```

##### 查找镜像

[docker search的使用详解_⑥②的博客-CSDN博客_docker search](https://blog.csdn.net/lw001x/article/details/107152016)

```shell
docker search image_name
```

##### 删除镜像

[Docker rmi 命令 | 菜鸟教程 (runoob.com)](https://www.runoob.com/docker/docker-rmi-command.html)

```shell
docekr rmi -f image_name
-f:强制删除
```

##### 构建镜像

```shell
docker bulid -t image_name:image_version
```



### 容器

##### 运行容器

```shell
docker run -it image_name /bin/bash
docker run -d --privileged=true mariadb_pei:v1.1 /usr/sbin/init
-i:交互式操作
-t:终端
```

```shell
##启动容器
docker start ID
##启动所有docker容器
docker start $(docker ps -aq)
```

##### 操作容器

```shell
##列出容器
docker ps
##列出所有容器
docker ps -a
##进入容器
docekr exec -it ID bash
##  exit退出
```

##### 终止容器

```shell
##删除终止的容器
docker rm ID
```

##### 容器制作成镜像

```shell
docker commit ID image_name:tag
```



##### 导出/导入容器

```shell
##导出
docker export ID > image_name.tar
docker save ID > image_name.tar
##导入
cat image_name.tar | docker import - docekr_name:TAG
docker load -i image_name.tar
```
