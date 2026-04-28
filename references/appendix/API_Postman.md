# Postman 示例包

Postman 是一款功能强大的网页调试与发送网页 HTTP 请求，并能运行测试用例的 Chrome 插件，可以用来很方便的模拟 GET 或者 POST 或者其他方式的请求来调试接口。


我们在这为您提供了全套的 ClassIn API Postman 示例代码，您可以使用它方便灵活得测试 ClassIn API。


## 安装 Postman

- 您可以在 [Chrome 网上应用店](https://chrome.google.com/webstore/category/extensions)安装 Postman 扩展程序
- 也可以在 [Postman 官网](https://www.getpostman.com/)下载并安装桌面版 Postman


## 测试 ClassIn API

**先下载 `Environments` -> 按照环境变量里的规则修改数据 -> 下载相关接口示例代码 -> 在示例代码里修改 SECRET -> 相关接口示例代码导入 Postman -> 导入 Environments**

- 将相关示例代码文件下载到本地，比如您下载的是用户相关接口，可以命名为 `classin-user-postman-collection.json`。

- 打开 Postman，点击左上角 `Import` 导入`classin-user-postman-collection.json`。请参考下图：

![Postman Import](../../img/postman-import.jpg)

- 点击右上角`齿轮`下面的 Manage Environments ，弹出的页面下方有 `Import` 按钮，选择 `Environments` 文件导入。请参考下图：

![environments](../../img/env.jpg)

- 导入成功后，您即可进行测试

- 另外，点击右侧 `Code` 可以查看根据 HTTP 请求自动生成的代码。Postman 支持当前最流行的编程语言，点击左侧的语言按钮进行切换。请参考下图：

![Postman Code Generation](../../img/postman-code-button.jpg)


## ClassIn API Postman 示例代码
_下载下列文件请右键另存为下载_

### Environments (导入后可将Environments中的value补充为真实数据)

<a href="../../postman/ClassIn.postman_environments.json" download="ClassIn.postman_environments.json">Environments</a>

### Lms Environments (导入后可将Environments中的value补充为真实数据)

<a href="../../postman/classin_lms.postman_environment.json" download="classin_lms.postman_environment.json">Lms Environments</a>

### 用户

<a href="../../postman/classin_user_v2.postman_collection.json" download="classin_user_v2.postman_collection.json">用户相关接口</a>

### 教室

<a href="../../postman/classin_classroom_v2.postman_collection.json" download="classin_classroom_v2.postman_collection.json">教室相关接口</a>

### Lms 相关接口 (导入后可将接口中的请求参数补充为真实数据)

<a href="../../postman/classin_lms.postman_collection.json" download="classin_lms.postman_collection.json">Lms 相关接口</a>

### 云盘

<a href="../../postman/classin_cloud_v2.postman_collection.json" download="classin_cloud_v2.postman_collection.json">云盘相关接口</a>
