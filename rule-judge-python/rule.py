# -*- coding:utf-8 -*-
"""
@author: ashing
@time: 2019/12/13 下午6:34
@mail: axingfly@gmail.com

Less is more.
"""

import json


class RuleParser(object):
    def __init__(self, rule):
        if isinstance(rule, str):
            self.rule = json.loads(rule)
        else:
            self.rule = rule
        self.validate(self.rule)

    class Functions(object):

        ALIAS = {
            '=': 'eq',
            '！=': 'neq',
            '>': 'gt',
            '>=': 'gte',
            '<': 'lt',
            '<=': 'lte',
            'and': 'and_',
            'in': 'in_',
            'or': 'or_',
            'not': 'not_',
            'str': 'str_',
            'int': 'int_',
            '+': 'plus',
            '-': 'minus',
            '*': 'multiply',
            '/': 'divide',
        }

        def eq(self, *args):
            return args[0] == args[1]

        def neq(self, *args):
            return args[0] != args[1]

        def in_(self, *args):
            return args[0] in args[1:]

        def gt(self, *args):
            return args[0] > args[1]

        def gte(self, *args):
            return args[0] >= args[1]

        def lt(self, *args):
            return args[0] < args[1]

        def lte(self, *args):
            return args[0] <= args[1]

        def not_(self, *args):
            return not args[0]

        def or_(self, *args):
            return any(args)

        def and_(self, *args):
            return all(args)

        def int_(self, *args):
            return int(args[0])

        def upper(self, *args):
            return args[0].upper()

        def lower(self, *args):
            return args[0].lower()

        def plus(self, *args):
            return sum(args)

        def minus(self, *args):
            return args[0] - args[1]

        def multiply(self, *args):
            return args[0] * args[1]

        def divide(self, *args):
            return float(args[0]) / float(args[1])

        def abs(self, *args):
            return abs(args[0])

    @staticmethod
    def validate(rule):
        if not isinstance(rule, list):
            # raise RuleEvaluationError('Rule must be a list， got {}'.format(type(rule)))
            raise ValueError('Rule must be a list， got {}'.format(type(rule)))
        if len(rule) < 2:
            # raise RuleEvaluationError('Must have at least one argument.')
            raise ValueError('Must have at least one argument.')

    def _evaluate(self, rule, fns):
        """
        递归执行list内容
        """

        def _recurse_eval(arg):
            if isinstance(arg, list):
                return self._evaluate(arg, fns)
            else:
                return arg

        r = map(_recurse_eval, rule)
        r = list(r)
        r[0] = self.Functions.ALIAS.get(r[0]) or r[0]
        func = getattr(fns, r[0])
        return func(*r[1:])

    def evaluate(self):
        fns = self.Functions()
        ret = self._evaluate(self.rule, fns)
        if not isinstance(ret, bool):
            # logger.warn('In common usage， a rule must return a bool value，'
            #             'but get {}， please check the rule to ensure it is true')
            print('In common usage， a rule must return a bool value，'
                  'but get {}， please check the rule to ensure it is true')
        return ret


if __name__ == '__main__':
    test_rule = [
        "or",
        [">", 3, 2],
        [">", 0, 0.05],
    ]
    rule_parser = RuleParser(test_rule)
    print(rule_parser.evaluate())
