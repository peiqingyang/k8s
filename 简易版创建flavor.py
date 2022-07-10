#-*-utf8-*-
import requests,json,time,os
headers = {"Content-Type": "application/json"}
headers["X-Auth-Token"] = os.popen("ssh root@192.168.5.229 source /etc/keystone/admin-openrc.sh && openstack token issue | awk '/ id/{print $4}'").read().strip('\n')
requests.post('http://192.168.5.229:8774/v2.1/flavors', headers=headers, json={
    'flavor': {
        'name': 'test_fluyfytfravor',
        'id': '6699996',
        'ram': 4096,
        'disk': 10,
        'vcpus': 8
    }
})