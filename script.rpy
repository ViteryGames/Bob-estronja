
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
    "Está amanhecendo."
    
    "Você quer esperar ou continuar?"
    
    menu:
        "Esperar":
            $ hora_do_dia += 6  # Passa 6 horas
            call mostrar_fundo
            "Agora são [hora_do_dia] horas."
        "Continuar":
            "Você seguiu em frente."

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
    play music "bobespon.mp3" fadein 2.0
default contrap1 = False
default nugget = False 
default mainmap = False
default money = 0
default macaca = False
define p = "Pautrick Estrela"
define bs = "Bob Esporra"
$ money = 0 
default sala_mensagem_exibida = False
default hora_do_dia = 14  # Começa às 6 da manhã
define som_opcao = "open.wav"




# Sobrescreve o comportamento padrão de menu para tocar somplay music :"bobesponja.ogg"

label cutscene:
  scene cuts1

  "Bob Esponja" "Turururu"

  show cuts2

  "Bob Esponja" "AHHHHHHHHHHH"
  
  show screen xerequinha 


 
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


