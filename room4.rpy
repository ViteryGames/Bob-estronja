default vezes_investigou = 0
default saida = 0
# Variável para controlar se a TV já foi quebrada
default tv_quebrada = False

# Imagens para a sequência da TV
image tv_reporter1 = "images/tv_reporter1.png"  # Frame 1 do peixe âncora
image tv_reporter2 = "images/tv_reporter2.png"  # Frame 2 do peixe âncora (boca aberta)
image tv_reporter3 = "images/tv_reporter3.png"  # Frame 3 do peixe âncora
image tv_batavo_soco = "images/tv_batavo_soco.png"  # Batavo dando um soco na TV
image tv_quebrada = "images/tv_quebrada.png"  # TV quebrada

# Animação do peixe âncora
image tv_reporter_anim:
    "tv_reporter1"
    pause 0.3
    "tv_reporter2"
    pause 0.3
    "tv_reporter3"
    pause 0.3
    repeat

label room4:
  # Desativa o mapa quando o jogador está dentro da casa
  $ mapa_disponivel = False
  
  # Verificar se é após 20h para redirecionar para quanaite
  if hora_do_dia >= 20:
    jump quanaite
  
  # Se não for noite, continua normalmente  
  scene quartobob

  show batavo1 at Transform(xzoom=-1):
    zoom 1.3 xpos 1000 ypos 200 

  "O que eu devo fazer agora?"

init python:
    # Armazena a referência ao menu original
    original_menu = renpy.display_menu

    # Função customizada para tocar som ao escolher
    def custom_menu(choices, *args, **kwargs):
        # Toca o som quando o jogador faz uma escolha
        renpy.play(som_opcao, channel="sound")
        # Chama o menu original
        return original_menu(choices, *args, **kwargs)

    # Substitui o menu padrão pelo customizado
    renpy.display_menu = custom_menu   

label chegada_em_casa:
    # Verificar se é após 20h para redirecionar para quanaite
    if hora_do_dia >= 20:
        jump quanaite
        
    # Se não for noite, continua normalmente
    # Exibe o texto "Você chegou em casa" apenas uma vez
    # Inicia um loop de opções que sempre retorna ao menu inicial
    while True:
        menu:
            "Ir para a sala":
                play sound som_opcao
                $ escolha = "cozinha"
                jump salabob

            "checar bob esponja":
                $ escolha = "bob"
                jump opcoes

            "Investigar":
                $ escolha = "inv"
                jump opcoes

label opcoes:
    # Aqui você pode personalizar o que acontece dependendo da escolha
    if escolha == "cozinha":
        "Você vai para a cozinha."
    elif escolha == "bob":
        show bobmorto
        "Bob esponja está desmaiado"
        hide bobmorto
    elif escolha == "inv":
        if vezes_investigou == 0:
            "Você descobre 10 dólares debaixo do colchão."
            "Dentro de um envelope escrito: 'Salário dos últimos 20 anos'."
            $ money += 10
        elif vezes_investigou == 1:
            "Você descobriu que hoje é o dia do contra."
            $ dia_do_contra = True 
        else:
            "Não há mais nada para investigar."
        $ vezes_investigou += 1
    elif escolha == "gary":
        # Desativa temporariamente o som de digitação
        $ temp_callbacks = config.all_character_callbacks[:]
        $ config.all_character_callbacks = []
        
        play sound "gary1.wav"
        $ renpy.music.set_volume(0.2, channel="sound")
        "Gary" "Meow"
        
        # Restaura o sistema de som de digitação
        $ config.all_character_callbacks = temp_callbacks
        
        jump salabob     

    # Volta automaticamente para o menu de opções após uma escolha
    # Aguarda 1 segundo antes de retornar
    jump chegada_em_casa

label salabob:
 # Verificar se é após 20h para redirecionar para quanaite
 if hora_do_dia >= 20:
    jump quanaite
    
 # Ainda dentro de casa, mapa continua desativado
 scene bg room4
 
 show batavo1 at Transform(xzoom=-1):
    zoom 1.0 xpos 1000 ypos 400

 show gary at left:
  zoom 0.3 xpos 500 ypos 1000
  
 
 while True:
      if not sala_mensagem_exibida:
         "Você está na sala"  

         $ sala_mensagem_exibida = True 

      menu:
            "Voltar para o quarto":
              scene quartobob

              show batavo1 at Transform(xzoom=-1) with fade:
                zoom 1.0 xpos 1000 ypos 400

              jump chegada_em_casa

            "Assistir TV":
                if not tv_quebrada:
                    # Primeira vez assistindo TV
                    # Mostrar a animação do peixe âncora
                    scene bg room4
                    show tv_reporter_anim
                    
                    # Diálogo do peixe âncora
                    "Peixe Âncora" "Notícia urgente! Um perigoso criminoso humano escapou da prisão em um barco!"
                    
                    "Peixe Âncora" "O barco naufragou próximo à Fenda do Biquíni! Qualquer informação deve ser reportada às auto-"
                    
                    # Batavo dá um soco na TV
                    hide tv_reporter_anim
                    show tv_batavo_soco
                    
                    play sound "punch.wav" volume 0.8
                    with hpunch
                    
                    b "CALA A BOCA, PORRA!"
                    
                    # TV quebrada
                    hide tv_batavo_soco
                    show tv_quebrada
                    
                    "Você quebrou a TV com um soco."
                    
                    # Marcar a TV como quebrada permanentemente
                    $ tv_quebrada = True
                else:
                    # TV já quebrada
                    scene bg room4
                    show tv_quebrada
                    
                    "A TV está quebrada."
                
                # Retornar ao menu da sala
                scene bg room4
                show batavo1 at Transform(xzoom=-1):
                    zoom 1.0 xpos 1000 ypos 400
                
                show gary at left:
                    zoom 0.3 xpos 500 ypos 1000
                
                jump salabob

            "Gary":
                $ escolha = "gary"
                jump opcoes

            "Sair":
                 play sound som_opcao
                   # Ativa o mapa quando o jogador sai de casa
                 $ saida += 1  # Incrementa a variável a cada clique
                 if saida == 1:
                     jump storymode  # Primeira vez, vai para storymode
                 if saida == 2:
                     jump day2  # Primeira vez, vai para storymode
                 if saida == 3:
                     jump day3  # Primeira vez, vai para storymode    
                 if saida == 4:
                     jump landal  # Primeira vez, vai para storymode       
                 else:
                     $ mapa_disponivel = True
                     call screen bobCasas # Da segunda vez em diante, mostra a tela

label casanoite:
 # Quando volta para casa à noite, desativa o mapa novamente
 $ mapa_disponivel = False
 
 scene quartobob noite

 show batavo1 at left with fade:
    zoom 1.2

 "O que eu devo fazer agora?"

 # Redirecionar para quanaite, que é o quarto do Bob à noite
 jump quanaite

label end1:
   # Ativa o mapa ao sair e mostrar as casas
   $ mapa_disponivel = True
   
   call screen bobCasas