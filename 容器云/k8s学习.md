**创建 YAML 文件**

创建文件 nginx-deployment.yaml，内容如下：

```yaml
apiVersion: apps/v1	#与k8s集群版本有关，使用 kubectl api-versions 即可查看当前集群支持的版本
kind: Deployment	#该配置的类型，我们使用的是 Deployment
metadata:	        #译名为元数据，即 Deployment 的一些基本属性和信息
  name: nginx-deployment	#Deployment 的名称
  labels:	    #标签，可以灵活定位一个或多个资源，其中key和value均可自定义，可以定义多组，目前不需要理解
    app: nginx	#为该Deployment设置key为app，value为nginx的标签
spec:	        #这是关于该Deployment的描述，可以理解为你期待该Deployment在k8s中如何使用
  replicas: 1	#使用该Deployment创建一个应用程序实例
  selector:	    #标签选择器，与上面的标签共同作用，目前不需要理解
    matchLabels: #选择包含标签app:nginx的资源
      app: nginx
  template:	    #这是选择或创建的Pod的模板
    metadata:	#Pod的元数据
      labels:	#Pod的标签，上面的selector即选择包含标签app:nginx的Pod
        app: nginx
    spec:	    #期望Pod实现的功能（即在pod中部署）
      containers:	#生成container，与docker中的container是同一种
      - name: nginx	#container的名称
        image: nginx:1.7.9	#使用镜像nginx:1.7.9创建container，该container默认80端口可访问    
```

**应用 YAML 文件**

```sh
kubectl apply -f nginx-deployment.yaml
```

**查看部署结果**

```sh
# 查看 Deployment
kubectl get deployments

# 查看 Pod
kubectl get pods
 
```

在[部署第一个应用程序](https://kuboard.cn/learning/k8s-basics/deploy-app.html) 中，我们使用了 kubectl 命令行界面部署了 nginx 并且查看了 Deployment 和 Pod。kubectl 还有如下四个常用命令，在我们排查问题时可以提供帮助：

- **kubectl get** - 显示资源列表

  ```sh
  # kubectl get 资源类型
  
  #获取类型为Deployment的资源列表
  kubectl get deployments
  
  #获取类型为Pod的资源列表
  kubectl get pods
  
  #获取类型为Node的资源列表
  kubectl get nodes
  ```

- 名称空间

  在命令后增加 `-A` 或 `--all-namespaces` 可查看所有 [名称空间中](https://kuboard.cn/learning/k8s-intermediate/obj/namespaces.html) 的对象，使用参数 `-n` 可查看指定名称空间的对象，例如

  ```sh
  # 查看所有名称空间的 Deployment
  kubectl get deployments -A
  kubectl get deployments --all-namespaces
  # 查看 kube-system 名称空间的 Deployment
  kubectl get deployments -n kube-system
  ```

  > [并非所有对象都在名称空间里](https://kuboard.cn/learning/k8s-intermediate/obj/namespaces.html#并非所有对象都在名称空间里)

- **kubectl describe** - 显示有关资源的详细信息

  ```sh
  # kubectl describe 资源类型 资源名称
  
  #查看名称为nginx-XXXXXX的Pod的信息
  kubectl describe pod nginx-XXXXXX	
  
  #查看名称为nginx的Deployment的信息
  kubectl describe deployment nginx	    
  ```

  **kubectl logs** - 查看pod中的容器的打印日志（和命令docker logs 类似）

  ```sh
  # kubectl logs Pod名称
  
  #查看名称为nginx-pod-XXXXXXX的Pod内的容器打印的日志
  #本案例中的 nginx-pod 没有输出日志，所以您看到的结果是空的
  kubectl logs -f nginx-pod-XXXXXXX   
  ```

- **kubectl exec** - 在pod中的容器环境内执行命令(和命令docker exec 类似)

  ```sh
  # kubectl exec Pod名称 操作命令
  
  # 在名称为nginx-pod-xxxxxx的Pod中运行bash
  kubectl exec -it nginx-pod-xxxxxx /bin/bash
  ```

请尝试在您的集群中执行一下上述的几个命令，了解如何通过 kubectl 操作 kubernetes 集群中的 Node、Pod、Container。