import pygame
import mazebuilder
import pathfinder
import math

cellsize = 20
WHITE = (255, 255, 255)
base03 = (0, 43, 54)
base02 = (7, 54, 66)
base01 = (88, 110, 117)
base00 = (101, 123, 131)
base0 = (131, 148, 150)
base1 = (147, 161, 161)
red = (220, 50, 47)
green = (133, 153, 0)
windowSize = (780, 580)	

def getDistance(a, b):
        ax, ay = a
        bx, by = b
        d1 = (ax-bx)**2
	d2 = (ay-by)**2
	re = d1+d2
	return math.sqrt(re)

def getMaze():
	re = mazebuilder.build(mazebuilder.createField(((windowSize[0]/cellsize)/2), ((windowSize[1]/cellsize)/2)))
	teleport = pathfinder.getRandomCorner((1,0), re)
	tx, ty = teleport
	re[ty][tx] = 'T'
	path = pathfinder.getPath((1,0), (37, 28), re)
	vwall = path[(len(path)/3)*2]
	vx,vy = vwall
	re[vy][vx] = 'W'
	plate = pathfinder.getRandomCorner((1,0), re)
	while getDistance(vwall, plate) < 2 or plate == teleport:
        	plate = pathfinder.getRandomCorner((1,0), re)
	px,py = plate
	ret = []
	re[py][px] = 'P'
	for y in range(len(re)):
		temp = []
		for x in range(len(re[y])):
			temp.append((re[y][x], 0))
		ret.append(temp)	
	return ret

def getGo(m):
	re = []
	for y in range(len(m)):
		for x in range(len(m[y])):
			if m[y][x][0] == 'T':
				re.append([(x,y), 'T'])
			elif m[y][x][0] == 'W':
				re.append([(x,y), 'W'])
			elif m[y][x][0] == 'P':
				re.append([(x,y), 'P'])
	return re	

#player position
ppos = (1,0)

#viewing distance
vision = 2

#building maze, plates and fakewalls
maze = getMaze()
gameObjects = getGo(maze)
print gameObjects
wallsymbols = ['#', 'W']

pState = 0

pygame.init()
display = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Mazegame v.1')
clock = pygame.time.Clock()

player = pygame.image.load('img/player.png')

def main():
	chrash = False
	while not chrash: #main game loop
		run()
		pygame.quit()

def run():
	while True:
		dir = 'WAIT'
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                        elif event.type == pygame.KEYDOWN:
                                if (event.key == pygame.K_LEFT):
                                        dir = 'LEFT'
                                elif (event.key == pygame.K_RIGHT):
                                        dir = 'RIGHT'
                                elif (event.key == pygame.K_UP):
                                        dir = 'UP'
                                elif (event.key == pygame.K_DOWN):
                                        dir = 'DOWN'
                movePlayer(dir)
                if checkPlayer():
			return
                display.fill(base03)
                drawField()
                #drawGrid()
                drawPlayer()
                pygame.display.update()
                clock.tick(60)

def getCoordsOfObject(object):
	global gameObjects
	for g in gameObjects:
		a,b = g
		if b == object:
			return a
	return None

def checkPlayer():
	global pState
	global ppos
	px, py = ppos
	if pState == 0:
		if ppos == getCoordsOfObject('P'):
			wx, wy = getCoordsOfObject('W')
			maze[wy][wx] = ('.', 1)
			pState = 1
	if ppos == (37, 28):	
		return True
	elif maze[py][px][0] == 'T':
		ppos = (1,0)
	return False	

def drawField():
	global maze
	global pState
	for y in range (0, len(maze)):
		for x in range(0, len(maze[y])):
			px, py = ppos
			if getDistance((x,y),(px,py)) < vision or maze[y][x][1] == 1:
				a,b = maze[y][x]
				maze[y][x] = (a,1)
				if maze[y][x][0] == '#':
					block = pygame.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
					pygame.draw.rect(display, base00, block)
				elif maze[y][x][0] == 'W':
					block = pygame.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
                               		pygame.draw.rect(display, base00, block)
				elif maze[y][x][0] == 'P':
					block = pygame.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
                              		pygame.draw.rect(display, red if pState == 0 else green, block)
				elif maze[y][x][0] == 'T':
                                        block = pygame.Rect(x*cellsize, y*cellsize, cellsize, cellsize)
                                        pygame.draw.rect(display, red, block)

	 			
def movePlayer(direction):
	global ppos
	x, y = ppos
	global windowSize
	dx, dy = windowSize
	if direction == 'UP' and y > 0:
		if maze[y-1][x][0] not in wallsymbols:
			ppos = (x,y-1)
	elif direction == 'DOWN' and y < (dy/cellsize)-1:
		if maze[y+1][x][0] not in wallsymbols:
			ppos = (x,y+1)
	elif direction == 'RIGHT' and x < (dx/cellsize)-1:
		if maze[y][x+1][0] not in wallsymbols:
			ppos = (x+1,y)
	elif direction == 'LEFT' and x > 0:
		if maze[y][x-1][0] not in wallsymbols:
			ppos = (x-1,y)
			
def drawPlayer():
	px, py = ppos
	display.blit(player, (px*cellsize,py*cellsize))

def drawGrid():
	global windowSize
	dx, dy = windowSize
	for x in range(0, dx, cellsize):
		pygame.draw.line(display, base00, (x, 0), (x, dy))
	for y in range(0, dy, cellsize):
		pygame.draw.line(display, base00, (0, y), (dx, y))

main()
