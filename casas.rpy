label casas:
    # Certifique-se de que a tela bobCasas é exibida
    call screen bobCasas

# Screen de seleção de casas com a screen xerequinha incluída
screen bobCasas:
    add "bg room1.jpg"
    
    # Adiciona a screen xerequinha para mostrar informações do dia
    use xerequinha
    
    # Botões das casas
    imagebutton:
        xpos 1300
        ypos 180
        idle "abacaxi idle.png"
        hover "abacaxi.png" 
        action Jump("salabob") 

    imagebutton:
        xpos 735
        ypos 195
        idle "lulah idle.png"
        hover "lulah hover.png" 
        action Show("casa_trancada_message")
        

    imagebutton:
        xpos 220
        ypos 510
        idle "preda idle.png"
        hover "preda hover.png" 
        action Jump("preda")

# Mensagem quando tenta entrar na casa da Lula Molusco
screen casa_trancada_message():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 300
        background "#336699"
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            text "A casa está trancada!" size 40 color "#FF9977" xalign 0.5 outlines [(2, "#CC6644", 0, 0)]
            text "Parece que a Lula Molusco não está em casa\nou não quer receber visitas." size 25 color "#FFFFFF" xalign 0.5 outlines [(1, "#003366", 1, 1)]
            
            textbutton "Fechar":
                action Hide("casa_trancada_message")
                xalign 0.5
                text_size 30
                text_color "#FFFFFF"
                text_hover_color "#FFFF99"
                text_outlines [(2, "#990000", 0, 0)]
                background "#DD3366"
                hover_background "#FF5588"