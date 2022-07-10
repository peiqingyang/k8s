```shell
##需要先执行一键部署centos_yum源
cat >> /etc/yum.repos.d/local.repo <<EOF
[k8s]
name=k8s
baseurl=ftp://192.168.10.10/k8s/kubernetes-repo
gpgcheck=0
enabled=1
EOF
```

