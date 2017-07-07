# -*-coding:UTF-8 -*-

from Syobopy.SyoboiAPI.db import DB
from Syobopy.SyoboiAPI.rss2 import RSS2
from Syobopy.util import Util

class Client(object):

    db = DB()
    rss2 = RSS2()
    util = Util(db, rss2)
