# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Demoes"
"""
  * @File    :   Demoes.py
  * @Time    :   2024/10/30 19:48:10
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from xy_request_handler_base.Base import Base


class Demo(Base):

    def get(self):
        self.write("Hello, xy_request_handler_base !")
