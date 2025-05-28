# explorar.rpy - Sistema de exploração para áreas externas
# Locais externos com opções de entrada nos locais

# Imagens das áreas durante o dia
image area_siricascudo_dia = "images/kk.jpg"
image area_sandy_dia = "images/casasandyy.png"
image area_aguasvivas_dia = "images/jellyfieldings.png"
image area_loja_dia = "images/bangnday.png"

# Imagens das áreas durante a noite
image area_siricascudo_noite = "images/siricascudo_exterior_noite.jpg"
image area_sandy_noite = "images/sandy_exterior_noite.jpg"
image area_aguasvivas_noite = "images/aguasvivas_exterior_noite.jpg"
image area_loja_noite = "images/bangnnight.png"

# Variáveis para rastrear se o jogador já visitou um local
default visitou_siricascudo = False
default visitou_sandy_exterior = False
default visitou_aguasvivas = False
default visitou_loja_exterior = False

# Label principal para exploração
label explorar_siricascudo:
    # Verificar se é muito tarde (após 20h)
    if hora_do_dia >= 20:
        scene area_siricascudo_noite
        "Está muito tarde. O Siri Cascudo já está fechado."
        
        menu:
            "Voltar para casa":
                jump room4
    else:
        # Mostrar a área durante o dia
        scene area_siricascudo_dia
        
        # Mostrar descrição apenas na primeira visita
        if not visitou_siricascudo:
            "Você está em frente ao Siri Cascudo. É um restaurante popular na Fenda do Biquíni."
            $ visitou_siricascudo = True
        
        menu:
            "Entrar no Siri Cascudo":
                # Chamar a screen lobbykk em vez de room2
                call screen lobbykk with fade
                
            "Voltar para o mapa":
                call screen mapScreen

label explorar_sandy:
    # Verificar se é muito tarde (após 20h)
    if hora_do_dia >= 20:
        scene area_sandy_noite
        "Está muito tarde. Sandy provavelmente está dormindo."
        
        menu:
            "Voltar para casa":
                jump room4
    else:
        # Mostrar a área durante o dia
        scene area_sandy_dia
        
        # Mostrar descrição apenas na primeira visita
        if not visitou_sandy_exterior:
            "Você está em frente à casa da Sandy. É uma cúpula de ar onde ela vive."
            $ visitou_sandy_exterior = True
        
        menu:
            "Visitar Sandy":
                jump sandy
                
            "Voltar para o mapa":
                call screen mapScreen

label explorar_aguasvivas:
    # Verificar se é muito tarde (após 20h)
    if hora_do_dia >= 20:
        scene area_aguasvivas_noite
        "Está muito tarde. É perigoso caçar águas-vivas à noite."
        
        menu:
            "Voltar para casa":
                jump room4
    else:
        # Mostrar a área durante o dia
        scene area_aguasvivas_dia
        
        # Mostrar descrição apenas na primeira visita
        if not visitou_aguasvivas:
            "Você está nos campos de águas-vivas. É um lugar perfeito para caçá-las."
            $ visitou_aguasvivas = True
        
        menu:
            "Caçar águas-vivas":
                # Verificar se tem uma rede (item ID 7)
                if 7 in inventario:
                    jump minigame_aguasvivas
                else:
                    "Você precisa de uma rede para caçar águas-vivas. Compre uma na loja."
                    jump explorar_aguasvivas
                
            "Voltar para o mapa":
                call screen mapScreen

label explorar_loja:
    # Verificar se é muito tarde (após 20h)
    if hora_do_dia >= 20:
        scene area_loja_noite
        "Está muito tarde. A loja já está fechada."
        
        menu:
            "Voltar para casa":
                jump room4
    else:
        # Mostrar a área durante o dia
        scene area_loja_dia
        
        # Mostrar descrição apenas na primeira visita
        if not visitou_loja_exterior:
            "Você está em frente à loja. Aqui você pode comprar itens úteis."
            $ visitou_loja_exterior = True
        
        menu:
            "Entrar na loja":
                jump barg
                
            "Voltar para o mapa":
                call screen mapScreen

# Adicione este código no arquivo screens.rpy ou myScreens.rpy para modificar a tela do mapa
# para que use as novas labels de exploração

screen mapScreen():
    modal True  # Bloqueia interações com telas abaixo
    
    # Imagem de fundo do mapa
    add "bg map.png"
    
    # Botões de navegação com links para as novas labels de exploração
    #Room 1
    imagebutton:
        xpos 545
        ypos 250
        idle "R1 idle.png"
        hover "R1 hover.png"
        action [Hide("mapScreen"), Jump("room1")]
        
    #Room 2 - Siri Cascudo
    imagebutton:
        xpos 22
        ypos 100
        idle "R2 idle.png"
        hover "R2 hover.png"
        action [Hide("mapScreen"), Jump("explorar_siricascudo")]
        
    #Room 3
    imagebutton:
        xpos 130
        ypos 385
        idle "R3 idle.png"
        hover "R3 hover.png"
        action [Hide("mapScreen"), Jump("room3")]
        
    #Room 4 - Sandy
    imagebutton:
        xpos 530
        ypos 600
        idle "R4 idle.png"
        hover "R4 hover.png"
        action [Hide("mapScreen"), Jump("explorar_sandy")]
    
    #Room 5
    imagebutton:
        xpos 1430
        ypos 25
        idle "R5 idle.png"
        hover "R5 hover.png"
        action [Hide("mapScreen"), Jump("praia")]
        
    #Campos de Águas-vivas
    imagebutton:
        xpos 1500
        ypos 590
        idle "jellyfields idle.png"
        hover "jellyfields hover.png"
        action [Hide("mapScreen"), Jump("explorar_aguasvivas")]
    
    #Loja
    imagebutton:
        xpos 1395
        ypos 310
        idle "loja idle.png"
        hover "loja hover.png"
        action [Hide("mapScreen"), Jump("explorar_loja")]
    
    # Botão para fechar o mapa
    textbutton "Fechar Mapa":
        action Hide("mapScreen")
        xalign 0.5
        yalign 0.95
        text_size 40
        text_color "#FFFFFF"
        text_hover_color "#FFFF99"
        text_outlines [(2, "#003399", 0, 0)]
        background "#225599"
        hover_background "#3366BB"