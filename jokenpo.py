import random

possibles = [1,2,3]
game_map = {1:'Pedra', 2:'Papel' ,3:'Tesoura'}
us = 0

def printres(resus,resbot, winner='Ninguém'):
    print ('\n------------------------------------')
    print(f'Você escolheu: {game_map[resus]} \nO bot escolheu: {game_map[resbot]} \n{winner} venceu!')
    print ('------------------------------------\n')

def user_input():
    user_choice = input('Digite 1 para PEDRA, 2 para PAPEL e 3 para TESOURA! \n_')

    try:
        return int(user_choice)
    except:
       print('\nEscolha um número!\n')
       rules()
       
def against_bot(lis):
    bot  = random.choice(lis)
    
#==============cases================#    
    if bot == us:
        printres(us, bot)

#case 1
    elif bot == 1:
        if us == 2:
            printres(us, bot, 'Você')
        elif us == 3:
            printres(us, bot, 'Bot')
                
#case 2
    elif bot == 2:
        if us == 3:
            printres(us, bot, 'Você')
        elif us == 1:
                printres(us, bot, 'Bot')
                
#case 3
    elif bot == 3:
        if us == 1:
            printres(us, bot, 'Você')
        elif us == 2:
                printres(us, bot, 'Bot')         
              
            
def rules():
    global us
    us = user_input()
    
    if us < 1:
        print ('\nNúmero inválido, tente novamente!\n')
        rules()      
    elif us > 3:
        print ('\nNúmero inválido, tente novamente!\n')
        rules()

    against_bot(possibles)

    rules()
    
rules()
