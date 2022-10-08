# Logic game given random number 1-999 have user guess number and if you the correct
# digit but wrong place return "Pico"/ "Fermi" if it correct number in correct place
# "Bagels" if the guess is wrong 
import random  


#function that determines what word is returned

def numberG(guess,randomNum):
    total = randomNum-guess
    guessN = str(guess)
    randN = str(randomNum)
    n1 = []
    n2 = []
    for i in guessN:
        n1.append(int(i))
    for j in randN:
        n2.append(int(j))

    if len(n1) == len(n2):    
        for k in range(len(n1)):
            
            if n1[k] == n2[k]:
                print(f'Fermi: {n1[k]}')
            if n1[k] in n2:

                print(f'Pico: {n1[k]}')
            else:
                print('Bagels')
            
    else:
        print("number isn't equal")

        

def bagels():
    print("In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: \n")
    print("“Pico” when your guess has a correct digit in the wrong place, \n")
    print("“Fermi” when your guess has a correct digit in the correct place, and \n")
    print("“Bagels” if your guess has no correct digits.\n") 
    print("“Numbers isnt equals” means guess to large or small")
    print("You have 10 tries to guess the secret number.")

    tries = 1 
    #random number 1-100
    number = random.randint(1,9999)

    #user guess 
    print(f'Guess#{tries}')
    userGuess = int(input("Please make a guess 1-999: "))
    
    while userGuess != number:
        

        tries += 1
        numberG(userGuess,number)
        print('___________________________________')
        print(f'Guess#{tries}')
        userGuess = int(input("Wrong please make anoter: "))
        
        
        
        if tries == 10:
            print(number)
            print('YOU FAILED!!!! EXITING NOW!')
            exit()
        if userGuess == number:
                print(f'You did it!!!!!!!!!!!!!!!!!!!!!!!! The number was {number}')
if __name__ == "__main__":
    bagels()