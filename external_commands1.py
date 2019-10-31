#!/usr/bin/env python
from subprocess import run, PIPE, CalledProcessError
from shlex import split

NETSTAT_CMD = 'netstat -an'

run(NETSTAT_CMD, shell=True)
print('-' * 60)

run(split(NETSTAT_CMD))
print('-' * 60)

LS_CMD = "ls DATA/*.txt"
# WINDOWS
# CMD = r"cmd /c dir DATA\*.txt"
run(LS_CMD, shell=True)
print('-' * 60)

try:
    process = run(split(NETSTAT_CMD), stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err.returncode)
    print(err)
else:
    for line in process.stdout.decode().splitlines():
        if "ESTAB" in line:
            print(line)
    bad_stuff = process.stderr.decode()





