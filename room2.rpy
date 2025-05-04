define lu = "Lula Pirusco"
default cozinha_mensagem = False
default contador_agridoce = 0  # Contador para ordenhar água-viva
default molho_agridoce_desbloqueado = False  # Controla se o molho agridoce está desbloqueado
define audio.gozada = "gozada.mp3"


# Imagens para a animação de "ordenha" da água-viva
image ordenha_frame1 = "images/ordenha1.png"  # Frame 1: Inicial (pênis fora)
image ordenha_frame2 = "images/ordenha2.png"  # Frame 2: Intermediário (pênis entrando)
image ordenha_frame3 = "images/ordenha3.png"  # Frame 3: Final (pênis mais fundo)

# Imagens para a animação de "clímax"
image gozada_frame1 = "images/gozada1.png"  # Frame 1: Inicial do clímax
image gozada_frame2 = "images/gozada2.png"  # Frame 2: Meio do clímax
image gozada_frame3 = "images/gozada3.png"  # Frame 3: Final do clímax

# Animação de ordenha em ATL
image ordenha_sequencia:
    "ordenha_frame1"
    pause 0.05
    "ordenha_frame2"
    pause 0.3
    "ordenha_frame3" 
    pause 0.3
    "ordenha_frame2"
    pause 0.3
    "ordenha_frame1"
    pause 0.05

# Som de gozada

# Animação contínua que roda em loop
image ordenha_anim:
    "ordenha_frame1"
    pause 0.2
    "ordenha_frame2" 
    pause 0.2
    "ordenha_frame3"
    pause 0.2
    "ordenha_frame2"
    pause 0.2
    repeat

# Imagens para a animação de "clímax"
image gozada_anim:
    "gozada_frame1"
    pause 0.25
    "gozada_frame2"
    pause 0.25
    "gozada_frame3"
    pause 0.5

# Caso as imagens não existam, criamos placeholders
init python:
    if not renpy.loadable("images/ordenha1.png"):
        renpy.image("ordenha_frame1", Solid("#FF80BF", xsize=300, ysize=300))
    if not renpy.loadable("images/ordenha2.png"):
        renpy.image("ordenha_frame2", Solid("#FFA0CF", xsize=320, ysize=320))
    if not renpy.loadable("images/ordenha3.png"):
        renpy.image("ordenha_frame3", Solid("#FFB0DF", xsize=340, ysize=340))

label room2:
  scene kk
  "Você chega no Siri Cracudo" 

  define k = "Seu siririca"
  
  show krab a at center with hpunch:
     zoom 0.75

  k "BOB ESPERMA!!!" 

  k "Posso saber onde vc estava?"
  menu:
      "Não sou o Bob Esperma. O verdadeiro ta amarrado em casa.":
       $escolha = "truth"
       jump siricas


      "Batendo punheta":
       $escolha = "punheta"
       jump siricas


      "Comendo a piranha da sua mãe":
       $escolha = "comituamae"
       jump siricas

      "Comendo a piranha da sua irmã":
       $escolha = "comituamae"
       jump siricas


      "Meu caracol passou mal Seu Siririca" :
       $escolha = "gary"
       jump siricas

label siricas:
  hide krab a
  if escolha == "punheta":  
     show krab happy:
        zoom 0.6 xpos 1000 ypos 400

     k "Tudo bem rapaz sem problemas"

     k "Já tive sua idade um dia, uma punhetinha aumenta na produtividade"

     k "Mas me avisa na próxima vez para evitar problemas ok?! Não seja igual o Rola Molusco que passa horas no banheiro..."

     hide patrick2
  elif escolha == "comituamae":
         show kradeath

         k "VAI TOMA NO CUUUU BOB ESPORRAAAA!!!"

         "Game over"

         return
  elif escolha == "truth":
       show krab4:
        zoom 0.6 xpos 1000 ypos 400 

       k "Puta merda..."
  elif escolha == "gary":
       show krab4:
        zoom 0.5 xpos 1000 ypos 520 

       k "Puxa rapaz que pena..."

       show krab4:
        zoom 0.5 xpos 1000 ypos 520  

       k "Que tal fritar uns hamburgueres de siri para se sentir melhor?"

label cozinha:
  # Esconder a interface xerequinha durante a cozinha
  hide screen xerequinha
  
  scene kitchen 

  show batavo1 at Transform(xzoom=-1):
    zoom 1.5 xpos 700 ypos 30
  
  
  while True:
      if not cozinha_mensagem:
         "Aqui é a cozinha do Siri Cracudo"  

         $ cozinha_mensagem = True 

      menu:
            "Adcionar um molho secreto":
                $ escolha = "gozo"
                jump chapa

            "Cozinhar com molho agridoce de água-viva" if 21 in inventario:
                $ escolha = "agridoce"
                jump ordenhar_aguaviva

            "Cozinhar com geleia de água-viva" if 23 in inventario:
                $ escolha = "geleia"
                jump chapa_geleia
                
            "Cozinhar com molho especial e abacaxi" if 19 in inventario:
                $ escolha = "abacaxi"
                jump chapa_abacaxi

            "Cozinhar um hamburguer de siri normal":
                $ escolha = "burguer"
                jump chapa

# Label para cozinhar com molho especial e abacaxi
label chapa_abacaxi:
    play audio "grelha.mp3" fadein 2.0

    show chapa

    "Você adiciona o molho secreto e fatias de abacaxi fresco aos hambúrgueres."
    "O aroma agridoce é simplesmente irresistível!"
    
    # Remover um abacaxi do inventário
    $ inventario.remove(19)
    
    pause(5)
    
    hide chapa
    
    "Seis horas depois" 
    $ hora_do_dia += 6
    
    pause(2)
    
    show kk night
    
    show krab happy:
        zoom 0.6 xpos 1000 ypos 400
    
    k "CACILDA, Bob Esperma!! Esses hambúrgueres estão DIVINOS!"
    k "O abacaxi deu um toque especial... tão docinho... TÃO LUCRATIVO!"
    k "Os clientes estão pagando o dobro só para comer mais desses!"
    
    $ money += 40
    "Você recebeu 40 dólares pelo hambúrguer com abacaxi!"
    
    stop music fadeout 3.0 
    $ hora_do_dia = 20
    
    # Mostrar a tela xerequinha antes de sair
    show screen xerequinha
    
    # Sair usando a label existente
    jump quanaite

# Label para ordenhar a água-viva para fazer o molho agridoce
label ordenhar_aguaviva:
    scene kitchen
    
    "Você pega uma água-viva do seu bolso e se prepara para extrair seu 'molho agridoce'."
    "Clique 20 vezes na água-viva para extrair o molho."
    
    $ contador_agridoce = 0
    
    # Tela para clicar na água-viva
    screen ordenhar_screen():
        modal True
        
        # Frame principal com a água-viva 
        # - Isso substituirá a cena quando a animação não estiver rodando
        add "ordenha_frame1" xalign 0.5 yalign 0.5
        
        # Mostrar a animação na mesma posição quando ativada
        if renpy.get_screen("ordenha_animacao"):
            add "ordenha_sequencia" xalign 0.5 yalign 0.5
        
        # Contador no topo da tela
        frame:
            xalign 0.5
            yalign 0.1
            padding (20, 10)
            text "Ordenhar: [contador_agridoce]/20" size 30 xalign 0.5
        
        # Botão "Meter" isolado no canto direito
        frame:
            xalign 0.9
            yalign 0.5
            padding (10, 10)
            
            textbutton "Meter":
                action [Play("sound", "gozada.mp3"),
                        Show("ordenha_animacao"),
                        SetVariable("contador_agridoce", contador_agridoce + 1),
                        If(contador_agridoce + 1 >= 20, 
                           Hide("ordenhar_screen"), 
                           NullAction())]
                text_size 30
                text_color "#FFFFFF"
                text_hover_color "#FF3366"
                text_outlines [(2, "#990000", 0, 0)]
                background "#DD0000"
                hover_background "#FF0000"
    
    # Tela para temporizador da animação
    screen ordenha_animacao():
        timer 1.0 action Hide("ordenha_animacao")
    
    # Mostrar a tela de ordenha
    show screen ordenhar_screen
    
    # Pausar até que o jogador complete os 20 cliques
    $ renpy.pause()
    
    # Tela para o clímax após completar 20 cliques
    "Você está prestes a extrair o molho!"
    
    menu:
        "Gozar":
            # Animação de clímax
            play sound "gozada.mp3" volume 1.0
            
            show gozada_frame1
            pause 0.3
            
            hide gozada_frame1
            show gozada_frame2
            pause 0.3
            
            hide gozada_frame2
            show gozada_frame3
            pause 0.4
            
            hide gozada_frame3
            
            # Efeito de tremedeira para intensificar o momento
            with hpunch
            with vpunch
            
            "POOOOORRA!!!"
            
            "Você conseguiu extrair o molho agridoce da água-viva!"
            "Agora vamos cozinhar com ele."
    
    # Remover uma água-viva do inventário
    $ inventario.remove(21)
    
    $ escolha = "agridoce"
    $ molho_agridoce_desbloqueado = True
    jump chapa

# Label para cozinhar com geleia de água-viva
label chapa_geleia:
    play audio "grelha.mp3" fadein 2.0

    show chapa

    "Você abre o pote de geleia de água-viva e espalha sobre os hambúrgueres."
    "O aroma doce e picante preenche a cozinha."
    
    # Remover um pote de geleia do inventário
    $ inventario.remove(23)
    
    pause(5)
    
    hide chapa
    
    "Algumas horas depois" 
    $ hora_do_dia += 6
    
    pause(2)
    
    show kk night
    
    show krab happy:
        zoom 0.6 xpos 1000 ypos 400
    
    k "UAU, Bob Esperma! Esses hambúrgueres com geleia de água-viva foram um sucesso absoluto!"
    k "Os clientes estão loucos por eles! DINHEIRO, DINHEIRO, DINHEIRO!"
    
    $ money += 30
    "Você recebeu 30 dólares pelo excelente serviço com a geleia de água-viva!"
    
    stop music fadeout 3.0 
    $ hora_do_dia = 20
    
    # Mostrar a tela xerequinha antes de sair
    show screen xerequinha
    
    # Sair usando a label existente
    jump quanaite

label chapa:
  
  play audio "grelha.mp3" fadein 2.0

  show chapa

  if escolha == "burguer":  
     pause(5)

     hide chapa

     "Algumas horas depois" 
     $ hora_do_dia += 6 

     pause(2)

     show kk night

     show krab happy:
      zoom 0.6 xpos 1000 ypos 400

     k "Vá pra casa rapaz, e ve se capricha mais amanhã os clientes estão reclamando que o gosto está uma merda."
     
     k "Não que eu me importe com isso se for uma vez ou outra,mas se manter esse ritmo vou perder DINHEI- digo meus amados clientes."
     
     # Mostrar a tela xerequinha antes de sair
     show screen xerequinha
     
     # Usar a label existente
     jump quanaite

  elif escolha == "gozo":
         show molho

         pause(2)

         show molho2

         pause(2)

         show molho3
         
         "Você adcinou o MOLHO SECRETO em todos os hamburgueres de siri"

         pause(2)

         "Algumas horas depois"
         $ hora_do_dia += 6  

         stop audio fadeout 2.0

         show kk night

         show krab happy:
          zoom 0.6 xpos 1000 ypos 400

         k "Vá pra casa rapaz, e continue com essa receita nova os clientes estão adorando!!"

         # Gerar uma recompensa aleatória entre 8 e 15 para o molho secreto
         $ recompensa = renpy.random.randint(8, 15)
         $ money += recompensa
         "Você recebeu [recompensa] dólares pelo ótimo serviço!"
         
         stop music fadeout 3.0 
         $ hora_do_dia = 20
         
         # Mostrar a tela xerequinha antes de sair
         show screen xerequinha
         
         # Sair usando a label existente
         jump quanaite

  elif escolha == "agridoce":
         show gozojam1

         pause(2)

         show gozojam2

         pause(2)

         show gozojam3
         
         "Você adicionou o MOLHO AGRIDOCE DE ÁGUA-VIVA em todos os hambúrgueres de siri"

         pause(2)

         "Algumas horas depois"
         $ hora_do_dia += 6  

         stop audio fadeout 2.0

         show kk night

         show krab happy:
          zoom 0.6 xpos 1000 ypos 400

         k "Caramba, Bob Esperma! Esse molho agridoce de água-viva é fantástico!"
         k "Os clientes estão pedindo mais! Continue assim e vou ficar rico... digo, vamos ficar ricos juntos!"

         # Gerar uma recompensa aleatória entre 8 e 25 para o molho agridoce
         $ recompensa = renpy.random.randint(8, 25)
         $ money += recompensa
         "Você recebeu [recompensa] dólares pelo serviço com molho agridoce!"
         
         stop music fadeout 3.0 
         $ hora_do_dia = 20
         
         # Mostrar a tela xerequinha antes de sair
         show screen xerequinha
         
         # Sair usando a label existente
         jump quanaite
  
  if nugget: 
    k "Vejo que alguem comeu seu rabo rapaz..."

  menu: 
     "Leave":
       # Mostrar a tela xerequinha antes de sair
       show screen xerequinha
       call screen mapScreen


label caixakk:
 scene caixa kk lula

 lu" Bom, acho que como eu sou o unico ser com QI positivo nesta espenunca de cidade, eu vou ter que perguntar"
 
 show lula com vc 

 lu" Quem é vc e onde esta aquele boiolinha quadrado?"

 menu:
            #"Se masturbar":
               # $ escolha = "quarto"
               # jump opcoes

            "Não sei do que está falando, eu sou ele!":
                $ escolha = "mentiu"
                jump luleta

            "Ignorar (fodase é o Lula Molusco)":
                $ escolha = "mentiu"
                jump luleta

label luleta:              
 if escolha == "mentiu":  
     pause(3)

   
   
     
     show caixa kk lula
     lu"Ta que se foda eu so venho aqui pra fazer banheirao mesmo"
     jump cozinha



label lobbykk: 

 play music "siricracudo.mp3" fadein 2.0

 screen lobbykk: 

    add "lobbykrab.png"  
    on "show" action Play("music", "siricracudo.mp3", fadein=2.0)
     


    imagebutton:
             xpos 920
             ypos 230
             idle "barco pirusco idle.png"
             hover "barco pirusco.png" 
             action Jump("caixakk")  

    imagebutton:
              xpos 1170
              ypos 200
              idle "porta kk idle.png"
              hover "porta kk hover.png" 
              action Jump("cozinha")     

    #imagebutton:
         # xpos 1490
         # ypos 200
          #idle "porta kk idle.png"
         # hover "porta kk hover.png" 
         # action Jump("banheirao")   

    imagebutton:
          xpos 263
          ypos 200
          idle "porta kk idle.png"
          hover "porta kk hover.png" 
          action Jump("sala_siririca")           

label banheirao: 
 scene banheirao 

 k"Meu piru ta mole hoje porra.."

 menu: 
    "Voltar":

       call screen lobbykk with fade
 
default visitou_sala_siririca = False

label sala_siririca:
    scene tutinha
    play music "siricracudo.mp3" fadein 2.0
    
    if not visitou_sala_siririca:
        "Você entra na sala do Seu Siririca"
        
        show krab a at center with fade:
            zoom 0.75
        
        k "O que você quer agora rapaz? Tá vendo que estou OCUPADO CONTANDO MEU DINHEI... digo, fazendo a contabilidade do restaurante!"
        $ visitou_sala_siririca = True
    else:
        show krab a at center with fade:
            zoom 0.75

    jump menu_principal_siririca