import random

wall = '#'
open = '.'

def createField(dx, dy):
	field = []
	nx = dx*2 +1
	field.append([wall]*nx)
	for y in range(dy):
		row = []
		for x in range(dx):
			row.append(wall)
			row.append(open)
		row.append(wall)
		field.append(row)
		field.append([wall]*nx)
	field[0][(random.randint(1,dx)*2)-1] = 'S'
	field[dy*2][(random.randint(3,dx)*2)-1] = 'E'
	return field

def printMaze(field):
	for f in field:
		print ''.join(f)
		
def possible(node, size):
	mx, my = size
	x, y = node
	check = [(x+2,y),(x-2,y),(x,y+2),(x,y-2)]
	re = []
	for c in check:
		if 0 < c[0] < mx and 0 < c[1] < my:
			re.append(c)
	random.shuffle(re)
	return re

def build(field):
	mx = len(field[0])
	my = len(field)
	start = (1,1)
	stack = [start]
	visited = [start]
	node = start
	while stack:
		dx, dy = node
		rnd = possible(node, (mx,my))
		m = (1,1)
		for r in rnd:
			if r not in visited:
				m = r
				break
		if m not in visited:
			x,y = m
			if dx != x:
				if dx < x:
					field[y][x-1] = open
				else:
					field[y][x+1] = open
			else:
				if dy < y:
					field[y-1][x] = open
				else:
					field[y+1][x] = open
			visited.append(m)
			stack.append(m)
			node = m
		else:
			node = stack.pop()
	return field

#printMaze(build(createField(10,10)))
