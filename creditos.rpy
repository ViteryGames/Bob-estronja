# creditos.rpy - Versão Corrigida para o problema de exibição

# Definir som para os créditos
define audio.oceanman = "oceanman.mp3"

# Label principal para os créditos
label creditos:
    # Esconder a interface de diálogo e a tela xerequinha
    $ renpy.hide_screen("xerequinha")
    window hide
    $ _game_menu_screen = None
    
    # Parar qualquer música que esteja tocando
    stop music fadeout 2.0
    
    # Tocar a música dos créditos - creditson.mp3 (mantida sua escolha de música)
    play music "creditson.mp3" fadein 2.0
    
    # Primeira imagem do Patchy dizendo "Ha, você está aí!"
    scene black
    show patchy1
    with dissolve
    
    # Variável para armazenar a resposta do menu
    $ menu_resposta = ""
    
    # Diálogo do Patchy Pirata conversando com o jogador - sem caixas de diálogo
    $ narrator_mode = True
    
    call screen tv_centered_text("HA! Você está aí, marujo! Que bom que você veio!")
    
    call screen tv_centered_text("Eu sou Patchy Sins, o maior fã de jogos hentai em todo o planeta!")
    
    call screen tv_centered_text("Vejo que você chegou ao final do jogo... ou pelo menos a esta versão dele!")
    
    # Menu customizado para evitar a caixa de diálogo tradicional - CORRIGIDO
    $ menu_resposta = renpy.call_screen("credits_menu")
    
    # Mostrar resposta baseada na escolha
    if menu_resposta == "gostei":
        call screen tv_centered_text("ARRR! Fico muito feliz em ouvir isso, marujo! Os criadorores do jogo vão adorar saber que você se divertiu!")
    elif menu_resposta == "interessante":
        call screen tv_centered_text("HAHAHA! Sei o que você quer dizer, camarada! É um jogo para adultos com um senso de humor bastante peculiar!")
    elif menu_resposta == "mais":
        call screen tv_centered_text("ESSA é a pergunta certa, marinheiro esperto!")
    
    # Segunda imagem do Patchy olhando para o telespectador
    hide patchy1
    show patchy2
    with dissolve
    
    call screen tv_centered_text("Deixe-me contar um segredo importante, só entre nós...")
    
    call screen tv_centered_text("Esta é apenas a versão 0.0.5 BETA do jogo Spornbob!")
    
    call screen tv_centered_text("Há MUITO mais conteúdo em desenvolvimento, com novas cenas, personagens e minigames!")
    
    call screen tv_centered_text("O criador do jogo está trabalhando incansavelmente em novos conteúdos...")
    
    call screen tv_centered_text("E você pode ter acesso antecipado a todo esse conteúdo extra visitando o Patreon dele!")
    
    # Menu customizado para perguntas sobre o Patreon - CORRIGIDO
    $ menu_resposta = renpy.call_screen("credits_menu_patreon")
    
    # Mostrar resposta baseada na escolha
    if menu_resposta == "como":
        call screen tv_centered_text("É simples, marujo! Basta clicar no botão que aparecerá na tela de créditos! Ou acessar diretamente patreon.com/franktopia no seu navegador!")
    elif menu_resposta == "exclusivo":
        call screen tv_centered_text("Há acesso antecipado, sprites do jogo, artes exclusivas, votações, interação direta com a equipe, playtests e muito mais!")
    elif menu_resposta == "olhada":
        call screen tv_centered_text("Sabia decisão, camarada! Não vai se arrepender!")
    
    call screen tv_centered_text("Agora, sem mais delongas, vamos aos créditos deste maravilhoso jogo!")
    
    call screen tv_centered_text("E lembre-se: SPORNBOB VOLTARÁ EM BREVE COM MUITO MAIS CONTEÚDO!")
    
    # Mostrar as 5 imagens de créditos em sequência
    hide patchy2
    
    # Trocar para a música oceanman aqui (mantido do seu código)
    play music audio.oceanman fadein 2.0
    
    # Imagem de créditos 1
    show creditos1
    with dissolve
    pause 3.0
    
    # Imagem de créditos 2
    hide creditos1
    show creditos2
    with dissolve
    pause 3.0
    
    # Imagem de créditos 3
    hide creditos2
    show creditos3
    with dissolve
    pause 3.0
    
    # Imagem de créditos 4
    hide creditos3
    show creditos4
    with dissolve
    pause 3.0
    
    # Imagem de créditos 5
    hide creditos4
    show creditos5
    with dissolve
    pause 3.0
    
    # Tela final com link clicável para o Patreon
    hide creditos5
    
    # Mostrar Patchy novamente antes da tela final
    show patchy1
    
    call screen tv_centered_text("Foi uma honra compartilhar esta aventura com você, marujo!")
    
    call screen tv_centered_text("Espero ver você novamente em breve no oceano das atualizações!")
    
    call screen tv_centered_text("Não se esqueça de conferir o Patreon, tem muitos tesouros escondidos lá!")
    
    call screen tv_centered_text("ARRRR! Até a próxima, camarada!")
    
    hide patchy1
    
    # Mostrar uma tela preta com o botão do Patreon
    call screen creditos_patreon
    
    # Restaurar a interface ao retornar ao jogo
    window show
    $ _game_menu_screen = "save"
    $ renpy.show_screen("xerequinha")  # CORRIGIDO: troquei show_screen por renpy.show_screen
    
    # Encerrar a música de créditos com fade
    stop music fadeout 2.0
    
    # Voltar para o quarto do Bob
    jump room4
    
    return

# Tela de texto centralizado para diálogos sem caixa - MANTIDA SUA POSIÇÃO ATUALIZADA (yalign 0.8)
screen tv_centered_text(text_to_show):
    modal True
    
    # Área clicável para avançar
    button:
        xfill True
        yfill True
        action Return()
    
    # Frame com tamanho limitado para caber na TV
    frame:
        xalign 0.5
        yalign 0.8  # Posição atualizada conforme seu código
        xsize 600  # Largura limitada para caber na TV
        background None
        padding (20, 20)
        
        text text_to_show:
            xalign 0.5
            text_align 0.5
            size 30  # Tamanho reduzido
            color "#FFFFFF"
            outlines [(2, "#000000", 0, 0)]
            layout "subtitle"  # Melhor quebra de linha para textos longos

# Menu customizado para escolhas durante os créditos
screen credits_menu():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.8
        xsize 600  # Largura limitada para caber na TV
        background None
        
        vbox:
            spacing 20
            xalign 0.5
            
            textbutton "Eu gostei muito do jogo!":
                action Return("gostei")
                xalign 0.5
                text_size 25  # Tamanho reduzido
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "O jogo foi... interessante...":
                action Return("interessante")
                xalign 0.5
                text_size 25  # Tamanho reduzido
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "Quando sai mais conteúdo?":
                action Return("mais")
                xalign 0.5
                text_size 25  # Tamanho reduzido
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"

# Menu customizado para perguntas sobre o Patreon
screen credits_menu_patreon():
    modal True
    
    frame:
        xalign 0.5
        yalign 0.8
        xsize 600  # Largura limitada para caber na TV
        background None
        
        vbox:
            spacing 20
            xalign 0.5
            
            textbutton "Como faço para acessar o Patreon?":
                action Return("como")
                xalign 0.5
                text_size 25  # Tamanho reduzido
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "O que tem de exclusivo no Patreon?":
                action Return("exclusivo")
                xalign 0.5
                text_size 25  # Tamanho reduzido
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"
                
            textbutton "Vou dar uma olhada!":
                action Return("olhada")
                xalign 0.5
                text_size 25  # Tamanho reduzido
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                text_outlines [(2, "#000000", 0, 0)]
                background "#00000080"
                hover_background "#33333380"

# Tela com botão para o Patreon
screen creditos_patreon():
    modal True
    tag creditos
    
    # Fundo escuro
    add "black"
    
    # Agradecimento
    vbox:
        xalign 0.5
        yalign 0.3
        spacing 20
        
        text "Obrigado por jogar Spornbob!" size 50 color "#FFDD00" xalign 0.5 outlines [(3, "#DD6600", 0, 0)]
        text "Versão 0.0.5 BETA" size 30 color "#FFFFFF" xalign 0.5 outlines [(2, "#555555", 0, 0)]
        
        null height 80
        
        text "Para mais conteúdo, atualizações e versões completas:" size 30 color "#FFFFFF" xalign 0.5
    
    # Botão grande do Patreon
    vbox:
        xalign 0.5
        yalign 0.7
        
        # Botão do Patreon estilizado
        textbutton "VISITE NOSSO PATREON":
            action OpenURL("https://www.patreon.com/franktopia")
            xalign 0.5
            text_size 40
            text_color "#FFFFFF"
            text_hover_color "#FF424D"  # Cor vermelha do Patreon
            text_outlines [(2, "#052D49", 0, 0)]
            background "#FF424D"  # Cor do botão é a cor do Patreon
            hover_background "#FF6B70"
            padding (50, 20)
        
        null height 20
        
        # URL do Patreon
        text "patreon.com/franktopia" size 30 color "#FF424D" xalign 0.5 outlines [(1, "#052D49", 0, 0)]
    
    # Botão para voltar para o quarto
    vbox:
        xalign 0.5
        yalign 0.95
        
        textbutton "Voltar para o quarto":
            action Return()
            xalign 0.5
            text_size 30
            text_color "#FFFFFF"
            text_hover_color "#FFDD00"
            text_outlines [(2, "#333333", 0, 0)]
            background "#444444"
            hover_background "#666666"
            padding (30, 10)