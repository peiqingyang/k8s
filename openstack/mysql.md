数据库操作

```mysql
##创建数据库
MariaDB [(none)]> create database test;
Query OK, 1 row affected (0.07 sec)
##使用数据库
MariaDB [(none)]> use test;
Database changed
##显示数据库列表
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| cinder             |
| glance             |
| heat               |
| information_schema |
| keystone           |
| mysql              |
| neutron            |
| nova               |
| nova_api           |
| nova_cell0         |
| performance_schema |
| test               |
+--------------------+
12 rows in set (0.00 sec)
##显示数据库中的表名
MariaDB [test]> show tables;
Empty set (0.00 sec)
##在库test中创建表company（表结构如(id int not null primary key,name varchar(50),addr varchar(255))所示），在表company中插入一条数据(1,"alibaba","china")。
MariaDB [test]> create table company(id int not null primary key,name varchar(50),addr varchar(255));
Query OK, 0 rows affected (0.19 sec)

MariaDB [test]> insert into company values (1,"alibaba","china");
Query OK, 1 row affected (0.00 sec)
##查看表内容
MariaDB [test]> select * from company;
+----+---------+-------+
| id | name    | addr  |
+----+---------+-------+
|  1 | alibaba | china |
+----+---------+-------+
1 row in set (0.00 sec)
```

