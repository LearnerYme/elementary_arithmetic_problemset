import numpy as np
import numpy.random as rd

def int_plus(params):
    num = params['num']
    if num == 0:
        return False
    low = params['low']
    high = params['high']
    maximum = params['maximum']
    if low > high:
        raise Exception('[Integer Plus] high must be lager than low.')
    if low == high:
        raise Exception('[Integer Plus] it is meaningless if low equals high.')
    if maximum < high or maximum < low*2:
        raise Exception('[Integer Plus] too small maximum.')
    problem_list = []
    ans_list = []
    for idx in range(1,1+num):
        while True:
            num1 = rd.randint(low,high)
            num2 = rd.randint(low,high)
            if num1 + num2 > maximum:
                continue
            else:
                if 0 < num < 100:
                    head = '[P%02d]'%idx
                elif 100 <= num < 1000:
                    head = '[P%03d]'%idx
                else:
                    head = '[P%d]'%idx
                item1 = '%d'%num1
                item2 = '%d'%num2
                if num1 < 0:
                    item1 = '(%s)'%item1
                if num2 < 0:
                    item2 = '(%s)'%item2
                problem_list.append('%s %s + %s = \n'%(head,item1,item2))
                ans_list.append('%s %d\n'%(head,num1+num2))
                break
    return problem_list, ans_list

def int_subtract(params):
    num = params['num']
    if num == 0:
        return False
    low = params['low']
    high = params['high']
    neg = params['neg']
    if neg == 'False' or neg == 'false':
        neg = False
    if low > high:
        raise Exception('[Integer Subtract] high must be lager than low.')
    if low == high:
            raise Exception('[Integer Subtract] it is meaningless if low equals high.')
    if neg is False:
        if low < 0:
            raise Exception('[Integer Subtract] negative low while neg is false.')
        if high < 0:
            raise Exception('[Integer Subtract] negative high while neg is false.')
    problem_list = []
    ans_list = []
    for idx in range(1,1+num):
        num1 = rd.randint(low,high)
        num2 = rd.randint(low,high)
        if neg is False and num1 < num2:
            num1, num2 = num2, num1
        if 0 < num < 100:
            head = '[S%02d]'%idx
        elif 100 <= num < 1000:
            head = '[S%03d]'%idx
        else:
            head = '[S%d]'%idx
        item1 = '%d'%num1
        item2 = '%d'%num2
        if num1 < 0:
            item1 = '(%s)'%item1
        if num2 < 0:
            item2 = '(%s)'%item2
        problem_list.append('%s %s - %s = \n'%(head,item1,item2))
        ans_list.append('%s %d\n'%(head,num1-num2))
    return problem_list, ans_list

def int_multiply(params):
    num = params['num']
    if num == 0:
        return False
    low = params['low']
    high = params['high']
    maximum = params['maximum']
    marker = params['marker']
    if low > high:
        raise Exception('[Integer Multiply] high must be lager than low.')
    if low == high:
        raise Exception('[Integer Multiply] it is meaningless if low equals high.')
    if maximum < high or maximum < low*low:
        raise Exception('[Integer Multiply] too small maximum.')
    problem_list = []
    ans_list = []
    for idx in range(1,1+num):
        while True:
            num1 = rd.randint(low,high)
            num2 = rd.randint(low,high)
            if num1 * num2 > maximum:
                continue
            else:
                if 0 < num < 100:
                    head = '[M%02d]'%idx
                elif 100 <= num < 1000:
                    head = '[M%03d]'%idx
                else:
                    head = '[M%d]'%idx
                item1 = '%d'%num1
                item2 = '%d'%num2
                if num1 < 0:
                    item1 = '(%s)'%item1
                if num2 < 0:
                    item2 = '(%s)'%item2
                problem_list.append('%s %s %s %s = \n'%(head,item1,marker,item2))
                ans_list.append('%s %d\n'%(head,num1*num2))
                break
    return problem_list, ans_list

def int_divide(params):
    num = params['num']
    if num == 0:
        return False
    maximum = params['maximum']
    maximum_divisor = params['maximum_divisor']
    marker = params['marker']
    #decimal = params['decimal']
    mod_ = params['mod']
    if maximum <= 3:
        raise Exception('[Integer Divide] maximum must be larger than 3.')
    problem_list = []
    ans_list = []
    for idx in range(1,1+num):
        while True:
            num1 = rd.randint(2,maximum)
            num2 = rd.randint(2,maximum_divisor)
            if mod_ is True or mod_ == 'True' or mod_ == 'true':
                res = num1 // num2
                if rd.randint(2) == 1:#p = 1/2
                    res, num2 = num2, res
                offset = num1 - res*num2
                if offset == 0 or offset >= num2:
                    continue
                else:
                    tail_problem = '%d %s %d = \n'%(num1,marker,num2)
                    tail_ans = '%d ... %d\n'%(res,offset)
            elif mod_ is False  or mod_ == 'False' or mod_ == 'false':
                res = num1 // num2
                num1 = res * num2
                if rd.randint(2) == 1:#p = 1/2
                    res, num2 = num2, res
                tail_problem = '%d %s %d = \n'%(num1,marker,num2)
                tail_ans = '%d\n'%(res)
            else:
                raise Exception('[Integer Divide] invalid mod.')
            if 0 < num < 100:
                head = '[D%02d]'%idx
            elif 100 <= num < 1000:
                head = '[D%03d]'%idx
            else:
                head = '[D%d]'%idx
            problem_list.append('%s %s'%(head,tail_problem))
            ans_list.append('%s %s'%(head,tail_ans))
            break
    return problem_list, ans_list

