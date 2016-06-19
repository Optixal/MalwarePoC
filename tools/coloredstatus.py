#!/usr/bin/python
# Made by Optixal

status = "\033[1m\033[94m[*]\033[0m "
def print_status(sentence):
    print status + sentence

good = "\033[1m\033[92m[+]\033[0m "
def print_good(sentence):
    print good + sentence

error = "\033[1m\033[91m[-]\033[0m "
def print_error(sentence):
    print error + sentence

warning = "\033[1m\033[93m[!]\033[0m "
def print_warning(sentence):
    print warning + sentence

money = "\033[1m\033[92m[$]\033[0m "
def print_money(sentence):
    print money + sentence

special = "\033[1m\033[38;5;198m[#]\033[0m "
def print_special(sentence):
    print special + sentence


