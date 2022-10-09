# coding=utf-8
# 判断状态结果

data = [
    {
        "state": "failed",
        "parent": "5ee2243e96b196ade5f11b35",
        "jid": "20200611123159190696",
        "jid_state": "failed",
        "id": 1,
    },
    {
        "state": "failed",
        "parent": "5ee2243e96b196ade5f11b35",
        "jid": "20200611123159190697",
        "jid_state": "failed",
        "id": 2,
    },
    {
        "state": "failed",
        "parent": "20200611123159190697",
        "jid": "20200611123159190697",
        "jid_state": "failed",
        "id": 2,
    },
    {
        "state": "done",
        "parent": "20200611123159190696",
        "jid": "20200611123354850723",
        "jid_state": "done",
        "id": 3,
    },
    {
        "state": "success",
        "parent": "20200611123159190696",
        "jid": "20200611123354850444",
        "jid_state": "success",
        "id": 4,
    },
    {
        "state": "failed",
        "parent": "20200611123354850444",
        "jid": "20200611123354850555",
        "jid_state": "failed",
        "id": 4,
    },
]

job_id = "5ee2243e96b196ade5f11b35" # 最顶层 user_job ID


def build_tree():
    res = []
    for i in data:
        if job_id == i['parent']:
            res.append(build_tree_sub(i))

    return res


def build_tree_sub(i: dict):
    for j in data:
        if j['parent'] == i['jid'] and j['jid'] != i['jid']:  # 排除本身
            i.setdefault('children', []).append(j)
            build_tree_sub(j)

    return i


def judge_state(i: dict, res: list):
    res.append(i['state'])
    children = i.get('children', None)
    if children:
        for j in children:
            judge_state(j, res)

    return res


if __name__ == "__main__":
    # 结果怎么判定？
    # A->B->C
    # A->B A->C
    # 除了第一个结果 后面都是只要有 success 即可
    res = build_tree()
    all_res = []  # 最后 set 然后根据规则判定是否是全部完成/失败/其他
    for i in res:
        i_res = []
        print(i)
        # print(f'{i["jid"]} state is {judge_state(i, i_res)}')
        j = judge_state(i, i_res)
        print(j)
        # 判断状态
        r = set(j)
        # TODO: 根据规则进行判断 然后 append 到 all_res 中
    
    # TODO: all_res 再根据相应规则进行判断

    """
        {'state': 'failed', 'parent': '5ee2243e96b196ade5f11b35', 'jid': '20200611123159190696', 'jid_state': 'failed', 'id': 1, 'children': [{'state': 'done', 'parent': '20200611123159190696', 'jid': '20200611123354850723', 'jid_state': 'done', 'id': 3}, {'state': 'success', 'parent': '20200611123159190696', 'jid': '20200611123354850444', 'jid_state': 'success', 'id': 4, 'children': [{'state': 'failed', 'parent': '20200611123354850444', 'jid': '20200611123354850555', 'jid_state': 'failed', 'id': 4}]}]}
        ['failed', 'done', 'success', 'failed']
        {'state': 'failed', 'parent': '5ee2243e96b196ade5f11b35', 'jid': '20200611123159190697', 'jid_state': 'failed', 'id': 2}
        ['failed']
    """
