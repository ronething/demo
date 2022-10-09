
# coding=utf-8

import json

input_file = '../Bookmarks'
out_file = '../bookmark.json'

# 最终存储 json 数据 data:[] list 的元素为 {"name":"xx","url":"xx"}
out_list = []


def json_for_node(node):
    """此函数只是为了学习一下 yield 的使用"""
    if 'url' in node:
        yield dict(name=node['name'], url=node['url'])
    elif 'children' in node:
        for n in node['children']:
            yield from json_for_node(n)
    else:
        yield 'nothing'


def export_json(node):
    if 'url' in node:
        out_list.append(dict(name=node['name'], url=node['url']))
    elif 'children' in node:
        for n in node['children']:
            export_json(n)
    else:
        return 'nothing'


def yield_main():
    with open(input_file, 'r', encoding='utf-8') as f:
        contents = json.load(f)

    bookmark_bar = json_for_node(contents['roots']['bookmark_bar'])
    other = json_for_node(contents['roots']['other'])
    for i in bookmark_bar:
        out_list.append(i)
    for i in other:
        out_list.append(i)
    # while True:
    #     try:
    #         out_list.append(next(next(other)))
    #     except StopIteration:
    #         break


def main():
    with open(input_file, 'r', encoding='utf-8') as f:
        contents = json.load(f)

    export_json(contents['roots']['bookmark_bar'])
    export_json(contents['roots']['other'])
    out_json = dict(data=out_list)
    with open(out_file, 'w+', encoding='utf-8') as f:
        json.dump(out_json, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
    # yield_main()
