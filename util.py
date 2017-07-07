# -*- coding:UTF-8 -*-

class Util(object):

    def __init__(self, db, rss2):
        self.db = db
        self.rss2 = rss2

    def title(self, tid):
        return self.db.get_title(tid)

    def showChInfo(self, chid):
        datas = self.db.chlookup()
        for data in datas["ChItem"]:
            if str(chid) == str(data["ChID"]):
                return data

    def chName(self, chid):
        data = self.showChInfo(chid)
        for key, val in data.items():
            if "ChName" == key:
                return val
