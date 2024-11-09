<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_request_handler_base/readme/README.zh-hant.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_request_handler_base

- [简体中文](../README.md)
- [繁體中文](README.zh-hant.md)
- [English](README.en.md)

## 說明

基於Tornado的RequestHandler基礎類，封裝了常用功能，方便快速開發,主要重置django模型和請求結束時候關閉數據庫連接.

## 程式碼庫

- <a href="https://github.com/xy-web-service/xy_request_handler_base.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-opensource/xy_request_handler_base.git" target="_blank">Gitee位址</a>  
- <a href="https://gitcode.com/xy-opensource/xy_request_handler_base.git" target="_blank">GitCode位址</a>  

## 安裝

```bash
# bash
pip install xy_request_handler_base
```

## 使用

> 詳情請查看 [Demoes.py](../samples/xy_web_server_demo/source/Runner/RequestHandlerDemo/Demoes.py)

```python
# Demoes.py

from xy_request_handler_base.Base import Base


class Demo(Base):

    def get(self):
        self.write("Hello, xy_request_handler_base !")

```

運作 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 以下倉庫
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github位址</a>  
> - <a href="https://gitee.com/xy-opensource/xy_web_server.git" target="_blank">Gitee位址</a>  
> - <a href="https://gitcode.com/xy-opensource/xy_web_server.git" target="_blank">GitCode位址</a>  

```bash
# bash

# 目前目錄為xy_request_handler_base的git本地倉庫所在目錄
# 切換到工程目錄
cd ./samples/xy_web_server_demo

# 啟動範例工程的Tornado服務
xy_web_server -w tornado start

# 預設啟動的Tornado服務url位址是: http://127.0.0.1:8400
# 瀏覽器開啟造訪 http://127.0.0.1:8400/demo 進行驗證
```

## 許可證
xy_request_handler_base 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```