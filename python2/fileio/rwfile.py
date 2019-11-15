# read a file then write it in console
# i use this to make I look like code something, but actually not

import os
import time
import sys
import random

def codingFake(filepath, cls_command='cls'):
	clear = lambda: os.system(cls_command)
	clear()

	file = open(filepath)
	dump = file.read()

	for c in dump:
		sys.stdout.write(c)
		sys.stdout.flush()
		r1 = random.randint(1, 20)
		r1 = r1 * 0.01
		time.sleep(r1)

codingFake("README.md", 'clear')