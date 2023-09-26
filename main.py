# Hangman game
# -----------------------------------

import random

WORDLIST_FILENAME = "words.txt"

asciiPics = [
  '''
  +---+
      |
      |
      |
      |
      |
=========''',
  '''
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

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist: list):
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord: str, lettersGuessed: list[str]):
    return True if len(secretWord) == len(''.join([letter if letter in secretWord else '' for letter in lettersGuessed])) else False



def getGuessedWord(secretWord: str, lettersGuessed: list):
    return ''.join([ character if character in lettersGuessed else '_ ' if character != secretWord[-1] or len(secretWord) == 1 else ' _' for character in secretWord])



def getAvailableLetters(lettersGuessed: list):
    return ''.join([letter if letter not in lettersGuessed else '' for letter in 'abcdefghijklmnopqrstuvwxyz'])

    

def hangman(secretWord: str):
    availableLetters = 8
    leftLetters = 0
    guessedLetters = []
    pic_step = 0
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secretWord), 'letters long.')

    while leftLetters < availableLetters and not isWordGuessed(secretWord, guessedLetters):
      if isWordGuessed(secretWord, guessedLetters):
        print('Congratulations, you won!')
        return
      print('------------')
      if pic_step != 0:
        print(asciiPics[round(pic_step) - 1])
      print("You have", availableLetters - leftLetters, "left.")
      print("Available letters:", getAvailableLetters(guessedLetters))
      letter = input('Please guess a letter:')
      if not len(letter):
        continue
      letter = letter[0].lower()
      if letter in guessedLetters:
        print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, guessedLetters))
      else:
        guessedLetters.append(letter)
        if letter not in secretWord:
          print('Oops! That letter is not in my word:', getGuessedWord(secretWord, guessedLetters))
          pic_step+=1
          leftLetters+=1
        if letter in secretWord:
          print("Good guess:", getGuessedWord(secretWord, guessedLetters))

    print('------------')
    if isWordGuessed(secretWord, guessedLetters):
      print('Congratulations, you won!')
    else:
      print(asciiPics[round(pic_step) - 1])
      print('Sorry, you ran out of guesses. The word was', secretWord + '.')



secretWord = chooseWord(wordlist).lower()
hangman('brah')
