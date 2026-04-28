# 接口调用入门指南

您在开始测试接口的时候，请先下载 Postman 工具，Postman 使您可以快速轻松地发布文档。Postman 自动提取您的示例请求，标头，代码段等，以动态示例和机器可读指令填充您的文档页面，还可以生成代码段，使用多种框架和语言从您的请求中生成代码片段，可用于从您自己的应用程序发出相同的请求。***点击 [此处](https://www.getpostman.com/downloads/)下载***

<video class="img-responsive v5_media-shadow" autoplay="true" loop="true" controls="" style="max-width:100%; height: auto;" ><source src="https://assets.getpostman.com/getpostman/videos/postman-api-documentation-walkthru.mp4" type="video/mp4"></video>


目前ClassIn API 接口有两个版本，部分接口对应v1，部分接口对应v2，两种接口postman测试例子如下：

### 测试接口（API v1）

 打开 ClassIn [接口文档](https://docs.eeo.cn/api/zh-hans/)，选择您要测试的接口，复制接口到 Postman URL处，填写好请求参数，点击 send ，查看测试结果即可。

注意事项：

 - SID、SECRET 需要开通 ClassIn API 方可获得，请联系您的客户经理开通
 - safeKey：MD5(SECRET+timeStamp) 固定 32 位全小写字符。可使用[在线工具](https://md5jiami.51240.com/)快速生成
 - timeStamp：	当前调用接口20分钟以内的 Unix Epoch 时间戳。可使用[在线工具](http://tool.chinaz.com/Tools/unixtime.aspx?jdfwkey=zfpdi&qq-pf-to=pcqq.c2c)快速生成

 示例：

 ![](../../img/postman2.png)

### 测试接口（API v2）

 打开 ClassIn [接口文档](https://docs.eeo.cn/api/zh-hans/)，选择您要测试的接口，复制接口到 Postman URL处，填写好请求header参数和body参数，点击 send ，查看测试结果即可。

注意事项：

 - sid、SECRET 需要开通 ClassIn API 方可获得，请联系您的客户经理开通
 - X-EEO-SIGN：MD5(参数串&key=secret) 固定 32 位全小写字符。具体参考[签名生成方式及代码示例](../appendix/signature.md)
 - timeStamp：	当前调用接口5分钟以内的 Unix Epoch 时间戳。可使用[在线工具](http://tool.chinaz.com/Tools/unixtime.aspx?jdfwkey=zfpdi&qq-pf-to=pcqq.c2c)快速生成

 示例：

 ![看看](../../img/apiv2pm.png)

### 查看测试结果

- 如上图测试结果返回“程序正常执行”，即证明接口调用成功。
- 如测试异常，则会返回错误码，可参照返回错误码进行修改请求参数，重新测试。

  示例：

  ![](../../img/postmanerror.png)

 102 错误原因分析：

  - 查看sid是否正确
  - safeKey 是否是 secret + timeStamp md5 加密后的结果（注意是小写）
  - SECRET 最好复制，不要手动填写，注意字母混淆
  - timeStamp 是否距当前时间20分钟之内的秒数（不是毫秒数，注意时区是北京时区）
  -  机构账号没有 API 对接权限，需要到 eeo.cn 后台确认下
  - 接口已经下线
  - 机构账号已经被暂停服务（合同到期、欠费等），请联系客户经理



### 生成代码段

   使用多种框架和语言从您的请求中生成代码片段，可用于从您自己的应用程序发出相同的请求。

  ![](../../img/postmancode.png)
