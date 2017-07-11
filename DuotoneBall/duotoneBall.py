# -*- coding: utf-8 -*-

import random

slist = []

for i in range(6):#记次循环
	while True:#条件循环
		s = random.randint(1, 33)
		print s
		if s in slist:#判断s这个值是否出现在sllit这个列表里面
			pass #占位符 没有任何的意义
		else:
			break
	slist.append(s)
slist.sort()
s_str = ''
for i in slist:
	s_str += '%02d ' %i
s = random.randint(1, 16)

print s_str + '+ %02d' %s
