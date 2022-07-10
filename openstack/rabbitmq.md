RabbitMQ

```shell
##使用RabbitMQ服务的相关命令创建用户chinaskill，密码为chinapd，并赋予该用户administrator权限。
[root@controller ~]# rabbitmqctl add_user chinaskil chinapd
Creating user "chinaskil"
[root@controller ~]# rabbitmqctl set_permissions -p / chinaskil ".*" ".*" ".*"
[root@controller ~]# rabbitmqctl set_user_tags chinaskil administrator
Setting tags for user "chinaskil" to [administrator]
[root@controller ~]# rabbitmqctl list_users
Listing users
chinaskil       [administrator]
openstack       []
guest   [administrator]

```



```shell
#提前配置 IP hostname firewalld

#安装
yum install -y rabbitmq-server
#图形化
rabbitmq-plugins enable rabbitmq_management
#启动
systemctl start rabbitmq-server
#新建用户  && 权限
rabbitmqctl add_user admin admin
rabbitmqctl set_user_tags admin administrator
rabbitmqctl list_users	#查看用户

#添加节点  在其他用户下
rabbitmqctl stop_app
rabbitmqctl join_cluster
rabbitmqctl join_cluster --ram rabbit@rmq1
rabbitmqctl start_app
rabbitmq-plugins enable rabbitmq_management
systemctl restart rabbitmq-server
```

