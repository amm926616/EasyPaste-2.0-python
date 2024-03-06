"""
Created on Mon Aug 14 10:23:08 2023

@author: adam178
"""

from pw_generator import Pw_Generator 
from activation_program import Activate
from datetime import datetime, timedelta
from easy_json import edit_values, read_values, initial_info_setup
import pyperclip
import tkinter as tk
from tkinter import filedialog
from pynput import keyboard
from pynput.keyboard import Listener
import subprocess


def activation():
	pg = Pw_Generator()
	pg.run_pw_generator()
	pc = pg.pc
	subscription_number = pg.hint
	activation = Activate(pc, subscription_number)
	return activation.passed

def calculate_expired_time():
	current_time = datetime.now()
	expired_time = current_time + timedelta(days=30)
	edit_values("expired_time", str(expired_time))

def check_time():
	data = read_values()
	expired_time = data["expired_time"]
	expired_time = datetime.strptime(expired_time, "%Y-%m-%d %H:%M:%S.%f")
	current_time = datetime.now()
	if current_time > expired_time:
		edit_values("sub_state", "HAVENTPAIDFORTHEPROGRAMYET")
		if activation():
			calculate_expired_time()
		exit()

initial_info_setup()
data = read_values()
if data['sub_state'] == 'HAVENTPAIDFORTHEPROGRAMYET':
	if activation():
		calculate_expired_time()

elif data['sub_state'] == 'ALREADYPAIDFORTHEPROGRAM':
	check_time()
	subprocess.run(['python', 'easy_paste.py'])








