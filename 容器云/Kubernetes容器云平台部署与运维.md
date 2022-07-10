###### 1、修改Pod数量限制(1分)

Kubernetes 默认每个节点只能启动110个Pod，由于业务需要，需要在所有节点上运行大量资源消耗非常小的Pod，请将每个节点默认限制的Pod数量改为200。完成后提交过程中所用到的命令以及查询结果。

```shell
##可创建的Pod数量是作为Kubelet的参数出现的，因此修改Kubelet服务的配置文件增加 --max-pod 参数即可。
[root@k8s-master-node1 ~]# vim /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
##添加并在启动命令尾部添加变量 $KUBELET_NODE_MAX_PODS 如下：
......
Environment="KUBELET_NODE_MAX_PODS=--max-pods=200"
ExecStart=
ExecStart=/usr/local/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS $KUBELET_NODE_MAX_PODS
```

保存之后，重启kubelet服务即可　

`systemctl daemon-reload`

`systemctl restart kubelet`

 **检查配置是否生效**

`kubectl describe nodes k8s-master-node1`

```shell
[root@k8s-master-node1 ~]# kubectl describe nodes k8s-master-node1 | grep pods:
  pods:                           110
  pods:                           110
[root@k8s-master-node1 ~]# systemctl daemon-reload
[root@k8s-master-node1 ~]# systemctl restart kubelet
[root@k8s-master-node1 ~]# kubectl describe nodes k8s-master-node1 | grep pods:
  pods:                           200
  pods:                           200
```



---

[Kubernetes限制节点启动的Pod数量 - 人艰不拆_zmc - 博客园 (cnblogs.com)](https://www.cnblogs.com/zhangmingcheng/p/16010149.html)

###### 2、修改NodePort端口范围(1分)

Kubernetes以NodePort方式暴露服务默认的端口范围为30000-32767，请将NodePort的端口范围修改为20000-65535。完成后提交过程中所用到的命令以及查询结果。

```shell
##1.修改kube-apiserver.yaml文件
vim /etc/kubernetes/manifests/kube-apiserver.yaml
...
--service-node-port-range=30000-32767
##修改为自己需要的范围
...

##2.重启apiserver
systemctl daemon-reload
systemctl restart kubelet
kubectl create -f  /etc/kubernetes/manifests/kube-apiserver.yaml
pod/kube-apiserver created
```

---

[如何修改kubernetes服务nodeport类型的端口范围 - 云计算 - 亿速云 (yisu.com)](https://www.yisu.com/zixun/522940.html)

###### 3、 Pod管理(2分)

在master节点/root目录下编写yaml文件nginx.yaml，具体要求如下：

（1）Pod名称：nginx-pod；

（2）命名空间：default；

（3）容器名称：mynginx；

（4）镜像：nginx；拉取策略：IfNotPresent；

（5）容器端口：80。

完成后使用该yaml文件创建Pod，并提交过程中所用到的命令以及查询结果。

> nginx-pod.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  namespace: default
spec:
  containers:
  - name: mynginx
    image: nginx:latest
    imagePullPolicy: IfNotPresent
    ports:
    - containerPort: 80
```

---

[(7条消息) Kubernetes中yaml文件Pod模板详解编写yaml文件启动服务_C_cccriston的博客-CSDN博客_pod 模板](https://blog.csdn.net/cbc_19/article/details/121287330)

[(7条消息) Kubernetes 运维题_小咔啦眯的博客-CSDN博客](https://blog.csdn.net/qq_45631844/article/details/115029551)

执行` kubectl apply -f nginx.yaml`

查看`kubectl get pods`

### **4、Pod安全策略(2分)**

在master节点/root目录下编写yaml文件policy.yaml，具体要求如下：

（1）安全策略名称：pod-policy；

（2）仅禁止创建特权模式的Pod；

（3）其它所有字段都被允许。

```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: pod-policy
  namespace: default
spec:
  privileged: false
#不允许特权模式的pod，禁止创建特权模式的pod
  seLinux: 
    rule: RunAsAny
  supplementalGroups: 
    rule: RunAsAny
  runAsUser: 
    rule: RunAsAny
  fsGroup: 
    rule: RunAsAny
  volumes:
    - "*"
```



###### 5.Deployment管理(2分)

在master节点/root目录下编写yaml文件nginx-deployment.yaml，具体要求如下：

（1）Deployment名称：nginx-deployment；

（2）命名空间：default；

（3）Pod名称：nginx-deployment，副本数：2；

（4）网络：hostNetwork；

（5）镜像：nginx；

（6）容器端口：80

完成后使用该yaml文件创建Deployment，并提交过程中所用到的命令以及查询结果。

> nginx-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: default
  labels: 
    app: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx-deployment
  template:
    metadata:
      labels:
        app: nginx-deployment
    spec:
      hostNetwork: true
      containers:
      - name: nginx-deployment
        image: nginx:latest
        ports:
        - containerPort: 80
```

###### 6、RBAC管理(2分)

在master节点/root目录下编写yaml文件role.yaml，具体要求如下：

（1）Role名称：pod-reader；

（2）命名空间：default；

（3）对default命名空间内的Pod拥有get、watch、list的权限。

> role.yaml

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get","watch","list"]
```

[k8s权限配置（ServiceAccount、Role、ClusterRole）_lihongbao80的博客-CSDN博客_k8s serviceaccount](https://blog.csdn.net/lihongbao80/article/details/120160933)

###### 7.HPA管理(2分)

在master节点/root目录下编写yaml文件deployment-hpa.yaml，具体要求如下：

（1）HPA名称：deployment-hpa；

（2）命名空间：default；

（3）基于deployment进行伸缩，副本数伸缩范围：1--10；

（4）期望每个Pod的CPU和内存使用率为50%。

> deployment-hpa.yaml

```yaml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: deployment-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: hpa
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

◎　scaleTargetRef：目标作用对象，可以是Deployment、ReplicationController或ReplicaSet。
◎　targetCPUUtilizationPercentage：期望每个Pod的CPU使用率都为50%，该使用率基于Pod设置的CPU Request值进行计算，例如该值为200m，那么系统将维持Pod的实际CPU使用值为100m。
◎　minReplicas和maxReplicas：Pod副本数量的最小值和最大值，系统将在这个范围内进行自动扩缩容操作，并维持每个Pod的CPU使用率为50%。



## 8、更新证书(3分)

Kubernetes默认的证书有效期只有一年时间，对于某些场景下一个足够长的证书有效期是非常有必要的。请将Kubernetes集群证书的有效期延长至10年。完成后提交过程中所用到的命令以及查询结果（需要用到的软件包在/桌面/附件/容器云附件/kubernetes_v1.18.1.tar.gz）



























[2021江苏省云计算技术与应用比赛 | 程序员灯塔 (wangt.cc)](https://www.wangt.cc/2021/04/2021江苏省云计算技术与应用比赛/)
