### 案例准备[RESTful编写Python运维.mp4](https://fdfs.douxuedu.com/group1/M00/00/4B/wKggBmIxsgWEQKs6AAAAAGsgpiU058.mp4)

沿用案例一的all-in-one云主机环境进行实验。

## 简单获取py需要的body json

```shell
##例如创建flavor
##在controller节点执行创建flavor类型的命令
openstack flavor create --disk 10 --ram 512 --vcpus 1 --id 107 test7 --debug
#在下面返回内容中找到POST请求
########################################################################################################
########################################################################################################
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
REQ: curl -g -i -X POST http://controller:8774/v2.1/flavors -H "Accept: application/json" -H "Content-Type: application/json" -H "User-Agent: python-novaclient" -H "X-Auth-Token: {SHA256}7d23660d347284ccadf15715aeacc255d379a45d13e29b9ebddea26271961175" -H "X-OpenStack-Nova-API-Version: 2.1" -d '{"flavor": {"vcpus": 1, "disk": 10, "name": "test7", "os-flavor-access:is_public": true, "rxtx_factor": 1.0, "OS-FLV-EXT-DATA:ephemeral": 0, "ram": 512, "id": "107", "swap": 0}}'
↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
########################################################################################################
########################################################################################################
##
##可以直接放在body里，有错误需要把"os-flavor-access:is_public":true改为True
```



```sh
START with options: flavor create --disk 10 --ram 512 --vcpus 1 --id 107 test7 --debug
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
command: flavor create -> openstackclient.compute.v2.flavor.CreateFlavor (auth=True)
Auth plugin password selected
auth_config_hook(): {'auth_type': 'password', 'beta_command': False, u'image_status_code_retries': '5', 'key': None, 'database_api_version': '1', 'data_processing_api_version': '1.1', 'auth_url': 'http://controller:5000/v3', 'additional_user_agent': [('osc-lib', '1.14.1')], u'network_api_version': u'2', u'message': u'', u'image_format': u'qcow2', 'networks': [], 'queues_api_version': '2', 'verify': True, 'dns_api_version': '2', u'object_store_api_version': u'1', 'username': 'admin', 'container_infra_api_version': '1', 'loadbalancer_api_version': '2.0', 'verbose_level': 3, 'region_name': '', u'baremetal_introspection_status_code_retries': '5', 'api_timeout': None, 'image_api_version': '2', 'auth': {'user_domain_name': 'demo', 'project_name': 'admin', 'project_domain_name': 'demo'}, 'default_domain': 'default', u'image_api_use_tasks': False, u'floating_ip_source': u'neutron', 'orchestration_api_version': '1', 'timing': False, 'password': '***', 'cacert': None, 'key_manager_api_version': '1', 'workflow_api_version': '2', u'baremetal_status_code_retries': '5', 'identity_api_version': '3', 'deferred_help': False, 'cert': None, u'secgroup_source': u'neutron', u'status': u'active', 'alarming_api_version': '2', 'debug': True, u'interface': 'public', u'disable_vendor_agent': {}}
Using auth plugin: password
Using parameters {'username': 'admin', 'project_name': 'admin', 'user_domain_name': 'demo', 'auth_url': 'http://controller:5000/v3', 'password': '***', 'project_domain_name': 'demo'}
Get auth_ref
REQ: curl -g -i -X GET http://controller:5000/v3 -H "Accept: application/json" -H "User-Agent: openstacksdk/0.36.4 keystoneauth1/3.17.3 python-requests/2.21.0 CPython/2.7.5"
Starting new HTTP connection (1): controller:5000
http://controller:5000 "GET /v3 HTTP/1.1" 200 250
RESP: [200] Connection: Keep-Alive Content-Length: 250 Content-Type: application/json Date: Wed, 13 Jul 2022 00:58:50 GMT Keep-Alive: timeout=5, max=100 Server: Apache/2.4.6 (CentOS) mod_wsgi/3.4 Python/2.7.5 Vary: X-Auth-Token x-openstack-request-id: req-bd33d9a9-db71-49d6-adfb-091357ef094e
RESP BODY: {"version": {"status": "stable", "updated": "2019-07-19T00:00:00Z", "media-types": [{"base": "application/json", "type": "application/vnd.openstack.identity-v3+json"}], "id": "v3.13", "links": [{"href": "http://controller:5000/v3/", "rel": "self"}]}}
GET call to http://controller:5000/v3 used request id req-bd33d9a9-db71-49d6-adfb-091357ef094e
Making authentication request to http://controller:5000/v3/auth/tokens
http://controller:5000 "POST /v3/auth/tokens HTTP/1.1" 201 6618
{"token": {"is_domain": false, "methods": ["password"], "roles": [{"id": "c3cb238a2ec6406e94ef9fb624581b21", "name": "admin"}, {"id": "ec55563a06e546c09d7009964a433855", "name": "reader"}, {"id": "89888c57b9ea4a1eb46e5de6134147b0", "name": "member"}], "expires_at": "2022-07-13T01:58:57.000000Z", "project": {"domain": {"id": "08c184632de74034aa6bdea69ceb78d9", "name": "demo"}, "id": "a0c673059a6642efaef370aab5ff342b", "name": "admin"}, "catalog": [{"endpoints": [{"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "141a38b63fbe42a3aff427eb36e016f8"}, {"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "5c86ba40228e48dda862c9549aa6c6b1"}, {"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "cfbb7d6ad5904f2383991d53d457f111"}], "type": "volumev2", "id": "0128b6211ac64b548da92a604465a12e", "name": "cinderv2"}, {"endpoints": [{"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "2fc1841ef9ce49b5a9198d79b7c1d11c"}, {"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "53301214415942418f6982ad3d9e9b29"}, {"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "db0438c9c7264ecebe20851366353465"}], "type": "volumev3", "id": "32f58eedeb9a4ae1a0210694e1056874", "name": "cinderv3"}, {"endpoints": [{"url": "http://controller:9292", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "a8523c105b014040b5a314270120d0a3"}, {"url": "http://controller:9292", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "bd29b7ebd45e48c5b78459f694d4c155"}, {"url": "http://controller:9292", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "df84f33f2c2543b48256df005664664d"}], "type": "image", "id": "45dd81142b904da3bad63eaa1822fd10", "name": "glance"}, {"endpoints": [{"url": "http://controller:8774/v2.1", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "994d0d0622a74234acdf53fb7b06169f"}, {"url": "http://controller:8774/v2.1", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "cd8e7f070b494f5184b1b7b273a53d57"}, {"url": "http://controller:8774/v2.1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "ec354da0e91c4f818bbedfb6419a1696"}], "type": "compute", "id": "6b07a08126244db280c6292794ef3f0d", "name": "nova"}, {"endpoints": [{"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "7303a061bb834bbf8a78cc37ff8b81a2"}, {"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "a2fa84cb57dc46419c53420481071774"}, {"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "b7d59b34848b4c58b7933b66f76fcaa0"}], "type": "orchestration", "id": "9144c2e24b1c4175be4705d62ab2b981", "name": "heat"}, {"endpoints": [{"url": "http://controller:9696", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "13946ec7d2b5431f994067a6280b1e3f"}, {"url": "http://controller:9696", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "59f2de9362024856931cb5acd8dfaee6"}, {"url": "http://controller:9696", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "f65b32c6e74643409b325ea76c590c07"}], "type": "network", "id": "a28ec1474d614f67835f1a0264614681", "name": "neutron"}, {"endpoints": [{"url": "http://controller:5000/v3/", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "3385951a819040d0818b23f5fc4802e7"}, {"url": "http://controller:5000/v3/", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "62cbe0a61b224312a786cd774364276f"}, {"url": "http://controller:5000/v3/", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "b03d1f4bea3b46568116f8797f77054e"}], "type": "identity", "id": "a7ac05e971f14410a3227e98705d7791", "name": "keystone"}, {"endpoints": [{"url": "http://controller:8080/v1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "259c1668774b405486d2f891984ee540"}, {"url": "http://controller:8080/v1/AUTH_a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "b9222fef8849457cbba663bea6fa31c4"}, {"url": "http://controller:8080/v1/AUTH_a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "e7839789bbf14d0981e5da4d25cb996f"}], "type": "object-store", "id": "b7a59dd9773e45aebb167f20cc5a3e3f", "name": "swift"}, {"endpoints": [{"url": "http://controller:8000/v1", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "0400f720c10b45cf80e6e013f36982ed"}, {"url": "http://controller:8000/v1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "45d4cf0c4b96496d85039eaa83c7bc49"}, {"url": "http://controller:8000/v1", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "880b89772e1b4e4ebcca82dffd6c4d1c"}], "type": "cloudformation", "id": "e0d29e4aa44c477fbf62ffb0bdcc44e2", "name": "heat-cfn"}, {"endpoints": [{"url": "http://controller:8778", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "3233c744e50e4db09024bba35365e750"}, {"url": "http://controller:8778", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "659c2d0052ef41a3be210c8f60f52531"}, {"url": "http://controller:8778", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "6fa0127e8d3e41a098da57d46f02ffda"}], "type": "placement", "id": "f6e0398060ae44bd8ddfe47655c9f1b9", "name": "placement"}], "user": {"domain": {"id": "08c184632de74034aa6bdea69ceb78d9", "name": "demo"}, "password_expires_at": null, "name": "admin", "id": "41914e6b93144f9f8bf868fe63d5031d"}, "audit_ids": ["gXmvLHjNTlahn-XjfHzOqg"], "issued_at": "2022-07-13T00:58:57.000000Z"}}
run(Namespace(columns=[], description=None, disk=10, ephemeral=0, fit_width=False, formatter='table', id=u'107', max_width=0, name=u'test7', noindent=False, prefix='', print_empty=False, project=None, project_domain=None, property=None, public=True, ram=512, rxtx_factor=1.0, swap=0, variables=[], vcpus=1))
Instantiating compute client for API Version Major: 2, Minor: 1
Instantiating compute api: <class 'openstackclient.api.compute_v2.APIv2'>
Instantiating identity client: <class 'keystoneclient.v3.client.Client'>
Making authentication request to http://controller:5000/v3/auth/tokens
http://controller:5000 "POST /v3/auth/tokens HTTP/1.1" 201 6618
{"token": {"is_domain": false, "methods": ["password"], "roles": [{"id": "c3cb238a2ec6406e94ef9fb624581b21", "name": "admin"}, {"id": "ec55563a06e546c09d7009964a433855", "name": "reader"}, {"id": "89888c57b9ea4a1eb46e5de6134147b0", "name": "member"}], "expires_at": "2022-07-13T01:59:04.000000Z", "project": {"domain": {"id": "08c184632de74034aa6bdea69ceb78d9", "name": "demo"}, "id": "a0c673059a6642efaef370aab5ff342b", "name": "admin"}, "catalog": [{"endpoints": [{"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "141a38b63fbe42a3aff427eb36e016f8"}, {"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "5c86ba40228e48dda862c9549aa6c6b1"}, {"url": "http://controller:8776/v2/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "cfbb7d6ad5904f2383991d53d457f111"}], "type": "volumev2", "id": "0128b6211ac64b548da92a604465a12e", "name": "cinderv2"}, {"endpoints": [{"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "2fc1841ef9ce49b5a9198d79b7c1d11c"}, {"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "53301214415942418f6982ad3d9e9b29"}, {"url": "http://controller:8776/v3/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "db0438c9c7264ecebe20851366353465"}], "type": "volumev3", "id": "32f58eedeb9a4ae1a0210694e1056874", "name": "cinderv3"}, {"endpoints": [{"url": "http://controller:9292", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "a8523c105b014040b5a314270120d0a3"}, {"url": "http://controller:9292", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "bd29b7ebd45e48c5b78459f694d4c155"}, {"url": "http://controller:9292", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "df84f33f2c2543b48256df005664664d"}], "type": "image", "id": "45dd81142b904da3bad63eaa1822fd10", "name": "glance"}, {"endpoints": [{"url": "http://controller:8774/v2.1", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "994d0d0622a74234acdf53fb7b06169f"}, {"url": "http://controller:8774/v2.1", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "cd8e7f070b494f5184b1b7b273a53d57"}, {"url": "http://controller:8774/v2.1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "ec354da0e91c4f818bbedfb6419a1696"}], "type": "compute", "id": "6b07a08126244db280c6292794ef3f0d", "name": "nova"}, {"endpoints": [{"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "7303a061bb834bbf8a78cc37ff8b81a2"}, {"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "a2fa84cb57dc46419c53420481071774"}, {"url": "http://controller:8004/v1/a0c673059a6642efaef370aab5ff342b", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "b7d59b34848b4c58b7933b66f76fcaa0"}], "type": "orchestration", "id": "9144c2e24b1c4175be4705d62ab2b981", "name": "heat"}, {"endpoints": [{"url": "http://controller:9696", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "13946ec7d2b5431f994067a6280b1e3f"}, {"url": "http://controller:9696", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "59f2de9362024856931cb5acd8dfaee6"}, {"url": "http://controller:9696", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "f65b32c6e74643409b325ea76c590c07"}], "type": "network", "id": "a28ec1474d614f67835f1a0264614681", "name": "neutron"}, {"endpoints": [{"url": "http://controller:5000/v3/", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "3385951a819040d0818b23f5fc4802e7"}, {"url": "http://controller:5000/v3/", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "62cbe0a61b224312a786cd774364276f"}, {"url": "http://controller:5000/v3/", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "b03d1f4bea3b46568116f8797f77054e"}], "type": "identity", "id": "a7ac05e971f14410a3227e98705d7791", "name": "keystone"}, {"endpoints": [{"url": "http://controller:8080/v1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "259c1668774b405486d2f891984ee540"}, {"url": "http://controller:8080/v1/AUTH_a0c673059a6642efaef370aab5ff342b", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "b9222fef8849457cbba663bea6fa31c4"}, {"url": "http://controller:8080/v1/AUTH_a0c673059a6642efaef370aab5ff342b", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "e7839789bbf14d0981e5da4d25cb996f"}], "type": "object-store", "id": "b7a59dd9773e45aebb167f20cc5a3e3f", "name": "swift"}, {"endpoints": [{"url": "http://controller:8000/v1", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "0400f720c10b45cf80e6e013f36982ed"}, {"url": "http://controller:8000/v1", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "45d4cf0c4b96496d85039eaa83c7bc49"}, {"url": "http://controller:8000/v1", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "880b89772e1b4e4ebcca82dffd6c4d1c"}], "type": "cloudformation", "id": "e0d29e4aa44c477fbf62ffb0bdcc44e2", "name": "heat-cfn"}, {"endpoints": [{"url": "http://controller:8778", "interface": "public", "region": "RegionOne", "region_id": "RegionOne", "id": "3233c744e50e4db09024bba35365e750"}, {"url": "http://controller:8778", "interface": "admin", "region": "RegionOne", "region_id": "RegionOne", "id": "659c2d0052ef41a3be210c8f60f52531"}, {"url": "http://controller:8778", "interface": "internal", "region": "RegionOne", "region_id": "RegionOne", "id": "6fa0127e8d3e41a098da57d46f02ffda"}], "type": "placement", "id": "f6e0398060ae44bd8ddfe47655c9f1b9", "name": "placement"}], "user": {"domain": {"id": "08c184632de74034aa6bdea69ceb78d9", "name": "demo"}, "password_expires_at": null, "name": "admin", "id": "41914e6b93144f9f8bf868fe63d5031d"}, "audit_ids": ["A_Rdf_ljTeiJLRCV5FZ06g"], "issued_at": "2022-07-13T00:59:04.000000Z"}}
########################################################################################################
#######################################在这里############################################################
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
REQ: curl -g -i -X POST http://controller:8774/v2.1/flavors -H "Accept: application/json" -H "Content-Type: application/json" -H "User-Agent: python-novaclient" -H "X-Auth-Token: {SHA256}7d23660d347284ccadf15715aeacc255d379a45d13e29b9ebddea26271961175" -H "X-OpenStack-Nova-API-Version: 2.1" -d '{"flavor": {"vcpus": 1, "disk": 10, "name": "test7", "os-flavor-access:is_public": true, "rxtx_factor": 1.0, "OS-FLV-EXT-DATA:ephemeral": 0, "ram": 512, "id": "107", "swap": 0}}'
↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
######################################在这里#############################################################
########################################################################################################
Starting new HTTP connection (1): controller:8774
http://controller:8774 "POST /v2.1/flavors HTTP/1.1" 200 359
RESP: [200] Connection: keep-alive Content-Length: 359 Content-Type: application/json Date: Wed, 13 Jul 2022 00:59:10 GMT Openstack-Api-Version: compute 2.1 Vary: OpenStack-API-Version, X-OpenStack-Nova-API-Version X-Compute-Request-Id: req-c9d696aa-ba40-4538-beb9-bcb1d4fa2f43 X-Openstack-Nova-Api-Version: 2.1 X-Openstack-Request-Id: req-c9d696aa-ba40-4538-beb9-bcb1d4fa2f43
RESP BODY: {"flavor": {"links": [{"href": "http://controller:8774/v2.1/flavors/107", "rel": "self"}, {"href": "http://controller:8774/flavors/107", "rel": "bookmark"}], "ram": 512, "OS-FLV-DISABLED:disabled": false, "os-flavor-access:is_public": true, "rxtx_factor": 1.0, "disk": 10, "id": "107", "name": "test7", "vcpus": 1, "swap": "", "OS-FLV-EXT-DATA:ephemeral": 0}}
POST call to compute for http://controller:8774/v2.1/flavors used request id req-c9d696aa-ba40-4538-beb9-bcb1d4fa2f43
REQ: curl -g -i -X GET http://controller:8774/v2.1/flavors/107/os-extra_specs -H "Accept: application/json" -H "User-Agent: python-novaclient" -H "X-Auth-Token: {SHA256}7d23660d347284ccadf15715aeacc255d379a45d13e29b9ebddea26271961175" -H "X-OpenStack-Nova-API-Version: 2.1"
http://controller:8774 "GET /v2.1/flavors/107/os-extra_specs HTTP/1.1" 200 19
RESP: [200] Connection: keep-alive Content-Length: 19 Content-Type: application/json Date: Wed, 13 Jul 2022 00:59:10 GMT Openstack-Api-Version: compute 2.1 Vary: OpenStack-API-Version, X-OpenStack-Nova-API-Version X-Compute-Request-Id: req-3e663fc6-6ae8-46f2-a11f-88e39c11fa03 X-Openstack-Nova-Api-Version: 2.1 X-Openstack-Request-Id: req-3e663fc6-6ae8-46f2-a11f-88e39c11fa03
RESP BODY: {"extra_specs": {}}
GET call to compute for http://controller:8774/v2.1/flavors/107/os-extra_specs used request id req-3e663fc6-6ae8-46f2-a11f-88e39c11fa03
+----------------------------+-------+
| Field                      | Value |
+----------------------------+-------+
| OS-FLV-DISABLED:disabled   | False |
| OS-FLV-EXT-DATA:ephemeral  | 0     |
| disk                       | 10    |
| id                         | 107   |
| name                       | test7 |
| os-flavor-access:is_public | True  |
| properties                 |       |
| ram                        | 512   |
| rxtx_factor                | 1.0   |
| swap                       |       |
| vcpus                      | 1     |
+----------------------------+-------+
clean_up CreateFlavor:
END return value: 0

```





### 案例实施

登录OpenStack平台，可以查看APIs的网站与端口。

```
[root@controller ~]# source /etc/keystone/admin-openrc.sh  
[root@controller ~]# openstack endpoint list -c "Service Name"  -c "Enabled"  -c "URL"  
```

查询Endpoint接口如图1所示：

![image1.png](python%E8%B0%83%E7%94%A8API.assets/wKggBmIvAOmAFyRCAACxYvLPOVM848.png)

图1

#### 1. 认证服务：用户管理

##### （1）接口说明

接口官网：https://docs.openstack.org/api-ref/identity/。
当前版本为V3.0.网站为：https://docs.openstack.org/api-ref/identity/v3/index.html
Identity服务生成访问OpenStack服务REST API的认证令牌。客户端通过向身份验证服务提供有效凭据来获取此令牌（Token）和其他服务API的URL端点。
每次向OpenStack服务请求REST API时，都需要在X-Auth-Token请求头中提供自己的认证令牌（Token）。
和大多数OpenStack项目一样，OpenStack Identity通过基于角色访问控制（RBAC）的方法定义策略规则来保护API。
Identity服务配置文件设置存储这些规则的JSON策略文件的名称和位置。
V3 API为所有GET请求实现了HEAD。 每个HEAD请求包含与对应的GET API相同的报头和HTTP状态代码。
以下以用户管理的Python实现案例，展示如何调用认证服务的APIs。具体APIs参考如下地址（如图2所示）：
https://docs.openstack.org/api-ref/identity/v3/index.html#users

![image2.png](python%E8%B0%83%E7%94%A8API.assets/wKggBmIvAPWAPpZzAABw8rr9M5U969.png)

图2
以下展示User增删查改的管理Python实现代码。
创建用户接口：POST /v3/users
请求参数见表2：
表2 请求参数

| Name                          | In   | Type    | Description  |
| :---------------------------- | :--- | :------ | :----------- |
| user                          | body | object  | 用户         |
| default_project_id (Optional) | body | string  | 项目ID       |
| domain_id (Optional)          | body | string  | 区域ID       |
| federated (Optional)          | body | list    | 用户联邦列表 |
| enabled (Optional)            | body | boolean | 是否启用     |
| name                          | body | string  | 用户名称     |
| password (Optional)           | body | string  | 密码         |
| extra (Optional)              | body | string  | 额外信息     |
| options (Optional)            | body | object  | 选项         |

创建用户body json案例如下：

```json
{  
    "user": {  
        "default_project_id": "263fd9",  
        "domain_id": "1789d1",  
        "enabled": true,  
        "federated": [  
            {  
                "idp_id": "efbab5a6acad4d108fec6c63d9609d83",  
                "protocols": [  
                    {  
                        "protocol_id": "mapped",  
                        "unique_id": "test@example.com"  
                    }  
                ]  
            }  
        ],  
        "name": "James Doe",  
        "password": "secretsecret",  
        "description": "James Doe user",  
        "email": "jdoe@example.com",  
        "options": {  
            "ignore_password_expiry": true  
        }  
    }  
}  
```

其他接口参数基本一致，可以查看每个接口的request与response的数据格式。

##### （2）代码实现

创建apis_user_manager.py文件实现，用户的创建、查找、删除、更新。代码如下：

```python
# Copyright 2021~2022 The Cloud Computing support Teams of ChinaSkills.  
import requests,json,time  
import logging  
#-----------logger-----------  
#get logger  
logger = logging.getLogger(__name__)  
# level  
logger.setLevel(logging.DEBUG)  
# format  
format = logging.Formatter('%(asctime)s %(message)s')  
# to console  
stream_handler  = logging.StreamHandler()  
stream_handler .setFormatter(format)  
logger.addHandler(stream_handler )  
#-----------logger-----------  
def get_auth_token(controller_ip, domain, user, password):  
    '''  
    :param controller_ip: openstack master ip address  
    :param domain: current user's domain  
    :param user: user name  
    :param password: user password  
    :return: keystoen auth Token for current user.  
    '''  
    try:  
        url = f"http://{controller_ip}:5000/v3/auth/tokens"  
        body = {  
                    "auth": {  
                        "identity": {  
                            "methods": [  
                                "password"  
                            ],  
                            "password": {  
                                "user": {  
                                    "domain": {  
                                        "name": domain  
                                    },  
                                    "name": user,  
                                    "password": password  
                                }  
                            }  
                        },  
                        "scope": {  
                            "project": {  
                                "domain": {  
                                    "name": domain  
                                },  
                                "name": user  
                            }  
                        }  
                    }  
                }  
        headers = {  
            "Content-Type": "application/json",  
        }  
        print(body)  
        Token = requests.post(url, data=json.dumps(body), headers=headers).headers['X-Subject-Token']  
        headers = {  
            "X-Auth-Token": Token  
        }  
        logger.debug(f"获取Token值：{str(Token)}")  
        return headers  
    except Exception as e:  
        logger.error(f"获取Token值失败，请检查访问云主机控制节点IP是否正确？输出错误信息如下：{str(e)}")  
        exit(0)  
#用户管理  
# print("代码执行成功")  
class user_manager:  
    def __init__(self, handers: dict, resUrl: str):  
        self.headers = handers  
        self.resUrl = resUrl  
    #      POST  /v3/users  Create user  
    def create_users(self, user_name, password:str, desc:str):  
        """  
        create a user with name and password and description.  
        :param user_name:  
        :param password:  
        :param desc:  
        :return:  
        """  
        body = {  
            "user": {  
                "name": user_name,  
                "password": password,  
                "description": desc,  
            }  
        }  
        status_code = requests.post(self.resUrl, data=json.dumps(body), headers=self.headers).text  
        logger.debug(f"返回状态:{str(status_code)}")  
        return status_code  
    # /v3/users    # List all users  
    def get_users(self):  
        """  
        :return:  
        """  
        status_code =  requests.get(self.resUrl, headers=self.headers).text  
        logger.debug(f"返回状态:{str(status_code)}")  
        return status_code  
    def get_user_id(self, user_name):  
        """  
        get user id by name.  
        :param user_name:  
        :return:  
        """  
        result = json.loads(requests.get(self.resUrl, headers=self.headers).text)  
        user_name = user_name  
        for item in result['users']:  
            if item['name'] == user_name:  
                return item['id']  
        return "NONE"  
    def get_user(self, id:str):  
        """  
        get a flavor by id.  
        :return:  
        """  
        api_url = self.resUrl + "/"+id  
        result = json.loads(requests.get(api_url, headers=self.headers).text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
    def delete_user(self, id:str):  
        """  
         delete a user by id.  
         :return:  
         """  
        api_url = self.resUrl + "/" + id  
        response = requests.delete(api_url, headers=self.headers)  
        # 204 - No ContentThe server has fulfilled the request.  
        if response.status_code == 204:  
            return {"User itemDeletedSuccess": response.status_code}  
        result = json.loads(response.text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
        # http://192.168.200.226:8774/v2.1/ get apis version infomation.  
    def update_User_password(self, id: str, original_password: str, new_password : str):  
        """  
        update a flavor desc by id.  
        :return:  
        """  
        self.headers['Content-Type'] = "application/json"  
        body = {  
            "user": {  
                "password": new_password,  
                "original_password": original_password  
            }  
        }  
        api_url = self.resUrl + "/" + id + "/password"  
        response = requests.post(api_url, data=json.dumps(body), headers=self.headers)  
        # Normal response codes: 204 without return text  
        if response.status_code == 204 :  
            return {"item Update Password Success": response.status_code}  
        result = json.loads(response.text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
if __name__ == '__main__':  
    # 1. openstack allinone （controller ) credentials  
    # host ip address  
    controller_ip = "192.168.200.226"  
    # domain name  
    domain = "demo"  
    # user name  
    user = "admin"  
    # user password  
    password = "000000"  
    headers = get_auth_token(controller_ip,domain,user,password)  
    print("headers:", headers)  
    #get all user  
    user_m = user_manager(headers, f"http://{controller_ip}:5000/v3/users")  
```

##### （3）代码验证

① 登录通过账号密码方式：使用get_auth_token()方法，通过该方法获取Token值。
② 封装了user_manager类，通过python request库实现对API的网络访问，实现对用户的增删查改操作。

- 创建：POST /v3/users
- 查询：get /v3/users
- 删除：delete /v3/users/id
- 更改密码：/v3/users/id/password"

具体可以通过官网的API说明。
③ 执行user_manager的每个方法进行代码测试，通过openstack user命令行或Dashboard界面进行研究者。

修改apis_user_manager.py的if __name__ == ‘__main__’:函数中OpenStack的IP、domain、user、password，执行apis_user_manager.py，进行查询所有、创建、根据ID查询、更新密码和删除验证。在apis_user_manager.py的if __name__ == '__main__'最后添加如下代码：

```
    #get all user  
    user_m = user_manager(headers, f"http://{controller_ip}:5000/v3/users")  
    # 1 查询所有  
    users = user_m.get_users()  
    print("查询所有users:", users)  
    # 2 创建  
    user = user_m.create_users("user_demo", "passw0rd","A user created by python code.")  
    print("创建用户:", user)  
    # get user id by name  
    id = user_m.get_user_id("user_demo")  
    print("User user_demo Id is:", id)  
    #3. 使用ID查询  
    user = user_m.get_user(id)  
    print(f"查询{id}用户:", user)  
    # 4. 更新密码  
    result = user_m.update_User_password(id, "passw0rd", "8assw52d")  
    print(f"更新密码{id}用户:", result)  
    #5. 删除新建用户  
    result = user_m.delete_user(id)  
    print(f"删除{id}用户:", result)  
```

然后执行apis_user_manager.py，结果如下：

```
[root@controller ~]# python3 apis_user_manager.py  
{'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'name': 'demo'}, 'name': 'admin', 'password': '000000'}}}, 'scope': {'project': {'domain': {'name': 'demo'}, 'name': 'admin'}}}}  
2022-03-10 13:24:37,146 获取Token值：gAAAAABiKYoR1bvKz87Qx2H5ULprGbheY3EIWsm6t3ry1St5-B7LFfRddB8VLVwdxY-HSHdMlG-0vcam-UKzfRqHziFXTL7oNPacSfrvk4qiZMqCHKaisI7nETxa9Qrgsd_a0trjCTNWxYgfalGLpBjSfNA4ccCdw_3i3LocRWY2OcJQ3ccPM5w  
headers: {'X-Auth-Token': 'gAAAAABiKYoR1bvKz87Qx2H5ULprGbheY3EIWsm6t3ry1St5-B7LFfRddB8VLVwdxY-HSHdMlG-0vcam-UKzfRqHziFXTL7oNPacSfrvk4qiZMqCHKaisI7nETxa9Qrgsd_a0trjCTNWxYgfalGLpBjSfNA4ccCdw_3i3LocRWY2OcJQ3ccPM5w'}  
2022-03-10 13:24:38,511 返回状态:{"users": [{"name": "admin", "links": {"self": "http://172.128.11.18:5000/v3/users/89f8027475294689ae6c0183fa35bf5a"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "options": {}, "default_project_id": "0b6f2d0be1d342e09edc31dc841db7a5", "id": "89f8027475294689ae6c0183fa35bf5a", "password_expires_at": null}, {"password_expires_at": null, "name": "demo", "links": {"self": "http://172.128.11.18:5000/v3/users/df883f8abb124254a4e04138e92ebad6"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "df883f8abb124254a4e04138e92ebad6", "options": {}}, {"password_expires_at": null, "name": "glance", "links": {"self": "http://172.128.11.18:5000/v3/users/5f149fe240114fb5ae43e6d9ea3585c9"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "5f149fe240114fb5ae43e6d9ea3585c9", "options": {}}, {"password_expires_at": null, "name": "placement", "links": {"self": "http://172.128.11.18:5000/v3/users/c12e3ae6719f4145b45890b4f32b1bde"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "c12e3ae6719f4145b45890b4f32b1bde", "options": {}}, {"password_expires_at": null, "name": "nova", "links": {"self": "http://172.128.11.18:5000/v3/users/214fedb287114f2d8bf09bbb665369bd"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "214fedb287114f2d8bf09bbb665369bd", "options": {}}, {"password_expires_at": null, "name": "neutron", "links": {"self": "http://172.128.11.18:5000/v3/users/a22d0df83e564c17a618429a136aa46d"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "a22d0df83e564c17a618429a136aa46d", "options": {}}, {"password_expires_at": null, "name": "cinder", "links": {"self": "http://172.128.11.18:5000/v3/users/70fd527b01f141d091d240b17ffa7532"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "70fd527b01f141d091d240b17ffa7532", "options": {}}, {"password_expires_at": null, "name": "swift", "links": {"self": "http://172.128.11.18:5000/v3/users/38fca0a11172451ebd4fdd34bab4a62c"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "38fca0a11172451ebd4fdd34bab4a62c", "options": {}}, {"password_expires_at": null, "name": "heat", "links": {"self": "http://172.128.11.18:5000/v3/users/c099073d62754032937dfd422e5253a1"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "c099073d62754032937dfd422e5253a1", "options": {}}, {"password_expires_at": null, "name": "heat_domain_admin", "links": {"self": "http://172.128.11.18:5000/v3/users/ff8b9ec030ba4de8a7b4fd847c94c3c3"}, "domain_id": "e62a73d6033d49e89a0fd711a87f7d7b", "enabled": true, "id": "ff8b9ec030ba4de8a7b4fd847c94c3c3", "options": {}}, {"password_expires_at": null, "name": "ceilometer", "links": {"self": "http://172.128.11.18:5000/v3/users/d35395e5ae554a5ea0fb5c2b5dbb2ba7"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "d35395e5ae554a5ea0fb5c2b5dbb2ba7", "options": {}}, {"password_expires_at": null, "name": "gnocchi", "links": {"self": "http://172.128.11.18:5000/v3/users/90deb816e8ee4ff7ae28d342f6074127"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "90deb816e8ee4ff7ae28d342f6074127", "options": {}}, {"password_expires_at": null, "name": "aodh", "links": {"self": "http://172.128.11.18:5000/v3/users/761b461915464665a29780738d9bb5fa"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "761b461915464665a29780738d9bb5fa", "options": {}}, {"password_expires_at": null, "name": "zun", "links": {"self": "http://172.128.11.18:5000/v3/users/2d8554f24c04452c8ffa9aa216a7c484"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "2d8554f24c04452c8ffa9aa216a7c484", "options": {}}, {"password_expires_at": null, "name": "kuryr", "links": {"self": "http://172.128.11.18:5000/v3/users/e9227d1e10c24ab2872b549157b4d376"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "e9227d1e10c24ab2872b549157b4d376", "options": {}}, {"password_expires_at": null, "name": "octavia", "links": {"self": "http://172.128.11.18:5000/v3/users/6a0958e6e55e4513a5f2451db007a2cc"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "6a0958e6e55e4513a5f2451db007a2cc", "options": {}}, {"password_expires_at": null, "name": "manila", "links": {"self": "http://172.128.11.18:5000/v3/users/77bba8c0d46c44578b8831e3d704ca97"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "77bba8c0d46c44578b8831e3d704ca97", "options": {}}, {"password_expires_at": null, "name": "cloudkitty", "links": {"self": "http://172.128.11.18:5000/v3/users/9f7da13262e44bf58c1bf29ee0318c81"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "9f7da13262e44bf58c1bf29ee0318c81", "options": {}}, {"password_expires_at": null, "name": "barbican", "links": {"self": "http://172.128.11.18:5000/v3/users/38ac5cab65974983b6a01be246e665a9"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "38ac5cab65974983b6a01be246e665a9", "options": {}}], "links": {"self": "http://172.128.11.18:5000/v3/users", "previous": null, "next": null}}  
查询所有users: {"users": [{"name": "admin", "links": {"self": "http://172.128.11.18:5000/v3/users/89f8027475294689ae6c0183fa35bf5a"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "options": {}, "default_project_id": "0b6f2d0be1d342e09edc31dc841db7a5", "id": "89f8027475294689ae6c0183fa35bf5a", "password_expires_at": null}, {"password_expires_at": null, "name": "demo", "links": {"self": "http://172.128.11.18:5000/v3/users/df883f8abb124254a4e04138e92ebad6"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "df883f8abb124254a4e04138e92ebad6", "options": {}}, {"password_expires_at": null, "name": "glance", "links": {"self": "http://172.128.11.18:5000/v3/users/5f149fe240114fb5ae43e6d9ea3585c9"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "5f149fe240114fb5ae43e6d9ea3585c9", "options": {}}, {"password_expires_at": null, "name": "placement", "links": {"self": "http://172.128.11.18:5000/v3/users/c12e3ae6719f4145b45890b4f32b1bde"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "c12e3ae6719f4145b45890b4f32b1bde", "options": {}}, {"password_expires_at": null, "name": "nova", "links": {"self": "http://172.128.11.18:5000/v3/users/214fedb287114f2d8bf09bbb665369bd"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "214fedb287114f2d8bf09bbb665369bd", "options": {}}, {"password_expires_at": null, "name": "neutron", "links": {"self": "http://172.128.11.18:5000/v3/users/a22d0df83e564c17a618429a136aa46d"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "a22d0df83e564c17a618429a136aa46d", "options": {}}, {"password_expires_at": null, "name": "cinder", "links": {"self": "http://172.128.11.18:5000/v3/users/70fd527b01f141d091d240b17ffa7532"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "70fd527b01f141d091d240b17ffa7532", "options": {}}, {"password_expires_at": null, "name": "swift", "links": {"self": "http://172.128.11.18:5000/v3/users/38fca0a11172451ebd4fdd34bab4a62c"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "38fca0a11172451ebd4fdd34bab4a62c", "options": {}}, {"password_expires_at": null, "name": "heat", "links": {"self": "http://172.128.11.18:5000/v3/users/c099073d62754032937dfd422e5253a1"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "c099073d62754032937dfd422e5253a1", "options": {}}, {"password_expires_at": null, "name": "heat_domain_admin", "links": {"self": "http://172.128.11.18:5000/v3/users/ff8b9ec030ba4de8a7b4fd847c94c3c3"}, "domain_id": "e62a73d6033d49e89a0fd711a87f7d7b", "enabled": true, "id": "ff8b9ec030ba4de8a7b4fd847c94c3c3", "options": {}}, {"password_expires_at": null, "name": "ceilometer", "links": {"self": "http://172.128.11.18:5000/v3/users/d35395e5ae554a5ea0fb5c2b5dbb2ba7"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "d35395e5ae554a5ea0fb5c2b5dbb2ba7", "options": {}}, {"password_expires_at": null, "name": "gnocchi", "links": {"self": "http://172.128.11.18:5000/v3/users/90deb816e8ee4ff7ae28d342f6074127"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "90deb816e8ee4ff7ae28d342f6074127", "options": {}}, {"password_expires_at": null, "name": "aodh", "links": {"self": "http://172.128.11.18:5000/v3/users/761b461915464665a29780738d9bb5fa"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "761b461915464665a29780738d9bb5fa", "options": {}}, {"password_expires_at": null, "name": "zun", "links": {"self": "http://172.128.11.18:5000/v3/users/2d8554f24c04452c8ffa9aa216a7c484"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "2d8554f24c04452c8ffa9aa216a7c484", "options": {}}, {"password_expires_at": null, "name": "kuryr", "links": {"self": "http://172.128.11.18:5000/v3/users/e9227d1e10c24ab2872b549157b4d376"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "e9227d1e10c24ab2872b549157b4d376", "options": {}}, {"password_expires_at": null, "name": "octavia", "links": {"self": "http://172.128.11.18:5000/v3/users/6a0958e6e55e4513a5f2451db007a2cc"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "6a0958e6e55e4513a5f2451db007a2cc", "options": {}}, {"password_expires_at": null, "name": "manila", "links": {"self": "http://172.128.11.18:5000/v3/users/77bba8c0d46c44578b8831e3d704ca97"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "77bba8c0d46c44578b8831e3d704ca97", "options": {}}, {"password_expires_at": null, "name": "cloudkitty", "links": {"self": "http://172.128.11.18:5000/v3/users/9f7da13262e44bf58c1bf29ee0318c81"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "9f7da13262e44bf58c1bf29ee0318c81", "options": {}}, {"password_expires_at": null, "name": "barbican", "links": {"self": "http://172.128.11.18:5000/v3/users/38ac5cab65974983b6a01be246e665a9"}, "domain_id": "720f960530dc4e1982ebc7bdfd261f86", "enabled": true, "id": "38ac5cab65974983b6a01be246e665a9", "options": {}}], "links": {"self": "http://172.128.11.18:5000/v3/users", "previous": null, "next": null}}  
创建用户: {"user": {"description": "A user created by python code.", "name": "user_demo", "domain_id": "default", "enabled": true, "links": {"self": "http://172.128.11.18:5000/v3/users/f0a881341365462a930381b82ef378ff"}, "options": {}, "id": "f0a881341365462a930381b82ef378ff", "password_expires_at": null}}  
2022-03-10 13:24:41,724 返回状态:{"user": {"description": "A user created by python code.", "name": "user_demo", "domain_id": "default", "enabled": true, "links": {"self": "http://172.128.11.18:5000/v3/users/f0a881341365462a930381b82ef378ff"}, "options": {}, "id": "f0a881341365462a930381b82ef378ff", "password_expires_at": null}}  
User user_demo Id is: f0a881341365462a930381b82ef378ff  
查询f0a881341365462a930381b82ef378ff用户: {'user': {'description': 'A user created by python code.', 'links': {'self': 'http://172.128.11.18:5000/v3/users/f0a881341365462a930381b82ef378ff'}, 'enabled': True, 'id': 'f0a881341365462a930381b82ef378ff', 'password_expires_at': None, 'options': {}, 'domain_id': 'default', 'name': 'user_demo'}}  
2022-03-10 13:24:44,021 返回信息:{'user': {'description': 'A user created by python code.', 'links': {'self': 'http://172.128.11.18:5000/v3/users/f0a881341365462a930381b82ef378ff'}, 'enabled': True, 'id': 'f0a881341365462a930381b82ef378ff', 'password_expires_at': None, 'options': {}, 'domain_id': 'default', 'name': 'user_demo'}}  
更新密码f0a881341365462a930381b82ef378ff用户: {'item Update Password Success': 204}  
删除f0a881341365462a930381b82ef378ff用户: {'User itemDeletedSuccess': 204}  
Process finished with exit code 0  
```

#### 2. 计算服务：实例类型管理

##### （1）接口说明

计算服务的API官网：
https://docs.openstack.org/api-guide/compute/index.html
Nova项目提供了RESTful HTTP服务：OpenStack Compute API。这些API提供了对计算资源的大规模可伸缩、随需应变、自服务访问能力。
API版本：
在Mitaka发布之后，每个Nova部署都有以下服务端点：

- / -可用版本列表
- /v2 -计算API的第一个版本，使用扩展（称之为计算API v2.0）
- /v2.1 -相同的API，只是使用了微版本

文档只要给出v2.1 API接口说明。
以下以主机类型（flavors）管理为案例，实现Python代码。具体APIs说明参见：https://docs.openstack.org/api-ref/compute/
接口清单如图3所示，涉及查询（Get）、创建（POST）、更新（PUT）与删除（DELETE）。

![image3.png](python%E8%B0%83%E7%94%A8API.assets/wKggBmIvAQuAE6SKAABYbLKm6pU238.png)

图3
具体参看：
https://docs.openstack.org/api-ref/compute/?expanded=list-flavors-detail,list-flavors-with-details-detail
创建Flavor使用接口：POST /flavors。创建flavor需要云管理员（administrators），调用正常响应码为200，错误响应码为badRequest(400), unauthorized(401), forbidden(403), conflict(409)。
请求（Request）参数见表3：
表3 请求（Request）参数说明

| 名称                                  | 位置 | 类型    | 描述                                                         |
| :------------------------------------ | :--- | :------ | :----------------------------------------------------------- |
| flavor                                | body | object  | Flavor一种主机类型。                                         |
| name                                  | body | string  | 名称。                                                       |
| description (Optional)                | body | string  | 描述可选（限制65535字符），自V2.55版本开始。                 |
| id (Optional)                         | body | string  | Flavor的ID，缺省为uuid。                                     |
| ram                                   | body | integer | 内存大小（单位MiB）。                                        |
| disk                                  | body | integer | 磁盘大小（单位GiB）。.                                       |
| vcpus                                 | body | integer | 虚拟CPU个数(vCPUs)。                                         |
| OS-FLV-EXT-DATA:ephemeral (Optional)  | body | integer | 临时磁盘的大小（单位GiB）。                                  |
| swap (Optional)                       | body | integer | 交换磁盘大小，单位为MiB。                                    |
| rxtx_factor (Optional)                | body | float   | 如果网络后端支持QOS扩展，将在端口上设置的接收/发送因子（作为一个浮动）。否则将被忽略。它的默认值是1.0。 |
| os-flavor-access:is_public (Optional) | body | boolean | 主机类型是公用还是项目专有？默认公用。                       |

响应（Response）说明见表4：
表4 响应（Response）说明

| 名称                                | 位置 | 类型    | 描述                                                         |
| :---------------------------------- | :--- | :------ | :----------------------------------------------------------- |
| flavor                              | body | object  | Flavor一种主机类型。                                         |
| name                                | body | string  | 名称。                                                       |
| description                         | body | string  | 描述可选（限制65535字符），自V2.55版本开始。                 |
| id                                  | body | string  | Flavor的ID，缺省为uuid。                                     |
| ram                                 | body | integer | 内存大小（单位MiB）。                                        |
| disk                                | body | integer | 磁盘大小（单位GiB）。.                                       |
| vcpus                               | body | integer | 虚拟CPU个数(vCPUs)。                                         |
| links                               | body | array   | 资源链接。                                                   |
| OS-FLV-EXT-DATA:ephemeral           | body | integer | 交换磁盘大小，单位为MiB。                                    |
| OS-FLV-DISABLED:disabled (Optional) | body | boolean | 是否禁用。通常只对管理用户可见。                             |
| swap                                | body | integer | 交换磁盘大小，单位为MiB。                                    |
| rxtx_factor                         | body | float   | 如果网络后端支持QOS扩展，将在端口上设置的接收/发送因子（作为一个浮动）。否则将被忽略。它的默认值是1.0。 |
| os-flavor-access:is_public          | body | boolean | 主机类型是公用还是项目专有？默认公用。                       |
| extra_specs (Optional)              | body | object  | 额外规格（key、value键值对），自V2.61。                      |

创建Flavor的body json案例：

Example Create Flavor (v2.55) :

```
{  
    "flavor": {  
        "name": "test_flavor",  
        "ram": 1024,  
        "vcpus": 2,  
        "disk": 10,  
        "id": "10",  
        "rxtx_factor": 2.0,  
        "description": "test description"  
    }  
}  
```

Example Create Flavor (v2.75) :

```
{  
    "flavor": {  
        "OS-FLV-DISABLED:disabled": false,  
        "disk": 10,  
        "OS-FLV-EXT-DATA:ephemeral": 0,  
        "os-flavor-access:is_public": true,  
        "id": "10",  
        "links": [  
            {  
                "href": "http://openstack.example.com/v2/6f70656e737461636b20342065766572/flavors/10",  
                "rel": "self"  
            },  
            {  
                "href": "http://openstack.example.com/6f70656e737461636b20342065766572/flavors/10",  
                "rel": "bookmark"  
            }  
        ],  
        "name": "test_flavor",  
        "ram": 1024,  
        "swap": 0,  
        "rxtx_factor": 2.0,  
        "vcpus": 2,  
        "description": "test description",  
        "extra_specs": {}  
    }  
}  
```

其他接口参数基本一致，可以查看每个接口的request与response的数据格式。

##### （2）代码实现

创建apis_flavor_manager.py文件实现，主机类型创建、查找、删除、更新。代码如下：

```
# Copyright 2021~2022 The Cloud Computing support Teams of ChinaSkills.  
import requests,json,time  
import logging  
#-----------logger-----------  
#get logger  
logger = logging.getLogger(__name__)  
# level  
logger.setLevel(logging.DEBUG)  
# format  
format = logging.Formatter('%(asctime)s %(message)s')  
# to console  
stream_handler  = logging.StreamHandler()  
stream_handler .setFormatter(format)  
logger.addHandler(stream_handler )  
#-----------logger-----------  
def get_auth_token(controller_ip, domain, user, password):  
    '''  
    :param controller_ip: openstack master ip address  
    :param domain: current user's domain  
    :param user: user name  
    :param password: user password  
    :return: keystoen auth Token for current user.  
    '''  
    try:  
        url = f"http://{controller_ip}:5000/v3/auth/tokens"  
        body = {  
                    "auth": {  
                        "identity": {  
                            "methods": [  
                                "password"  
                            ],  
                            "password": {  
                                "user": {  
                                    "domain": {  
                                        "name": domain  
                                    },  
                                    "name": user,  
                                    "password": password  
                                }  
                            }  
                        },  
                        "scope": {  
                            "project": {  
                                "domain": {  
                                    "name": domain  
                                },  
                                "name": user  
                            }  
                        }  
                    }  
                }  
        headers = {  
            "Content-Type": "application/json",  
        }  
        print(body)  
        Token = requests.post(url, data=json.dumps(body), headers=headers).headers['X-Subject-Token']  
        headers = {  
            "X-Auth-Token": Token  
        }  
        logger.debug(f"获取Token值：{str(Token)}")  
        return headers  
    except Exception as e:  
        logger.error(f"获取Token值失败，请检查访问云主机控制节点IP是否正确？输出错误信息如下：{str(e)}")  
        exit(0)  
class flavor_manager:  
    def __init__(self,handers:dict,resUrl:str):  
        self.headers=handers  
        self.resUrl=resUrl  
    #创建flavor类型  
    def create_flavor(self,flavor_name:str,ram,vcpus,disk,id):  
        """  
        :param flavor_name:  
        :param ram:  
        :param vcpus:  
        :param disk:  
        :param id:  
        :return status_code:  
        """  
        self.headers['Content-Type']="application/json"  
        body={  
            "flavor":{  
                "name":flavor_name,  
                "ram":ram,  
                "vcpus":vcpus,  
                "disk":disk,  
                "id":id,  
            }  
        }  
        logger.debug(f"创建flavor请求body:{str(body)}")  
        status_code = requests.post(self.resUrl, data=json.dumps(body), headers=self.headers).text  
        logger.debug(f"返回状态:{str(status_code)}")  
        return  status_code  
    #获取all flavors  
    def get_flavors(self):  
        """  
        get all flavors  
        :return:  
        """  
        result = json.loads(requests.get(self.resUrl,headers=self.headers).text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
        # 获取flavor_id  
    def get_flavor(self, id:str):  
        """  
        get a flavor by id.  
        :return:  
        """  
        api_url = self.resUrl + "/"+id  
        result = json.loads(requests.get(api_url, headers=self.headers).text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
    def delete_flavor(self, id:str):  
        """  
        delete a flavor by id.  
        :return:  
        """  
        api_url = self.resUrl + "/"+id  
        response = requests.delete(api_url, headers=self.headers)  
        #Normal response codes: 202 without return text  
        if response.status_code == 202:  
            return {"itemDeletedSuccess": response.status_code}  
        result = json.loads(response.text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
    #http://192.168.200.226:8774/v2.1/ get apis version infomation.  
    def update_flavor_desc(self, id: str, desc:str):  
        """  
        update a flavor desc by id.(需要带小版本号）  
        :return:  
        """  
        # 特别注意：This API is available starting with microversion 2.55.  
        self.headers['X-OpenStack-Nova-API-Version'] = "2.55"  
        self.headers['Content-Type'] = "application/json"  
        body = {  
            "flavor": {  
                "description": desc  
            }  
        }  
        api_url = self.resUrl + "/" + id  
        response = requests.put(api_url, data=json.dumps(body), headers=self.headers)  
        # Normal response codes: 202 without return text  
        if response.status_code == 202:  
            return {"itemUpdateSuccess": response.status_code}  
        result = json.loads(response.text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
if __name__ == '__main__':  
    # 1. openstack allinone （controller ) credentials  
    # host ip address  
    controller_ip = "192.168.200.226"  
    # domain name  
    domain = "demo"  
    # user name  
    user = "admin"  
    # user password  
    password = "000000"  
    headers = get_auth_token(controller_ip,domain,user,password)  
    print("headers:", headers)  
    #. get token  
    flavor_m = flavor_manager(headers, f"http://{controller_ip}:8774/v2.1/flavors")  
```

##### （3）代码验证

① 登录通过账号密码方式：使用get_auth_token()方法，通过该方法获取Token值。
② 封装了flavor_manager类，通过python request库实现对API的网络访问，实现对用户的增删查改操作。

- 创建：POST v2.1/flavors
- 查询：get v2.1/flavors
- 删除：delete v2.1/flavors/id
- 更改密码：put v2.1/flavors/id

具体可以通过官网的API说明。
③ 执行flavor_manager的每个方法进行代码测试，通过openstack flavor命令行或Dashboard界面进行研究者。

修改apis_flavor_manager.py的if __name__ == ‘__main__’:函数中OpenStack的IP、domain、user、password，执行apis_flavor_manager.py，进行查询所有、创建、根据ID查询、更新描述。在apis_flavor_manager.py的 __name__ == '__main__'代码段最后添加如下代码：

```
#. get token  
    flavor_m = flavor_manager(headers, f"http://{controller_ip}:8774/v2.1/flavors")  
    #1 查所有  
    flavors = flavor_m.get_flavors()  
    print("查询所有flavors:", flavors)  
    #  
    #2 如果存在，先删除存在的flavor 100000  
    flavor = flavor_m.delete_flavor("100000")  
    print("查询id=100000 flavor:", flavor)  
    #  
    #3 创建 flavor first 100000  
    # # id 是唯一的  
    status_code = flavor_m.create_flavor(flavor_name="flavor_small", ram=1024, vcpus=1, disk=10, id=100000)  
    print("创建主机类型:", status_code)  
    #4 查询  
    flavor = flavor_m.get_flavor("100000")  
    print("查询id=100000 flavor:", flavor)  
    #  
    #5 更新描述  
    status_code = flavor_m.update_flavor_desc("100000",  "Update description skill_china")  
    print("更新主机类型描述:", status_code)  
    #6 查询  
    flavors = flavor_m.get_flavor("100000")  
    print("查询所有flavors:", flavors)  
    #  
    # print("---------finished------------")  
```

通过OpenStack平台查询镜像ID、FlavorID、网络ID，替换以上参数，然后执行apis_flavor_manager.py，结果如下：

```
[root@controller ~]# python3 apis_flavor_manager.py  
{'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'name': 'demo'}, 'name': 'admin', 'password': '000000'}}}, 'scope': {'project': {'domain': {'name': 'demo'}, 'name': 'admin'}}}}  
headers: {'X-Auth-Token': 'gAAAAABiKYYsaQyAaxh8lleESSUcUz01l-PYNoHMuptZ8sQLRD5hcSG9nPS6e39n1yVi1P6sPv1dfQVH7YAvJnMik5sEHW0ci7B8IDjrTz5hncpKr9xdqNSBskLAuJFBK49iNIj8w4eBF-LWi-vR454wju7zJiULjeWXdTiIDz6mDOJN1HyBwx4'}  
2022-03-10 13:07:59,869 获取Token值：gAAAAABiKYYsaQyAaxh8lleESSUcUz01l-PYNoHMuptZ8sQLRD5hcSG9nPS6e39n1yVi1P6sPv1dfQVH7YAvJnMik5sEHW0ci7B8IDjrTz5hncpKr9xdqNSBskLAuJFBK49iNIj8w4eBF-LWi-vR454wju7zJiULjeWXdTiIDz6mDOJN1HyBwx4  
查询所有flavors: {'flavors': [{'id': '1', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/1', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/1', 'rel': 'bookmark'}], 'name': 'm1.tiny'}, {'id': '2', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/2', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/2', 'rel': 'bookmark'}], 'name': 'm1.small'}, {'id': '3', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/3', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/3', 'rel': 'bookmark'}], 'name': 'm1.medium'}]}  
2022-03-10 13:08:00,454 返回信息:{'flavors': [{'id': '1', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/1', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/1', 'rel': 'bookmark'}], 'name': 'm1.tiny'}, {'id': '2', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/2', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/2', 'rel': 'bookmark'}], 'name': 'm1.small'}, {'id': '3', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/3', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/3', 'rel': 'bookmark'}], 'name': 'm1.medium'}]}  
查询id=100000 flavor: {'itemNotFound': {'message': 'Flavor 100000 could not be found.', 'code': 404}}  
2022-03-10 13:08:00,963 返回信息:{'itemNotFound': {'message': 'Flavor 100000 could not be found.', 'code': 404}}  
2022-03-10 13:08:00,963 创建flavor请求body:{'flavor': {'name': 'flavor_small', 'ram': 1024, 'vcpus': 1, 'disk': 10, 'id': 100000}}  
2022-03-10 13:08:01,516 返回状态:{"flavor": {"links": [{"href": "http://172.128.11.18:8774/v2.1/flavors/100000", "rel": "self"}, {"href": "http://172.128.11.18:8774/flavors/100000", "rel": "bookmark"}], "ram": 1024, "OS-FLV-DISABLED:disabled": false, "os-flavor-access:is_public": true, "rxtx_factor": 1.0, "disk": 10, "id": "100000", "name": "flavor_small", "vcpus": 1, "swap": "", "OS-FLV-EXT-DATA:ephemeral": 0}}  
创建主机类型: {"flavor": {"links": [{"href": "http://172.128.11.18:8774/v2.1/flavors/100000", "rel": "self"}, {"href": "http://172.128.11.18:8774/flavors/100000", "rel": "bookmark"}], "ram": 1024, "OS-FLV-DISABLED:disabled": false, "os-flavor-access:is_public": true, "rxtx_factor": 1.0, "disk": 10, "id": "100000", "name": "flavor_small", "vcpus": 1, "swap": "", "OS-FLV-EXT-DATA:ephemeral": 0}}  
2022-03-10 13:08:02,041 返回信息:{'flavor': {'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/100000', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/100000', 'rel': 'bookmark'}], 'ram': 1024, 'OS-FLV-DISABLED:disabled': False, 'os-flavor-access:is_public': True, 'rxtx_factor': 1.0, 'disk': 10, 'id': '100000', 'name': 'flavor_small', 'vcpus': 1, 'swap': '', 'OS-FLV-EXT-DATA:ephemeral': 0}}  
查询id=100000 flavor: {'flavor': {'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/100000', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/100000', 'rel': 'bookmark'}], 'ram': 1024, 'OS-FLV-DISABLED:disabled': False, 'os-flavor-access:is_public': True, 'rxtx_factor': 1.0, 'disk': 10, 'id': '100000', 'name': 'flavor_small', 'vcpus': 1, 'swap': '', 'OS-FLV-EXT-DATA:ephemeral': 0}}  
更新主机类型描述: {'flavor': {'description': 'Update description skill_china', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/100000', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/100000', 'rel': 'bookmark'}], 'ram': 1024, 'OS-FLV-DISABLED:disabled': False, 'os-flavor-access:is_public': True, 'rxtx_factor': 1.0, 'disk': 10, 'id': '100000', 'name': 'flavor_small', 'vcpus': 1, 'swap': '', 'OS-FLV-EXT-DATA:ephemeral': 0}}  
2022-03-10 13:08:02,522 返回信息:{'flavor': {'description': 'Update description skill_china', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/100000', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/100000', 'rel': 'bookmark'}], 'ram': 1024, 'OS-FLV-DISABLED:disabled': False, 'os-flavor-access:is_public': True, 'rxtx_factor': 1.0, 'disk': 10, 'id': '100000', 'name': 'flavor_small', 'vcpus': 1, 'swap': '', 'OS-FLV-EXT-DATA:ephemeral': 0}}  
查询所有flavors: {'flavor': {'description': 'Update description skill_china', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/100000', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/100000', 'rel': 'bookmark'}], 'ram': 1024, 'OS-FLV-DISABLED:disabled': False, 'os-flavor-access:is_public': True, 'rxtx_factor': 1.0, 'disk': 10, 'id': '100000', 'name': 'flavor_small', 'vcpus': 1, 'swap': '', 'OS-FLV-EXT-DATA:ephemeral': 0}}  
2022-03-10 13:08:02,933 返回信息:{'flavor': {'description': 'Update description skill_china', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/flavors/100000', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/flavors/100000', 'rel': 'bookmark'}], 'ram': 1024, 'OS-FLV-DISABLED:disabled': False, 'os-flavor-access:is_public': True, 'rxtx_factor': 1.0, 'disk': 10, 'id': '100000', 'name': 'flavor_small', 'vcpus': 1, 'swap': '', 'OS-FLV-EXT-DATA:ephemeral': 0}}  
Process finished with exit code 0  
```
```

#### 3. 计算服务：云主机管理

##### （1）接口说明

计算服务的API官网：
https://docs.openstack.org/api-guide/compute/index.html
Nova项目提供了RESTful HTTP服务：OpenStack Compute API。这些API提供了对计算资源的大规模可伸缩、随需应变、自服务访问能力。
API版本：
在Mitaka发布之后，每个Nova部署都应该有以下服务端点：

- / -可用版本列表
- /v2 -计算API的第一个版本，使用扩展（称之为计算API v2.0）
- /v2.1 -相同的API，只是使用了微版本

文档只要给出v2.1 API接口说明。
以下以主机（servers）管理为案例，实现Python代码。具体APIs说明参见：
https://docs.openstack.org/api-ref/compute/
接口清单如图4所示，涉及查询（Get）、创建（POST）、更新（PUT）与删除（DELETE）。

![image4.png](python%E8%B0%83%E7%94%A8API.assets/wKggBmIvAR-AKo-8AADF51QGaU0448.png)

图4
具体参看：https://docs.openstack.org/api-ref/compute/#servers-servers
创建主机接口说明：
创建servers使用接口：POST /servers。创建Server需要租户管理员权限，调用正常响应码为202，错误响应码为badRequest(400), unauthorized(401), forbidden(403), itemNotFound(404),conflict(409)。
请求（Request）说明（主要参数）见表5：
表5请求（Request）参数说明

| 名称                         | 位置 | 类型   | 描述           |
| :--------------------------- | :--- | :----- | :------------- |
| server                       | body | object | 云主机         |
| flavorRef                    | body | string | 云主机类型ID。 |
| name                         | body | string | 名称           |
| networks                     | body | array  | 网络           |
| networks.uuid (Optional)     | body | string | 网络UUID       |
| networks.port (Optional)     | body | string | 网络端口       |
| networks.fixed_ip (Optional) | body | string | 固定IP         |

创建云主机的body json案例如下：

```
{  
    "server" : {  
        "name" : "device-tagging-server",  
        "imageRef": "70a599e0-31e7-49b7-b260-868f441e862b",  
        "flavorRef" : "http://openstack.example.com/flavors/1",  
        "networks" : [{  
            "uuid" : "3cb9bc59-5699-4588-a4b1-b87f96708bc6",  
            "tag": "nic1"  
        }],  
        "block_device_mapping_v2": [{  
            "uuid": "70a599e0-31e7-49b7-b260-868f441e862b",  
            "source_type": "image",  
            "destination_type": "volume",  
            "boot_index": 0,  
            "volume_size": "1",  
            "tag": "disk1"  
        }]  
    }  
}  
```

响应Response见表6：
表6 响应Response参数说明

| 名称                                | 位置 | 类型    | 描述                                                         |
| :---------------------------------- | :--- | :------ | :----------------------------------------------------------- |
| flavor                              | body | object  | Flavor一种主机类型。                                         |
| name                                | body | string  | 名称。                                                       |
| description                         | body | string  | 描述可选（限制65535字符），自V2.55版本开始。                 |
| id                                  | body | string  | Flavor的ID，缺省为uuid。                                     |
| ram                                 | body | integer | 内存大小（单位MiB）。                                        |
| disk                                | body | integer | 磁盘大小（单位GiB）。.                                       |
| vcpus                               | body | integer | 虚拟CPU个数(vCPUs)。                                         |
| links                               | body | array   | 资源链接。                                                   |
| OS-FLV-EXT-DATA:ephemeral           | body | integer | 交换磁盘大小，单位为MiB。                                    |
| OS-FLV-DISABLED:disabled (Optional) | body | boolean | 是否禁用。通常只对管理用户可见。                             |
| swap                                | body | integer | 交换磁盘大小，单位为MiB。                                    |
| rxtx_factor                         | body | float   | 如果网络后端支持QOS扩展，将在端口上设置的接收/发送因子（作为一个浮动）。否则将被忽略。它的默认值是1.0。 |
| os-flavor-access:is_public          | body | boolean | 主机类型是公用还是项目专有？默认公用。                       |
| extra_specs (Optional)              | body | object  | 额外规格(key、value键值对)，自V2.61。                        |

Example Create Flavor (v2.55)：

```
{  
    "flavor": {  
        "name": "test_flavor",  
        "ram": 1024,  
        "vcpus": 2,  
        "disk": 10,  
        "id": "10",  
        "rxtx_factor": 2.0,  
        "description": "test description"  
    }  
}  
```

Example Create Flavor (v2.75)：

```
{  
    "flavor": {  
        "OS-FLV-DISABLED:disabled": false,  
        "disk": 10,  
        "OS-FLV-EXT-DATA:ephemeral": 0,  
        "os-flavor-access:is_public": true,  
        "id": "10",  
        "links": [  
            {  
                "href": "http://openstack.example.com/v2/6f70656e737461636b20342065766572/flavors/10",  
                "rel": "self"  
            },  
            {  
                "href": "http://openstack.example.com/6f70656e737461636b20342065766572/flavors/10",  
                "rel": "bookmark"  
            }  
        ],  
        "name": "test_flavor",  
        "ram": 1024,  
        "swap": 0,  
        "rxtx_factor": 2.0,  
        "vcpus": 2,  
        "description": "test description",  
        "extra_specs": {}  
    }  
}  
```

##### （2）代码实现

创建apis_server_manager.py文件实现，主机类型创建、查找、删除、更新。代码如下：

```
# Copyright 2021~2022 The Cloud Computing support Teams of ChinaSkills.

import requests, json, time
import logging

# -----------logger-----------
# get logger
logger = logging.getLogger(__name__)
# level
logger.setLevel(logging.DEBUG)
# format
format = logging.Formatter('%(asctime)s %(message)s')
# to console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(format)
logger.addHandler(stream_handler)


# -----------logger-----------

def get_auth_token(controller_ip, domain, user, password):
    '''
    :param controller_ip: openstack master ip address
    :param domain: current user's domain
    :param user: user name
    :param password: user password
    :return: keystoen auth Token for current user.
    '''

    try:
        url = f"http://{controller_ip}:5000/v3/auth/tokens"
        body = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "domain": {
                                "name": domain
                            },
                            "name": user,
                            "password": password
                        }
                    }
                },
                "scope": {
                    "project": {
                        "domain": {
                            "name": domain
                        },
                        "name": user
                    }
                }
            }
        }
    
        headers = {
            "Content-Type": "application/json",
        }
        print(body)
        Token = requests.post(url, data=json.dumps(body), headers=headers).headers['X-Subject-Token']
    
        headers = {
            "X-Auth-Token": Token
        }
        logger.debug(f"获取Token值：{str(Token)}")
        return headers
    except Exception as e:
        logger.error(f"获取Token值失败，请检查访问云主机控制节点IP是否正确？输出错误信息如下：{str(e)}")
        exit(0)


# 云主机管理
# https://docs.openstack.org/api-ref/compute/?expanded=#list-servers
class server_manager:
    def __init__(self, handers: dict, resUrl: str):
        self.headers = handers
        self.resUrl = resUrl

        #      POST  v2/servers
    
    def create_server(self, server_name: str, imageRef, flavorRef, networks_id):
        """
        :param server_name:
        :param container_format:
        :param disk_format:
        :return:
        """
        body = {
            "server": {
                "name": server_name,
                "flavorRef": flavorRef,
                "imageRef": imageRef,
                "networks": [{
                    "uuid": networks_id
                }],
            }
        }
    
        # 必须内容 name、flavorRef、networks、imageRef
    
        response = requests.post(self.resUrl, data=json.dumps(body), headers=self.headers)
        logger.debug(response.status_code)
        if response.status_code == 202:
            return {"serverItemCreatedSuccess": response.status_code}
    
        return response.text


    # 获取glance镜像id
    def get_server_id(self, server_name: str):
        result = json.loads(requests.get(self.resUrl, headers=self.headers).text)
        logger.debug(result)
        for item in result['servers']:
            if (item['name'] == server_name):
                return item['id']
        return ""
    # ----------------------------
    # /v2/servers
    # List servers
    def get_servers(self):
        """
    
        :return:
        """
        status_code = requests.get(self.resUrl, headers=self.headers).text
        logger.debug(f"返回状态:{str(status_code)}")
        return status_code
    
    # /v2/servers/{server_id} Show server
    
    def get_server(self, id: str):
        """
        get a flavor by id.
        :return:
        """
        api_url = self.resUrl + "/" + id
        response = requests.get(api_url, headers=self.headers)
        result = json.loads(response.text)
        logger.debug(f"返回信息:{str(result)}")
        return result
    
    # /v2/servers/{server_id} Delete server
    def delete_server(self, id: str):
        """
         delete a user by id.
         :return:
         """
        api_url = self.resUrl + "/" + id
        response = requests.delete(api_url, headers=self.headers)
    
        # 204 - No Content	The server has fulfilled the request.
        if response.status_code == 204:
            return {"server itemDeletedSuccess": response.status_code}
    
        result = json.loads(response.text)
        logger.debug(f"返回信息:{str(result)}")
        return result
    
        # http://192.168.200.226:8774/v2.1/ get apis version infomation.


if __name__ == '__main__':
    # 1. openstack allinone （controller ) credentials
    # host ip address
    controller_ip = "192.168.200.226"
    # domain name
    domain = "demo"
    # user name
    user = "admin"
    # user password
    password = "000000"
    headers = get_auth_token(controller_ip, domain, user, password)
    print("headers:", headers)
```

##### （3）代码验证

① 登录通过账号密码方式：使用get_auth_token()方法，通过该方法获取Token值。
② 封装了server_manager类，通过python request库实现对API的网络访问，实现对用户的增删查改操作。

- 创建：POST v2.1/flavors
- 查询：get v2.1/flavors
- 删除：delete v2.1/flavors/id
- 更改密码：put v2.1/flavors/id

具体可以通过官网的API说明。
③执行server_manager的每个方法进行代码测试，通过openstack server命令行或Dashboard界面进行研究者。
修改apis_server_manager.py的if __name__ == ‘__main__’:函数中OpenStack的IP、domain、user、password，执行apis_server_manager.py，进行查询所有、创建、根据ID查询、更新描述。

```
[root@controller ~]# openstack image list
+-------------------------------------+-----------+--------+
| ID                                  | Name      | Status |
+-------------------------------------+-----------+--------+
|d50222d2-f737-4b47-ba7c-38eaa2418ff0 | cirros    | active |
|038ba49b-ddee-4e0f-8ecb-6f64d2788138 | cirros002 | active |
+-------------------------------------+-----------+--------+
[root@controller ~]# openstack network list
+------------------------------------+------+--------------------------------------+
| ID                                 | Name | Subnets                              |
+------------------------------------+------+--------------------------------------+
|df62ea19-3e33-40bf-9f41-f2c5f343b3e7| net  | a16130c4-79c1-4ae8-9bc3-c167ee009d63 |
+------------------------------------+------+--------------------------------------+
```

在apis_ server *manager.py的 __name*_ == '__main__'代码段最后添加如下代码：

```
server_m = server_manager(headers, f"http://{controller_ip}:8774/v2.1/servers")  
# 1 查所有  
servers = server_m.get_servers()  
print("查询所有servers:", servers)  
print("-----------finished----------")  
#2 创建  
# 通过apis或openstack命令查询网络net1 ID、镜像 cirros ID、主机类型ID m1.tiny 1  
imageRef = "8372926e-517a-4c69-8d24-01e972bbe4a2"  
flavorRef = "1"  
networks_id = "4bd2cb47-d3c4-48ed-afd9-4e4488677c5c"  
networks_name = "net1"  
result = server_m.create_server("server_001",imageRef, flavorRef,networks_id)  
print(f"创建 云主机:", result)  
#2 查询id  
id = server_m.get_server_id(server_name="server_001")  
print("server_001，id为: ", id)  
#3 查一个云主机  
result = server_m.get_server(id)  
print(f"查询{id}云主机:", result)  
# delete a 云主机  
result = server_m.delete_server(id)  
print(f"删除{id}云主机:", result)  
```

然后执行apis_server_manager.py，结果如下：

```
[root@controller ~]# python3 apis_server_manager.py  
{'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'name': 'demo'}, 'name': 'admin', 'password': '000000'}}}, 'scope': {'project': {'domain': {'name': 'demo'}, 'name': 'admin'}}}}  
2022-03-10 13:22:41,080 获取Token值：gAAAAABiKYmdnf1LDjTT0KSaK55jvsrnLWvwHEEXsIIppNx_WcVKliwp-xHnryAgPXBs-tg0fQSs8bwWG9GwFHbZxWqRrseRJUsAlmqbplkExmwOYFdJqnV-yMQp5tStc4fFnctB2jgF-lZS03V9l_0Uza84tFsH-JVhoiy6Hw5xCzm3sUHsNLM  
headers: {'X-Auth-Token': 'gAAAAABiKYmdnf1LDjTT0KSaK55jvsrnLWvwHEEXsIIppNx_WcVKliwp-xHnryAgPXBs-tg0fQSs8bwWG9GwFHbZxWqRrseRJUsAlmqbplkExmwOYFdJqnV-yMQp5tStc4fFnctB2jgF-lZS03V9l_0Uza84tFsH-JVhoiy6Hw5xCzm3sUHsNLM'}  
查询所有servers: {"servers": [{"id": "57b04243-d8fc-4f53-a6ae-3a7271bb920a", "links": [{"href": "http://172.128.11.18:8774/v2.1/servers/57b04243-d8fc-4f53-a6ae-3a7271bb920a", "rel": "self"}, {"href": "http://172.128.11.18:8774/servers/57b04243-d8fc-4f53-a6ae-3a7271bb920a", "rel": "bookmark"}], "name": "test"}]}  
-----------finished----------  
2022-03-10 13:22:41,827 返回状态:{"servers": [{"id": "57b04243-d8fc-4f53-a6ae-3a7271bb920a", "links": [{"href": "http://172.128.11.18:8774/v2.1/servers/57b04243-d8fc-4f53-a6ae-3a7271bb920a", "rel": "self"}, {"href": "http://172.128.11.18:8774/servers/57b04243-d8fc-4f53-a6ae-3a7271bb920a", "rel": "bookmark"}], "name": "test"}]}  
2022-03-10 13:22:49,752 202  
创建 云主机: {'serverItemCreatedSuccess': 202}  
server_001，id为:  3c636f98-91ab-4b44-8de8-21ff04e56875  
2022-03-10 13:22:50,895 {'servers': [{'id': '3c636f98-91ab-4b44-8de8-21ff04e56875', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/servers/3c636f98-91ab-4b44-8de8-21ff04e56875', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/servers/3c636f98-91ab-4b44-8de8-21ff04e56875', 'rel': 'bookmark'}], 'name': 'server_001'}, {'id': '57b04243-d8fc-4f53-a6ae-3a7271bb920a', 'links': [{'href': 'http://172.128.11.18:8774/v2.1/servers/57b04243-d8fc-4f53-a6ae-3a7271bb920a', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/servers/57b04243-d8fc-4f53-a6ae-3a7271bb920a', 'rel': 'bookmark'}], 'name': 'test'}]}  
2022-03-10 13:22:52,828 返回信息:{'server': {'OS-EXT-STS:task_state': 'scheduling', 'addresses': {}, 'links': [{'href': 'http://172.128.11.18:8774/v2.1/servers/3c636f98-91ab-4b44-8de8-21ff04e56875', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/servers/3c636f98-91ab-4b44-8de8-21ff04e56875', 'rel': 'bookmark'}], 'image': {'id': 'd50222d2-f737-4b47-ba7c-38eaa2418ff0', 'links': [{'href': 'http://172.128.11.18:8774/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0', 'rel': 'bookmark'}]}, 'OS-EXT-STS:vm_state': 'building', 'OS-EXT-SRV-ATTR:instance_name': '', 'OS-SRV-USG:launched_at': None, 'flavor': {'id': '1', 'links': [{'href': 'http://172.128.11.18:8774/flavors/1', 'rel': 'bookmark'}]}, 'id': '3c636f98-91ab-4b44-8de8-21ff04e56875', 'user_id': '89f8027475294689ae6c0183fa35bf5a', 'OS-DCF:diskConfig': 'MANUAL', 'accessIPv4': '', 'accessIPv6': '', 'progress': 0, 'OS-EXT-STS:power_state': 0, 'OS-EXT-AZ:availability_zone': '', 'config_drive': '', 'status': 'BUILD', 'updated': '2022-03-10T05:16:23Z', 'hostId': '', 'OS-EXT-SRV-ATTR:host': None, 'OS-SRV-USG:terminated_at': None, 'key_name': None, 'OS-EXT-SRV-ATTR:hypervisor_hostname': None, 'name': 'server_001', 'created': '2022-03-10T05:16:22Z', 'tenant_id': '0b6f2d0be1d342e09edc31dc841db7a5', 'os-extended-volumes:volumes_attached': [], 'metadata': {}}}  
查询3c636f98-91ab-4b44-8de8-21ff04e56875云主机: {'server': {'OS-EXT-STS:task_state': 'scheduling', 'addresses': {}, 'links': [{'href': 'http://172.128.11.18:8774/v2.1/servers/3c636f98-91ab-4b44-8de8-21ff04e56875', 'rel': 'self'}, {'href': 'http://172.128.11.18:8774/servers/3c636f98-91ab-4b44-8de8-21ff04e56875', 'rel': 'bookmark'}], 'image': {'id': 'd50222d2-f737-4b47-ba7c-38eaa2418ff0', 'links': [{'href': 'http://172.128.11.18:8774/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0', 'rel': 'bookmark'}]}, 'OS-EXT-STS:vm_state': 'building', 'OS-EXT-SRV-ATTR:instance_name': '', 'OS-SRV-USG:launched_at': None, 'flavor': {'id': '1', 'links': [{'href': 'http://172.128.11.18:8774/flavors/1', 'rel': 'bookmark'}]}, 'id': '3c636f98-91ab-4b44-8de8-21ff04e56875', 'user_id': '89f8027475294689ae6c0183fa35bf5a', 'OS-DCF:diskConfig': 'MANUAL', 'accessIPv4': '', 'accessIPv6': '', 'progress': 0, 'OS-EXT-STS:power_state': 0, 'OS-EXT-AZ:availability_zone': '', 'config_drive': '', 'status': 'BUILD', 'updated': '2022-03-10T05:16:23Z', 'hostId': '', 'OS-EXT-SRV-ATTR:host': None, 'OS-SRV-USG:terminated_at': None, 'key_name': None, 'OS-EXT-SRV-ATTR:hypervisor_hostname': None, 'name': 'server_001', 'created': '2022-03-10T05:16:22Z', 'tenant_id': '0b6f2d0be1d342e09edc31dc841db7a5', 'os-extended-volumes:volumes_attached': [], 'metadata': {}}}  
Process finished with exit code 0  
```

#### 4. 镜像管理代码

##### （1）接口说明

镜像(glance)服务的API官网：
https://docs.openstack.org/api-ref/image/v2/index.html
Glance项目提供了RESTful HTTP服务：OpenStack Image Serivce API。
以下以镜像（images）管理为案例，实现Python代码。具体APIs接口清单如图5所示，涉及查询（Get）、创建（POST）、更新（PUT）与删除（DELETE）。

![image5.png](python%E8%B0%83%E7%94%A8API.assets/wKggBmIvATKAXjU4AACI7onSfZY244.png)

图5
具体参看：
https://docs.openstack.org/api-ref/compute/?expanded=list-images-detail
创建镜像接口说明：POST /v2/images
创建镜像调用正常响应码为201，错误响应码为400，401，403，409，413， 415。
请求（Request）说明见表7：
表7 请求（Request）说明

| 名称                        | 位置 | 类型    | 描述                                                         |
| :-------------------------- | :--- | :------ | :----------------------------------------------------------- |
| container_format (Optional) | body | enum    | 容器格式，如：ami，ari，aki，bare，ovf，ova，或docker。      |
| disk_format (Optional)      | body | enum    | 磁盘格式，如：ami，ari，aki，vhd，vhdx，vmdk，raw，qcow2，vdi，ploop或iso。 |
| id (Optional)               | body | string  | 镜像ID（UUID格式）。                                         |
| min_disk (Optional)         | body | integer | 最小磁盘大小（GB单位）。                                     |
| min_ram (Optional)          | body | integer | 最小内存大小（MB单位）。                                     |
| name (Optional)             | body | string  | 名称。                                                       |
| protected (Optional)        | body | boolean | 是否包含不被删除。                                           |
| tags (Optional)             | body | array   | 标签                                                         |
| visibility (Optional)       | body | string  | 开放性（公开、私有、共享）。                                 |

请求案例代码如下：

```
{  
    "container_format": "bare",  
    "disk_format": "raw",  
    "name": "Ubuntu",  
    "id": "b2173dd3-7ad6-4362-baa6-a68bce3565cb"  
}  
```

响应信息见表8：
表8 响应信息

| 名称                                      | 位置   | 类型    | 描述                                                |
| :---------------------------------------- | :----- | :------ | :-------------------------------------------------- |
| Location                                  | header | string  | 镜像文件URL路径                                     |
| OpenStack-image-import-methods (Optional) | header | string  | Import方法（自v2.6增加）。                          |
| OpenStack-image-store-ids (Optional)      | header | string  | 后端存储ID。                                        |
| checksum                                  | body   | string  | 检验Hash码。                                        |
| container_format                          | body   | enum    | 容器格式。                                          |
| created_at                                | body   | string  | 创建时间。                                          |
| disk_format                               | body   | enum    | 磁盘格式。                                          |
| file                                      | body   | string  | 虚拟机镜像文件URL地址。                             |
| id                                        | body   | string  | 镜像ID（UUID格式）。                                |
| min_disk                                  | body   | integer | 最小磁盘大小（GB单位）。                            |
| min_ram                                   | body   | integer | 最小内存大小（MB单位）。                            |
| name                                      | body   | string  | 名称。                                              |
| os_hash_algo                              | body   | string  | 计算图像数据的安全哈希值的算法（自v2.7增加）。      |
| os_hash_value                             | body   | string  | 计算的图像数据的安全哈希的hexdigest（自v2.7增加）。 |
| os_hidden                                 | body   | boolean | 是否隐藏（自v2.7增加）。                            |
| owner                                     | body   | string  | 所有者的标识符。                                    |
| protected                                 | body   | boolean | 是否保护。                                          |
| schema                                    | body   | string  | 描述虚拟机映像的schema URL。                        |
| self                                      | body   | string  | 虚拟机镜像的URL。                                   |
| size                                      | body   | integer | 镜像数据大学（bytes）。                             |
| status                                    | body   | string  | 状态                                                |
| tags                                      | body   | array   | 标签                                                |
| updated_at                                | body   | string  | 更新日期。                                          |
| virtual_size                              | body   | integer | 虚拟大小                                            |
| visibility                                | body   | string  | 开放性（公开、私有、共享）。                        |
| direct_url (Optional)                     | body   | string  | 访问保存在外部存储中的映像文件URL。                 |
| locations (Optional)                      | body   | array   | 地址。                                              |

响应（Response）案例：

```
{  
    "status": "queued",  
    "name": "Ubuntu",  
    "tags": [],  
    "container_format": "bare",  
    "created_at": "2015-11-29T22:21:42Z",  
    "size": null,  
    "disk_format": "raw",  
    "updated_at": "2015-11-29T22:21:42Z",  
    "visibility": "private",  
    "locations": [],  
    "self": "/v2/images/b2173dd3-7ad6-4362-baa6-a68bce3565cb",  
    "min_disk": 0,  
    "protected": false,  
    "id": "b2173dd3-7ad6-4362-baa6-a68bce3565cb",  
    "file": "/v2/images/b2173dd3-7ad6-4362-baa6-a68bce3565cb/file",  
    "checksum": null,  
    "os_hash_algo": null,  
    "os_hash_value": null,  
    "os_hidden": false,  
    "owner": "bab7d5c60cd041a0a36f7c4b6e1dd978",  
    "virtual_size": null,  
    "min_ram": 0,  
    "schema": "/v2/schemas/image"  
}  
```

其他接口的参数创建相似，可以查看具体APIs说明

##### （2）代码实现

创建apis_image_manager.py文件实现，主机类型创建、查找、删除、更新。代码如下：

```
# Copyright 2021~2022 The Cloud Computing support Teams of ChinaSkills.  
import requests, json, time  
import logging  
# -----------logger-----------  
# get logger  
logger = logging.getLogger(__name__)  
# level  
logger.setLevel(logging.DEBUG)  
# format  
format = logging.Formatter('%(asctime)s %(message)s')  
# to console  
stream_handler = logging.StreamHandler()  
stream_handler.setFormatter(format)  
logger.addHandler(stream_handler)  
# -----------logger-----------  
def get_auth_token(controller_ip, domain, user, password):  
    '''  
    :param controller_ip: openstack master ip address  
    :param domain: current user's domain  
    :param user: user name  
    :param password: user password  
    :return: keystoen auth Token for current user.  
    '''  
    try:  
        url = f"http://{controller_ip}:5000/v3/auth/tokens"  
        body = {  
            "auth": {  
                "identity": {  
                    "methods": [  
                        "password"  
                    ],  
                    "password": {  
                        "user": {  
                            "domain": {  
                                "name": domain  
                            },  
                            "name": user,  
                            "password": password  
                        }  
                    }  
                },  
                "scope": {  
                    "project": {  
                        "domain": {  
                            "name": domain  
                        },  
                        "name": user  
                    }  
                }  
            }  
        }  
        headers = {  
            "Content-Type": "application/json",  
        }  
        print(body)  
        Token = requests.post(url, data=json.dumps(body), headers=headers).headers['X-Subject-Token']  
        headers = {  
            "X-Auth-Token": Token  
        }  
        logger.debug(f"获取Token值：{str(Token)}")  
        return headers  
    except Exception as e:  
        logger.error(f"获取Token值失败，请检查访问云主机控制节点IP是否正确？输出错误信息如下：{str(e)}")  
        exit(0)  
# 镜像管理  
class image_manager:  
    def __init__(self, handers: dict, resUrl: str):  
        self.headers = handers  
        self.resUrl = resUrl  
    #POST  v2/images  
    def create_image(self, image_name: str, container_format="bare", disk_format="qcow2"):  
        """  
        :param image_name:  
        :param container_format:  
        :param disk_format:  
        :return:  
        """  
        body = {  
            "container_format": container_format,  
            "disk_format": disk_format,  
            "name": image_name  
        }  
        response = requests.post(self.resUrl, data=json.dumps(body), headers=self.headers)  
        logger.debug(response.status_code)  
        if response.status_code == 201:  
            return {"ImageItemCreatedSuccess": response.status_code}  
        return response.text  
    # 获取glance镜像id  
    def get_image_id(self, image_name: str):  
        result = json.loads(requests.get(self.resUrl, headers=self.headers).text)  
        logger.debug(result)  
        for item in result['images']:  
            if (item['name'] == image_name):  
                return item['id']  
    # 上传glance镜像  
    # Image data¶ Uploads and downloads raw image data.  
    # These operations may be restricted to administrators. Consult your cloud operator’s documentation for details.  
    # /v2/images/{image_id}/file  
    # 镜像可以重名  
    def upload_iamge_data(self, image_id: str, file_path=""):  
        """  
        :param image_id:  
        :param file_path:  
        :return:  
        """  
        self.resUrl = self.resUrl + "/" + image_id + "/file"  
        self.headers['Content-Type'] = "application/octet-stream"  
        response = requests.put(self.resUrl, data=open(file_path, 'rb').read(), headers=self.headers)  
        logger.debug(response.status_code)  
        if response.status_code == 204:  
            return {"ImageItemCreatedSuccess": response.status_code}  
        return response.text  
    # ----------------------------  
    # /v2/images  
    # List images  
    def get_images(self):  
        """  
        :return:  
        """  
        status_code = requests.get(self.resUrl, headers=self.headers).text  
        logger.debug(f"返回状态:{str(status_code)}")  
        return status_code  
    # /v2/images/{image_id} Show image  
    def get_image(self, id: str):  
        """  
        get a flavor by id.  
        :return:  
        """  
        api_url = self.resUrl + "/" + id  
        response = requests.get(api_url, headers=self.headers)  
        result = json.loads(response.text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
    # /v2/images/{image_id} Delete image  
    def delete_image(self, id: str):  
        """  
         delete a image by id.  
         :return:  
         """  
        api_url = self.resUrl + "/" + id  
        response = requests.delete(api_url, headers=self.headers)  
        # 204 - No ContentThe server has fulfilled the request.  
        if response.status_code == 204:  
            return {"Image itemDeletedSuccess": response.status_code}  
        result = json.loads(response.text)  
        logger.debug(f"返回信息:{str(result)}")  
        return result  
        # http://192.168.200.226:8774/v2.1/ get apis version infomation.  
if __name__ == '__main__':  
    # 1. openstack allinone （controller ) credentials  
    # host ip address  
    controller_ip = "192.168.200.226"  
    # domain name  
    domain = "demo"  
    # user name  
    user = "admin"  
    # user password  
    password = "000000"  
    headers = get_auth_token(controller_ip, domain, user, password)  
    print("headers:", headers)  
```

##### （3）代码验证

① 登录通过账号密码方式：使用get_auth_token()方法，通过该方法获取Token值。
② 封装了image_manager类，通过python request库实现对API的网络访问，实现对用户的增删查改操作。

- 创建：post v2/images
- 查询：get v2/images
- 删除：delete v2/images/id
- 更改密码：put v2/images/id

具体可以通过官网的API说明。
（3）执行image_manager的每个方法进行代码测试，通过openstack image命令行或Dashboard界面进行研究者。
修改apis_image_manager.py的if __name__ == ‘__main__’:函数中OpenStack的IP、domain、user、password，执行apis_image_manager.py，进行查询所有、创建、根据ID查询、更新描述。在apis_image_manager.py的 __name__ == '__main__'代码段最后添加如下代码：

```
#  http://controller:9292  
    image_m = image_manager(headers, f"http://{controller_ip}:9292/v2/images")  
    # 1 查所有  
    images = image_m.get_images()  
    print("查询所有images:", images)  
    #2 创建镜像（注意，镜像允许同名）  
    result = image_m.create_image(image_name="cirros002")  # 调用glance-api中创建镜像方法  
    print(f"创建cirros002 镜像:", result)  
    #    #1.1查询id  
    id = image_m.get_image_id(image_name="cirros002")  
    print("cirros002镜像的，id为: ", id)  
    # 1.2 上传镜像文件  
    result = image_m.upload_iamge_data(id, file_path="cirros-0.3.4-x86_64-disk.img")  
    print(f"上传{id}镜像:", result)  
```

然后执行apis_image_manager.py，结果如下：

```
[root@controller ~]# python3 apis_image_manager.py  
{'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'name': 'demo'}, 'name': 'admin', 'password': '000000'}}}, 'scope': {'project': {'domain': {'name': 'demo'}, 'name': 'admin'}}}}  
headers: {'X-Auth-Token': 'gAAAAABiKYbUS0SDwZzUhzjEuBFQmqWjRxrtCqcdmEpPvEt29dbwRWfjj_GLaLhqiErU0qsfNQN5leEMS788SshaSGFXKwScCAumH22lB2INMbVm9hV4Gn2OnZjkvM0PsJ-DVoIK136QIS6FwZPVI93Xqujawpkw5762db9nI9Gmd3wOxZWDBqs'}  
2022-03-10 13:10:48,187 获取Token值：gAAAAABiKYbUS0SDwZzUhzjEuBFQmqWjRxrtCqcdmEpPvEt29dbwRWfjj_GLaLhqiErU0qsfNQN5leEMS788SshaSGFXKwScCAumH22lB2INMbVm9hV4Gn2OnZjkvM0PsJ-DVoIK136QIS6FwZPVI93Xqujawpkw5762db9nI9Gmd3wOxZWDBqs  
2022-03-10 13:10:48,803 返回状态:{"images": [{"container_format": "bare", "min_ram": 0, "updated_at": "2022-03-10T00:56:57Z", "file": "/v2/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0/file", "owner": "0b6f2d0be1d342e09edc31dc841db7a5", "id": "d50222d2-f737-4b47-ba7c-38eaa2418ff0", "size": 13287936, "self": "/v2/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0", "disk_format": "qcow2", "os_hash_algo": "sha512", "schema": "/v2/schemas/image", "status": "active", "tags": [], "visibility": "shared", "min_disk": 0, "virtual_size": null, "name": "cirros", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "created_at": "2022-03-10T00:56:56Z", "os_hidden": false, "protected": false, "os_hash_value": "1b03ca1bc3fafe448b90583c12f367949f8b0e665685979d95b004e48574b953316799e23240f4f739d1b5eb4c4ca24d38fdc6f4f9d8247a2bc64db25d6bbdb2"}], "schema": "/v2/schemas/images", "first": "/v2/images"}  
查询所有images: {"images": [{"container_format": "bare", "min_ram": 0, "updated_at": "2022-03-10T00:56:57Z", "file": "/v2/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0/file", "owner": "0b6f2d0be1d342e09edc31dc841db7a5", "id": "d50222d2-f737-4b47-ba7c-38eaa2418ff0", "size": 13287936, "self": "/v2/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0", "disk_format": "qcow2", "os_hash_algo": "sha512", "schema": "/v2/schemas/image", "status": "active", "tags": [], "visibility": "shared", "min_disk": 0, "virtual_size": null, "name": "cirros", "checksum": "ee1eca47dc88f4879d8a229cc70a07c6", "created_at": "2022-03-10T00:56:56Z", "os_hidden": false, "protected": false, "os_hash_value": "1b03ca1bc3fafe448b90583c12f367949f8b0e665685979d95b004e48574b953316799e23240f4f739d1b5eb4c4ca24d38fdc6f4f9d8247a2bc64db25d6bbdb2"}], "schema": "/v2/schemas/images", "first": "/v2/images"}  
创建cirros002 镜像: {'ImageItemCreatedSuccess': 201}  
2022-03-10 13:10:49,569 201  
2022-03-10 13:10:50,145 {'images': [{'container_format': 'bare', 'min_ram': 0, 'updated_at': '2022-03-10T05:04:21Z', 'file': '/v2/images/038ba49b-ddee-4e0f-8ecb-6f64d2788138/file', 'owner': '0b6f2d0be1d342e09edc31dc841db7a5', 'id': '038ba49b-ddee-4e0f-8ecb-6f64d2788138', 'size': None, 'self': '/v2/images/038ba49b-ddee-4e0f-8ecb-6f64d2788138', 'disk_format': 'qcow2', 'os_hash_algo': None, 'schema': '/v2/schemas/image', 'status': 'queued', 'tags': [], 'visibility': 'shared', 'min_disk': 0, 'virtual_size': None, 'name': 'cirros002', 'checksum': None, 'created_at': '2022-03-10T05:04:21Z', 'os_hidden': False, 'protected': False, 'os_hash_value': None}, {'container_format': 'bare', 'min_ram': 0, 'updated_at': '2022-03-10T00:56:57Z', 'file': '/v2/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0/file', 'owner': '0b6f2d0be1d342e09edc31dc841db7a5', 'id': 'd50222d2-f737-4b47-ba7c-38eaa2418ff0', 'size': 13287936, 'self': '/v2/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0', 'disk_format': 'qcow2', 'os_hash_algo': 'sha512', 'schema': '/v2/schemas/image', 'status': 'active', 'tags': [], 'visibility': 'shared', 'min_disk': 0, 'virtual_size': None, 'name': 'cirros', 'checksum': 'ee1eca47dc88f4879d8a229cc70a07c6', 'created_at': '2022-03-10T00:56:56Z', 'os_hidden': False, 'protected': False, 'os_hash_value': '1b03ca1bc3fafe448b90583c12f367949f8b0e665685979d95b004e48574b953316799e23240f4f739d1b5eb4c4ca24d38fdc6f4f9d8247a2bc64db25d6bbdb2'}], 'schema': '/v2/schemas/images', 'first': '/v2/images'}  
cirros002镜像的，id为:  038ba49b-ddee-4e0f-8ecb-6f64d2788138  
上传038ba49b-ddee-4e0f-8ecb-6f64d2788138镜像: {'ImageItemCreatedSuccess': 204}  
```

镜像上传需要一定时间，上传后再查询与删除。替换上面输出的ID，最后再添加如下代码：

```
  id = "038ba49b-ddee-4e0f-8ecb-6f64d2788138"
    result = image_m.get_image(id)
    print(f"查询{id}镜像:", result)

    # 4. delete a user
    result = image_m.delete_image(id)
    print(f"删除{id}镜像:", result)
```

删除或注释以下代码：

```
 # 1 查所有
    images = image_m.get_images()
    print("查询所有images:", images)
    
    #2 创建镜像（注意，镜像允许同名）
    result = image_m.create_image(image_name="cirros002")  # 调用glance-api中创建镜像方法
    print(f"创建cirros002 镜像:", result)
    #    #1.1查询id
    id = image_m.get_image_id(image_name="cirros002")
    print("cirros002镜像的，id为: ", id)
    # 1.2 上传镜像文件
    result = image_m.upload_iamge_data(id, file_path="cirros-0.3.4-x86_64-disk.img")
    print(f"上传{id}镜像:", result)
```

然后执行apis_image_manager.py，结果如下：

```
[root@controller ~]# python3 apis_image_manager.py  
{'auth': {'identity': {'methods': ['password'], 'password': {'user': {'domain': {'name': 'demo'}, 'name': 'admin', 'password': '000000'}}}, 'scope': {'project': {'domain': {'name': 'demo'}, 'name': 'admin'}}}}  
2022-03-10 13:14:29,986 获取Token值：gAAAAABiKYeyF3CRflZXsarjvfvtkGs86paQe4PeWG6n2I25gjIhyQ8rUdjmDZAWZme0V2meKwIA_-hEEfTObPpo-Zggq0nvIdyzhRau-6H0uhpZx1awr3O3HLsoj8QOtOS0NhIBFed-QAPpCw3uduh_HwSVJ-Se7axa1Mq26cAFyUSKVakxJsg  
headers: {'X-Auth-Token': 'gAAAAABiKYeyF3CRflZXsarjvfvtkGs86paQe4PeWG6n2I25gjIhyQ8rUdjmDZAWZme0V2meKwIA_-hEEfTObPpo-Zggq0nvIdyzhRau-6H0uhpZx1awr3O3HLsoj8QOtOS0NhIBFed-QAPpCw3uduh_HwSVJ-Se7axa1Mq26cAFyUSKVakxJsg'}  
2022-03-10 13:14:30,462 返回信息:{'container_format': 'bare', 'min_ram': 0, 'updated_at': '2022-03-10T05:04:25Z', 'file': '/v2/images/038ba49b-ddee-4e0f-8ecb-6f64d2788138/file', 'owner': '0b6f2d0be1d342e09edc31dc841db7a5', 'id': '038ba49b-ddee-4e0f-8ecb-6f64d2788138', 'size': 13287936, 'self': '/v2/images/038ba49b-ddee-4e0f-8ecb-6f64d2788138', 'disk_format': 'qcow2', 'os_hash_algo': 'sha512', 'schema': '/v2/schemas/image', 'status': 'active', 'tags': [], 'visibility': 'shared', 'min_disk': 0, 'virtual_size': None, 'name': 'cirros002', 'checksum': 'ee1eca47dc88f4879d8a229cc70a07c6', 'created_at': '2022-03-10T05:04:21Z', 'os_hidden': False, 'protected': False, 'os_hash_value': '1b03ca1bc3fafe448b90583c12f367949f8b0e665685979d95b004e48574b953316799e23240f4f739d1b5eb4c4ca24d38fdc6f4f9d8247a2bc64db25d6bbdb2'}  
查询038ba49b-ddee-4e0f-8ecb-6f64d2788138镜像: {'container_format': 'bare', 'min_ram': 0, 'updated_at': '2022-03-10T05:04:25Z', 'file': '/v2/images/038ba49b-ddee-4e0f-8ecb-6f64d2788138/file', 'owner': '0b6f2d0be1d342e09edc31dc841db7a5', 'id': '038ba49b-ddee-4e0f-8ecb-6f64d2788138', 'size': 13287936, 'self': '/v2/images/038ba49b-ddee-4e0f-8ecb-6f64d2788138', 'disk_format': 'qcow2', 'os_hash_algo': 'sha512', 'schema': '/v2/schemas/image', 'status': 'active', 'tags': [], 'visibility': 'shared', 'min_disk': 0, 'virtual_size': None, 'name': 'cirros002', 'checksum': 'ee1eca47dc88f4879d8a229cc70a07c6', 'created_at': '2022-03-10T05:04:21Z', 'os_hidden': False, 'protected': False, 'os_hash_value': '1b03ca1bc3fafe448b90583c12f367949f8b0e665685979d95b004e48574b953316799e23240f4f739d1b5eb4c4ca24d38fdc6f4f9d8247a2bc64db25d6bbdb2'}  
-----------finished----------  
```

**注意：此实验是连续实验，请不要释放实验资源。**
```

### 案例准备[OpenStack SDK编写Python运维.mp4](https://fdfs.douxuedu.com/group1/M00/00/4B/wKggBmIxs36EYofaAAAAAOKhpKs227.mp4)

沿用案例一的all-in-one云主机环境进行实验。

### 案例实施

OpenStack Python SDK官方文档参见：
https://docs.openstack.org/openstacksdk/latest/user/index.html。
通过OpenStack Python SDK可以编写自动化Python脚本，用于创建和管理Openstack云环境中的资源。SDK实现了Python绑定OpenStack API，这能够让你使用Python实现自动化任务通过调用Python对象，而不用直接调用REST接口。
源代码地址为：https://github.com/openstack/openstacksdk。提供完整源代码及examples案例代码。如图6所示：

![image6.png](python%E8%B0%83%E7%94%A8API.assets/wKggBmIvAXGABACRAAGfkQa5fR4903.png)

图6
Python的OpenStack模块下每种资源提供一个对应的模块实现。安装 OpenStack SDK：

```
$ pip install openstacksdk  
```

查找认证的Endpoint地址：

```
keystone     | identity       | True    | internal  | http://controller:5000/v3/  
```

执行以下代码的机器，需要配置hostname：controller IP。

#### 1. 用户认证

前面通过调用Restful APIs封装用户、主机、镜像等管理类，由于调用SDK非常简单，这里采用一个模块sdk_manager来统一实现。
（1）认证方式：采用账户名密码方式，通过openstack. connect()建立连接。
（2）用户管理：通过openstack. connect.identity模块实现。
新建sdk_manager_identity.py，用户查询与项目代码如下：

```
import json,logging  
import openstack  
#openstack logger  
# openstack.enable_logging(debug=True)  
#文档地址  
# https://docs.openstack.org/openstacksdk/latest/user/index.html  
def create_connection(auth_url, user_domain_name, username, password):  
    """  
    建立连接  
    :param auth_url:  
    :param user_domain_name:  
    :param username:  
    :param password:  
    :return:  
    """  
    return openstack.connect(  
        auth_url=auth_url,  
        user_domain_name=user_domain_name,  
        username=username,  
        password=password,  
    )  
#user Manager  
# 参见文档  
# https://docs.openstack.org/openstacksdk/latest/user/guides/identity.html  
#openstack.connection.Connection  
class user_manager:  
    def __init__(self, connect:openstack.connection.Connection):  
        self.connect = connect  
    def list_users(self):  
        """  
        get User Resource.list object.  
        :return:  
        """  
        users = self.connect.identity.users()  
        #to json  
        user_jsons = {}  
        for user in users:  
            user_jsons[user['name']] = user  
        return json.dumps(user_jsons,indent=2)  
    def list_projects(self):  
        """  
        :return:  
        """  
        projects = self.connect.identity.projects()  
        # to json  
        projects_jsons = {}  
        for item in projects:  
            projects_jsons[item['name']] = item  
        return json.dumps(projects_jsons, indent=2)  
    def list_domains(self):  
        """  
        :return:  
        """  
        items = self.connect.identity.domains()  
        # to json  
        items_jsons = {}  
        for item in items:  
            items_jsons[item['name']] = item  
        return json.dumps(items_jsons, indent=2)  
if __name__ == '__main__':  
    # Initialize connection(通过配置文件）  
    auth_url = "http://172.128.11.18:5000/v3/"  
    username = "admin"  
    password = "000000"  
    user_domain_name = 'demo'  
    conn = create_connection(auth_url, user_domain_name, username, password)  
    #查用户  
    print("-------users-------")  
    user_m = user_manager(conn)  
    result = user_m.list_users()  
    print(result)  
    # 查项目  
    print("-------projects-------")  
    result = user_m.list_projects()  
    print(result)  
    # 查域  
    print("-------domains-------")  
    result = user_m.list_domains()  
    print(result)  
```

以上代码分别通过create_connection、user_manager实现建立连接、用户与项目的查询，__main__方法提供测试代码，可以逐个方法进行测试验证。相关的执行结果，可以通过命令行或dashboard界面进行验证。
执行sdk_manager_identity.py，结果如下：

```
[root@controller ~]# python3 sdk_manager_identity.py  
{'auth_url': 'http://172.128.11.18:5000/v3/', 'user_domain_name': 'demo', 'username': 'admin', 'password': '000000'}  
-------users-------  
{  
  "admin": {  
    "default_project_id": "0b6f2d0be1d342e09edc31dc841db7a5",  
    "description": null,  
    "domain_id": "720f960530dc4e1982ebc7bdfd261f86",  
    "email": null,  
    "is_enabled": true,  
    "links": {  
      "self": "http://172.128.11.18:5000/v3/users/89f8027475294689ae6c0183fa35bf5a"  
    },  
    "name": "admin",  
    "password": null,  
    "password_expires_at": null,  
    "id": "89f8027475294689ae6c0183fa35bf5a",  
    "name": "admin",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  },  
  ......  
  }  
}  
-------projects-------  
{  
  "admin": {  
    "description": "Admin Project",  
    "domain_id": "720f960530dc4e1982ebc7bdfd261f86",  
    "is_domain": false,  
    "is_enabled": true,  
    "name": "admin",  
    "options": {},  
    "parent_id": "720f960530dc4e1982ebc7bdfd261f86",  
    "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
    "name": "admin",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    },  
    "tags": []  
  },  
  "demo": {  
    "description": "Demo Project",  
    "domain_id": "720f960530dc4e1982ebc7bdfd261f86",  
    "is_domain": false,  
    "is_enabled": true,  
    "name": "demo",  
    "options": {},  
    "parent_id": "720f960530dc4e1982ebc7bdfd261f86",  
    "id": "32bb0b4849bc405a82aed64b7c0072fe",  
    "name": "demo",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    },  
    "tags": []  
  },  
  "service": {  
    "description": "Service Project",  
    "domain_id": "720f960530dc4e1982ebc7bdfd261f86",  
    "is_domain": false,  
    "is_enabled": true,  
    "name": "service",  
    "options": {},  
    "parent_id": "720f960530dc4e1982ebc7bdfd261f86",  
    "id": "b47586b9fe8845c0b65ac944616cb934",  
    "name": "service",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    },  
    "tags": []  
  }  
}  
-------domains-------  
{  
  "demo": {  
    "description": "Default Domain",  
    "is_enabled": true,  
    "name": "demo",  
    "links": {  
      "self": "http://172.128.11.18:5000/v3/domains/720f960530dc4e1982ebc7bdfd261f86"  
    },  
    "id": "720f960530dc4e1982ebc7bdfd261f86",  
    "name": "demo",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  },  
  "Default": {  
    "description": "The default domain",  
    "is_enabled": true,  
    "name": "Default",  
    "links": {  
      "self": "http://172.128.11.18:5000/v3/domains/default"  
    },  
    "id": "default",  
    "name": "Default",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  },  
  "heat": {  
    "description": "Stack projects and users",  
    "is_enabled": true,  
    "name": "heat",  
    "links": {  
      "self": "http://172.128.11.18:5000/v3/domains/e62a73d6033d49e89a0fd711a87f7d7b"  
    },  
    "id": "e62a73d6033d49e89a0fd711a87f7d7b",  
    "name": "heat",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  }  
}  
Process finished with exit code 0  
```

官网提供了查询User、Project、Domain资源的Python案例，资源的封装通过代理模式实现，参考类如下：

```
class IdentityService(service_description.ServiceDescription):  
    """The identity service."""  
    supported_versions = {  
        '2': _proxy_v2.Proxy,  
        '3': _proxy_v3.Proxy,  
    }  
```

思考一下如何通过SDK创建与更新资源。

#### 2. 计算资源案例

计算资源前面通过调用Restful APIs封装主机、镜像等管理类，在模块增加主机、镜像、主机类型、网络的管理实现。
（1）主机管理：通过openstack. connect.compute模块实现。
（2）镜像、主机类型、网络：也通过openstack. connect.compute模块实现。另外openstack.connect.image、openstack.connect.network也实现镜像与网络操作。
在sdk_manager_compute.py下修改为如下代码：

```
import json,logging  
import openstack  
#openstack logger  
# openstack.enable_logging(debug=True)  
#文档地址  
# https://docs.openstack.org/openstacksdk/latest/user/index.html  
def create_connection(auth_url, user_domain_name, username, password):  
    """  
    建立连接  
    :param auth_url:  
    :param user_domain_name:  
    :param username:  
    :param password:  
    :return:  
    """  
    return openstack.connect(  
        auth_url=auth_url,  
        user_domain_name=user_domain_name,  
        username=username,  
        password=password,  
    )  
#user Manager  
# 参见文档  
# https://docs.openstack.org/openstacksdk/latest/user/guides/identity.html  
#openstack.connection.Connection  
#云主机管理  
class server_manager:  
    def __init__(self, connect):  
        self.connect = connect  
    def list_servers(self):  
        """  
        查询所有云主机.  
        :return:  
        """  
        #to json  
        items = self.connect.compute.servers()  
        server_jsons = {}  
        for server in items:  
            server_jsons[server['name']] = server  
        # return ""  
        return items# json.dumps(server_jsons,indent=2,skipkeys=True)  
    def create_server(self, server_name, image_name, flavor_name,networ_name):  
        """  
        create a server.  
        :param server_name:  
        :param image_name:  
        :param flavor_name:  
        :param networ_name:  
        :return:  
        """  
        image = self.connect.compute.find_image(image_name)  
        flavor = self.connect.compute.find_flavor(flavor_name)  
        network = self.connect.network.find_network(networ_name)  
        server = self.connect.compute.create_server(  
            name=server_name, image_id=image.id, flavor_id=flavor.id,  
            networks=[{"uuid": network.id}])  
        result = self.connect.compute.wait_for_server(server)  
        return result #json.dumps(result,indent=2,skipkeys=True)  
    def delete_server(self, server_name):  
        """  
        删除云主机  
        :param server_name:  
        :return:  
        """  
        server = self.connect.compute.find_server(server_name)  
        result = self.connect.compute.delete_server(server)  
        return result #json.dumps(result, indent=2, skipkeys=True)  
    def get_server(self, server_name):  
        """  
        获取云主机  
        :param server_name:  
        :return:  
        """  
        server = self.connect.compute.find_server(server_name)  
        return json.dumps(server, indent=2, skipkeys=True)  
class image_manager:  
    def __init__(self, connect):  
        self.connect = connect  
    def list_images(self):  
        """  
        查询所有镜像  
        :return:  
        """  
        #to json  
        items = self.connect.compute.images()  
        images_jsons = {}  
        for image in items:  
            images_jsons[image['name']] = image  
        return json.dumps(images_jsons,indent=2)  
    def get_image(self, image_name:str):  
        """  
        查询镜像  
        :return:  
        """  
        #to json  
        image = self.connect.compute.find_image(image_name)  
        return json.dumps(image,indent=2)  
class flavor_manager:  
    def __init__(self, connect):  
        self.connect = connect  
    def list_flavors(self):  
        """  
        查询所有云主机类型  
        :return:  
        """  
        #to json  
        items = self.connect.compute.flavors()  
        flavors_jsons = {}  
        for flavor in items:  
            flavors_jsons[flavor['name']] = flavor  
        return json.dumps(flavors_jsons,indent=2)  
    def get_flavor(self, flavor_name:str):  
        """  
        根据名称获取云主机类.  
        :return:  
        """  
        #to json  
        flavor = self.connect.compute.find_flavor(flavor_name)  
        return json.dumps(flavor,indent=2)  
class network_manager:  
    def __init__(self, connect):  
        self.connect = connect  
    def list_networks(self):  
        """  
        查询所有网络.  
        :return:  
        """  
        #to json  
        items = self.connect.network.networks()  
        items_jsons = {}  
        for network in items:  
            items_jsons[network['name']] = network  
        return json.dumps(items_jsons,indent=2)  
    def get_network(self, network_name:str):  
        """  
        跟名称查询网络.  
        :return:  
        """  
        #to json  
        flavor = self.connect.compute.find_network(network_name)  
        return json.dumps(flavor,indent=2)  
if __name__ == '__main__':  
    # Initialize connection(通过配置文件）  
    auth_url = "http://172.128.11.18:5000/v3/"  
    username = "admin"  
    password = "000000"  
    user_domain_name = 'demo'  
    conn = create_connection(auth_url, user_domain_name, username, password)  
    # 1 查询flavors  
    print("list flavors--------")  
    sdk_m = flavor_manager(conn)  
    flavors = sdk_m.list_flavors()  
    print("flavors:", flavors)  
    # 2 镜像管理  
    sdk_m = image_manager(conn)  
    items = sdk_m.list_images()  
    print("image:", items)  
    # 3 网络管理  
    print("list networks--------")  
    sdk_m = network_manager(conn)  
    networks = sdk_m.list_networks()  
    print("networks:", networks)  
    #4 查询 云主机  
    sdk_m = server_manager(conn)  
    servers = sdk_m.list_servers()  
    print("servers:", servers)  
    #5 创建云主机  
    print("creat server--------")  
    servers = sdk_m.create_server("test_song","cirros","m1.tiny","net")  
    print("servers:", servers)  
    #6 删除云主机  
    result = sdk_m.delete_server("test_song")  
    print("servers:", result)  
```

以上代码分别通过user_manager、server_manager、image_manager、flavor_manager、network_manager实现镜像、云主机、镜像、主机类型、网络的增删除改。每种资源的操作都提供对应的方法直接操作，非常简单，其他资源或方法可以通过源码或帮助文件进行操作。
__main__方法提供测试代码，可以逐个方法进行测试验证。相关的执行结果，可以通过命令行或Dashboard界面进行验证。
执行结果如下：

```
[root@controller ~]# python3 sdk_manager_compute.py  
{'auth_url': 'http://172.128.11.18:5000/v3/', 'user_domain_name': 'demo', 'username': 'admin', 'password': '000000'}  
list flavors--------  
flavors: {  
  "m1.tiny": {  
    "links": [  
      {  
        "href": "http://controller:8774/v2.1/flavors/1",  
        "rel": "self"  
      },  
      {  
        "href": "http://controller:8774/flavors/1",  
        "rel": "bookmark"  
      }  
    ],  
    "name": "m1.tiny",  
    "description": null,  
    "disk": 10,  
    "is_public": true,  
    "ram": 512,  
    "vcpus": 1,  
    "swap": "",  
    "ephemeral": 0,  
    "is_disabled": false,  
    "rxtx_factor": 1.0,  
    "extra_specs": {},  
    "id": "1",  
    "name": "m1.tiny",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  },  
  "flavor_small": {  
    "links": [  
      {  
        "href": "http://controller:8774/v2.1/flavors/100000",  
        "rel": "self"  
      },  
      {  
        "href": "http://controller:8774/flavors/100000",  
        "rel": "bookmark"  
      }  
    ],  
    "name": "flavor_small",  
    "description": "Update description skill_china",  
    "disk": 10,  
    "is_public": true,  
    "ram": 1024,  
    "vcpus": 1,  
    "swap": "",  
    "ephemeral": 0,  
    "is_disabled": false,  
    "rxtx_factor": 1.0,  
    "extra_specs": {},  
    "id": "100000",  
    "name": "flavor_small",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  },  
  "m1.small": {  
    "links": [  
      {  
        "href": "http://controller:8774/v2.1/flavors/2",  
        "rel": "self"  
      },  
      {  
        "href": "http://controller:8774/flavors/2",  
        "rel": "bookmark"  
      }  
    ],  
    "name": "m1.small",  
    "description": null,  
    "disk": 20,  
    "is_public": true,  
    "ram": 1024,  
    "vcpus": 1,  
    "swap": "",  
    "ephemeral": 0,  
    "is_disabled": false,  
    "rxtx_factor": 1.0,  
    "extra_specs": {},  
    "id": "2",  
    "name": "m1.small",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  },  
  "m1.medium": {  
    "links": [  
      {  
        "href": "http://controller:8774/v2.1/flavors/3",  
        "rel": "self"  
      },  
      {  
        "href": "http://controller:8774/flavors/3",  
        "rel": "bookmark"  
      }  
    ],  
    "name": "m1.medium",  
    "description": null,  
    "disk": 40,  
    "is_public": true,  
    "ram": 2048,  
    "vcpus": 2,  
    "swap": "",  
    "ephemeral": 0,  
    "is_disabled": false,  
    "rxtx_factor": 1.0,  
    "extra_specs": {},  
    "id": "3",  
    "name": "m1.medium",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  }  
}  
image: {  
  "cirros": {  
    "links": [  
      {  
        "href": "http://controller:8774/v2.1/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0",  
        "rel": "self"  
      },  
      {  
        "href": "http://controller:8774/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0",  
        "rel": "bookmark"  
      },  
      {  
        "href": "http://controller:9292/images/d50222d2-f737-4b47-ba7c-38eaa2418ff0",  
        "type": "application/vnd.openstack.image",  
        "rel": "alternate"  
      }  
    ],  
    "name": "cirros",  
    "created_at": "2022-03-10T00:56:56Z",  
    "metadata": {},  
    "min_disk": 0,  
    "min_ram": 0,  
    "progress": 100,  
    "status": "ACTIVE",  
    "updated_at": "2022-03-10T00:56:57Z",  
    "size": 13287936,  
    "id": "d50222d2-f737-4b47-ba7c-38eaa2418ff0",  
    "name": "cirros",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    }  
  }  
}  
list networks--------  
networks: {  
  "net": {  
    "availability_zone_hints": [],  
    "availability_zones": [  
      "nova"  
    ],  
    "created_at": "2022-03-10T01:21:52Z",  
    "description": "",  
    "dns_domain": null,  
    "ipv4_address_scope_id": null,  
    "ipv6_address_scope_id": null,  
    "is_admin_state_up": true,  
    "is_default": null,  
    "is_port_security_enabled": true,  
    "is_router_external": false,  
    "is_shared": false,  
    "mtu": 1450,  
    "name": "net",  
    "project_id": "0b6f2d0be1d342e09edc31dc841db7a5",  
    "provider_network_type": "vxlan",  
    "provider_physical_network": null,  
    "provider_segmentation_id": 12,  
    "qos_policy_id": null,  
    "segments": null,  
    "status": "ACTIVE",  
    "subnet_ids": [  
      "a16130c4-79c1-4ae8-9bc3-c167ee009d63"  
    ],  
    "updated_at": "2022-03-10T01:21:53Z",  
    "is_vlan_transparent": null,  
    "revision_number": 2,  
    "id": "df62ea19-3e33-40bf-9f41-f2c5f343b3e7",  
    "name": "net",  
    "location": {  
      "cloud": "defaults",  
      "region_name": "",  
      "zone": null,  
      "project": {  
        "id": "0b6f2d0be1d342e09edc31dc841db7a5",  
        "name": null,  
        "domain_id": null,  
        "domain_name": null  
      }  
    },  
    "tags": []  
  }  
}  
servers: <generator object Resource.list at 0x00000285B98AF8E0>  
creat server--------  
servers: openstack.compute.v2.server.Server(name=test_song, imageRef=d50222d2-f737-4b47-ba7c-38eaa2418ff0, flavorRef=1, networks=[{'uuid': 'df62ea19-3e33-40bf-9f41-f2c5f343b3e7'}], security_groups=[{'name': 'default'}], OS-DCF:diskConfig=MANUAL, id=25554b93-65b2-472b-9bc0-344c4f405a50, links=[{'href':...
```

计算资源或其他资源的Python调用类似，可以查看接口进行测试。