import numpy as np
import numpy.random as rd
from tools import int_plus
from tools import int_subtract
from tools import int_multiply
from tools import int_divide
import json
import datetime
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('-conf',default='conf.json')
conf = parser.parse_args().conf

#load configures
with open(conf) as f:
    params = json.load(f)

filename = params['filename']
ansname = params['ansname']
if filename == 'time':
    time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = './problemset_' + time_str
    ansname = './answer_' + time_str

int_plus_params = params['int_plus']
int_subtract_params = params['int_subtract']
int_multiply_params = params['int_multiply']
int_divide_params = params['int_divide']

unitary = params['unitary']
if unitary is not False:
    for item in [int_plus_params, int_subtract_params, int_multiply_params, int_divide_params]:
        if item['num'] == 0:
            continue
        else:
            item['num'] = unitary

shuffle = params['shuffle']

problem_list = []
ans_list = []
psa = int_plus(int_plus_params)
if psa is not False:
    problem_list += psa[0]
    ans_list += psa[1]
psa = int_subtract(int_subtract_params)
if psa is not False:
    problem_list += psa[0]
    ans_list += psa[1]
psa = int_multiply(int_multiply_params)
if psa is not False:
    problem_list += psa[0]
    ans_list += psa[1]
psa = int_divide(int_divide_params)
if psa is not False:
    problem_list += psa[0]
    ans_list += psa[1]
with open(filename,'w') as f:
    if shuffle:
        random.shuffle(problem_list)
    for item in problem_list:
        f.write(item)
with open(ansname,'w') as f:
    for item in ans_list:
        f.write(item)

