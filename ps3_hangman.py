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
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord: str, lettersGuessed: list[str]):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return True if len(secretWord) == len(''.join([letter if letter in secretWord else '' for letter in lettersGuessed])) else False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join([ character if character in lettersGuessed else '_ ' if character != secretWord[-1] or len(secretWord) == 1 else ' _' for character in secretWord])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join([letter if letter not in lettersGuessed else '' for letter in 'abcdefghijklmnopqrstuvwxyz'])

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    '''
    availableLetters = 8
    leftLetters = 0
    guessedLetters = []
    pic_step = 0
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(secretWord), 'letters long.')

    while leftLetters < availableLetters and not isWordGuessed(secretWord, guessedLetters):
      if isWordGuessed(secretWord, guessedLetters):
        continue
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
hangman(secretWord)
