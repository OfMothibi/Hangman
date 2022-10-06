from curses.ascii import isalpha
from pickle import FALSE
import random
import string
from words import word_list

def display_hangman(tries):    
    stages = [""" 
                       
                     |_0_|
                       |
                      / \\
                  
                  
                  """,
                  """
                  _______
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
    """function to randomly select a word from a txt document

    Returns:
        string: word for user to guess
    """
    file = open("words.txt")
    words = file.readlines()
    index = random.randrange(0,len(words))
    word=words[index].upper()
    return word

def get_word():
    """function to get a word from a python list

    Returns:
        string: word for user to guess
    """
    if input("Pick a source for the words.\n\tText file(T)\n\t  or\n\tPython List(P)\n").upper()=="T":
        word=get_text_word().strip()
    else:
        word = random.choice(word_list)
    return word.upper()

def is_letter(word,guess,word_completion:string,guessed,guessed_letters:list,tries):
    """Takes letter guesses and returns values depending on whether they are right, wrong, or previously entered

    Args:
        word (string): the word that the user is attempting to guess
        guess (string): user input that must be a letter
        word_completion (string): displays the progress that the user has made with their guesses
        guessed (boolean): used to determine whether the guess is correct
        guessed_letters (list): previously entered letter guesses 
        tries (int): index for list of hangman figures
    """
    return_list=[]
    if guess in guessed_letters:
        print("You already guessed this letter. Please guess again")
    elif guess not in word:
        print(guess+" is not in the word.")
        guessed_letters.append(guess)
        tries-=1
    else:
        print("Yes, {guess} is in the word!")
        guessed_letters.append(guess)
        word_as_list=list(word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            word_as_list[index]= guess
            word_completion=''.join(word_as_list)
            if "_" not in word_completion:
                guessed=True
    return_list.append(word_completion)
    return_list.append(guessed)
    return_list.append(guessed_letters)
    return_list.append(tries)
    return(return_list)

def is_word(word,guess,guessed,guessed_words:list,tries):
    """Takes word guesses and returns values depending on whether they are right, wrong, or previously entered

    Args:
        word (string): the word that the user is attempting to guess
        guess (string): user input that must be a word
        word_completion (string): displays the progress that the user has made with their guesses
        guessed (boolean): used to determine whether the guess is correct
        guessed_words (list): previously entered word guesses 
        tries (int): index for list of hangman figures

    Returns:
        list: returns values used in the game screen
    """
    return_list=[]
    if guess == word:
        guessed=True
    elif guess in guessed_words:
        print("You already guessed ",guess)
        tries -=1
    else:
        print(guess, " is incorrect.")
        guessed_words.append(guess)
        tries-=1
    return_list.append(guessed)
    return_list.append(guessed_words)
    return_list.append(tries)
    return return_list

def game_screen(tries,word_completion,guessed_words,guessed_letters):
    """Display the hangman figure, progress of the guess and lists of previously entered guesses

    Args:
        tries (int): indictes the index of the list of hangman figures
        word_completion (string): displays the progress of the guess
        guessed_words (list): the valid guess words the user has previously entered
        guessed_letters (list): the valid guess letters the user has previously entered
    """
    print(display_hangman(tries))
    print(word_completion)
    print("\nYou have tried the following letters and words:\n->{guessed_words}\n-> {guessed_letters}\n")

def play(word):
    """_summary_

    Args:
        word (String): a random word for the user to guess

    Variables:
        word_completion (String): space for the user to see their progress with guesses
        guessed (boolean): indicates whether the user has finished guessing
        guessed_letters (list): a list of the letters entered by the user
        guessed_words (list): a list of the words the user has entered
        tries (int): the number of guesses the user can attempt
    """
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
            results=is_letter(word,guess,word_completion,guessed,guessed_letters,tries)
            word_completion=results[0]
            guessed=results[1]
            guessed_letters=results[2]
            tries=results[3]
        elif len(guess)==len(word) and guess.isalpha():
            results=is_word(word,guess,guessed,guessed_words,tries)
            guessed=results[0]
            guessed_words=results[1]
            tries=results[2]
        else:
            print("Invalid guess")
        game_screen(tries,word_completion,guessed_words,guessed_letters)
    if guessed:
        print(display_hangman(0))
        print(word,"\nCongratulations, you guessed the correct word! You win! Your enemies weep knowing that your prowess in guessing is unmatched")
    else:
        print("Sorry you ran out of tries. Your enemies laugh at your failing and cheer on your downfall.")

def home_screen():
    """Main menu prividing options for users
    """
    print("Welcome to Hangman:\n")
    ans=input("\n\tPress (1) to see the rules.\n\tPress (2) to add words to the text file.\n\tPress (any) to play\n\t")
    if ans=="1":
        rules()
    elif ans=='2':
        add_text()
    else:
        start_game()

def rules():
    """Displays the game rules
    """
    print("1.You have six attempts to guess the hidden word\n2.You can guess either a single letter or the whole word")
    ans = input("Are you ready to play? (Y) or any other key to quit").upper()
    if ans == 'Y':
        start_game()
    else:
        home_screen()

def add_text():
    """Adds words to a txt doc
    """
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

def start_game():
    """Function to initiate the game and keep it running
    """
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word=get_word()
        play(word)

def main():
    home_screen()

if __name__== "__main__":
    main()  