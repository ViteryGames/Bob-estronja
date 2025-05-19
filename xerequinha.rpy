screen xerequinha:
    # Informações básicas com tema submarino - lado esquerdo
    text "Money = [money]" xpos 50 ypos 50 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    text "Tempo = [hora_do_dia]h" xpos 50 ypos 100 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    #text "Saida = [saida]" xpos 50 ypos 150 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    text "Dia = [dia]" xpos 50 ypos 150 size 50 color "#8CEFFD" outlines [(2, "#0066CC", 0, 0), (4, "#003366", 1, 1)]
    
    # Mostra a quantidade de camisinhas com efeito de contorno - lado esquerdo
    #$ qnt_camisinhas = inventario.count(14)
    #if qnt_camisinhas > 0:
        #text "Camisinhas = [qnt_camisinhas]/5" xpos 50 ypos 200 size 50 color "#FF99CC" outlines [(2, "#CC0066", 0, 0), (4, "#990033", 1, 1)]
    
    # Mostra a quantidade de nozes com efeito de contorno - lado esquerdo
    #$ qnt_nozes = inventario.count(3)
    #if qnt_nozes > 0:
        #text "Nozes = [qnt_nozes]/10" xpos 50 ypos 250 size 50 color "#DDBB77" outlines [(2, "#996633", 0, 0), (4, "#663300", 1, 1)]
    
    # Mostra a quantidade de águas-vivas capturadas - lado esquerdo
    #$ qnt_aguas_vivas = inventario.count(21)
    #if qnt_aguas_vivas > 0:
        #text "Águas-vivas = [qnt_aguas_vivas]" xpos 50 ypos 300 size 50 color "#FF80BF" outlines [(2, "#CC0066", 0, 0), (4, "#990033", 1, 1)]
    
    # Botões para Mapa e Inventário - lado direito
    vbox:
        xpos 1500  # Posicionado na direita da tela
        ypos 50    # Alinhado com o topo
        spacing 20
        
        # O botão do mapa só aparece se mapa_disponivel for True
        if mapa_disponivel:
            textbutton "Mapa":
                action Show("mapScreen")
                text_size 40
                text_color "#FFFFFF"
                text_hover_color "#FFCC00"
                text_outlines [(2, "#003399", 0, 0)]
                background "#225599"
                hover_background "#3366BB"
        else:
            # Versão desabilitada do botão quando o mapa não está disponível
            textbutton "Mapa":
                action NullAction()
                text_size 40
                text_color "#888888"  # Cor cinza para indicar desabilitado
                text_outlines [(2, "#003366", 0, 0)]
                background "#113344"  # Cor escura para indicar desabilitado
                sensitive False
            
        textbutton "Inventário":
            action Show("inventarioScreen")
            text_size 40
            text_color "#FFFFFF"
            text_hover_color "#FFCC00"
            text_outlines [(2, "#006633", 0, 0)]
            background "#228866"
            hover_background "#33AA88"

# Tela de Inventário
screen inventarioScreen():
    modal True  # Bloqueia interações com telas abaixo
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background "#225599"  # Azul escuro como água profunda
        
        vbox:
            xalign 0.5
            yalign 0.0
            xsize 780
            ysize 540
            spacing 20
            
            text "SEU INVENTÁRIO" size 50 color "#8CEFFD" xalign 0.5 outlines [(3, "#003366", 0, 0), (5, "#002244", 1, 1)]
            
            # Verificar se o inventário está vazio
            if len(inventario) == 0:
                text "Seu inventário está vazio!" size 30 color "#FF9977" xalign 0.5 outlines [(2, "#CC6644", 0, 0)]
            else:
                # Calcula quantos itens diferentes tem no inventário (sem contar duplicados como camisinhas e nozes)
                $ itens_unicos = []
                $ itens_multiplos = {3: 0, 14: 0, 21: 0}  # Dicionário para contar nozes (3), camisinhas (14) e águas-vivas (21)
                
                python:
                    for item_id in inventario:
                        if item_id == 3:  # Nozes
                            itens_multiplos[3] += 1
                        elif item_id == 14:  # Camisinhas
                            itens_multiplos[14] += 1
                        elif item_id == 21:  # Águas-vivas
                            itens_multiplos[21] += 1
                        elif item_id not in itens_unicos:
                            itens_unicos.append(item_id)
                
                # Cria uma área com scroll para muitos itens
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    xsize 760
                    ysize 400
                    
                    vbox:
                        spacing 15
                        xalign 0.5
                        
                        # Mostrar itens que podem ter múltiplas unidades
                        if itens_multiplos[3] > 0:  # Nozes
                            frame:
                                xsize 700
                                background "#336644"  # Verde escuro como algas marinhas
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    text "Nozes" size 30 color "#DDBB77" outlines [(2, "#996633", 0, 0)]
                                    text "Quantidade: [itens_multiplos[3]]/10" size 25 color "#EEDDAA" outlines [(1, "#AA8844", 0, 0)]
                                    text "Um petisco nutritivo e saudável." size 20 color "#FFFFFF" outlines [(1, "#004400", 1, 1)]
                        
                        if itens_multiplos[14] > 0:  # Camisinhas
                            frame:
                                xsize 700
                                background "#993366"  # Rosa escuro
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    text "Camisinhas" size 30 color "#FF99CC" outlines [(2, "#CC0066", 0, 0)]
                                    text "Quantidade: [itens_multiplos[14]]/5" size 25 color "#FFBBDD" outlines [(1, "#CC6699", 0, 0)]
                                    text "Proteção é importante para certas atividades." size 20 color "#FFFFFF" outlines [(1, "#660033", 1, 1)]
                                    
                        if itens_multiplos[21] > 0:  # Águas-vivas capturadas
                            frame:
                                xsize 700
                                background "#CC6699"  # Rosa médio
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    text "Águas-vivas Capturadas" size 30 color "#FF80BF" outlines [(2, "#CC0066", 0, 0)]
                                    text "Quantidade: [itens_multiplos[21]]" size 25 color "#FFBBDD" outlines [(1, "#CC6699", 0, 0)]
                                    text "Criaturas gelatinosas que você capturou. Valiosas para coleção ou uso em receitas." size 20 color "#FFFFFF" outlines [(1, "#660033", 1, 1)]
                        
                        # Mostrar outros itens únicos
                        for item_id in itens_unicos:
                            frame:
                                xsize 700
                                background "#336699"  # Azul médio como oceano
                                padding (20, 10)
                                
                                vbox:
                                    spacing 5
                                    # CORREÇÃO: Verificar se item_id está em itens_loja antes de acessar
                                    if item_id in itens_loja:
                                        text itens_loja[item_id]["nome"] size 30 color "#99CCFF" outlines [(2, "#0044AA", 0, 0)]
                                        text "Preço: $[itens_loja[item_id]['preco']]" size 25 color "#AADDFF" outlines [(1, "#0066CC", 0, 0)]
                                        
                                        # Descrições personalizadas para alguns itens
                                        if item_id == 1:  # Chapéu de Cowboy
                                            text "Um chapéu estiloso para parecer um verdadeiro cowboy." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 15:  # Boneca Inflável
                                            text "Uma companhia para noites solitárias." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 7:  # Rede de Caçar Águas-Vivas
                                            text "Ferramenta essencial para caçar águas-vivas. Permite capturar mais quando usar o minigame." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        elif item_id == 8:  # Pote para Águas-Vivas
                                            text "Um recipiente especial para guardar águas-vivas. Diferente das que você captura no jogo." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                        else:
                                            text "Item útil para sua aventura." size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
                                    # Se for o item águas-vivas (ID 21) que está no dicionário separado
                                    elif item_id == 21:
                                        text "Água-viva Capturada" size 30 color "#FF80BF" outlines [(2, "#CC0066", 0, 0)]
                                        text "Preço: $25" size 25 color "#FFBBDD" outlines [(1, "#CC6699", 0, 0)]
                                        text "Uma água-viva brilhante que você capturou. Pode ser usada em várias receitas ou vendida." size 20 color "#FFFFFF" outlines [(1, "#660033", 1, 1)]
                                    # Fallback para qualquer outro item não reconhecido
                                    else:
                                        text "Item Desconhecido" size 30 color "#AAAAAA" outlines [(2, "#555555", 0, 0)]
                                        text "Item não catalogado" size 20 color "#FFFFFF" outlines [(1, "#003366", 1, 1)]
        
        # Botão para fechar o inventário - estilo de bolha submarina
        textbutton "Fechar":
            action Hide("inventarioScreen")
            xalign 0.5
            yalign 0.95
            text_size 40
            text_color "#FFFFFF"
            text_hover_color "#FFFF99"
            text_outlines [(2, "#990000", 0, 0)]
            background "#DD3366"
            hover_background "#FF5588"