import random

options = ['sang', 'kaghaz', 'gheichi']
userPoint = 0
computerPoint = 0
for i in range(3) :
    pc = random.choice(options)
    user = input('lotfan az beyn "sang", "kaghaz", "ghechi" yek mored entekhab konid        ')
    if pc != user :
        if user == 'sang' and pc == 'gheichi' :
            userPoint += 1
        elif user == 'gheichi' and pc == 'kaghaz' :
            userPoint += 1
        elif user == 'kaghaz' and pc == 'sang' :
            userPoint += 1
        elif pc == 'gheichi' and user == 'kaghaz' :
            computerPoint += 1
        elif pc == 'kaghaz' and user == 'sang' :
            computerPoint += 1
        elif pc == 'sang' and user == 'gheichi' :
            computerPoint +=1
    print('user = ',user +'\n')
    print('computer = ',pc+'\n')        
    if userPoint > computerPoint :
        print('natije bazi = bordi\n','emtiaz shoma= ',userPoint ,'emtiaz computer=',computerPoint ,'\n')
    elif computerPoint >userPoint :
        print('natije bazi = bakhti\n','emtiaz shoma= ',userPoint ,'emtiaz computer=',computerPoint,'\n')   
    elif userPoint == computerPoint :
        print('natije bazi = mosavi\n','emtiaz shoma= ',userPoint ,'emtiaz computer=',computerPoint,'\n')          
