<base target="_blank">

# 网页大直播场景应用


## 什么是网页大直播？
 ![!deprecated](../../img/waring.png) 注意：因小程序一些限制，本文档提供的方案均不支持对接微信小程序。

   
ClassIn 网页大直播是指教师使用 ClassIn 教室进行授课，学生使用网页观看直播课程。   
本文档提供了两种对接方案供您选择，以便将直播页面内置到您的平台/app 上。  
网页大直播相对互动在线教室而言，大直播不限制参与的观看端数量，观看端也无须下载 ClassIn。缺点是只有简单的聊天互动，不支持音视频以及教室内其他复杂的教学互动。   
应用场景适用于各种成千上万人的大班课、活动直播、录播课等，对互动需求不多的场景。

## 一 iframe 嵌套 ClassIn 直播回放页面

**本方案是在您的客户端（APP、网页等）嵌套 ClassIn 的直播回放页面，直播回放页面地址获取参考 [ClassIn 直播回放地址获取方式](#11-如何获取classin直播回放播放器地址)**  

  - **优点：** 低开发成本，无需开发网页播放器；支持设置登录账号后观看；支持ClassIn后台下载直播回放观看数据或接入ClassIn消息订阅服务进而订阅相关数据；  

  - **缺点：** 可扩展性低，需要使用ClassIn提供的网页界面。网页链接本身不具备鉴权功能，如果暴露链接，可能导致直播内容被可见范围外的用户看到，需要平台方通过技术手段防止地址暴露；  

  - **应用场景：** 大直播引流、公益直播，大班课;  

  - **对接步骤：** 用户、排课对接→记录课节页面直播回放地址→将直播回放页面用iframe内嵌到相应的网页→消息订阅接口接收用户观看记录数据→将观看数据处理存储并展现
  - **代码示例：** 在页面加入iframe  ``` <iframe src="https://www.eeo.cn/live.php?lessonKey=0a9c56ba30c05733"></iframe> ``` 效果展示：  [点击跳转查看](http://api-demo3.eeo.im/iframeDemo/)  


### 1.1 如何获取ClassIn直播回放播放器地址？

**[创建课堂](../LMS/createClassroom.md) 、[编辑课堂](../LMS/updateClassroom.md)、[获取直播回放地址](../broadcast/getWebcastUrl.md) 均可获取课节直播回放地址，响应中参数名：live_url，此地址在直播时即直播地址，待课节结束后自动转换为回放地址； 例：`https://www.eeo.cn/live.php?lessonKey=0a9c56ba30c05733`**  

我们在返回的课节直播播放器页面植入了聊天室功能。课节可以设置登录后才能观看或者登录后才能聊天，此时用户需要填写手机号登录后才可以观看及聊天。  
为了您更便捷的使用此功能，我们提供了用户免登录的操作，请参考下方1.2  
  
### 1.2 直播播放器中聊天室免二次登录

**如果直播回放页面需要用户进行登录后才能观看，该方法可实现用户免密登录，无须用户再次输入账号密码。（账号信息体现在直播聊天室，直播回放观看数据中）**

##### 1.2.1  课节直播回放地址免二次登录

  - 当您获得课节直播回放地址之后
    + 例：`https://www.eeo.cn/live.php?lessonKey=xxx`
    + 您需要增加 account、nickname、checkCode 拼接在 `https://live.eeo.cn/live_partner.html?lessonKey=00d1c98a91c52568` 地址后边。 **注意：这个免二次登录地址与直播播放器地址不是同一个地址**
  + 具体参数及规则如下
    + 具体参数有 secret、lessonKey、account、nickname、checkCode
    + secret 为 SECRET，在 eeo.cn API 对接密钥处可获得
    + 从直播器地址中可以获得 lessonKey
    + account 为学生账号(长度小于32个字符)，nickname 为学生昵称(长度小于24个字符)
    + checkCode = md5(secret+lessonKey+account+nickname)
  - URL 拼接示例
    + `https://live.eeo.cn/live_partner.html?lessonKey=00d1c98a91c52568&account=13700000000&nickname=classin&checkCode=d8c57caf088529b4ddd15b0f694d847b`

##### 1.2.2  课程直播回放地址免二次登录  

- **注意：此地址可跳转至课程下任何课节直播回放，如不想用户查看课程下所有课节，请使用上述单个课节直播回放地址免二次登录**
- 当您通过[获取课程直播/回放播放器地址](https://docs.eeo.cn/api/zh-hans/broadcast/getWebcastUrl.html)接口获得播放器链接之后
  + 例：`https://www.eeo.cn/webcast.php?courseKey=xxx&lessonid=xxx`
  + 从直播器地址中可以获得 courseKey、lessonid
  + 您需要增加 account、nickname、checkCode 拼接在 `https://live.eeo.cn/webcast_partner.html` 地址后边。  **注意：这个免二次登录地址与直播播放器地址不是同一个地址**
- 具体参数及规则如下
  + 具体参数有 courseKey、lessonid、account、nickname、checkCode
  + 其中 lessonid 为可选，其他参数皆为必选
  + account 为学生账号(长度小于32个字符)，nickname 为学生昵称(长度小于24个字符)
  + checkCode = md5(secret+courseKey+account+nickname)
  + secret 为 SECRET，在 eeo.cn API 对接密钥处可获得
- URL 拼接示例
  + `https://live.eeo.cn/webcast_partner.html?courseKey=7be856f28907f1a2&lessonid=123456&account=18600123456&nickname=eeo&checkCode=febe50cd50ba4d3af506bfa118a3845b`  

##### 1.2.3 如何获取用户观看直播回放的数据  

参考[消息订阅部分](https://docs.eeo.cn/api/zh-hans/datasub/)  
在课节内实时推送的数据订阅里包括了直播观看数据，在课节结束后推送的消息数据里包括了回放数据的推送。将所需的消息类型发给技术支持即可订阅。     
  
## 二 拉流方案，需平台开发相关播放器

    注意：该方案需要您的平台开发自己的播放器页面，ClassIn 只提供直播画面。   

**如果您网站有自己的播放器，支持播放直播流地址或者回放的mp4文件，或者您希望自行定义直播页面的样式功能，可以采取这种方案。这种方案只使用ClassIn教室的直播视频流，您需要进行页面其他部分的开发**  

  - **优点：** 可扩展性极佳，方便二次开发，鉴权、加密、记录等；  

  - **缺点：** 开发成本高，需要较高技术能力，需主动完成网页播放器开发，并对各端进行适配；如需回放，还需订阅回放推送[课后生成的录课文件数据](https://docs.eeo.cn/api/zh-hans/datasub/classrelated.html#课后生成的录课文件数据);  

  - **应用场景：** 录播课售卖、对直播安全要求性较高，高度定制化等；  
  - **对接步骤：** 用户、排课对接→记录课节拉流地址→直播：页面用播放器播放拉流地址→消息订阅接口接收生成的录课文件地址→回放：页面用播放器播放录课文件地址  

### 2.1 如何获取拉流地址？

**[创建课堂](../LMS/createClassroom.md) 、[编辑课堂](../LMS/updateClassroom.md)、[获取直播回放地址](../broadcast/getWebcastUrl.md) 均可获取拉流地址，目前支持3种拉流协议，分别为RTMP,HLS 和 FLV；**

附拉流地址优缺点对比，以下对比仅供参考。

|     | RTMP | HLS | FLV（HTTP-FLV） |
| --- | ---- | --- | --- |
| 全称 | Real Time Message Protocol | HTTP Liveing Streaming | RTMP over HTTP |
| 协议 | TCP 长连接 | HTTP 短连接 | HTTP 长连接 |
| 原理 | 每个时刻的数据收到后立刻转发 | 集合一段时间的数据，生成 ts 切片文件（三片），并更新 m3u8 索引 | 同 RTMP，使用 HTTP 协议（80 端口）|
| 延时 | 1-3s | 5-20s(依切片情况) | 1-3s |
| Web 支持 | H5 中需要使用插件 | 支持 H5 | H5 中需要使用插件 |
| 其他 | 跨平台支持较差，需要 Flash 技术支持 | 播放时需要多次请求，对于网络质量要求高 | 需要 Flash 技术支持，不支持多音频流、多视频流，不便于 seek（即拖进度条） |

## 三 常见问题QA

> Q1. 什么是 iframe，如何使用？  
> A1. iframe 一般用来包含别的页面，例如我们可以在我们自己的网站页面加载别人网站或者本站其他页面的内容;  通常我们使用 iframe 直接直接在页面嵌套iframe标签指定src就可以了，详细可参考[iframe 使用教程](https://blog.csdn.net/qq_27009517/article/details/124476405)；  
> 例：``` <iframe src="url"></iframe> ```  
>
> Q2. 拉流是什么，如何使用？  
> A2. 拉流：指服务器已有直播内容，用指定地址进行拉取的过程。即是指服务器里面有流媒体视频文件，这些视频文件根据不同的网络协议类型（如 RTMP、HLS、FLV）被读取的过程，称之为拉流；[【流媒体】推流与拉流简介](https://blog.csdn.net/weixin_44299027/article/details/122711869)  
开源流媒体解决方案推荐：https://blog.51cto.com/lovebetterworld/3988613 仅供参考；  

