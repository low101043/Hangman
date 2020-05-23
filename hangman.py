import random
from termcolor import cprint, colored
    
























































def menu():
    menuOption = input(colored("Choose an option.  \n 1. Solo Player \n 2. 2 Player \n Enter 1 or 2: ", 'blue'))  #This will ask the user which conversion they want to do

    while menuOption not in["1", "2"]:
        menuOption = input(colored("Choose an option.  \n 1. Solo \n 2. 2 Player \n  Enter 1 or 2:  ", 'red'))  #This will ask the user which conversion they want to do
    
    return menuOption

def wordMaker():
    
    word = input("Please enter a word: ")
    
    while word.isalpha() == False:
        word = input("Please enter a valid word: ")
        
    word = word.lower()
    
    return word
    
def random_word_generator():
    
    randomWords = ["happy", "important", "cake", "ball", "enter", "computer", "option", "time", "mail", "word", "ready", "walking", "unhappy", "queen", "quirk", "dwarf", "console", "games", "python", "science", "software", "engineering", "please", "linux", "year", "university", "school", "number", "battery", "files", "documents", "search", "friend", "three", "maths", "equation", "subjects", "physics", "program", "school", "animal", "monkey", "music", "pencil", "disclosure", "time", "sound", "charge", "light", "star", "wars", "trek", "discovery", "force", "mass", "chop", "chips" "last", "cinematic", "film", "pacific", "painting", "pig", "alarm", "twig", "rules", "packinging", "turtle", "hyper", "text", "capital", "keyboard", "menu", "due", "duke", "expedition", "song", "blood", "faith", "religion", "trignometry", "strain", "stress", "law", "social", "media", "hidden", "king", "quirky", "exclamation", "subtraction", "addition", "good", "great", "phone", "commenwealth", "ear", "book", "cross", "egg", "blue", "yellow", "greece", "rival", "regions", "running", "cheifs", "imagine", "dragons", "try", "united", "kingdom", "town", "city", "line", "return"]
    lengthOfList = len(randomWords)
    randomNumber = random.randint(0, lengthOfList - 1)
    randomWord = randomWords[randomNumber]

    return randomWord

def wordHide(wordToUse):
    
    hiddenWord = ""
    for letter in wordToUse:
        hiddenWord = hiddenWord + "_ "
    
    print(hiddenWord)
    return hiddenWord
    
def enteringLetter(alpahabetToUse):
    
    letter = input("Please guess a letter: ")
    
    while letter.isalpha() == False or len(letter) != 1 or letter not in alpahabetToUse:
        letter = input("{} is invalid.  Please enter a letter: ".format(letter))
    letterLower = letter.lower()
    
   
    return letterLower
    
def checkLetter(letterToUse, wordToGuess, guessedWord):
    
    done = False
    finishedLocal = False
    checkWord = ""
    for character in wordToGuess:

        checkWord = checkWord + character + " "
        if letterToUse == character:
            listWord = list(guessedWord)
            listGuess = list(checkWord)
            numberOfTimes = checkWord.count(letterToUse)
            if numberOfTimes >  1:
                posistion = 0
                for i in range(0,numberOfTimes):
                    index = listGuess.index(letterToUse, posistion, len(listGuess))
                    listWord[index] = letterToUse
                    posistion = index + 1
            else:
                
                index = listGuess.index(letterToUse)
                listWord[index] = letterToUse

            guessedWordSecond = ""            
            for letter in listWord:
                guessedWordSecond = guessedWordSecond + letter
            done = True

        
    if done == True:
        print(colored("This letter is in the word", 'cyan', attrs = ['blink']))
        if "_" not in guessedWordSecond:
            finishedLocal = True
    else:
        print(colored("This is not in the word", 'magenta', attrs = ['underline']))
        guessedWordSecond = guessedWord
        
    print("\n" + guessedWordSecond)
        
        
    return done, guessedWordSecond, finishedLocal


    
def alphabetSorter(alphabet, letter):
    
    for letterInAlphabet in alphabet:
        if letterInAlphabet == letter:
            indexToUse = alphabet.index(letter)
            del alphabet[indexToUse]
    print("Letters remaining", alphabet)
    return alphabet
    
def livesLeft(lives, done):
    
    if done == False:
        lives = lives -1
        
    if lives == 0:
        print(" ___")
        print("|   |")
        print("|   O")
        print("|  -|-")
        print('|   /\ ')
        print("|")
        
        print("You're dead")
    
    elif lives == 1:
        print(" ___")
        print("|   |")
        print("|   O")
        print("|  -|-")
        print('|    ')
        print("|")
    
    elif lives == 2:
        print(" ___")
        print("|   |")
        print("|   O")
        print("|   |")
        print('|    ')
        print("|")
        
    elif lives == 3:
        print(" ___")
        print("|   |")
        print("|   O")
        print("|   ")
        print('|    ')
        print("|")
    
    elif lives == 4:
        print(" ___")
        print("|   |")
        print("|   ")
        print("|  ")
        print('|   ')
        print("|")
    
    elif lives == 5:
        print(" ___")
        print("|   ")
        print("|   ")
        print("|  ")
        print('|   ')
        print("|")    
        
    elif lives == 6:
        print(" ")
        print("|   ")
        print("|   ")
        print("|  ")
        print('|   ')
        print("|")
    
    elif lives == 7:
        print(" ")
        print("   ")
        print("   ")
        print("|  ")
        print('|   ')
        print("|")
        
    elif lives == 8:
        print(" ")
        print("   ")
        print("   ")
        print("  ")
        print('|    ')
        print("|")
        
    elif lives == 9:
        print(" ")
        print("   ")
        print("   ")
        print("  ")
        print('    ')
        print("|")
    
    elif lives == 10:
        print(" ")
        print("   ")
        print("   ")
        print("  ")
        print('    ')
        print("")
        
    return lives

looper = True
print(colored("Welcome to Hangman.", 'cyan'))

while looper ==True:
    
    menuOption = menu()
    alphabetUsed = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "u", "r", "s", "t", "u", "v", "w", "x", "w", "y", "z"]   
    livesGlobal = 10
    if menuOption == "1":
        #Solo Main
        
        gameOver = False
        print("You have 10 lives to try and guess this random word")
        wordWhichToGuess = random_word_generator()
        wordWhichIsHidden = wordHide(wordWhichToGuess)
        while livesGlobal != 0 and gameOver == False:
            letterGlobal = enteringLetter(alphabetUsed)
            doneGlobal, wordWhichIsHidden, gameOver = checkLetter(letterGlobal, wordWhichToGuess, wordWhichIsHidden)
            alphabetUsed = alphabetSorter(alphabetUsed, letterGlobal)
            livesGlobal = livesLeft(livesGlobal, doneGlobal)
            
            print("You have", livesGlobal ,"live(s) left")
        
        
        if gameOver == True:
            print(colored("\n Well done you have guessed the word", 'green'))
        else:
            print("\n Game Over.  The word is {}".format(wordWhichToGuess))
        
        
        
    else:
        #Multiplayer Main
        
        gameOver = False
        print("You have 10 lives to try and guess the random word your friend has typed")
        wordWhichToGuess = wordMaker()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        wordWhichIsHidden = wordHide(wordWhichToGuess)
        while livesGlobal != 0 and gameOver == False:
            letterGlobal = enteringLetter(alphabetUsed)
            doneGlobal, wordWhichIsHidden, gameOver = checkLetter(letterGlobal, wordWhichToGuess, wordWhichIsHidden)
            alphabetUsed = alphabetSorter(alphabetUsed, letterGlobal)
            livesGlobal = livesLeft(livesGlobal, doneGlobal)
            
            print("You have", livesGlobal ,"live(s) left")
        
        
        if gameOver == True:
            print("\n Well done you have guessed the word")
        else:
            print("\n Game Over.  The word is {}".format(wordWhichToGuess))
        
        
#Make a menu AND AGAIN (I have)
#1 Player – Random Word  (Output: Word), Enter a letter (Letter, Letter), Check letter, Lives, Output letter
#2 Player – Enter Word (Validate) , Enter a letter (Validate), Check letter, Lives, Output letter

