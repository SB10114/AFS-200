word = 'pineapple'

win = False 

guesses = [ ]

wordBoard = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

turns = 5
while turns > 0 and not win:
    def showBoard():
        str = ''
        for char in wordBoard:
            str += char + ' '
        print(str)
    showBoard()

    guess = input('Please choose a letter: ')


    def checkLetter(guess):
        found = False
        for i in range(0, len(wordBoard)):
            if word[i] == guess:
                found = True
                wordBoard[i] = guess
                #print(wordBoard[i])
        return found


    guessed = False
    for i in range(0, len(guesses)):
            if guesses[i] == guess:
                guessed = True


    if guessed == True:
        print('You have used this letter, guess again!')
    else:
        guesses.append(guess)
        print(guesses)
        found = checkLetter(guess)
        if found == False:
            print('This letter is not in the word ')
            #take a turn away
        else: 
            print('Yes this is a letter! ') 
            #iterate through wordBoard(for loop)
            #is there any item that is = to _
            #if yes, then leave it
            #if not, the word is found win = true

    showBoard()

failed = 0
     
for char in word:
      
    if char in guesses:
        print(char, end=" ")
             
    else:
            print("_")
            print(char, end=" ")
             
            failed += 1
             
 
    if failed == 0:
       
        print("You Win")
         
        
        print("The word is: ", word)
        break
     
    print()
    guess = input("guess a character:")
     

    guesses += guess
     
    if guess not in word:
         
        turns -= 1
         
     
        print("Wrong")
         
    
        print("You have", + turns, 'more guesses')
         
if turns == 0:
    print("You Loose")
#if statement that checks IF they won and prints word and congratulations
#if statement checks if turns are smaller than one