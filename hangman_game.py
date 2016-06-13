#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~~#~#~#~#~#~#~#~#~#~#~#
# Game of Hangman
# Part of my Python learning process
# Author: June K.
# Date: June 2016
#
# Simple text game you can run on command line with 
# Python 2.7 installed.
#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#

import random

class Hangman():
    
    def __init__(self):
        self.word = ''
        self.valid_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.guessed = []
        self.fullword = []
        self.tries = 6
        
    def chooseword(self):
        words = []
        with open('wordlist.txt') as f:
            for i in f:
                words.append(i.strip())
        self.word = random.choice(words)
        return self.word
    
    # make sure the input is part of the alphabet
    def valid_letter(self, letter):
        return letter in self.valid_letters
       
    def checkletter(self, letter):            
        if letter not in self.word:
            print "Sorry,", letter, "is not in the word."
            self.guessed.append(letter)
        else:
            location =  [i for i, l in enumerate(self.word)if l == letter]
            for l in location:
                self.fullword[l] = letter
            return ' '.join(self.fullword)

    def get_tries(self):
        self.tries -= 1
        return self.tries
   
    def play(self):
        self.word = self.chooseword()
        self.fullword = ['_'] * len(self.word)
        print ' '.join(self.fullword)
        
        while True:
            # Check to see if the word is complete first.
            theword = ''.join(self.fullword)
            if theword == self.word:
                self.win()
                return False
            # If not, lets keeping going.
            letter = raw_input('Guess a Letter ').lower()
            # Check if player wants to Quit the game.
            if letter == 'quit':
                print "The word was: ", self.word, "Would you like to play again? y/n?"
                self.play_again()
                return False
            # Check if player wants to guess the full word.
            if letter == 'guess':
                guess = raw_input('What is your guess? ').lower()
                while True:
                    if guess == self.word:
                        self.win()
                        return False
                    if guess != self.word:
                        s = "Sorry, That's not the right answer. Would you like to guess again? y/n? "
                        again = raw_input(s).lower()
                        if again == 'y':
                            guess = raw_input('What is your guess? ').lower()
                        elif again == 'n':
                            break
                        elif again != 'y' or again != 'n':
                            print "Please choose y or n"
            # Check if input is a single character
            elif not self.valid_letter(letter) or len(letter) > 1:
                print "Please enter a valid letter."
            # Check if letter has already been guessed.
            elif letter in self.guessed or letter in theword:
                print "You already guessed that letter."
            else:
                if not self.checkletter(letter):
                    tries = self.get_tries()
                    if tries == 0:
                        self.lose()
                        break
                    else:
                        print ' '.join(self.fullword)
                        print self.guessed,'Tries left:', tries
                else:
                    print self.checkletter(letter)
                    print self.guessed
    
    def play_again(self):
        while True:
            play = raw_input('y/n? ').lower()
            if play == 'n':
                print "Ok.  Another time then. Bye!"
                break
            elif play == 'y':
                print "Let's play again!"
                newgame = Hangman()
                newgame.play()
                break
            elif play != 'y' or play != 'n':
                print "Please choose y or n"
       
    def win(self):
        print "You've won the game!  Would you like to play again?"
        self.play_again()
                
    def lose(self):
        print "Sorry you lost. The word was:",self.word,'Would you like to play again?'
        self.play_again()
            
 
if __name__ == '__main__':
    print """Welcome to Hangman.
           Type these commands at any time:
           'quit' to stop playing.
           'guess' to guess the complete word."""
    newgame = Hangman()
    newgame.play()
