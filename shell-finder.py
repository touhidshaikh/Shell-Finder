#!/usr/bin/env python


"""
Author : Touhid M.Shaikh
Data  : 28th Apr, 2017
Description : This Script helps ypu to find Proper Shell COde for you Target system
Warnning : Education Purpose only. 
"""

import sys
import urllib2
from prettytable import PrettyTable


def banner():
    ban = """ 
\033[1;32;40m  _________\033[1;31;40m.__           .__  .__  \033[1;32;40m_________  \033[1;32;40m          .___      \033[0m
\033[1;32;40m /   _____/\033[1;31;40m|  |__   ____ |  | |  | \033[1;32;40m\_   ___ \ \033[1;32;40m ____   __| _/____  \033[0m
\033[1;32;40m \_____  \ \033[1;31;40m|  |  \_/ __ \|  | |  | \033[1;32;40m/    \  \/ \033[1;32;40m/  _ \ / __ |/ __ \ \033[0m
\033[1;32;40m /        \\\033[1;31;40m|   Y  \  ___/|  |_|  |_\033[1;32;40m\     \___(\033[1;32;40m  <_> ) /_/ \  ___/ \033[0m
\033[1;32;40m/_______  /\033[1;31;40m|___|  /\___  >____/____\033[1;32;40m/\______  /\033[1;32;40m\____/\____ |\___  >\033[0m
\033[1;32;40m        \/ \033[1;31;40m     \/     \/          \033[1;32;40m        \/ \033[1;32;40m           \/    \/ \033[0m   
\033[1;31;40mvisit : http://www.touhidshaikh.com Author : \033[1;33;40m @touhidshaikh22         \033[0m    """
    return ban

if len(sys.argv) == 1:
    print "Use : ",sys.argv[0]," <keyword> <keyword>"
    sys.exit()

def help():

    return h
keyword = ""
k = len(sys.argv)
for i in range(1,k):
    if i < k-1 :
        keyword = keyword + sys.argv[i] + "*"
    else:
        keyword = keyword + sys.argv[i]



print banner()


table = PrettyTable(["Author","Platform","Description","URL"])
url = "http://shell-storm.org/api/?s="+(keyword)


print "\033[2;31;40mConnecting to Database........\033[0m\n"

print "Rquest URL is : ",url

connection = urllib2.Request(url)
response = urllib2.urlopen(connection)
a = response.read()
a = a.split("\n")

for i in a:
    if not i:
        continue
    else:
        i = i.split("::::")
        author = i[0]
        platform = i[1]
        des = i[2]
        u = i[4]
        i = [author,platform,des[0:41],u]
        table.add_row(i)


print table
