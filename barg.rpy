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
        "Você pega sua Espada e se prepara para a aventura!"
    else:
        "Você não tem uma Espada. Talvez devesse comprar uma..."
default inventario = []  # Lista de itens comprados (IDs)
default pagina_atual = 1  # Controla a página atual da loja

# Definindo os 20 itens da loja
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
    19: {"nome": "Abacaxi", "preco": 10},
    20: {"nome": "Item Misterioso 2", "preco": 4000}
}

# Função para comprar itens
init python:
    def comprar_item(id_item):
        global money, inventario
        item = itens_loja[id_item]
        if money >= item["preco"] and id_item not in inventario:
            money -= item["preco"]
            inventario.append(id_item)
            renpy.notify(f"{item['nome']} comprado com sucesso!")
        else:
            if id_item in inventario:
                renpy.notify("Você já possui este item!")
            else:
                renpy.notify("Moedas insuficientes!")

# Funções para mudar de página
init python:
    def proxima_pagina():
        global pagina_atual
        if pagina_atual < 4:  # Agora são 4 páginas (20 itens ÷ 6 itens por página = 4 páginas)
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
            
            # Grid de itens (3 colunas x 2 linhas = 6 itens por página)
            grid 3 2:
                xalign 0.5
                spacing 30  # Aumentado o espaçamento entre itens
                
                # Determina quais itens mostrar com base na página atual
                $ inicio = (pagina_atual - 1) * 6 + 1
                $ fim = min(pagina_atual * 6, 20)
                
                # Mostra os itens da página atual
                for id_item in range(inicio, fim + 1):
                    # Cria um frame para cada item
                    frame:
                        xsize 220
                        ysize 180
                        
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 15
                            
                            # Preço (agora com fonte um pouco maior)
                            if id_item in inventario:
                                text "Comprado" xalign 0.5 size 18
                            else:
                                text "Preço: [itens_loja[id_item]['preco']]" xalign 0.5 size 18
                            
                            # Nome do item (agora com fonte ainda maior)
                            text itens_loja[id_item]["nome"]:
                                xalign 0.5
                                text_align 0.5
                                xmaximum 200
                                size 22  # Aumentado para 22
                                
                            # Botão de compra (agora com fonte menor)
                            if id_item not in inventario:
                                textbutton "Comprar":
                                    action Function(comprar_item, id_item)
                                    xalign 0.5
                                    text_size 12  # Tamanho de fonte reduzido
            
            # Navegação entre páginas
            hbox:
                spacing 100  # Aumentado o espaçamento entre os botões
                xalign 0.5
                
                # Botão página anterior
                textbutton "< Anterior" action Function(pagina_anterior) sensitive pagina_atual > 1 xpadding 20 ypadding 10  # Aumentado o padding
                
                # Botão próxima página
                textbutton "Próxima >" action Function(proxima_pagina) sensitive pagina_atual < 4 xpadding 20 ypadding 10  # Aumentado o padding
            
            # Botão para sair da loja
            textbutton "Sair da Loja" action Jump("room4") xalign 0.5 xpadding 30 ypadding 15  # Aumentado o padding 
