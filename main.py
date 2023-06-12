from pyautogui import *
from keyboard import *

# Coordenadas no mapa
cabana = (840, 311)
ninja = (726, 430) 
superM = (824, 424) 
domador_1 = (676, 387)
domador_2 = (726, 667)
etiene = (927, 447)
continuar = (941, 912)
home = (735, 864)

tempo_espera = 0.1
duracao = 0.3
while 1:
    click(827, 931) # Play
    sleep(0.2)
    click(278, 431) # Voltar (pagina de mapas)
    sleep(tempo_espera)
    click(1373, 264) # Castelo Sombrio
    sleep(tempo_espera)
    click(629, 428) # Facil
    sleep(tempo_espera)
    click(1287, 458) # Esvaziamento
    sleep(6)
    click(956, 765) # OK
    sleep(1)

    # Posicionamento
    send('k')
    click(cabana, duration=0.5)
    send('d')
    click(ninja, duration=duracao) 
    send('s')
    click(superM, duration=duracao) 
    send('i')
    click(domador_1, duration=duracao)
    send('u')
    click(etiene, duration=duracao)
    send('i')
    click(domador_2, duration=0.5)

    # Compras
    click(cabana)
    sleep(tempo_espera)
    send(';')
    sleep(tempo_espera)
    send(';')

    click(superM)
    for _ in range(3):
        send('.')
        sleep(tempo_espera)
        send(',')
        sleep(tempo_espera)

    click(ninja)
    for _ in range(4):
        send(',')
        sleep(tempo_espera)
        send(';')
        sleep(tempo_espera)

    click(cabana)
    send('backspace')
    sleep(tempo_espera)

    click(domador_1)
    sleep(tempo_espera)
    send('.')
    sleep(tempo_espera)
    send(';')
    sleep(tempo_espera)

    click(etiene)
    sleep(tempo_espera)
    send(',')
    sleep(tempo_espera)

    click(domador_2)
    sleep(tempo_espera)
    send('.')
    sleep(tempo_espera)
    send(';')
    
    # Play
    send('space')
    sleep(tempo_espera)
    send('space')

    # Level UP
    for _ in range(62):
        sleep(5)
        level_up = locateOnScreen('imagens/level_up.png', region=(942, 391, 32, 25))
        if level_up:
            click(interval=1, clicks=2)
            
    # Vitoria
    while 1:
        sleep(1)
        vitoria = locateOnScreen('imagens/vitoria.png', region=(529, 163, 38, 29))
        if vitoria:
            print(vitoria)
            print('encontrado')
            break
        else:
            print('nao encontrado')

    # Reestart
    click(continuar)
    sleep(1)
    click(home)
    sleep(2)

    # Evento de aniversario
    if locateOnScreen('imagens/bolo.png', region=(126, 21, 41, 43)):
        click(locateCenterOnScreen('imagens/voltar.png'))
    
