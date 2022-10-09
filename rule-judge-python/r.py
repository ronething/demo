# -*- coding:utf-8 -*-
"""
@author: ashing
@time: 2019/12/16 上午9:22
@mail: axingfly@gmail.com

Less is more.
"""


class Functions(object):
    ALIAS = {
        '=': 'eq',
        '!=': 'neq',
        '>': 'gt',
        '>=': 'gte',
        '<': 'lt',
        '<=': 'lte',
        'inc': 'inc_',
    }

    def eq(self, *args):
        return args[0] == args[1]

    def neq(self, *args):
        return args[0] != args[1]

    def inc_(self, *args):  # 包含
        return args[1] in args[0]

    def gt(self, *args):
        return args[0] > args[1]

    def gte(self, *args):
        return args[0] >= args[1]

    def lt(self, *args):
        return args[0] < args[1]

    def lte(self, *args):
        return args[0] <= args[1]


# expr = [{"hostip": "127.0.0.1"}, "and", {"hostname": r"*vmware*"}, "or", {"hostip": "123"}]
expr = [["hostip", "=", "127.0.0.1"], "and", ["hostname", "inc", "vmware"], "or", ["hostip", "=", "123"]]


def main():
    # gen_rule()
    res = judge_rule()
    print(res)


def gen_rule():
    if not expr:
        raise ValueError("list 为空")
    and_list = []
    or_list = []
    c_and = True
    and_list.append(expr[0])
    if len(expr) > 1:
        for i in expr[1:]:
            if i == "and":
                c_and = True
            elif i == "or":
                c_and = False
            else:
                if c_and:
                    and_list.append(i)
                else:
                    or_list.append(i)
    else:
        and_list.append(expr[0])
    print("and list is", and_list)
    print("or list is", or_list)
    db_dict = {
        "and": and_list,
        "or": or_list,
        "user": "ashing",
        "report": "ronething",
    }
    print(db_dict)


def judge_rule(alert_msg):  # alert_msg 为告警信息
    alert_message = {  # mock 告警信息
        "hostip": "192.0.0.1",
        "hostname": "ashing-virtual-vmware",
        "hostgroup": "hh"
    }
    # TODO: 参数为 dict 获取出 dict["and"] and dict["or"]
    # TODO: 后续需要嵌套循环 rule_list 的取出需要排序 数据库需要给一个字段可以进行 asc
    # TODO: 如果 and_list or or_list 为空，则对应的 list 返回 False
    rule_list = [
        {
            "and": [['hostip', '=', '127.0.0.1'], ['hostname', 'inc', 'vmware']],
            "or": [['hostip', '=', '123']],
            "user": "zhangsan"
        },
        {
            "and": [['hostip', 'inc', '192'], ['hostname', 'inc', 'vmware']],
            "or": None,
            "user": "lisi"
        }
    ]
    if not rule_list:
        return
    for i in rule_list:
        and_list = i.get('and')
        or_list = i.get('or')
        and_res = judge_and(and_list, alert_message)
        or_res = judge_or(or_list, alert_message)
        res = and_res or or_res  # 最后进行或操作
        if res:
            # 匹配到一条直接 break
            print("match rule", i.get('user'))
            break
    return


def judge_and(a, msg):
    """:return True of False"""
    if not a:
        return False
    for i in a:
        fns = Functions()
        op = getattr(fns, fns.ALIAS.get(i[1]))
        op_res = op(msg.get(i[0], ""), i[2])
        if not op_res:
            return False
    return True


def judge_or(o, msg):
    """:return True of False"""
    if not o:
        return False
    for i in o:
        fns = Functions()
        op = getattr(fns, fns.ALIAS.get(i[1]))
        op_res = op(msg.get(i[0], ""), i[2])
        if op_res:
            return True
    return False


if __name__ == '__main__':
    main()
