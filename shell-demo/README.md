# 根据Linux系统应用与开发教程写的脚本程序

```shell
demo01.sh 位置变量
demo02.sh 算数运算 expr
demo03.sh 条件判断
demo04.sh 以shell命令返回值作为判断条件
demo05.sh case分支
demo06.sh for语句
demo07.sh shift命令 执行一次使得位置变量左移一个位置
demo08.sh 函数 （有问题:不知道如何输出指定的第几个参数 echo ${$n}不可以）
demo10.sh 学习debug 见下文
```

## 条件判断

-   条件判断的结果0为真 1为假 这和c语言有所不同
-   用`test` 和`[]`进行字符串判断



```
问：linux中 nano编辑文件 怎么把tab键设定为空4格，而且要像使用空格键一样有4个空格
```

```shell
答：编辑 ~/.nanorc, 插入如下内容
set tabsize 4
set tabstospaces
```

`demo10.sh Debug`

```shell
> sh -x ./demo10.sh 1 2 3
output:
+ [ 3 -eq 0 ]
+ sum=0
+ [ 3 -eq 0 ]
+ expr 0 + 1
+ sum=1
+ shift
+ [ 2 -eq 0 ]
+ expr 1 + 2
+ sum=3
+ shift
+ [ 1 -eq 0 ]
+ expr 3 + 3
+ sum=6
+ shift
+ [ 0 -eq 0 ]
+ echo 6
6
```

## 重定向

-   `>` 代表写入
-   `>>` 代表追加