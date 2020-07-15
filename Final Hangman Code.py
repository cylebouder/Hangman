# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
WORDLIST_FILENAME = "Hangman Words.txt"
print ("Hello! Welcome to Hard Hangman! This is just like regular hangman. ")
print ("If you guess a vowel wrong, you lose 2 guesses.('Y' does not count ")
print ("as a vowel) If you guess a consonant wrong, you lose 1 guess. Also,")
print ("you will lose a warning if you guess a letter twice or if you guess")
print ("an invalid letter. If you type '*', you get a hint. You will only ")
print ("get a hint if you got at least 2 letters right. If you win, it will")
print ("show you haw many points you got which is just the amount of unique")
print ("letters multiplied by the amount of guesses left. ")
print (" ")
print (" ")

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# end of helper code

# -----------------------------------

# Load the list of words into the letters_guessedable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
letters_guessed = []
#secret_word = random.choice(wordlist)
def is_word_guessed(secret_word, letters_guessed):
    
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = secret_word.lower()
    swletters = set(secret_word)
    for item in swletters:
        if item not in letters_guessed:
            return False
        return True
        

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    #Homework: Simplify down to 8-9 lines
    #Create 1 letters_guessedable
    #Ask Dad for hints from Mr. Tim's Solution 
    # Output: string with _ and spaces: apple should be a_ _ le
    guessedword = ""
    swletters = list(secret_word)
    for item in swletters:
        if item in letters_guessed:
            guessedword += item
        else:
            guessedword += "_ "
    return guessedword
            #do nothing
    #If guessed letter is in the real word, add it to guessedword. 
    #Else, don't add it to guessedword. 
       
    
   
   
def get_available_letters(letters_guessed):
    alphabet = list(string.ascii_lowercase)
    available_letters = ""
    for item in alphabet:
        if item not in letters_guessed:
            available_letters += item
    print ("Available letters: " + str(available_letters))
    return list(available_letters)
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    swlist = list(secret_word)
    guesses = 6
    warning = 3
    warn = 0
    alphabet = list(string.ascii_lowercase)
    vowels = ["a", "e", "i", "o", "u"]
    get_available_letters(letters_guessed)
    print ("I am thinking of a word that is " + str(len(swlist)) + " letters long. ")
    print ("You have " + str(warning) + " warnings left.")
    print ("------------------------------------------------------------")
    while guesses > 0 and get_guessed_word(secret_word, letters_guessed) != secret_word:
        warn = 0
        warn1 = 0
        tracker = 0
        print ("You have " + str(guesses) + " guesses left. ")
        get_available_letters(letters_guessed)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess not in alphabet and warning > 0:
            letters_guessed.append(guess)
            current = get_guessed_word(secret_word, letters_guessed)
            warning -= 1
            warn1 = 1
            print ("Oops! That is not a valid letter. You have " + str(warning) + " warnings left: "+ str(current))
            tracker = 1
            warn += 1
        if guess in letters_guessed and warning > 0 and warn1 == 0:
            warning -= 1
            letters_guessed.append(guess)
            current = get_guessed_word(secret_word, letters_guessed)
            print ("Oops! You've already guessed that letter. You have " + str(warning) + " warnings left: " + str(current))
            warn = 1
            tracker = 1
        elif guess not in alphabet and warning < 1 and tracker == 0:
            letters_guessed.append(guess)
            current = get_guessed_word(secret_word, letters_guessed)
            guesses -= 1
            warn1 = 1
            print ("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+ str(current))
            warn += 1
        elif guess in letters_guessed and warning < 1 and warn1 == 0 and tracker == 0:
            letters_guessed.append(guess)
            current = get_guessed_word(secret_word, letters_guessed)
            print ("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + str(current))
            guesses -= 1
            warn = 1
        elif guess not in swlist and warn == 0:
            letters_guessed.append(guess)
            current = get_guessed_word(secret_word, letters_guessed)
            if guess not in vowels:
                guesses -= 1
            if guess in vowels:
                guesses -= 2
            print ("Oops! That letter is not in my word: " + str(current))
        if guess in swlist and warn == 0:
            letters_guessed.append(guess)
            current = get_guessed_word(secret_word, letters_guessed)
            print ("Good guess! " + str(current))
        warn = 0
        print ("------------------------------------------------------------")
    if guesses <= 0:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ". ")
    elif get_guessed_word(secret_word, letters_guessed) == secret_word:
        print ("Congratulations, you won!")
        print ("Your total score for this game was " + str(guesses * len(set(secret_word))) + ". ")
    #print(get_guessed_word(secret_word, letters_guessed))
    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    mwletters = []
    owletters = list(other_word)
    for item in list(my_word):
        if item != " ":
            mwletters.append(item)
    if len(mwletters) == len(owletters):
        tracker = 0
        index = 0
        for i in range(len(mwletters)):
            if mwletters[index] != owletters[index] and mwletters[index] != "_":
                tracker = 1
            index += 1
        if tracker == 1:
            return False
        elif tracker == 0:
            return True
    return False
    """
    1. Same length (Check)
    2. For loop that goes through every letter (Check)
    3. Checking to see if the letters are the same in the same places
    4. Or if the the letter is a blank
    5. If there is at least one wrong, it returns 'False'
    6. If there is nothing wrong, it returns 'True'
    """
    #app_ _ == aplpe
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"


def show_possible_matches(my_word):
    matches = ""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            matches += other_word
            matches += ", "
    list_for_matches = list(matches)
    for i in range(2):
        list_for_matches.pop(-1)
    matches = ""
    for item in list_for_matches:
        matches += item
    return matches
    
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
def hangman_with_hints(secret_word):
    swlist = list(secret_word)
    guesses = 6
    warning = 3
    warn = 0
    g = 0
    alphabet = list(string.ascii_lowercase)
    vowels = ["a", "e", "i", "o", "u"]
    get_available_letters(letters_guessed)
    print ("I am thinking of a word that is " + str(len(swlist)) + " letters long. ")
    print ("You have " + str(warning) + " warnings left.")
    print ("------------------------------------------------------------")
    while guesses > 0 and get_guessed_word(secret_word, letters_guessed) != secret_word:
        warn = 0
        warn1 = 0
        tracker = 0
        print ("You have " + str(guesses) + " guesses left. ")
        get_available_letters(letters_guessed)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess != "*":
            if guess not in alphabet and warning > 0:
                letters_guessed.append(guess)
                current = get_guessed_word(secret_word, letters_guessed)
                warning -= 1
                warn1 = 1
                print ("Oops! That is not a valid letter. You have " + str(warning) + " warnings left: "+ str(current))
                tracker = 1
                warn += 1
            if guess in letters_guessed and warning > 0 and warn1 == 0:
                warning -= 1
                letters_guessed.append(guess)
                current = get_guessed_word(secret_word, letters_guessed)
                print ("Oops! You've already guessed that letter. You have " + str(warning) + " warnings left: " + str(current))
                warn = 1
                tracker = 1
            elif guess not in alphabet and warning < 1 and tracker == 0:
                letters_guessed.append(guess)
                current = get_guessed_word(secret_word, letters_guessed)
                guesses -= 1
                warn1 = 1
                print ("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+ str(current))
                warn += 1
            elif guess in letters_guessed and warning < 1 and warn1 == 0 and tracker == 0:
                letters_guessed.append(guess)
                current = get_guessed_word(secret_word, letters_guessed)
                print ("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + str(current))
                guesses -= 1
                warn = 1
            elif guess not in swlist and warn == 0:
                letters_guessed.append(guess)
                current = get_guessed_word(secret_word, letters_guessed)
                if guess not in vowels:
                    guesses -= 1
                if guess in vowels:
                    guesses -= 2
                print ("Oops! That letter is not in my word: " + str(current))
            if guess in swlist and warn == 0:
                letters_guessed.append(guess)
                current = get_guessed_word(secret_word, letters_guessed)
                print ("Good guess! " + str(current))
                g +=1
        if guess == "*":
            my_word = get_guessed_word(secret_word, letters_guessed)
            if g > 1:
                print(show_possible_matches(my_word))
            else:
                print ("Sorry, you haven't guessed enough letters right to get hints. ")
        warn = 0
        print ("------------------------------------------------------------")
    if guesses <= 0:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ". ")
    elif get_guessed_word(secret_word, letters_guessed) == secret_word:
        print ("Congratulations, you won!")
        print ("Your total score for this game was " + str(guesses * len(set(secret_word))) + ". ")
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #mark
    #secret_word = choose_word(wordlist)
    
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
