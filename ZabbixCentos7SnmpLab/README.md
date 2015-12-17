Vagrant Zabbix Centos 7 Lab
===========================
Run Vagrant
-----------

    vagrant destroy -f && vg_start=`date` && vagrant up && vg_stop=`date` && echo $vg_start && echo $vg_stop  
    or  
    vagrant destroy -f  
    vagrant up

Settings files
--------------

    /etc/zabbix/zabbix_agentd.conf  
    /etc/zabbix/zabbix_server.conf  
    /etc/httpd/conf.d/zabbix.conf
    /etc/snmp/snmptrapd.conf
    /etc/snmp/snmptt.ini
    /etc/snmptt.conf  


Firewall
--------

    firewall-cmd --permanent --add-port=10050/tcp  
    firewall-cmd --permanent --add-port=10051/tcp  
    systemctl restart firewalld

SELinux
-------

    setsebool -P httpd_can_connect_zabbix=1
    grep snmptt /var/log/audit/audit.log | audit2allow -M snmptt
    semodule -i snmptt.pp

Links
-------------

http://repo.zabbix.com/zabbix/2.4/rhel/7/x86_64/  
https://www.zabbix.com/documentation/2.4/  
http://blog.zabbix.com/  
https://www.zabbix.com/forum/  
https://share.zabbix.com/  
https://github.com/zabbix/zabbix-community-repos  
http://monitoringartist.github.io/zabbix-searcher/  
https://ru.wikipedia.org/wiki/Сравнение_систем_мониторинга_сети  
https://www.netways.de/fileadmin/images/Events_Trainings/Events/OSDC/2009/Slides_2009/Alexei_Vladishev_Open_Source_Monitoring_with_Zabbix.pdf  
https://sdcast.ksdaemon.ru/2015/08/sdcast-29/  
SNMP Traps:  
https://www.zabbix.com/documentation/2.4/manual/config/items/itemtypes/snmptrap  
http://software-radar.com/article/zabbix-24-прием-snmp-трапов-как-это-работает  
https://www.zabbix.org/wiki/ConfigureSnmptrapsCentos6_RHEL6  

### Author
	Anton Prykhodko