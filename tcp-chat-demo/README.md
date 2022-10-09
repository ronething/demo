# TCP/IP 协议简单聊天程序

来自 实验楼

---

遇到的问题：

实验用的是 python2 版本

我用的是 python3 版本

在 sockt.send 和 recv 的时候需要 进行 str 和 bytes 类型的转换

---

Python3中的Bytes和str之间的关系 

文本总是unicode字符集，用str类型表示。

二进制数据则由bytes表示。（通过socket在网络上传输数据时必须要用二进制格式）

Python不会以任何隐式的方式混用str和bytes，所以我们不能在代码中拼接字符串和字节包
当然字符串和字节，是可以被相互转换的。

借用一个其他的图来说明转换关系：

![](https://i.loli.net/2018/10/19/5bc8cd179d1bf.png)

string 通过 encode 编码成 bytes 类型，而 bytes 格式的数据又可以通过 decode 来解码成 str 类型。
encode 用来对 string 格式个数据进行编码：

str = '你好'

str.encode('UTF-8') -->表示源数据是什么格式的，不指定的话，默认为UTF-8

b'\xe4\xbd\xa0\xe5\xa5\xbd'

decode 用来对bytes格式的数据进行解码：

str = b'\xe4\xbd\xa0\xe5\xa5\xbd'

str.decode('UTF-8') -->表示把二进制数据解释成 什么格式的数据（默认UTF-8，待测）

来自 博客园 侵删