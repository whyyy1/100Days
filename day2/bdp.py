import datetime, random

def randomBd(num):
    pass




def birthdayPara():
    total = int(input('How many birthdays to generate: (MAX 100)'))
    bd = []
    
    while len(bd) < total:
        randM = random.randint(1,12)
        if randM == 4 or 6 or 8 or 11:
            randD = random.randint(1,30)
        if randM == 2: 
            randD = random.randint(1,28)
        else: 
            randD = random.randint(1,31)
        randY = random.randint(0,2022)

        randomDate = datetime.date(randY,randM, randD)
        bd.append([randomDate.day,randomDate.month])
        
    print(bd)


birthdayPara()