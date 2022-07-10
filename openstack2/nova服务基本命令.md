#### 创建flavor类型

使用命令创建一个flavor，10G的硬盘大小，512M内存，1颗vCPU，ID为10，名称为centos。命令如下：

```
openstack flavor create --disk 10 --ram 512 --vcpus 1 --id 10 centos
```

#### 查看flavor类型

```bash
openstack flavor list
#通过命令查看创建的“centos”的flavor类型详细信息。命令如下：
openstack flavor show centos
```

#### 查看访问安全组

```shell
#查看当前所创建的访问安全组列表
openstack security group list
#查看安全组中的安全规则
openstack security group rule list default
#查看任意规则的详细信息
openstack  security group rule show ID
```

#### 创建安全组

```shell
openstack security group create test
```

#### 删除安全组

```shell
openstack security group delete test
openstack security group list
```

#### 添加规则

```shell
#入口方向添加ICMP TCP UDP
openstack security group rule create --protocol icmp --ingress default 
openstack security group rule create --protocol tcp --ingress default 
openstack security group rule create --protocol udp --ingress default 
```

#### 创建网络

```shell
#查看可用的镜像&&类型
openstack image list
openstack flavor list
#创建网络和子网
openstack network create --provider-network-type vlan --provider-physical-network provider network-vlan --provider-segment 200
openstack subnet list
openstack subnet create  --network network-vlan  --allocation-pool start=192.168.200.100,end=192.168.200.200 --gateway 192.168.200.1 --subnet-range 192.168.200.0/24  subnet-vlan
```

#### 修改OpenStack平台

修改Nova服务配置文件，设置参数“virt_type=qemu”。命令参数如下：

```shell
crudini --set /etc/nova/nova.conf libvirt virt_type qemu
systemctl restart openstack-nova-compute
```

#### 启动云主机

通过命令创建云主机，使用cirros镜像，flavor为1核vCPU、512M内存、10G硬盘，使用network-vlan网络。云主机名为“cirros-test”创建命令如下：

```shell
openstack server create --image cirros-0.3.4 --flavor 10 --network network-vlan cirros-test
```

#### 查看虚拟机

```shell
openstack server list
```

#### 操作虚拟机

```shell
#关机
openstack server stop cirros-test
#开机
openstack server start cirros-test
#重启
openstack server reboot cirros-test
```

