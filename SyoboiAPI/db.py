# -*- coding:UTF-8 -*-

import json
import os
import sys
import xmltodict

from Syobopy.SyoboiAPI.SyoboiBaseAPI import SyoboiBaseAPI

class DB(SyoboiBaseAPI):

    API = "db.php"

    def _get_parse_xml(self, options):
        request = self._request(options)
        xml = request.read()
        datas = xmltodict.parse(xml)
        return datas

    def get_title(self, tid):
        data = self.titlelookup(TID=tid)
        title = data["TitleItem"]["Title"]
        return title

    def proglookup(self, **options):
        options["Command"] = "ProgLookup"
        options["JOIN"] = "SubTitles"
        datas = self._get_parse_xml(options)
        return datas["ProgLookupResponse"]["ProgItems"]["ProgItem"]

    def titlelookup(self, **options):
        options["Command"] = "TitleLookup"
        datas = self._get_parse_xml(options)
        data = datas["TitleLookupResponse"]
        result = data["Result"]
        titleitem = data["TitleItems"]["TitleItem"]
        d = {
            "Code": result["Code"],
            "Message": result["Message"],
            "TitleItem": titleitem
        }
        return d

    def chlookup(self):
        options = {
            "Command": "ChLookup"
        }
        datas = self._get_parse_xml(options)
        data = datas["ChLookupResponse"]
        result = data["Result"]
        chitem = data["ChItems"]["ChItem"]
        d = {
            "Code": result["Code"],
            "Message": result["Message"],
            "ChItem": chitem
        }
        return d
