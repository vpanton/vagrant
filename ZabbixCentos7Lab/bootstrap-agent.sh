#!/usr/bin/env bash

sudo rpm --import http://repo.zabbix.com/RPM-GPG-KEY-ZABBIX
sudo rpm -ivh http://repo.zabbix.com/zabbix/2.4/rhel/7/x86_64/zabbix-release-2.4-1.el7.noarch.rpm
sudo yum install -y zabbix-agent vim
sudo systemctl enable zabbix-agent
sudo systemctl start zabbix-agent

