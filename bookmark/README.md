# chrome bookmark 整理统计生成词云

## 0x00

- bookmark 结构分析

首先读取 bookmark 不同操作系统的 bookmark 在不同的路径，可浏览这一段[代码](https://github.com/bdesham/chrome-export/blob/927e0ec273798294d4f06b323794a0ee5b2967eb/export-chrome-bookmarks#L99)

```python
if system() == "Darwin":
    input_filename = expanduser("~/Library/Application Support/Google/Chrome/Default/History")
elif system() == "Linux":
    input_filename = expanduser("~/.config/google-chrome/Default/History")
elif system() == "Windows":
    input_filename = environ["LOCALAPPDATA"] + r"\Google\Chrome\User Data\Default\History"
```

通过 `json.load()` 或 `json.loads()` 方法读出内容并赋值给 contents

```sh
In [35]: contents.keys()                                                      
Out[35]: dict_keys(['checksum', 'roots', 'version'])
```

checksum 和 version 我们不关心

重点在 roots 里面存放着 chrome 浏览器的所有书签

```sh
In [37]: contents['roots'].keys()                                             
Out[37]: dict_keys(['bookmark_bar', 'other', 'sync_transaction_version', 'synced'])
```

其中 bookmark_bar 和 other 分别表示书签栏和其他书签 属于同级事物

```sh
In [40]: contents['roots']['bookmark_bar']['name']                            
Out[40]: '书签栏'

In [41]: contents['roots']['other']['name']                                   
Out[41]: '其他书签'

In [42]: contents['roots']['bookmark_bar'].keys()                             
Out[42]: dict_keys(['children', 'date_added', 'date_modified', 'id', 'name', 'sync_transaction_version', 'type'])

In [43]: contents['roots']['other'].keys()                                    
Out[43]: dict_keys(['children', 'date_added', 'date_modified', 'id', 'name', 'sync_transaction_version', 'type'])
```

其中，children 下面是一个 list 而 list 中的每个元素其实是一个 dict 表示具体书签项目

每个具体的书签项目拥有的 key

```sh
date_added
id
meta_info
name
sync_transaction_version
type
url
```

明白了原理就 OK 了，具体看 `code/bookmark.py`

## 0x01

- jieba 分词

没啥好说的，我也不会，根据官方样例照着写就行。

## 0x02

- wordcloud 生成词云图

`from wordcloud import WordCloud`

点进去看这个类的一些配置即可，也可以使用搜索引擎查看一些别人写的例子。

```python
bookmark_cloud = WordCloud(font_path=fontpath,
                            background_color="white",
                            max_words=None,
                            max_font_size=248,
                            random_state=42,
                            width=2560, height=1600
                            )
bookmark_cloud.generate_from_frequencies(contents) # 需要注意的是 这里传入的 contents 是一个字典 dict
```

## 0x03 Development

```sh
git clone [repo] && cd [repo]
# 将 Bookmarks 书签文件放置于项目根目录
pipenv install # 如果你还没有安装 pipenv 通过 pip(3) install pipenv 解决
pipenv run python code/summary.py
```

## 0x04

![最终效果](./bookmark.png)

notice: 字体需要自行添加到 font 目录

## 0x05

参考资料：

- [chrome-export](https://github.com/bdesham/chrome-export)
- [jieba](https://github.com/fxsjy/jieba)
- [wordcloud](https://github.com/amueller/word_cloud)
