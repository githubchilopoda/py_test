#!/usr/bin/python
# coding=utf-8
import datetime
import os
from monitor import monitor


def main():
    today_time = datetime.datetime.now()
    print 'begin: ', datetime.datetime.strftime(today_time, '%Y-%m-%d %H:%M:%S')
    print 'run mysql_proc_project'
    try:
        flag = os.system('/home/capvision/script/mysql_proc_project.sh')
        if flag != 0:
            monitor.send_mail(monitor.mail_to_list, "192.168.50.95 mysql_proc_project ",
                              '192.168.50.95 run mysql_proc_project error')
    except Exception, e:
        monitor.send_mail(monitor.mail_to_list, "192.168.50.95 mysql_proc_project ", e)
    today_time = datetime.datetime.now()
    print 'end: ', datetime.datetime.strftime(today_time, '%Y-%m-%d %H:%M:%S')


main()
