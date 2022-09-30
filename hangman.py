from curses.ascii import isalpha
from pickle import FALSE
import random
from words import word_list

def display_hangman(tries):
    stages = [""" 
                       
                     |_0_|
                       |
                      / \\
                  
                  
                  """,
                  """_______
                  |     |
                  |     0
                  |    /|\\
                  |    / \\
                  |
                  -
                  """,
                  """ 
                  _______
                  |     |
                  |     0
                  |    /|\\
                  |    /
                  |
                  -""",
                  """ 
                  _______
                  |     |
                  |     0
                  |    /|\\
                  |    
                  |
                  -""",""" 
                  _______
                  |     |
                  |     0
                  |    /|
                  |    
                  |
                  -""",
                  """ 
                  _______
                  |     |
                  |     0
                  |    /
                  |    
                  |
                  -""",
                  """ 
                  _______
                  |     |
                  |     0
                  |    
                  |    
                  |
                  -""",
                  """ 
                  _______
                  |     |
                  |     
                  |    
                  |    
                  |
                  -"""]
    return(stages[tries])

def get_text_word():
    file = open("words.txt")
    words = file.readlines()
    index = random.randrange(0,len(words))
    word=words[index].upper()
    return word

def get_word():
    if input("Pick a source for the words.\n\tText file(T)\n\t  or\n\tPython List(P)\n").upper()=="T":
        word=get_text_word().strip()
    else:
        word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_'*len(word)
    guessed = False
    guessed_letters = []
    guessed_words=[]
    tries=7
    print("Let's play HANGMAN!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries >1:
        guess = input("Please guess a word or letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter. Please guess again")
            elif guess not in word:
                print(guess+" is not in the word.")
                guessed_letters.append(guess)
                tries-=1
            else:
                print("Yes, ", guess," is in the word!")
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index]= guess
                    word_completion=''.join(word_as_list)
                    if "_" not in word_completion:
                        guessed=True
        elif len(guess)==len(word) and guess.isalpha():
            if guess == word:
                guessed=True
            elif guess in guessed_words:
                print("You already guessed ",guess)
                tries -=1
            else:
                print(guess, " is incorrect.")
                guessed_words.append(guess)
                tries-=1
        else:
            print("Invalid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print(display_hangman(0))
        print(word,"\nCongratulations, you guessed the correct word! You win! Your enemies weep knowing that your prowess in guessing is unmatched")
    else:
        print("Sorry you ran out of tries. Your enemies laugh at your failing and cheer on your downfall.")

def home_screen():
    print("Welcome to Hangman:\n")
    ans=input("\n\tPress (1) to see the rules.\n\tPress (2) to add words to the text file.\n\tPress (any) to play\n\t")
    if ans=="1":
        rules()
    elif ans=='2':
        add_text()
    else:
        word = get_word()
        play(word)
        while input("Play again? (Y/N)").upper() == "Y":
            word=get_word()
            play(word)

def rules():
    print("1.You have six attempts to guess the hidden word\n2.You can guess either a single letter or the whole word")
    ans = input("Are you ready to play? (Y) or any other key to quit").upper()
    if ans == 'Y':
        word=get_word()
        play(word)
    else:
        home_screen()

def add_text():
    file = open("words.txt",'a')
    writing = True
    while writing:
        word=input("What word would you like to add to the text file? ")
        file.write(word)
        file.write('\n')
        print("You added ",word,"\n")
        ans=input("Would you like to add another word? (Y/N)").upper()
        if ans == 'N':
            file.close()
            home_screen()
            break
        else:
            continue

def main():
    home_screen()

if __name__== "__main__":
    main()  