# BARRAZA SÁNCHEZ JESÚS ENRIQUE
# INTELIGENCIA ARTIFICIAL 6-7PM
import random

def drawBoard(board):
	# Esta función imprime el tablero que se pasó.
    # "board" es una lista de 10 cadenas que representan el tablero (ignore el índice 0)
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('--+---+--')
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('--+---+--')
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def inputPlayerLetter():
	# Permite al jugador escribir qué letra quiere ser.
    # Devuelve una lista con la letra del jugador como primer elemento y la letra de la computadora como segundo.
	letter=''
	while not(letter=='X' or letter=='O'):
		print("¿Quieres ser 'X' o 'O'?")
		letter = input().upper()

	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']


def whoGoesFirst():
	print('¿Quieres ir primero? (Si o no)')
	if  input().lower().startswith('s'):
		return 'player'
	else:
		return 'computer'

def playAgain():
	# Esta función devuelve True si el jugador quiere volver a jugar; de lo contrario, devuelve False.
	print('¿Quieres jugar de nuevo? (Si o no)?')
	return input().lower().startswith('s')


def makeMove(board, letter, move):
	board[move] = letter


def isWinner(board,letter):
	# Esta función devuelve True si ese jugador ha ganado.
	return ((board[1]==letter and board[2]==letter and board[3]==letter) or
			(board[4]==letter and board[5]==letter and board[6]==letter) or
			(board[7]==letter and board[8]==letter and board[9]==letter) or
			(board[1]==letter and board[4]==letter and board[7]==letter) or
			(board[2]==letter and board[5]==letter and board[8]==letter) or
			(board[3]==letter and board[6]==letter and board[9]==letter) or
			(board[1]==letter and board[5]==letter and board[9]==letter) or
			(board[3]==letter and board[5]==letter and board[7]==letter))


def getBoardCopy(board):
	# Hace un duplicado de la lista del tablero y lo devuelve como duplicado.
	dupBoard = []

	for i in board:
		dupBoard.append(i)

	return dupBoard


def isSpaceFree(board, move):
	return board[move] == ' '


def getPlayerMove(board):
# Deja que el jugador escriba su movimiento.
	move = '' 
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
		print('¿Cuál es tu próximo movimiento? (1-9)')
		move = input()
	return int(move)


def chooseRandomMoveFromList(board, movesList):
	# Devuelve un movimiento válido de la lista de aprobados en el tablero de aprobados.
    # Devuelve Ninguno si no hay un movimiento válido.
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None


def minimax(board, depth, isMax, alpha, beta, computerLetter):
	# En este apartado se determina dónde mover y devolver ese movimiento.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if isWinner(board, computerLetter):
		return 10
	if isWinner(board, playerLetter):
		return -10
	if isBoardFull(board):
		return 0

	if isMax:
		best = -1000

		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = computerLetter
				best = max(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) - depth)
				alpha = max(alpha, best)
				board[i] = ' '

				if alpha >= beta:
					break

		return best
	else:
		best = 1000

		for i in range(1,10):
			if isSpaceFree(board, i):
				board[i] = playerLetter
				best = min(best, minimax(board, depth+1, not isMax, alpha, beta, computerLetter) + depth)
				beta = min(beta, best)
				board[i] = ' '

				if alpha >= beta:
					break

		return best


def findBestMove(board, computerLetter):
	# Dado un tablero y la letra de la computadora, determina dónde mover y devolver ese movimiento.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	bestVal = -1000
	bestMove = -1


	for i in range(1,10):
		if isSpaceFree(board, i):
			board[i] = computerLetter

			moveVal = minimax(board, 0, False, -1000, 1000, computerLetter)

			board[i] = ' '

			if moveVal > bestVal:
				bestMove = i
				bestVal = moveVal

	return bestMove


def isBoardFull(board):
	# Devuelve True si se han ocupado todos los espacios del tablero. De lo contrario, devuelva Falso.
	for i in range(1,10):
		if isSpaceFree(board, i):
			return False
	return True


print('\nBienvenido al juego del gato!\n')
print('Referencia de numeración en el tablero')
drawBoard('0 1 2 3 4 5 6 7 8 9'.split())
print('')

while True:
	# Restablecer el tablero
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('El' + turn + ' va primero')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			drawBoard(theBoard)
			move = getPlayerMove(theBoard)
			makeMove(theBoard, playerLetter, move)

			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Tu ganaste el juego')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('El juego es un empate')
					break
				else:
					turn = 'computer'
		else:
			move = findBestMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)

			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('Perdiste el juego')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('El juego es un empaxte')
					break
				else:
					turn = 'player'
	if not playAgain():
		break