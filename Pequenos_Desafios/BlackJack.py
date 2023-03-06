#jogo de blackjack!
from IPython.display import clear_output
from time import sleep
import random #importing important stuff

player_name = ""
bet = 0
total_money = 0
card_value = 0
player_total_value = 0
player_draws = 0
total_bet = 0
dealer_total_value = 0 #declaring global variables

class naipe(object):
    def __init__(self,cartas = [2,3,4,5,6,7,8,9,10,'Q','J','K','A']):
        self.cartas=cartas     
espadas = naipe()
copas = naipe()
ouros = naipe()
paus = naipe()
naipes = ['espadas','copas','ouros','paus']

class hand (object):
    def __init__ (self,cards = []):
        self.cards = cards   
dealer = hand()
player = hand()

def initial_draw_of_cards_player():
    global player_draws, player_total_value, player, total_money, bet, total_bet
    player_draws = 0
    player_total_value = 0
    player.cards = []
    
    while player_draws < 2:
        chosen_naipe = random.choice(naipes)
    
        if chosen_naipe == 'espadas':
            drawn_card = random.choice(espadas.cartas)
            espadas.cartas.pop(espadas.cartas.index(drawn_card))
            player.cards.append(drawn_card)
            print('Você tirou um ' + str(drawn_card) + ' de espadas!')
            
        elif chosen_naipe == 'copas':
            drawn_card = random.choice(copas.cartas)
            copas.cartas.pop(copas.cartas.index(drawn_card))
            player.cards.append(drawn_card)
            print('Você tirou um ' + str(drawn_card) + ' de copas!')
            
        elif chosen_naipe == 'ouros':
            drawn_card = random.choice(ouros.cartas)
            ouros.cartas.pop(ouros.cartas.index(drawn_card))
            player.cards.append(drawn_card)
            print('Você tirou um ' + str(drawn_card) + ' de ouros!')
            
        elif chosen_naipe == 'paus':
            drawn_card = random.choice(paus.cartas)
            paus.cartas.pop(paus.cartas.index(drawn_card))
            player.cards.append(drawn_card)
            print('Você tirou um ' + str(drawn_card) + ' de paus!')
        
        if drawn_card == 'Q' or drawn_card == 'J' or drawn_card == 'K':
            card_value = 10
        elif drawn_card == 'A':
            card_value = 11
        else:
            card_value = drawn_card
            
        player_total_value += card_value
        player_draws += 1
    
    if player_total_value in range (9,12):
        print("Sua mão está em " + str(player_total_value) + "\n")
        
        double_down = input("Você pode fazer um double-down! Gostaria de dobrar sua aposta? (S ou N)\t")
        if double_down.upper() == 'S':
            total_money += float(bet)
            total_bet += float(bet)
            bet = 2 * float(bet)
            print("Sua aposta passou para R$ " + str(bet))
            draw_of_cards_player()
            
    elif player_total_value < 21:
        print("Sua mão está em " + str(player_total_value) + "\n")
        draw_of_cards_player()
        
    elif player_total_value == 21:
        print("\nBLACKJACK! Você venceu e ganha 1,5x o valor da aposta!")
        total_money += 1.5 * float(bet)
        
        print("Parabéns " + str(player_name) + "! Você agora tem R$ " + str(total_money - total_bet))

def initial_draw_of_cards_dealer():
    global dealer_total_value, dealer
    dealer.cards = []
    dealer_total_value = 0
    chosen_naipe = random.choice(naipes)
    
    if chosen_naipe == 'espadas':
        drawn_card = random.choice(espadas.cartas)
        espadas.cartas.pop(espadas.cartas.index(drawn_card))
        dealer.cards.append(drawn_card)
        print('O dealer tirou um ' + str(drawn_card) + ' de espadas!\n')
        
    elif chosen_naipe == 'copas':
        drawn_card = random.choice(copas.cartas)
        copas.cartas.pop(copas.cartas.index(drawn_card))
        dealer.cards.append(drawn_card)
        print('O dealer tirou um ' + str(drawn_card) + ' de copas!\n')
        
    elif chosen_naipe == 'ouros':
        drawn_card = random.choice(ouros.cartas)
        ouros.cartas.pop(ouros.cartas.index(drawn_card))
        dealer.cards.append(drawn_card)
        print('O dealer tirou um ' + str(drawn_card) + ' de ouros!\n')
        
    elif chosen_naipe == 'paus':
        drawn_card = random.choice(paus.cartas)
        paus.cartas.pop(paus.cartas.index(drawn_card))
        dealer.cards.append(drawn_card)
        print('O dealer tirou um ' + str(drawn_card) + ' de paus!\n')
        
    if drawn_card == 'Q' or drawn_card == 'J' or drawn_card == 'K':
        card_value = 10
    elif drawn_card == 'A':
        card_value = 11
    else:
        card_value = drawn_card
        
    dealer_total_value += card_value

def draw_of_cards_player():
    while True:
        continue_playing = input("Deseja continuar jogando? (S ou N)\t")
        
        if continue_playing.upper() == "N":
            print("\nVez do dealer:")
            draw_of_cards_dealer()
            break
            
        elif continue_playing.upper() == "S":
            global player_total_value, player, total_money, bet, total_bet
            
            chosen_naipe = random.choice(naipes)
    
            if chosen_naipe == 'espadas':
                drawn_card = random.choice(espadas.cartas)
                espadas.cartas.pop(espadas.cartas.index(drawn_card))
                player.cards.append(drawn_card)
                print('Você tirou um ' + str(drawn_card) + ' de espadas!')
                
            elif chosen_naipe == 'copas':
                drawn_card = random.choice(copas.cartas)
                copas.cartas.pop(copas.cartas.index(drawn_card))
                player.cards.append(drawn_card)
                print('Você tirou um ' + str(drawn_card) + ' de copas!')
                
            elif chosen_naipe == 'ouros':
                drawn_card = random.choice(ouros.cartas)
                ouros.cartas.pop(ouros.cartas.index(drawn_card))
                player.cards.append(drawn_card)
                print('Você tirou um ' + str(drawn_card) + ' de ouros!')
                
            elif chosen_naipe == 'paus':
                drawn_card = random.choice(paus.cartas)
                paus.cartas.pop(paus.cartas.index(drawn_card))
                player.cards.append(drawn_card)
                print('Você tirou um ' + str(drawn_card) + ' de paus!')
        
            if drawn_card == 'Q' or drawn_card == 'J' or drawn_card == 'K':
                card_value = 10
            elif drawn_card == 'A':
                card_value = 11
            else:
                card_value = drawn_card
                
            player_total_value += card_value
            
            if player_total_value > 21 and player.cards.count('A') == 0:
                print("\nVocê estourou! Sua mão teve valor de " + str(player_total_value))
                print("A casa venceu!")
                total_money -= float(bet)
                
                print("Não foi dessa vez " + str(player_name) + "! Você agora tem um saldo de R$ " + str(total_money - total_bet))
                break
                
            elif player_total_value > 21 and player.cards.count('A') > 0:
                player.cards.remove('A')
                player_total_value -= 10
                print("Sua mão está em " + str(player_total_value) + "\n")
                continue
                
            elif player_total_value == 21:
                print("\nBLACKJACK! Você venceu e ganhou 1,5x o valor da aposta!")
                total_money += 1.5 * float(bet)
                
                print("Parabéns " + str(player_name) + "! Você agora tem R$ " + str(total_money - total_bet))
                break
                
            else:
                print("Sua mão está em " + str(player_total_value) + "\n")
                continue
        else:
            print("\nPor favor, insira uma resposta válida!")
            continue

def draw_of_cards_dealer():
    global player_total_value, dealer_total_value, dealer, player_name, total_money, bet, total_bet
    while True:
        if dealer_total_value > player_total_value and dealer_total_value >= 17:
            print("\nO dealer venceu!")
            print("Mão do dealer: " + str(dealer_total_value))
            print("Mão do " + str(player_name) + ": " + str(player_total_value))
            total_money -= float(bet)
            
            print("Não foi dessa vez " + str(player_name) + "! Você agora tem um saldo de R$ " + str(total_money - total_bet))
            break
            
        else:
            chosen_naipe = random.choice(naipes)
    
            if chosen_naipe == 'espadas':
                drawn_card = random.choice(espadas.cartas)
                espadas.cartas.pop(espadas.cartas.index(drawn_card))
                dealer.cards.append(drawn_card)
                print('\nO dealer tirou um ' + str(drawn_card) + ' de espadas!')
                
            elif chosen_naipe == 'copas':
                drawn_card = random.choice(copas.cartas)
                copas.cartas.pop(copas.cartas.index(drawn_card))
                dealer.cards.append(drawn_card)
                print('\nO dealer tirou um ' + str(drawn_card) + ' de copas!')
                
            elif chosen_naipe == 'ouros':
                drawn_card = random.choice(ouros.cartas)
                ouros.cartas.pop(ouros.cartas.index(drawn_card))
                dealer.cards.append(drawn_card)
                print('\nO dealer tirou um ' + str(drawn_card) + ' de ouros!')
                
            elif chosen_naipe == 'paus':
                drawn_card = random.choice(paus.cartas)
                paus.cartas.pop(paus.cartas.index(drawn_card))
                dealer.cards.append(drawn_card)
                print('\nO dealer tirou um ' + str(drawn_card) + ' de paus!')
        
            if drawn_card == 'Q' or drawn_card == 'J' or drawn_card == 'K':
                card_value = 10
            elif drawn_card == 'A':
                card_value = 11
            else:
                card_value = drawn_card
                
            dealer_total_value += card_value
            
            if dealer_total_value > 21 and dealer.cards.count('A') == 0:
                print("\nO dealer estourou! Sua mão teve valor de " + str(dealer_total_value))
                print("O jogador venceu!")
                total_money += float(bet)
            
                print("Parabéns " + str(player_name) + "! Você agora tem um saldo de R$ " + str(total_money - total_bet))
                break
                
            elif dealer_total_value > 21 and dealer.cards.count('A') > 0:
                dealer.cards.remove('A')
                dealer_total_value -= 10
                print("A mão do dealer está em " + str(dealer_total_value))
                continue
                
            elif dealer_total_value == 21:
                print("\nBLACKJACK! O dealer venceu!")
                total_money -= float(bet)
                print("Não foi dessa vez " + str(player_name) + "! Você agora tem um saldo de R$ " + str(total_money - total_bet))
                break
                
            else:
                print("A mão do dealer está em " + str(dealer_total_value))
                continue

def play_game():
    
    espadas.cartas = [2,3,4,5,6,7,8,9,10,'Q','J','K','A']
    copas.cartas = [2,3,4,5,6,7,8,9,10,'Q','J','K','A']
    ouros.cartas = [2,3,4,5,6,7,8,9,10,'Q','J','K','A']
    paus.cartas = [2,3,4,5,6,7,8,9,10,'Q','J','K','A']
    
    global player_name, bet, total_money, total_bet
    total_money = 0
    total_bet = 0
    
    print("\nOlá! Bem-vindo(a) ao cassino do Vini! Vamos jogar um BlackJack?")
    sleep(0.1)
    player_name = input("Primeiro, qual o seu nome?\n").capitalize()
    print("\nVai ser um prazer jogar com você, " + str(player_name)+ "!")
    
    while True:
        while True:
            try:
                bet = input("\n" + str(player_name) + ", qual será sua aposta em R$ para esse jogo?\t")
                bet_check = int(bet)
            except:
                print("Insira um número válido!")
                continue
            else:
                break
        total_money += float(bet)
        total_bet += float(bet)
        print("Uuuh, feeling lucky huh? Vamos ver como você vai se virar!\n")
        sleep(0.5)
        print("Vamos começar o jogo!")
        sleep(0.5)
        initial_draw_of_cards_dealer()
        sleep(1)
        initial_draw_of_cards_player()
        
        continue_betting = input("\nGostaria de continuar jogando " + str(player_name) + "? (S ou N)\t")
        if continue_betting.upper() == 'S':
            clear_output()
            
            if (total_money - total_bet) >= 0:
                print("Seu lucro (valor total - valor apostado) até agora é de R$ " + str(total_money - total_bet))
            else:
                print("Suas perdas até agora somam -R$ " + str(-(total_money-total_bet)))
            continue
            
        elif (total_money-total_bet) >= 0:
            print("\nUau, você realmente estava se sentindo sortudo em?")
            print("Você teve um lucro de R$ " + str(total_money - total_bet) + "!")
            print("Foi um prazer ter você aqui " + str(player_name) + "! Até breve!")
            break
            
        else:
            print("\nNão foi dessa vez em? Você perdeu R$ " + str(total_money - total_bet))
            print("Foi um prazer tomar seu dinheiro " + str(player_name) + "! Até breve!")
            break


play_game()