# Define os sons que você quer tocar durante a digitação
define audio.typing = "bubbles.mp3"  # Som para diálogos de personagens
define audio.narration = "generic.mp3"  # Som para narração/texto sem personagem

# Código para controlar o som de digitação
init python:
    # Variável global para controlar se o som está tocando
    typing_sound_playing = False
    
    # Função para iniciar e parar o som durante a digitação
    def typing_sound_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            # Inicia o som quando o texto começa a ser mostrado
            renpy.music.play(audio.typing, channel="sound", loop=True)
            typing_sound_playing = True
        
        elif event == "slow_done" or event == "end":
            # Para o som quando toda a digitação termina
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False
    
    # Função para callback de narração (textos sem personagem)
    def narration_sound_callback(event, **kwargs):
        global typing_sound_playing
        
        if event == "show":
            # Inicia o som quando o texto começa a ser mostrado
            renpy.music.play(audio.narration, channel="sound", loop=True)
            typing_sound_playing = True
        
        elif event == "slow_done" or event == "end":
            # Para o som quando toda a digitação termina
            if typing_sound_playing:
                renpy.music.stop(channel="sound")
                typing_sound_playing = False

# Definindo o narrador com o callback de narração
define narrator = Character(None, callback=narration_sound_callback)

# Configure o callback para ser chamado nos eventos de texto de personagens
init python:
    config.all_character_callbacks.append(typing_sound_callback)

# Resto do código original...
image fundo_dia = "fundo_dia.jpg"
image fundo_noite = "fundo_noite.jpg"


label mostrar_fundo():
    if hora_do_dia >= 6 and hora_do_dia < 18:
        show fundo_dia
    else:
        show fundo_noite
    return 

label inicio:
    call mostrar_fundo
    "Está amanhecendo."  # Vai usar generic.mp3
    
    "Você quer esperar ou continuar?"  # Vai usar generic.mp3
    
    menu:
        "Esperar":
            $ hora_do_dia += 6  # Passa 6 horas
            call mostrar_fundo
            "Agora são [hora_do_dia] horas."  # Vai usar generic.mp3
        "Continuar":
            "Você seguiu em frente."  # Vai usar generic.mp3

    return

label avancar_tempo():
    $ hora_do_dia += 6
    if hora_do_dia >= 24:
        $ hora_do_dia = 0  # Volta para meia-noite
    return

#label start:
    "Bem-vindo ao sistema de dia e noite!"
    
    # Mostra o fundo atual
    #call mostrar_fundo
    
    # Loop principal do jogo
    #while True:
       # menu:
            #"Esperar (passar 6 horas)":
                #call avancar_tempo
               # call mostrar_fundo
               # "Agora são [hora_do_dia] horas."
           # "Sair do jogo":
               # return





label start:
    
    #Toca a música "bobesponja.ogg"
    play music "bobesponja.mp3" fadein 2.0
default contrap1 = False
default nugget = False 
default mainmap = False
default money = 0
default macaca = False
define p = Character("Pautrick Estrela", callback=typing_sound_callback)
define bs = Character("Bob Esporra", callback=typing_sound_callback)
$ money = 0 
default sala_mensagem_exibida = False
default hora_do_dia = 8  # Começa às 6 da manhã
define som_opcao = "open.wav"
default mapa_disponivel = False



# Sobrescreve o comportamento padrão de menu para tocar somplay music :"bobesponja.ogg"

label cutscene:
    # Começar com música de suspense
    play music "susmusic.mp3" fadein 2.0
    play audio "bubaus.mp3" fadein 1.0
    
    scene ingameburuba with fade

    "Uh... o que?"
    show cutscene2 with fade
    
    "O que é aquilo? Um abacaxi??!!"
    
    show cuts1

    "Bob Esporra" "La lala lala"  # Vai usar bubbles.mp3 porque tem nome de personagem

    # Quando aparece o franky, tocar o grito
    play audio "classicdrama.mp3"
    play audio "gritobob.mp3" volume 0.18
    show frankys with hpunch

    "Bob Esporra" "AHHHHHHHHHHH"  # Vai usar bubbles.mp3 porque tem nome de personagem
    
    # Fade para tela preta após a última imagem
    scene black with fade
    
    # Tocar o som de rasgasso na tela preta
    play audio "rasgazzo.mp3"
    # Aguardar um pouco para o som tocar
    pause 5.0

    play audio "gritobob.mp3" volume 0.18
    "Bob esporra" "NÃO! PARE! MINHAS ROUPAS! MEU ROSTO! O QUE ESTÁ FAZENDO!"
    play audio "franklaugh.mp3"
    "You" "CALA BOCA PORRA!"

    scene black with fade
    play audio "fewmom.mp3"

    show fewmom

    pause 3.0
    
    show screen xerequinha 
    stop audio
    stop sound
    stop music
    stop audio

    jump room4

if mainmap = True:
  call screen mapScreen
   
 

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   #scene areia
    #Código para exibir texto na tela
    #text "{size=40}{color=#008000}[money]/[oppois_hit]{/color}{/size} Money" xpos 1100 ypos 50

    #image areia:
    # "areia.png"
    # zoom 1.5 
     
    #show areia
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #image batavo:
    # "batavo.png"
    # zoom 1.35 

    #image hard:
     #"hard.png"
    # zoom 1.35 
     
   # show batavo at left
    

    # These display lines of dialogue.

  #  "Bob Estrupo" "Oi bem?" 
   # "Bob Estrupro" "Caguei nas calças"
  #  with fade

    # This ends the game.
    
  #  "Dou you like niggers"
  #  menu: 

   #  "Yes": 

   #       jump choices1_a

   #  "Fuck you SpornBob":

   #       jump choices1_b

   # label choices1_a:
   #           "Good"

   # label choices1_b:
   #          "Uuuh"  with fade

   # "Dou you like raping for fun?"
   # menu: 

   #  "Yes": 

   #       jump choices2_a

    # "Fuck you SpornBob":

   #       jump choices2_b

  #  label choices2_a:
  #            "Good"
              
  #            show hard at left
              
   # label choices2_b:
   #          "Uuuh"

# (Continuação do código anterior)

# Dia 4 (Continuação)

    
return