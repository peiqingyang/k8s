

基本数据结构

```shell
对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）

对象的一组键值对，使用冒号结构表示。
animal: pets

数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）

一组连词线开头的行，构成一个数组。
- Cat
- Dog
- Goldfish

纯量（scalars）：单个的、不可再分的值
纯量是最基本的、不可再分的值。以下数据类型都属于 JavaScript 的纯量。

字符串
布尔值
整数
浮点数
Null
时间
日期
```

##### 讲解

```yaml
verison: "**"	##docker-compose的版本

services: 
  
  tomact: 		##服务名字
    image: image_nem:tag			##镜像
    ports: 
      - **:**		##端口映射     类似于docker run -p
  
  mysql:
    image: mysql:**
    ports: 
      - **:**
    envoronment:		##相当于docekr run -e
      - MYSQL_ROOT_PASSWORD:000000
  ##  - "MYSQL_ROOT_PASSWORD=000000"  ##
    volumes:  ##给容器和宿主机指定卷，类似于docker run -v
      - /root/mysqldata/:/var/lab/mysql
  ##  - mysqldata:/var/lab/mysql  ##别名  
volumes:
  mysqldata:  ##生命数据卷别名
```







##### 案例

```yaml
services:
  ##服务
  frontend:
    ##镜像
    image: awesome/webapp
    ##端口映射
    ports:
      - "443:8043"
    ##网络
    networks:
      - front-tier
      - back-tier
    configs:
      - httpd-config
    secrets:
      - server-certificate

  backend:
    image: awesome/database
    volumes:
      - db-data:/etc/data
    networks:
      - back-tier

volumes:
  db-data:
    driver: flocker
    driver_opts:
      size: "10GiB"

configs:
  httpd-config:
    external: true

secrets:
  server-certificate:
    external: true

networks:
  # The presence of these objects is sufficient to define them
  front-tier: {}
  back-tier: {}
```

