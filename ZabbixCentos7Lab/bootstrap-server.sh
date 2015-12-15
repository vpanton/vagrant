#!/usr/bin/env bash

sudo rpm --import http://repo.zabbix.com/RPM-GPG-KEY-ZABBIX
sudo rpm -ivh http://repo.zabbix.com/zabbix/2.4/rhel/7/x86_64/zabbix-release-2.4-1.el7.noarch.rpm
sudo yum -y install zabbix-server-mysql zabbix-web-mysql mariadb mariadb-server zabbix-agent zabbix-java-gateway vim
sudo systemctl start mariadb
mysql -u root -e "create database zabbix character set utf8;"
mysql -u root -e "grant all privileges on zabbix.* to 'zabbix'@'localhost';"
mysql -u root -e "flush privileges;"
mysql -u zabbix zabbix < /usr/share/doc/zabbix-server-mysql-2.4.*/create/schema.sql
mysql -u zabbix zabbix < /usr/share/doc/zabbix-server-mysql-2.4.*/create/images.sql
mysql -u zabbix zabbix < /usr/share/doc/zabbix-server-mysql-2.4.*/create/data.sql
sudo setsebool -P httpd_can_connect_zabbix=1
sudo systemctl enable zabbix-server
sudo systemctl enable zabbix-agent
sudo systemctl enable mariadb
sudo systemctl enable httpd
sudo systemctl start zabbix-server
sudo systemctl start zabbix-agent
sudo systemctl start httpd