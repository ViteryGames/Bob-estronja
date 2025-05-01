screen mapScreen():
    modal True  # Bloqueia interações com telas abaixo
    
    # Imagem de fundo do mapa
    add "bg map.png"
    
    # Botões de navegação
    #Room 1
    imagebutton:
        xpos 545
        ypos 250
        idle "R1 idle.png"
        hover "R1 hover.png"
        action [Hide("mapScreen"), Jump("room1")]
        
    #Room 2
    imagebutton:
        xpos 22
        ypos 100
        idle "R2 idle.png"
        hover "R2 hover.png"
        action [Hide("mapScreen"), Call("lobbykk")]
        
    #Room 3
    imagebutton:
        xpos 130
        ypos 385
        idle "R3 idle.png"
        hover "R3 hover.png"
        action [Hide("mapScreen"), Jump("balde_de_lixo")]
        
    imagebutton:
        xpos 530
        ypos 600
        idle "R4 idle.png"
        hover "R4 hover.png"
        action [Hide("mapScreen"), Jump("sandy")]
    
    imagebutton:
        xpos 1430
        ypos 25
        idle "R5 idle.png"
        hover "R5 hover.png"
        action [Hide("mapScreen"), Jump("praia")]
        
    imagebutton:
        xpos 1500
        ypos 590
        idle "jellyfields idle.png"
        hover "jellyfields hover.png"
        action [Hide("mapScreen"), Jump("minigame_aguasvivas")]
    
    imagebutton:
        xpos 1395
        ypos 310
        idle "loja idle.png"
        hover "loja hover.png"
        action [Hide("mapScreen"), Jump("barg")]
    
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