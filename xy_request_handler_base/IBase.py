# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "IBase"
"""
  * @File    :   IBase.py
  * @Time    :   2023/04/29 22:54:31
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""
import logging
from django.db import connections, connection


class IBase:
    def log(self, message):
        logging.info(message)

    def close_old_connections(self):
        for conn in connections.all():
            conn.close_if_unusable_or_obsolete()
