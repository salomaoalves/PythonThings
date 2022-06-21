# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
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

	def __init__(self, word):
		self.word = word
		self.missed_letters = []
		self.guessed_letters = []
		
	#guess the letter
	def guess(self, letter):
		if letter in self.word and letter not in self.guessed_letters:
			self.guessed_letters.append(letter)
		elif letter not in self.word and letter not in self.missed_letters:
			self.missed_letters.append(letter)
		else:
			return False
		return True
		
	#check is the game finished
	def hangman_over(self):
		return self.hangman_won() or (len(self.missed_letters) == 6)
		
	#check if the player won
	def hangman_won(self):
		if '_' not in self.hide_word():
			return True
		return False
		
	#hide word on the board
	def hide_word(self):
		rtn = ''
		for letter in self.word:
			if letter not in self.guessed_letters:
				rtn += '_'
			else:
				rtn += letter
		return rtn
		
	#game status and score
	def print_game_status(self):
		print (board[len(self.missed_letters)])
		print ('\nWords: ' + self.hide_word())
		print ('\nWrong Letters: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Correct Letters: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()

def rand_word():
        with open("hangman_words.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()

def main():
	game = Hangman(rand_word())

	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\nType a letter: ')
		game.guess(user_input)

	game.print_game_status()	

	if game.hangman_won():
		print ('\nCongrats!! You win!!')
	else:
		print ('\nGame over! You lost.')
		print ('The word was ' + game.word)
		

if __name__ == "__main__":
	main()
