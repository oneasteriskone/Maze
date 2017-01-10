import random

def getRandomCorner(start, field):
	stack = [start]
	visited = [start, (0,0)]
	node = start
	dir = (0,0)
	while stack:
		moves = getMoves(node, field)
		for m in moves:
			if m not in visited:
				dir = m
				break
		if dir not in visited:
			visited.append(dir)
			node = dir
		else: 
			stack.pop()
	return dir

def find(start, end, field):
	queue = [start]
	visited = [start]
	plist = [(1,0)]
	while queue:
		node = queue.pop()
		moves = getMoves(node, field)
		for m in moves:
			if m not in visited:
				visited.append(m)
				queue.insert(0,m)
				plist.append(node)
	re = (visited, plist)
	return re

def backtrack(start, end, visit, par):
	re = [start]
	node = start
	while node != end:
		node = par[visit.index(node)]
		re.append(node)
	re.append(end)
	return list(reversed(re))
		

def getMoves(node, field):
	wall = ['#', 'W']
	dx, dy = node
	possible = [(dx+1,dy),(dx-1,dy),(dx,dy+1),(dx,dy-1)]
	re = []
	for p in possible:
		x,y = p
		if (0 < x < len(field[0])) and (0 < y < len(field)):
			if field[y][x] not in wall:
				re.append(p)		
	return re

def getPath(start, end, maze):
	field = maze
	v, p = find(start, end, field)
	re = backtrack(end, start, v, p)
	return re
