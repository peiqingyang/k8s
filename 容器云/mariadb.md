登录mariadb

`mariadb -uroot -p000000`

添加用户

```shell
##第一种
mariadb -uadmin -p
输入密码

##第二种登录后
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
ON TUTORIALS.*
TO 'admin'@'localhost'
IDENTIFIED BY '000000';
```

查看数据库

`show databases`

使用数据库

`use database_name`

列出该数据库所有数据表

`show tables`

显示表属性

`show columns from tables_name;`

显示表详细索引信息

`show index from tables_name`

创建数据库

`create database runoob;`

删除数据库

`drop databaes runoob;`