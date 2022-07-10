## 1.安装Jenkins环境

查看k8s集群状态和节点信息

```shell
kubeclt get cs						#状态
kubectl get nodes					#集群信息
```

解压镜像包（？？？）

`tar -xvf jenkins.tar`

导入镜像

`docker load -i jenkins.tar`

安装Jenkins

```shell
docker run -d --name jenkins -p 8080:8080 -u root \
-v /home/jenkins_home:/var/jenkins_home \
-v /var/run/docker.sock:/var/run/docker.sock \
-v $(which docker):/usr/bin/docker \
-v /usr/bin/kubectl:/usr/local/bin/kubectl \
-v /root/.kube:/root/.kube \
jenkins/jenkins:2.262-centos
```

gitlab

```shell
docker run -d -h gitlab -p 1022:22 -p 81:80 -p 443:443 \
--volume /srv/gitlab/config:/etc/gitlab \
--volume /srv/gitlab/gitlab/logs:/var/log/gitlab \
--volume /srv/gitlab/gitlab/data:/var/opt/gitl    
--restart always --name mygitlab gitlab/gitlab-ce:12.9.2-ce.0

```

