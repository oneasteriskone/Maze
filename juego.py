import mazegame

def iniciarJuego():
	mazegame.main()


def dificultad(dif):
	if dif == 1:
		mazegame.windowSize = (300, 300)
	elif dif == 2:
		mazegame.windowSize = (780, 580)
	elif dif == 3:
		mazegame.windowSize = (1000, 2000)
	else:
		return False

def movimiento():
	pass

def algo():
	pass