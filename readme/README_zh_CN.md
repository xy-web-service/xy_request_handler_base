<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:11
 * @FilePath: /xy_request_handler_base/readme/README_zh_CN.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_request_handler_base

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)


## 说明

基于Tornado的RequestHandler基础类，封装了常用功能，方便快速开发,主要重置django模型和请求结束时候关闭数据库连接.

## 源码仓库

- <a href="https://github.com/xy-web-service/xy_request_handler_base.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-web-service/xy_request_handler_base.git" target="_blank">Gitee地址</a>

## 安装

```bash
# bash
pip install xy_request_handler_base
```

## 使用

> 详情请查看 [Demoes.py](../samples/xy_web_server_demo/source/Runner/RequestHandlerDemo/Demoes.py)

```python
# Demoes.py

from xy_request_handler_base.Base import Base


class Demo(Base):

    def get(self):
        self.write("Hello, xy_request_handler_base !")

```

## 许可证
xy_request_handler_base 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](../LICENSE) 文件。

## 捐赠

如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```