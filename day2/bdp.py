import datetime, random

def compareBd(list):
    count = 0
    #loops through list comparing all the values to each other 
    for a, birthdayA in enumerate(list):
        for b, birthdayB in enumerate(list[a + 1:]):
            # print(a,birthdayA,b,birthdayB)
            if birthdayA == birthdayB:
                count +=1
                print(birthdayA)
    
    # else:
    #     print(f'had no matches, now running 10000 sims to see what we get ')
        
    #     for i in range(10000):
    #         if i % 10000 == 0:
    #             print(i,"simulations ran")
            

def birthdayPara(total=0):
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
    compareBd(bd)
    

    


birthdayPara()