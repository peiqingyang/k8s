集群节点

| master | 192.168.10.20     |
| ------ | ----------------- |
| worker | **192.168.10.30** |

># 基础环境准备

### 在 master 节点安装 kubeeasy 工具

```shell
mv /opt/kubeeasy /usr/bin/kubeeasy
cd /usr/bin/
```

### 在 master 节点执行以下命令完成依赖包的安装

```shell
kubeeasy install depend \
--host 192.168.10.20,192.168.10.30 \
--user root \
--password 000000 \
--offline-file /opt/dependencies/base-rpms.tar.gz

```

### 执行命令查看安装详情或排查错误

```shell
[root@master bin]# tail -f /var/log/kubeinstall.log
  lvm2-libs.x86_64 7:2.02.187-6.el7_9.5
  openssl.x86_64 1:1.0.2k-25.el7_9
  openssl-libs.x86_64 1:1.0.2k-25.el7_9
  python.x86_64 0:2.7.5-90.el7
  python-libs.x86_64 0:2.7.5-90.el7
  util-linux.x86_64 0:2.23.2-65.el7_9.1
  zlib.x86_64 0:1.2.7-19.el7_9

完毕！
[2022-06-18 17:27:19] INFO:    [install] 192.168.10.30: install dependencies packages succeeded.

```

### 在master节点执行查看集群连通性

```shell
kubeeasy check ssh \
--host 192.168.10.20,192.168.10.30 \
--user root \
--password 000000
```

### 在 master 节点执行以下命令完成集群所有节点间的免密钥配置

```shell
kubeeasy create ssh-keygen \
--master 192.168.10.20 \
--worker 192.168.10.30 \
--user root --password 000000
```

---

> # 部署 Kubernetes 集群

### 安装Kubernetes

```shell
kubeeasy install kubernetes \
--master 192.168.10.20 \
--worker 192.168.10.30 \
--user root \
--password 000000 \
--version 1.22.1 \
--offline-file /opt/kubernetes.tar.gz
```

### 查看安装详情 && 部署完查看集群状态 && 查看节点负载情况

```shell
tail -f /var/log/kubeinstall.log
kubectl cluster-info
kubectl top nodes --use-protocol-buffers
```

### 登录平台

```tex
在浏览器上访问一道云云开发平台（http://master_IP:30080），如图所示：
```

---

> 部署KubeVirt

### 安装KubeVirt

```shell
kubeeasy add --virt kubevirt
##查看pod
kubectl -n kubevirt get pods
```

### 部署Istio

```shell
kubeeasy add --istio istio
##查看pod
kubectl -n istio-system get pods
```

### Istio可视化

```shell
访问Prometheus（http://master_IP:30090）
```

---

> # 部署Harbar仓库

### 安装HarBor仓库

```shell
kubeeasy add --registry harbor
## 查看状态
systemctl status harbor
## 在Web端通过http://master_ip访问Harbor
## 使用管理员账号（admin/Harbor12345）登录Harbor
```

---

### 重置集群

```shell
## 若集群部署失败或出现故障，可重置集群重新部署
[root@k8s-master-node1~]#kubeeasy reset
## 之后再次执行安装
```

### 添加节点

```shell
## master节点执行安装依赖包
kubeeasy install depend \
--host 192.168.100.40 \    ##192.168.100.40为新加节点
--user root \
--password 000000 \
--offline-file /opt/dependencies/base-rpms.tar.gz
```

```shell
## master节点执行加入集群
kubeesay add \
--worker 192.168.100.40 \
--user root \
--password 000000 \
--offline-file /opt/kubernetes.tar.gz
```

## kubeesay - -help

```markdown
 -m       |     --master     |       master节点IP
 -w       |     --worker     |       worker节点IP
 -host    |     --host       |       其他节点IP 
 -u       |     --user       |       用户名 默认root
 -p       |     --password   |       密码   默认000000
 -P       |     --port       |       端口   默认22
 -v       |     --version    |       版本   默认1.22.1
```

