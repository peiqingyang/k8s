#### 创建flavor类型

使用命令创建一个flavor，10G的硬盘大小，512M内存，1颗vCPU，ID为10，名称为centos。命令如下：

```
openstack flavor create --disk 10 --ram 512 --vcpus 1 --id 10 centos
```

#### 查看flavor类型

```shell
START with options: token issue --debug
options: Namespace(access_key='', access_secret='***', access_token='***', access_token_endpoint='', access_token_type='', aodh_endpoint='', application_credential_id='', application_credential_name='', application_credential_secret='***', auth_methods='', auth_type='', auth_url='http://controller:5000/v3', cacert=None, cert='', client_id='', client_secret='***', cloud='', code='', consumer_key='', consumer_secret='***', debug=True, default_domain='default', default_domain_id='', default_domain_name='', deferred_help=False, discovery_endpoint='', domain_id='', domain_name='', endpoint='', identity_provider='', identity_provider_url='', insecure=None, interface='public', key='', log_file=None, openid_scope='', os_alarming_api_version='2', os_beta_command=False, os_compute_api_version='', os_container_infra_api_version='1', os_data_processing_api_version='1.1', os_data_processing_url='', os_database_api_version='1', os_dns_api_version='2', os_identity_api_version='3', os_image_api_version='2', os_key_manager_api_version='1', os_loadbalancer_api_version='2.0', os_network_api_version='', os_object_api_version='', os_orchestration_api_version='1', os_project_id=None, os_project_name=None, os_queues_api_version='2', os_volume_api_version='', os_workflow_api_version='2', passcode='', password='***', profile='', project_domain_id='', project_domain_name='demo', project_id='', project_name='admin', protocol='', redirect_uri='', region_name='', remote_project_domain_id='', remote_project_domain_name='', remote_project_id='', remote_project_name='', roles='', service_provider='', service_provider_endpoint='', service_provider_entity_id='', system_scope='', timing=False, token='***', trust_id='', user_domain_id='', user_domain_name='demo', user_id='', username='admin', verbose_level=3, verify=None)
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'image_status_code_retries': '5', 'key': None, 'database_api_version': '1', 'data_processing_api_version': '1.1', 'auth_url': 'http://controller:5000/v3', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], 'queues_api_version': '2', 'verify': True, 'dns_api_version': '2', u'object_store_api_version': u'1', 'username': 'admin', 'container_infra_api_version': '1', 'loadbalancer_api_version': '2.0', 'verbose_level': 3, 'region_name': '', u'baremetal_introspection_status_code_retries': '5', 'api_timeout': None, 'image_api_version': '2', 'auth': {'user_domain_name': 'demo', 'project_name': 'admin', 'project_domain_name': 'demo'}, 'default_domain': 'default', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'orchestration_api_version': '1', 'timing': False, 'password': '***', 'cacert': None, 'key_manager_api_version': '1', 'workflow_api_version': '2', u'baremetal_status_code_retries': '5', 'identity_api_version': '3', 'deferred_help': False, 'cert': None, u'secgroup_source': u'neutron', u'status': u'active', 'alarming_api_version': '2', 'debug': True, u'interface': 'public', u'disable_vendor_agent': {}}
defaults: {u'auth_type': 'password', u'status': u'active', u'image_status_code_retries': 5, u'baremetal_introspection_status_code_retries': 5, 'api_timeout': None, 'cacert': None, u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'key': None, u'interface': None, u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', u'baremetal_status_code_retries': 5, 'verify': True, 'cert': None, u'secgroup_source': u'neutron', u'object_store_api_version': u'1', u'disable_vendor_agent': {}}
cloud cfg: {'auth_type': 'password', 'beta_command': False, u'image_status_code_retries': '5', 'orchestration_api_version': '1', 'database_api_version': '1', 'data_processing_api_version': '1.1', 'auth_url': 'http://controller:5000/v3', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], 'queues_api_version': '2', 'verify': True, 'dns_api_version': '2', u'object_store_api_version': u'1', 'username': 'admin', 'container_infra_api_version': '1', 'loadbalancer_api_version': '2.0', 'verbose_level': 3, 'region_name': '', u'baremetal_introspection_status_code_retries': '5', 'api_timeout': None, 'image_api_version': '2', 'auth': {'user_domain_name': 'demo', 'project_name': 'admin', 'project_domain_name': 'demo'}, 'default_domain': 'default', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'key': None, 'timing': False, 'password': '***', 'cacert': None, 'key_manager_api_version': '1', 'workflow_api_version': '2', u'baremetal_status_code_retries': '5', 'identity_api_version': '3', 'deferred_help': False, 'cert': None, u'secgroup_source': u'neutron', u'status': u'active', 'alarming_api_version': '2', 'debug': True, u'interface': 'public', u'disable_vendor_agent': {}}
compute API version 2.1, cmd group openstack.compute.v2
network API version 2, cmd group openstack.network.v2
image API version 2, cmd group openstack.image.v2
volume API version 3, cmd group openstack.volume.v3
identity API version 3, cmd group openstack.identity.v3
object_store API version 1, cmd group openstack.object_store.v1
messaging API version 2, cmd group openstack.messaging.v2
database API version 1, cmd group openstack.database.v1
data_processing API version 1.1, cmd group openstack.data_processing.v1
load_balancer API version 2.0, cmd group openstack.load_balancer.v2
neutronclient API version 2, cmd group openstack.neutronclient.v2
workflow_engine API version 2, cmd group openstack.workflow_engine.v2
container_infra API version 1, cmd group openstack.container_infra.v1
orchestration API version 1, cmd group openstack.orchestration.v1
dns API version 2, cmd group openstack.dns.v2
key_manager API version 1, cmd group openstack.key_manager.v1
alarming API version 2, cmd group openstack.alarming.v2
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'image_status_code_retries': '5', 'key': None, 'database_api_version': '1', 'data_processing_api_version': '1.1', 'auth_url': 'http://controller:5000/v3', u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], 'queues_api_version': '2', 'verify': True, 'dns_api_version': '2', u'object_store_api_version': u'1', 'username': 'admin', 'container_infra_api_version': '1', 'loadbalancer_api_version': '2.0', 'verbose_level': 3, 'region_name': '', u'baremetal_introspection_status_code_retries': '5', 'api_timeout': None, 'image_api_version': '2', 'auth': {'user_domain_name': 'demo', 'project_name': 'admin', 'project_domain_name': 'demo'}, 'default_domain': 'default', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'orchestration_api_version': '1', 'timing': False, 'password': '***', 'cacert': None, 'key_manager_api_version': '1', 'workflow_api_version': '2', u'baremetal_status_code_retries': '5', 'identity_api_version': '3', 'deferred_help': False, 'cert': None, u'secgroup_source': u'neutron', u'status': u'active', 'alarming_api_version': '2', 'debug': True, u'interface': 'public', u'disable_vendor_agent': {}}
command: token issue -> openstackclient.identity.v3.token.IssueToken (auth=True)
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'image_status_code_retries': '5', 'key': None, 'database_api_version': '1', 'data_processing_api_version': '1.1', 'auth_url': 'http://controller:5000/v3', 'additional_user_agent': [('osc-lib', '1.14.1')], u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], 'queues_api_version': '2', 'verify': True, 'dns_api_version': '2', u'object_store_api_version': u'1', 'username': 'admin', 'container_infra_api_version': '1', 'loadbalancer_api_version': '2.0', 'verbose_level': 3, 'region_name': '', u'baremetal_introspection_status_code_retries': '5', 'api_timeout': None, 'image_api_version': '2', 'auth': {'user_domain_name': 'demo', 'project_name': 'admin', 'project_domain_name': 'demo'}, 'default_domain': 'default', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'orchestration_api_version': '1', 'timing': False, 'password': '***', 'cacert': None, 'key_manager_api_version': '1', 'workflow_api_version': '2', u'baremetal_status_code_retries': '5', 'identity_api_version': '3', 'deferred_help': False, 'cert': None, u'secgroup_source': u'neutron', u'status': u'active', 'alarming_api_version': '2', 'debug': True, u'interface': 'public', u'disable_vendor_agent': {}}
Using auth plugin: password
Using parameters {'username': 'admin', 'project_name': 'admin', 'user_domain_name': 'demo', 'auth_url': 'http://controller:5000/v3', 'password': '***', 'project_domain_name': 'demo'}
Get auth_ref
REQ: curl -g -i -X GET http://controller:5000/v3 -H "Accept: application/json" -H "User-Agent: openstacksdk/0.36.4 keystoneauth1/3.17.3 python-requests/2.21.0 CPython/2.7.5"
Starting new HTTP connection (1): controller:5000
http://controller:5000 "GET /v3 HTTP/1.1" 200 250
RESP: [200] Connection: Keep-Alive Content-Length: 250 Content-Type: application/json Date: Tue, 12 Jul 2022 03:19:49 GMT Keep-Alive: timeout=5, max=100 Server: Apache/2.4.6 (CentOS) mod_wsgi/3.4 Python/2.7.5 Vary: X-Auth-Token x-openstack-request-id: req-88e96315-9c75-4cfa-9d29-f63d2991274e
RESP BODY: {"version": {"status": "stable", "updated": "2019-07-19T00:00:00Z", "media-types": [{"base": "application/json", "type": "application/vnd.openstack.identity-v3+json"}], "id": "v3.13", "links": [{"href": "http://controller:5000/v3/", "rel": "self"}]}}
GET call to http://controller:5000/v3 used request id req-88e96315-9c75-4cfa-9d29-f63d2991274e
Making authentication request to http://controller:5000/v3/auth/tokens
http://controller:5000 "POST /v3/auth/tokens HTTP/1.1" 201 6618
{"token": {"is_domain": false, "methods": ["password"], "roles": [{"id": "c3cb238a2ec6406e94ef9fb624581b21", "name": "admin"}, {"id": "ec55563a06e546c09d7009964a433855", "name": "reader"}, {"id": "89888c57b9ea4a1eb46e5de6134147b0", "name": "member"}], "expires_at": "2022-07-12T04:19:49.000000Z", "project": {"domain": {"id": "08c184632de74034aa6bdea69ceb78d9", "name": "demo"}, "id": "a0c673059a6642efaef370aab5ff342b", "name": "admin"}, "catalog": [{"endpoints": [{"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "141a38b63fbe42a3aff427eb36e016f8"}, {"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "5c86ba40228e48dda862c9549aa6c6b1"}, {"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "cfbb7d6ad5904f2383991d53d457f111"}], "type": "volumev2", "id": "0128b6211ac64b548da92a604465a12e", "name": "cinderv2"}, {"endpoints": [{"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "2fc1841ef9ce49b5a9198d79b7c1d11c"}, {"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "53301214415942418f6982ad3d9e9b29"}, {"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "db0438c9c7264ecebe20851366353465"}], "type": "volumev3", "id": "32f58eedeb9a4ae1a0210694e1056874", "name": "cinderv3"}, {"endpoints": [{"url": "http://controller:9292", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "a8523c105b014040b5a314270120d0a3"}, {"url": "http://controller:9292", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "bd29b7ebd45e48c5b78459f694d4c155"}, {"url": "http://controller:9292", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "df84f33f2c2543b48256df005664664d"}], "type": "image", "id": "45dd81142b904da3bad63eaa1822fd10", "name": "glance"}, {"endpoints": [{"url": "http://controller:8774/v2.1", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "994d0d0622a74234acdf53fb7b06169f"}, {"url": "http://controller:8774/v2.1", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "cd8e7f070b494f5184b1b7b273a53d57"}, {"url": "http://controller:8774/v2.1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "ec354da0e91c4f818bbedfb6419a1696"}], "type": "compute", "id": "6b07a08126244db280c6292794ef3f0d", "name": "nova"}, {"endpoints": [{"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "7303a061bb834bbf8a78cc37ff8b81a2"}, {"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "a2fa84cb57dc46419c53420481071774"}, {"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "b7d59b34848b4c58b7933b66f76fcaa0"}], "type": "orchestration", "id": "9144c2e24b1c4175be4705d62ab2b981", "name": "heat"}, {"endpoints": [{"url": "http://controller:9696", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "13946ec7d2b5431f994067a6280b1e3f"}, {"url": "http://controller:9696", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "59f2de9362024856931cb5acd8dfaee6"}, {"url": "http://controller:9696", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "f65b32c6e74643409b325ea76c590c07"}], "type": "network", "id": "a28ec1474d614f67835f1a0264614681", "name": "neutron"}, {"endpoints": [{"url": "http://controller:5000/v3/", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "3385951a819040d0818b23f5fc4802e7"}, {"url": "http://controller:5000/v3/", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "62cbe0a61b224312a786cd774364276f"}, {"url": "http://controller:5000/v3/", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "b03d1f4bea3b46568116f8797f77054e"}], "type": "identity", "id": "a7ac05e971f14410a3227e98705d7791", "name": "keystone"}, {"endpoints": [{"url": "http://controller:8080/v1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "259c1668774b405486d2f891984ee540"}, {"url": "http://controller:8080/v1/AUTH_a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "b9222fef8849457cbba663bea6fa31c4"}, {"url": "http://controller:8080/v1/AUTH_a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "e7839789bbf14d0981e5da4d25cb996f"}], "type": "object-store", "id": "b7a59dd9773e45aebb167f20cc5a3e3f", "name": "swift"}, {"endpoints": [{"url": "http://controller:8000/v1", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "0400f720c10b45cf80e6e013f36982ed"}, {"url": "http://controller:8000/v1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "45d4cf0c4b96496d85039eaa83c7bc49"}, {"url": "http://controller:8000/v1", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "880b89772e1b4e4ebcca82dffd6c4d1c"}], "type": "cloudformation", "id": "e0d29e4aa44c477fbf62ffb0bdcc44e2", "name": "heat-cfn"}, {"endpoints": [{"url": "http://controller:8778", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "3233c744e50e4db09024bba35365e750"}, {"url": "http://controller:8778", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "659c2d0052ef41a3be210c8f60f52531"}, {"url": "http://controller:8778", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "6fa0127e8d3e41a098da57d46f02ffda"}], "type": "placement", "id": "f6e0398060ae44bd8ddfe47655c9f1b9", "name": "placement"}], "user": {"domain": {"id": "08c184632de74034aa6bdea69ceb78d9", "name": "demo"}, "password_expires_at": null, "name": "admin", "id": "41914e6b93144f9f8bf868fe63d5031d"}, "audit_ids": ["4NHci14bQD-Gv9rDmv3lew"], "issued_at": "2022-07-12T03:19:49.000000Z"}}
run(Namespace(columns=[], fit_width=False, formatter='table', max_width=0, noindent=False, prefix='', print_empty=False, variables=[]))


```



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

