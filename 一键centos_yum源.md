```shell
rm -rf /etc/yum.repos.d/*
touch /etc/yum.repos.d/local.repo
cat >> /etc/yum.repos.d/local.repo <<EOF
[centos]
name=centos
baseurl=ftp://192.168.10.10/centos2009
gpgcheck=0
enabled=1
EOF

```

