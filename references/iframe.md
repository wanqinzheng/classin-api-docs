# ClassIn 下载按钮链接 API 说明

## 主要用途：

放置机构页面，供用户下载最新的 ClassIn 客户端，而不需要手动更新链接地址。

## 效果预览：
_以下为效果预览，并非最新版本_。
**WinXP 于 2019 年 5 月 1 号之后停用。**


[ClassIn Win7下载按钮](https://download.eeo.cn/client/classin_win_install_4.0.1.80_s.exe)

[ClassIn MacOS下载按钮](https://download.eeo.cn/client/classin_mac_install_4.0.1.80_s.dmg)

移动端下载地址二维码: <br><img data-id="classInImage_mdqr" width="120" alt="classIn mobile download" src="https://www.eeo.cn/assets/images/qr_eeomobiledownload.png">
    <br>
<script type="text/javascript" charset="utf-8" src="https://www.eeo.cn/sysshare/custom/seturl_classindownload.js"></script>

## 使用说明：

#### 将下方代码复制到您的网站页面的&lt;body&gt;标签内,其中&lt;a&gt;链接替换为您的下载按钮,请保证&lt;a&gt;标签[data-id]属性一致

```
  <a data-id="classInDownLoad_auto">classIn 自动判断下载按钮</a><br />
  <a data-id="classInDownLoad_win7">ClassIn win7下载按钮</a><br />
  <a data-id="classInDownLoad_macOS">ClassIn macOS下载按钮</a><br />
  <a data-id="classInDownLoad_iOS">classIn iOS下载按钮</a><br />
  <a data-id="classInDownLoad_android">classIn Android下载按钮</a><br />
  移动端下载地址二维码: <br /><img data-id="classInImage_mdqr" alt="classIn mobile download">
  <script type="text/javascript" charset="utf-8" src="https://www.eeo.cn/sysshare/custom/seturl_classindownload.js"></script>
```
