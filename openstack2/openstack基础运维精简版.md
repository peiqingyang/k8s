```shell
#创建镜像
glanec image-create --name cirros --disk-format qcow2 --container-format bare --progress < image

#查看镜像
glance image-list
 
#修改镜像
glance image-update --min-disk=1 ID
glance image-update --min-ram=1024 ID

#删除镜像
glance image-delete ID

#创建flavor
openstack flavor create --disk 10 --ram 1024 --vcpus 1 --id 10 flavor_name

#查看flavor
opensatck flavor list
openstack flavor show flavor_name

#查看安全组
openstack security group list

#查看安全组规则
openstack security group rule list default
openstack security group rule show ID

#创建安全组
openstack security group create test

#删除安全组
openstack security group delete test

#添加安全组规则
openstack security group rule create --protocal icmp --ingress defilt
openstack security group rule create --protocal icmp --egress defilt

#创建网络
openstack network create --provider-network-type vlan --provider-phtsical-network provider network-vlan --provider-segment 200

#创建子网
openstack subnet create --network network-vlan --allocation-pool start=192.168.200.100,end=192.168.200.200 --gateway 192.168.200.1 --subnet-range 192.168.200.0/24 subnet-vlan

#查看网络&&子网
openstack network list
openstack subnet list

#修改openstack平台
crudini --set /etc/nova/nova.conf libvirt virt_type qemu
systemctl restart openstack-nova-compute

#创建云主机
openstack server create --image cirros --flavor 10 --network network-vlan cirros-test

#查看云主机
openstack server list

#操作虚拟机
openstack server stop cirros-test
openstack server start cirros-test
openstack server reboot cirros-test

#创建块储存
openstack volume create --size 1 volume_name

#查看块储存
openstack volume list 
openstack volume show volume_name

#挂载云硬盘
openstack server add volume cirros-test volume_name

#扩展卷
openstack server remove volume cirros-test volume_name##取消挂载
openstack volume set --size 3 volume ##修改大小
openstack server add volume cirros-test volume_name##挂载

  #验证卷大小
#可以看到卷“volume”挂载至云主机“cirros-test”上盘符的名称为/dev/vdb，使用virsh工具登录云主机，输入命令“lsblk”查看云硬盘大小是否为3G
openstack volume list
virsh list -all
virsh console instance-00000001
Connected to domain instance-00000001 

#创建容器
openstack container create swift-test

#查看容器
openstack container list
openstack container show swift-test

#创建对象
openstack object craete swift-test */*   #本地目录

#查看对象
openstack object list swift-test
openstack object show swift-test */*

#下载对象
openstack object save swift-test */*

#删除对象
openstack object delete swift-test */*

#删除容器
openstack container delete swift-test

###分片存储
#创建容器
swift post test
#查询容器
swift list
swift stat test
#上传镜像并分片存储
swift upload test -S 10000000 image_name
#查看cirros镜像的存储路径
swift stat test cirros-0.3.4-x86_64-disk.img 
#查看存储路径中的数据片
swift list test_segments
```

