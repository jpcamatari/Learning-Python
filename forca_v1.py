# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
from asyncore import read
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.letraErrada = []
		self.letraCerta = []
		
	# Método para adivinhar a letra
	def certa(self, letra):
		if letra in self.word and letra not in self.letraCerta:
			self.letraCerta.append(letra)
		elif letra not in self.word and letra not in self.letraErrada:
			self.letraErrada.append(letra)
		else:
			return False
		return True
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.letraErrada) == 6)

		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.hide_word():
			return True
		return False
		

	# Método para não mostrar a letra no board
	def hide_word(self):
		lista = ''
		for letra in self.word:
			if letra not in self.letraCerta:
				lista += '_'
			else:
				lista += letra
		return lista

		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.letraErrada)])
		print('\nPalavra: '+ self.hide_word())
		print('\nLetras Erradas: ',)
		for letra in self.letraErrada:
			print(letra,)
		print()
		print('\nLetra Corretas: ',)
		for letra in self.letraCerta:
			print(letra,)
		print()

		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.guess(user_input)

	# Verifica o status do jogo
	print(game.print_game_status)	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won:
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

