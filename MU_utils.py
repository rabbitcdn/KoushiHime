# -*- coding: utf-8 -*-
import redis
import uuid
import logging
import logging.handlers
import os
import sys
import pdb
import re
os.chdir(os.path.dirname(sys.argv[0]))
r=redis.Redis(host="localhost",port=6379,db=0)
def unique_str():
    return str(uuid.uuid1())
def loggingInit(logname):
    isExists=os.path.exists('log')
    if not isExists:
        os.mkdir('log')
    LogExists=os.path.exists(logname)
    if not LogExists:
        f=open(logname,'w')
        f.close()
    log=logging.getLogger(logname)
    log.setLevel(logging.DEBUG)
    logHandler=logging.handlers.RotatingFileHandler(logname,maxBytes=10*1024*1024,backupCount=5)
    logHandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    logHandler.setFormatter(formatter)
    log.addHandler(logHandler)
    return log
def for_dict(dic):
    Categories = []
    if isinstance(dic,dict):
            key = dic['query']['pages'].keys()[0]
            value= dic[key]
            for i in value:
                if value[i]['title']:
                    Categories.append(value[i]['title'])
                break
    return Categories
