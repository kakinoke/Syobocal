# -*- coding:UTF-8 -*-

import json
import os
from urllib.parse import urlencode
from urllib.request import urlopen
import xml.etree.ElementTree as etree
import xmltodict

class SyoboiBaseAPI(object):

    ENDPOINT = "http://cal.syoboi.jp"

    def _get_api(self, api):
        url = os.path.join(self.ENDPOINT, api)
        return url

    def _parse_xml(self, xml):
        root = etree.fromstring(xml)
        return root

    def _get_url(self, options):
        post_data = urlencode(options)
        url = "{}?{}".format(self._get_api(self.API), post_data)
        return url

    def _request(self, options):
        url = self._get_url(options)
        request = urlopen(url)
        return request
