# -*-coding:UTF-8 -*-

from Syobocal.SyoboiAPI.db import DB
from Syobocal.SyoboiAPI.rss2 import RSS2
from Syobocal.util import Util

class Client(object):

    db = DB()
    rss2 = RSS2()
    util = Util(db, rss2)
