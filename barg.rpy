label barg: 
    scene barganinha:
      zoom 1.2

    "Bem-vindo ao jogo!"
    "Você tem [money] moedas para gastar na loja."
    
    # Mostra a loja e espera o jogador sair
    call screen loja
    
    # Após a loja, continua a história
    "Você saiu da loja!"
    
    # Exemplo de uso de um item comprado
    if 1 in inventario:
        "Você pega sua Chapéu de Cowboy e se prepara para a aventura!"
    else:
        "Você não tem um Chapéu de Cowboy. Talvez devesse comprar um..."

default inventario = []  # Lista de itens comprados (IDs)
default pagina_atual = 1  # Controla a página atual da loja
default agua_viva_capturadas = 0  # Contador para águas-vivas capturadas no minigame

# Definindo os 20 itens originais da loja 
# Acrescentando o item 21 (água-viva) e 22 (geleia) e 23 (pote com jeleia) para que possa ser referenciado pelo inventário
define itens_loja = {
    1: {"nome": "Chapéu de Cowboy", "preco": 50},
    2: {"nome": "Chocolate", "preco": 3},
    3: {"nome": "Nozes", "preco": 5},
    4: {"nome": "Chave de Fenda", "preco": 20},
    5: {"nome": "Torta de Algas", "preco": 10},
    6: {"nome": "Torta de Nozes (Diretamente do Texas)", "preco": 30},
    7: {"nome": "Rede de Caçar Águas-Vivas", "preco": 15},
    8: {"nome": "Pote para Águas-Vivas", "preco": 2},
    9: {"nome": "Clarinete", "preco": 60},
    10: {"nome": "Livros", "preco": 10},
    11: {"nome": "Ração para Caracóis", "preco": 5},
    12: {"nome": "Sanduíche", "preco": 10},
    13: {"nome": "Saco de Pão para Hambúrguer", "preco": 15},
    14: {"nome": "Camisinha", "preco": 5},
    15: {"nome": "Boneca Inflável", "preco": 400},
    16: {"nome": "Bolha de Sabão", "preco": 10},
    17: {"nome": "Sonífero", "preco": 25},
    18: {"nome": "Garrafa de Vidro", "preco": 15},
    19: {"nome": "Abacaxi", "preco": 8},  # ATUALIZADO: preço reduzido para 8 moedas
    20: {"nome": "Item Misterioso 2", "preco": 4000},
    21: {"nome": "Água-viva Capturada", "preco": 25},  # Item adicionado para referência
    22: {"nome": "Geleia de Água-viva", "preco": 40},  # Item adicionado para referência
    23: {"nome": "Pote com Jeleia", "preco": 50}       # Item adicionado para referência
}

# Lista dos items que realmente aparecem na loja
define itens_mostrados_loja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Função para comprar itens
init python:
    def comprar_item(id_item):
        global money, inventario
        item = itens_loja[id_item]
        
        # Verificar limites para itens especiais
        if id_item == 14:  # Camisinha
            qnt_camisinhas = inventario.count(14)
            if qnt_camisinhas >= 5:
                renpy.notify("Você já tem o número máximo de camisinhas (5)!")
                return
                
        elif id_item == 3:  # Nozes
            qnt_nozes = inventario.count(3)
            if qnt_nozes >= 10:
                renpy.notify("Você já tem o número máximo de nozes (10)!")
                return
                
        elif id_item == 8:  # Pote para Águas-Vivas
            qnt_potes = inventario.count(8)
            if qnt_potes >= 5:
                renpy.notify("Você já tem o número máximo de potes para águas-vivas (5)!")
                return
        
        # Verificar se tem dinheiro suficiente
        if money >= item["preco"]:
            money -= item["preco"]
            
            # Para itens que podem ser comprados várias vezes
            if id_item == 14:  # Camisinha
                inventario.append(id_item)
                renpy.notify("Camisinha comprada com sucesso!")
            elif id_item == 3:  # Nozes
                inventario.append(id_item)
                renpy.notify("Nozes compradas com sucesso!")
            elif id_item == 8:  # Pote para Águas-Vivas
                inventario.append(id_item)
                renpy.notify("Pote para Águas-Vivas comprado com sucesso!")
            # Para outros itens, verificamos se já possui
            elif id_item not in inventario:
                inventario.append(id_item)
                renpy.notify(f"{item['nome']} comprado com sucesso!")
            else:
                renpy.notify("Você já possui este item!")
                money += item["preco"]  # Devolve o dinheiro
        else:
            renpy.notify("Moedas insuficientes!")
    
    # Função para adicionar águas-vivas capturadas ao inventário
    def adicionar_aguas_vivas_ao_inventario(quantidade):
        global inventario, agua_viva_capturadas
        
        # Adiciona água-viva capturada (ID 21) ao inventário
        for i in range(quantidade):
            inventario.append(21)
        
        # Atualiza o contador total
        agua_viva_capturadas += quantidade
        
        renpy.notify(f"{quantidade} águas-vivas adicionadas ao inventário!")

# Funções para mudar de página
init python:
    def proxima_pagina():
        global pagina_atual
        # Calcula o número total de páginas baseado no número de itens mostrados na loja
        total_paginas = (len(itens_mostrados_loja) + 5) // 6  # 6 itens por página, arredondando para cima
        if pagina_atual < total_paginas:
            pagina_atual += 1

    def pagina_anterior():
        global pagina_atual
        if pagina_atual > 1:
            pagina_atual -= 1

# Interface da loja com itens em grid
screen loja():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        
        vbox:
            spacing 30  # Aumentado o espaçamento entre elementos
            xalign 0.5
            
            # Título e moedas
            text "Loja de Itens - Página [pagina_atual]" xalign 0.5 size 28  # Aumentado o tamanho
            text "Moedas: [money]" xalign 0.5 size 24  # Aumentado o tamanho
            
            # Mostrar quantidade de itens acumuláveis
            $ qnt_camisinhas = inventario.count(14)
            $ qnt_nozes = inventario.count(3)
            $ qnt_potes = inventario.count(8)
            hbox:
                spacing 30
                xalign 0.5
                if qnt_camisinhas > 0:
                    text "Camisinhas: [qnt_camisinhas]/5" xalign 0.5 size 22 color "#00CC00"
                if qnt_nozes > 0:
                    text "Nozes: [qnt_nozes]/10" xalign 0.5 size 22 color "#00CC00"
                if qnt_potes > 0:
                    text "Potes: [qnt_potes]/5" xalign 0.5 size 22 color "#00CC00"
            
            # Grid de itens (3 colunas x 2 linhas = 6 itens por página)
            grid 3 2:
                xalign 0.5
                spacing 30  # Aumentado o espaçamento entre itens
                
                # Determina quais itens mostrar com base na página atual
                $ inicio = (pagina_atual - 1) * 6
                $ fim = min(pagina_atual * 6 - 1, len(itens_mostrados_loja) - 1)
                
                # Mostra os itens da página atual
                for i in range(inicio, fim + 1):
                    $ id_item = itens_mostrados_loja[i]
                    # Cria um frame para cada item
                    frame:
                        xsize 220
                        ysize 180
                        
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 15
                            
                            # Preço com fonte um pouco maior
                            text "Preço: [itens_loja[id_item]['preco']]" xalign 0.5 size 18
                            
                            # Nome do item com fonte ainda maior
                            text itens_loja[id_item]["nome"]:
                                xalign 0.5
                                text_align 0.5
                                xmaximum 200
                                size 22  # Aumentado para 22
                            
                            # Status para itens acumuláveis
                            if id_item == 14:  # Camisinha
                                if qnt_camisinhas >= 5:
                                    text "Máximo atingido!" xalign 0.5 size 16 color "#CC0000"
                                else:
                                    text "Possui: [qnt_camisinhas]/5" xalign 0.5 size 16 color "#0066CC"
                            elif id_item == 3:  # Nozes
                                if qnt_nozes >= 10:
                                    text "Máximo atingido!" xalign 0.5 size 16 color "#CC0000"
                                else:
                                    text "Possui: [qnt_nozes]/10" xalign 0.5 size 16 color "#0066CC"
                            elif id_item == 8:  # Pote para Águas-Vivas
                                if qnt_potes >= 5:
                                    text "Máximo atingido!" xalign 0.5 size 16 color "#CC0000"
                                else:
                                    text "Possui: [qnt_potes]/5" xalign 0.5 size 16 color "#0066CC"
                            elif id_item in inventario and id_item not in [3, 8, 14]:  # Outros itens
                                text "Já possui" xalign 0.5 size 16 color "#CC0000"
                                
                            # Botão de compra (desabilitado se atingiu máximo)
                            if id_item == 14 and qnt_camisinhas >= 5:
                                textbutton "Comprar":
                                    action NullAction()
                                    xalign 0.5
                                    text_size 12
                                    sensitive False
                            elif id_item == 3 and qnt_nozes >= 10:
                                textbutton "Comprar":
                                    action NullAction()
                                    xalign 0.5
                                    text_size 12
                                    sensitive False
                            elif id_item == 8 and qnt_potes >= 5:
                                textbutton "Comprar":
                                    action NullAction()
                                    xalign 0.5
                                    text_size 12
                                    sensitive False
                            elif id_item not in inventario or id_item in [3, 8, 14]:
                                textbutton "Comprar":
                                    action Function(comprar_item, id_item)
                                    xalign 0.5
                                    text_size 12
                            else:
                                textbutton "Comprar":
                                    action NullAction()
                                    xalign 0.5
                                    text_size 12
                                    sensitive False
            
            # Navegação entre páginas
            hbox:
                spacing 100  # Aumentado o espaçamento entre os botões
                xalign 0.5
                
                # Botão página anterior
                textbutton "< Anterior" action Function(pagina_anterior) sensitive pagina_atual > 1 xpadding 20 ypadding 10  # Aumentado o padding
                
                # Botão próxima página
                $ total_paginas = (len(itens_mostrados_loja) + 5) // 6  # Calcula o número total de páginas
                textbutton "Próxima >" action Function(proxima_pagina) sensitive pagina_atual < total_paginas xpadding 20 ypadding 10  # Aumentado o padding
            
            # Botão para sair da loja
            textbutton "Sair da Loja" action Jump("room4") xalign 0.5 xpadding 30 ypadding 15  # Aumentado o padding