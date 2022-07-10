##### mkdir -p

```bash
mkdir -p /**/{name_1,name2}/{name3,name4}
##   name_1 && name_2属于同一级  name_3 && name_4属于同一级
##   name_1 && name_2下都会有name_3 && name_4
```

##### 创建角色

在创建roles角色目录之前，考虑将OpenStack云平台的安装步骤拆分为多个roles执行，这样的话，Playbook易于编写和读懂

```tree
.
├── group_vars
│   └── all
├── install_openstack.yaml
└── roles
    ├── cinder-compute
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── cinder-controller
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── dashboard
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── glance
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── heat
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── init
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   │   └── main.yaml
    │   ├── templates
    │   └── vars
    ├── keystone
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── mariadb
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── neutron-compute
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── neutron-controller
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── nova-compute
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── nova-controller
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    ├── swift-compute
    │   ├── files
    │   ├── handlers
    │   ├── meta
    │   ├── tasks
    │   ├── templates
    │   └── vars
    └── swift-controller
        ├── files
        ├── handlers
        ├── meta
        ├── tasks
        ├── templates
        └── vars
```

##### playbook剧本

init角色

```shell
##@ /opt/openstack_ansible/roles/init/tasks/main.yaml

- name: move repos
  shell: mv /etc/yum.repos.d/* /media
- name: create local.repo
  copy: src=local.repo dest=/etc/yum.repos.d/
- name: install openstack-iaas
  yum: name=openstack-iaas state=present
- name: openrc.sh
  template: src=openrc.sh.j2 dest=/etc/openstack/openrc.sh
- name: install pre-host
  shell: iaas-pre-host.sh
```

 `copy: src=local.repo         dest=/etc/yum.repos.d/`

src：代表ansible节点的文件 

dest ：是要COPY的位置

` yum: name=openstack-iaas state=present`

```tex
使用yum_repository管理器来管理软件包，其选项有：
file：配置文件的名字，不包含.repo，会自动加上.repo
name：描述名(yum仓库的名字)
state：状态（present安装，absent卸载，latest最新版本）
description：仓库的描述信息
baseurl:yum源地址
enabled：是否开启yum仓库，yes/no
gpgcheck：是否检查软件包的完整性，yes/no
gpgkey：公钥地址
```

`template: src=openrc.sh.j2 dest=/etc/openstack/openrc.sh`

template功能：可以根据和参考模块文件，动态生成相类似的配置文件
template文件必须存放于templates目录下，且命名为 .j2 结尾
yaml/yml 文件需和templates目录平级

##### openrc.sh.j2

因为设置的变量，所以需要在/opt/openstack_ansible/group_vars/all 中声明变量

```

```

