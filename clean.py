#!/usr/bin/python

### This script's purpose is simply to make the raw
### keylogger output more human-readable.

logfile = '/var/log/area.log'

replace_map = {
    '<l_ctrl>': '^',
    '<r_ctrl>': '^',
    '<l_shift>': '',
    '<r_shift>': '',
    '<l_alt>': '',
    '<r_alt>': '',
    '<enter>': '\n',
    '<backspace>': '\b',
    '^c': '^c\n',
}

f = open(logfile,'r')
newdata = f.read()
f.close()

for key in replace_map:
    newdata = newdata.replace(key,replace_map[key])

print newdata
