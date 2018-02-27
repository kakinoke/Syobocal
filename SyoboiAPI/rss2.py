# -*- coding:UTF-8 -*-

import json
import os
import xmltodict
from urllib.request import urlopen

from Syobocal.SyoboiAPI.SyoboiBaseAPI import SyoboiBaseAPI

class RSS2(SyoboiBaseAPI):

    API = "rss2.php"

    def _request(self, options):
        url = self._get_url(options)
        request = urlopen(url)
        return request.read()

    def _get_parse_json(self, options):
        request = self._request(options)
        return json.loads(request)

    def get(self, **options):
        options["alt"] = "json"
        datas = self._get_parse_json(options)
        return datas["items"]

