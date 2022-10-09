# coding=utf-8
# 构建状态树

data = [{
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
    "state": "success",
    "parent": "20200611123159190696",
    "jid": "20200611123354850723",
    "jid_state": "success",
    "id": 3,
}]

job_id = "5ee2243e96b196ade5f11b35"


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


if __name__ == "__main__":
    print(build_tree())
