#couldnt get this thing to work
#!/usr/bin/env python
# coding=utf-8
import sys
import sqlite3 as lite
import requests
import time
from BeautifulSoup import BeautifulSoup
import dataset
import time
import datetime

db = dataset.connect('sqlite:///./database/data.sqlite')
db.begin()
db.commit()
time.sleep(3)

    
