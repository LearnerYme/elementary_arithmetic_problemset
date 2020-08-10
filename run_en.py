import tkinter as tk
import os
import json

conf = 'conf.json'
with open(conf) as f:
    params = json.load(f)

filename_json = params['filename']
ansname_json = params['ansname']
unitary_json = params['unitary']
shuffle_json = params['shuffle']
int_plus = params['int_plus']
int_subtract = params['int_subtract']
int_multiply = params['int_multiply']
int_divide = params['int_divide']

#initializing windows
win = tk.Tk()
win.title('Elementary Arithmetic Problem Set - Yme')
win.geometry('800x800+200+50')
tk.Label(win, text='Elementary Arithmetic Problemset', font=('Arial',32)).pack()

#save file settings
frame_fn = tk.Frame(win)
frame_fn.pack(side=tk.TOP)
filename = tk.StringVar()
ansname = tk.StringVar()
timesave = tk.BooleanVar()
timesave.set(False)
filename_label = tk.Label(frame_fn,text='Save problem set to:')
ansname_label = tk.Label(frame_fn,text='Save answer to:')
filename_entry = tk.Entry(frame_fn, textvariable=filename, width=40)
ansname_entry = tk.Entry(frame_fn, textvariable=ansname, width=40)
timesave_check = tk.Checkbutton(frame_fn, text='save with time', variable=timesave)
timesave_label = tk.Label(frame_fn, text='select to save as "default name + time"')
filename_entry.insert(tk.INSERT, filename_json)
ansname_entry.insert(tk.INSERT, ansname_json)
filename_label.grid(row=0, column=0)
filename_entry.grid(row=0, column=1)
timesave_check.grid(row=0, column=2)
timesave_label.grid(row=1, column=2)
ansname_label.grid(row=1, column=0)
ansname_entry.grid(row=1, column=1)

#unitary and shuffle settings
frame_us = tk.Frame(win)
frame_us.pack()
unitary = tk.BooleanVar()
unitary_value = tk.IntVar()
if unitary_json is False:
    unitary.set(False)
    unitary_value.set(0)
else:
    unitary.set(True)
    unitary_value.set(unitary_json)
shuffle = tk.BooleanVar()
unitary.set(unitary_json)
shuffle.set(shuffle_json)
unitary_check = tk.Checkbutton(frame_us, text='unify the number of problems', variable=unitary)
unitary_entry = tk.Entry(frame_us, textvariable=unitary_value, width=10)
unitary_label = tk.Label(frame_us, text='those problem numbers = 0 will not be affected')
shuffle_check = tk.Checkbutton(frame_us, text='shuffle problems', variable=shuffle)
unitary_check.grid(row=0, column=0)
unitary_entry.grid(row=0, column=1)
unitary_label.grid(row=0, column=2)
shuffle_check.grid(row=1, column=0)

#problem settings frame
frame_ar = tk.Frame(win)
frame_ar.pack()
frame_ar_p = tk.Frame(frame_ar)
frame_ar_s = tk.Frame(frame_ar)
frame_ar_m = tk.Frame(frame_ar)
frame_ar_d = tk.Frame(frame_ar)
frame_ar_p.grid(row=0, column=0)
frame_ar_s.grid(row=0, column=1)
frame_ar_m.grid(row=1, column=0)
frame_ar_d.grid(row=1, column=1)
plus_label = tk.Label(frame_ar_p, text='ADDITION setting', font=('Calibri',20))
subtract_label = tk.Label(frame_ar_s, text='SUBTRACTION settings', font=('Calibri',20))
multiply_label = tk.Label(frame_ar_m, text='MULTIPLICATION settings', font=('Calibri',20))
divide_label = tk.Label(frame_ar_d, text='DIVISION settings', font=('Calibri',20))
plus_label.grid(row=0, column=0)
subtract_label.grid(row=0, column=0)
multiply_label.grid(row=0, column=0)
divide_label.grid(row=0, column=0)
#plus settings
plus_num_json = int_plus['num']
plus_low_json = int_plus['low']
plus_high_json = int_plus['high']
plus_maximum_json = int_plus['maximum']
plus_num_int = tk.IntVar()
plus_num_int.set(plus_num_json)
plus_num_label = tk.Label(frame_ar_p, text='problem number:')
plus_num_entry = tk.Entry(frame_ar_p, textvariable=plus_num_int, width=6)
plus_low_int = tk.IntVar()
plus_low_int.set(plus_low_json)
plus_low_label = tk.Label(frame_ar_p, text='minimum:')
plus_low_entry = tk.Entry(frame_ar_p, textvariable=plus_low_int, width=6)
plus_high_int = tk.IntVar()
plus_high_int.set(plus_high_json)
plus_high_label = tk.Label(frame_ar_p, text='maximum:')
plus_high_entry = tk.Entry(frame_ar_p, textvariable=plus_high_int, width=6)
plus_maximum_int = tk.IntVar()
plus_maximum_int.set(plus_maximum_json)
plus_maximum_label = tk.Label(frame_ar_p, text='maximum of result:')
plus_maximum_entry = tk.Entry(frame_ar_p, textvariable=plus_maximum_int, width=6)
plus_num_label.grid(row=1, column=0)
plus_low_label.grid(row=2, column=0)
plus_high_label.grid(row=3, column=0)
plus_maximum_label.grid(row=4, column=0)
plus_num_entry.grid(row=1, column=1)
plus_low_entry.grid(row=2, column=1)
plus_high_entry.grid(row=3, column=1)
plus_maximum_entry.grid(row=4, column=1)
#subtract settings
subtract_num_json = int_subtract['num']
subtract_low_json = int_subtract['low']
subtract_high_json = int_subtract['high']
subtract_neg_json = int_subtract['neg']
subtract_num_int = tk.IntVar()
subtract_num_int.set(subtract_num_json)
subtract_num_label = tk.Label(frame_ar_s, text='problem number:')
subtract_num_entry = tk.Entry(frame_ar_s, textvariable=subtract_num_int, width=6)
subtract_low_int = tk.IntVar()
subtract_low_int.set(subtract_low_json)
subtract_low_label = tk.Label(frame_ar_s, text='minimum:')
subtract_low_entry = tk.Entry(frame_ar_s, textvariable=subtract_low_int, width=6)
subtract_high_int = tk.IntVar()
subtract_high_int.set(subtract_high_json)
subtract_high_label = tk.Label(frame_ar_s, text='maximum:')
subtract_high_entry = tk.Entry(frame_ar_s, textvariable=subtract_high_int, width=6)
subtract_neg_bool = tk.BooleanVar()
subtract_neg_bool.set(subtract_neg_json)
subtract_neg_check = tk.Checkbutton(frame_ar_s, text='allow negative numbers', variable=subtract_neg_bool)
subtract_num_label.grid(row=1, column=0)
subtract_low_label.grid(row=2, column=0)
subtract_high_label.grid(row=3, column=0)
subtract_num_entry.grid(row=1, column=1)
subtract_low_entry.grid(row=2, column=1)
subtract_high_entry.grid(row=3, column=1)
subtract_neg_check.grid(row=4, column=1)
#multiply settings
multiply_num_json = int_multiply['num']
multiply_low_json = int_multiply['low']
multiply_high_json = int_multiply['high']
multiply_maximum_json = int_multiply['maximum']
multiply_marker_json = int_multiply['marker']
multiply_num_int = tk.IntVar()
multiply_num_int.set(multiply_num_json)
multiply_num_label = tk.Label(frame_ar_m, text='problem number:')
multiply_num_entry = tk.Entry(frame_ar_m, textvariable=multiply_num_int, width=6)
multiply_low_int = tk.IntVar()
multiply_low_int.set(multiply_low_json)
multiply_low_label = tk.Label(frame_ar_m, text='minimum:')
multiply_low_entry = tk.Entry(frame_ar_m, textvariable=multiply_low_int, width=6)
multiply_high_int = tk.IntVar()
multiply_high_int.set(multiply_high_json)
multiply_high_label = tk.Label(frame_ar_m, text='maximum:')
multiply_high_entry = tk.Entry(frame_ar_m, textvariable=multiply_high_int, width=6)
multiply_maximum_int = tk.IntVar()
multiply_maximum_int.set(multiply_maximum_json)
multiply_maximum_label = tk.Label(frame_ar_m, text='maximum of result:')
multiply_maximum_entry = tk.Entry(frame_ar_m, textvariable=multiply_maximum_int, width=6)
multiply_marker_str = tk.StringVar()
multiply_marker_str.set(multiply_marker_json)
multiply_marker_label = tk.Label(frame_ar_m, text='multiplication symbol: ')
multiply_marker_entry = tk.Entry(frame_ar_m, textvariable=multiply_marker_str, width=3)
multiply_num_label.grid(row=1, column=0)
multiply_low_label.grid(row=2, column=0)
multiply_high_label.grid(row=3, column=0)
multiply_maximum_label.grid(row=4, column=0)
multiply_marker_label.grid(row=5, column=0)
multiply_num_entry.grid(row=1, column=1)
multiply_low_entry.grid(row=2, column=1)
multiply_high_entry.grid(row=3, column=1)
multiply_maximum_entry.grid(row=4, column=1)
multiply_marker_entry.grid(row=5, column=1)
#divide settings
divide_num_json = int_divide['num']
divide_maximum_json = int_divide['maximum']
divide_maximum_divisor_json = int_divide['maximum_divisor']
divide_decimal_json = int_divide['decimal']
divide_marker_json = int_divide['marker']
divide_mod_json = int_divide['mod']
divide_num_int = tk.IntVar()
divide_num_int.set(divide_num_json)
divide_num_label = tk.Label(frame_ar_d, text='problem number:')
divide_num_entry = tk.Entry(frame_ar_d, textvariable=divide_num_int, width=6)
divide_maximum_int = tk.IntVar()
divide_maximum_int.set(divide_maximum_json)
divide_maximum_label = tk.Label(frame_ar_d, text='maximum of divident:')
divide_maximum_entry = tk.Entry(frame_ar_d, textvariable=divide_maximum_int, width=6)
divide_maximum_divisor_int = tk.IntVar()
divide_maximum_divisor_int.set(divide_maximum_divisor_json)
divide_maximum_divisor_label = tk.Label(frame_ar_d, text='maximum of divisor:')
divide_maximum_divisor_entry = tk.Entry(frame_ar_d, textvariable=divide_maximum_divisor_int, width=6)
divide_marker_str = tk.StringVar()
divide_marker_str.set(divide_marker_json)
divide_marker_label = tk.Label(frame_ar_d, text='division symbol: ')
divide_marker_entry = tk.Entry(frame_ar_d, textvariable=divide_marker_str, width=3)
divide_decimal_bool = tk.BooleanVar()
divide_decimal_bool.set(divide_decimal_json)
divide_decimal_check = tk.Checkbutton(frame_ar_d, text='decimal', variable=divide_decimal_bool)
divide_decimal_label = tk.Label(frame_ar_d, text='no use yet, in development')
divide_mod_bool = tk.BooleanVar()
divide_mod_bool.set(divide_mod_json)
divide_mod_check = tk.Checkbutton(frame_ar_d, text='remainder', variable=divide_mod_bool)
divide_mod_label = tk.Label(frame_ar_d, text='if not selected, problems will not have remainders')
divide_num_label.grid(row=1, column=0)
divide_maximum_label.grid(row=2, column=0)
divide_maximum_divisor_label.grid(row=3, column=0)
divide_marker_label.grid(row=4, column=0)
divide_decimal_check.grid(row=5, column=0)
divide_mod_check.grid(row=6, column=0)
divide_num_entry.grid(row=1, column=1)
divide_maximum_entry.grid(row=2, column=1)
divide_maximum_divisor_entry.grid(row=3, column=1)
divide_marker_entry.grid(row=4, column=1)
divide_decimal_label.grid(row=5, column=1)
divide_mod_label.grid(row=6, column=1)

#status window
status_window = tk.Text(win, height=16)
status_window.pack()

#save and generate and reset
frame_sgr = tk.Frame(win)
frame_sgr.pack()
#save
def save_cmd():
    conf_temp = params
    if timesave.get() is True:
        conf_temp['filename'] = 'time'
    else:
        conf_temp['filename'] = filename.get()
    conf_temp['ansname'] = ansname.get()

    if unitary.get() is False:
        conf_temp['unitary'] = unitary.get()
    else:
        conf_temp['unitary'] = unitary_value.get()
    conf_temp['shuffle'] = shuffle.get()

    conf_temp['int_plus']['num'] = plus_num_int.get()
    conf_temp['int_plus']['low'] = plus_low_int.get()
    conf_temp['int_plus']['high'] = plus_high_int.get()
    conf_temp['int_plus']['maximum'] = plus_maximum_int.get()

    conf_temp['int_subtract']['num'] = subtract_num_int.get()
    conf_temp['int_subtract']['low'] = subtract_low_int.get()
    conf_temp['int_subtract']['high'] = subtract_high_int.get()
    conf_temp['int_subtract']['neg'] = subtract_neg_bool.get()

    conf_temp['int_multiply']['num'] = multiply_num_int.get()
    conf_temp['int_multiply']['low'] = multiply_low_int.get()
    conf_temp['int_multiply']['high'] = multiply_high_int.get()
    conf_temp['int_multiply']['maximum'] = multiply_maximum_int.get()
    conf_temp['int_multiply']['marker'] = multiply_marker_str.get()

    conf_temp['int_divide']['num'] = divide_num_int.get()
    conf_temp['int_divide']['maximum'] = divide_maximum_int.get()
    conf_temp['int_divide']['maximum_divisor'] = divide_maximum_divisor_int.get()
    conf_temp['int_divide']['marker'] = divide_marker_str.get()
    conf_temp['int_divide']['decimal'] = divide_decimal_bool.get()
    conf_temp['int_divide']['mod'] = divide_mod_bool.get()

    with open('conf.json','w') as f:
        json.dump(conf_temp,f)

    status_window.delete(0.0, tk.END)
    status_window.insert(tk.INSERT, 'Settings saved!')     
    return
save_button = tk.Button(frame_sgr, text='SAVE', command=save_cmd)
save_button.grid(row=0, column=0)
#generate
def generate_cmd():
    os.system('python3 problemset.py')
    status_window.delete(0.0, tk.END)
    status_window.insert(tk.INSERT, 'Problem set generated!')    
    return
generate_button = tk.Button(frame_sgr, text='SUBMIT', command=generate_cmd)
generate_button.grid(row=0, column=1)
#reset
def reset_cmd():
    filename_entry.delete(0, tk.END)
    filename_entry.insert(tk.INSERT, filename_json)
    ansname_entry.delete(0, tk.END)
    ansname_entry.insert(tk.INSERT, ansname_json)
    timesave_check.deselect()
    if unitary_json is False:
        unitary_check.deselect()
    else:
        unitary_check.select()
        unitary_entry.delete(0, tk.END)
        unitary_entry.insert(tk.INSERT, unitary_json)
    if shuffle_json is False:
        shuffle_check.deselect()
    else:
        shuffle_check.select()

    plus_num_entry.delete(0, tk.END)
    plus_num_entry.insert(tk.INSERT, plus_num_json)
    plus_low_entry.delete(0, tk.END)
    plus_low_entry.insert(tk.INSERT, plus_low_json)
    plus_high_entry.delete(0, tk.END)
    plus_high_entry.insert(tk.INSERT, plus_high_json)
    plus_maximum_entry.delete(0, tk.END)
    plus_maximum_entry.insert(tk.INSERT, plus_maximum_json)

    subtract_num_entry.delete(0, tk.END)
    subtract_num_entry.insert(tk.INSERT, subtract_num_json)
    subtract_low_entry.delete(0, tk.END)
    subtract_low_entry.insert(tk.INSERT, subtract_low_json)
    subtract_high_entry.delete(0, tk.END)
    subtract_high_entry.insert(tk.INSERT, subtract_high_json)
    if subtract_neg_json is False:
        subtract_neg_check.deselect()
    else:
        subtract_neg_check.select()

    multiply_num_entry.delete(0, tk.END)
    multiply_num_entry.insert(tk.INSERT, multiply_num_json)
    multiply_low_entry.delete(0, tk.END)
    multiply_low_entry.insert(tk.INSERT, multiply_low_json)
    multiply_high_entry.delete(0, tk.END)
    multiply_high_entry.insert(tk.INSERT, multiply_high_json)
    multiply_maximum_entry.delete(0, tk.END)
    multiply_maximum_entry.insert(tk.INSERT, multiply_maximum_json)
    multiply_marker_entry.delete(0, tk.END)
    multiply_marker_entry.insert(tk.INSERT, multiply_marker_json)

    divide_num_entry.delete(0, tk.END)
    divide_num_entry.insert(tk.INSERT, divide_num_json)
    divide_maximum_entry.delete(0, tk.END)
    divide_maximum_entry.insert(tk.INSERT, divide_maximum_json)
    divide_maximum_divisor_entry.delete(0, tk.END)
    divide_maximum_divisor_entry.insert(tk.INSERT, divide_maximum_divisor_json)
    divide_marker_entry.delete(0, tk.END)
    divide_marker_entry.insert(tk.INSERT, divide_marker_json)
    if divide_decimal_json is False:
        divide_decimal_check.deselect()
    else:
        divide_decimal_check.select()
    if divide_mod_json is False:
        divide_mod_check.deselect()
    else:
        divide_mod_check.select()

    status_window.delete(0.0, tk.END)
    status_window.insert(tk.INSERT, 'All settings resetted!')

    return
reset_button = tk.Button(frame_sgr, text='RESET', command=reset_cmd)
reset_button.grid(row=0, column=2)

#information about me
def about_cmd():
    status_window.delete(0.0, tk.END)
    with open('aboutme.txt','r') as f:
        about_info = f.read()
    status_window.insert(tk.INSERT, about_info)
    return
about_buttom = tk.Button(win, text='ABOUT THIS TOOL', command=about_cmd)
about_buttom.pack()

win.mainloop()