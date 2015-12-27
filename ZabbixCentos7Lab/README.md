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


Firewall
--------

    firewall-cmd --permanent --add-port=10050/tcp  
    firewall-cmd --permanent --add-port=10051/tcp  
    systemctl restart firewalld

SELinux
-------

    setsebool -P httpd_can_connect_zabbix=1

Links
-------------
Tools:  
https://www.virtualbox.org/  
https://www.vagrantup.com/  
Documentation:  
https://www.zabbix.com/documentation/2.4/
https://ru.wikipedia.org/wiki/Сравнение_систем_мониторинга_сети  
https://www.netways.de/fileadmin/images/Events_Trainings/Events/OSDC/2009/Slides_2009/Alexei_Vladishev_Open_Source_Monitoring_with_Zabbix.pdf  
https://xakep.ru/2014/08/13/using-zabbix/  
https://sdcast.ksdaemon.ru/2015/08/sdcast-29/  
http://blog.zabbix.com/  
https://www.zabbix.com/forum/  
Repos:  
http://repo.zabbix.com/zabbix/2.4/rhel/7/x86_64/  
https://share.zabbix.com/  
https://github.com/zabbix/zabbix-community-repos  
http://monitoringartist.github.io/zabbix-searcher/  

Versions
--------
    $ vagrant --version
    Vagrant 1.7.4
    $ "/cygdrive/c/Program Files/Oracle/VirtualBox/VBoxManage.exe" --version
    4.3.12r93733


### Author
	Anton Prykhodko
