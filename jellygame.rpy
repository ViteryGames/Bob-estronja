# Mini-jogo de Caça às Águas-vivas (aguasvivas.rpy)
# Versão com sistema de geleia de águas-vivas

# Variáveis de controle
default jogou_minigame_antes = False  # Controla se o jogador já jogou pelo menos uma vez
default total_geleia_feita = 0  # Total de geleia feita ao longo do jogo

# Configuração da tela para o mini-jogo
init -10 python:
    # Classe para águas-vivas
    class AguaViva:
        def __init__(self, x, y, velocidade, visivel=True, id=0):
            self.x = x
            self.y = y
            self.velocidade = velocidade
            self.visivel = visivel
            self.id = id
    
    def inicializar_aguas_vivas():
        global ag_pontos, ag_tempo_restante, ag_jogo_ativo, aguas_vivas
        
        # Resetar contadores
        ag_pontos = 0
        ag_tempo_restante = 10.0
        ag_jogo_ativo = True
        
        # Criar águas-vivas
        aguas_vivas = []
        for i in range(8):
            fila = i % 4  # 4 fileiras para 8 águas-vivas
            pos_y = 200 + (fila * 180)  # Espaçamento vertical
            pos_x = -150 - (renpy.random.randint(0, 3) * 150)  # Posições variadas
            vel = renpy.random.randint(20, 30)  # Velocidades
            aguas_vivas.append(AguaViva(pos_x, pos_y, vel, True, i))
    
    def atualizar_aguas_vivas():
        global aguas_vivas
        for q in aguas_vivas:
            if q.x > config.screen_width:
                # Quando sai da tela, volta para esquerda
                q.x = -150
                q.visivel = True
                q.velocidade = renpy.random.randint(20, 30)
            else:
                # Move água-viva
                q.x += q.velocidade
    
    def clicar_agua_viva(id):
        global aguas_vivas, ag_pontos
        # Marca a água-viva como invisível
        for q in aguas_vivas:
            if q.id == id and q.visivel:
                q.visivel = False
                ag_pontos += 1
                break
    
    def adicionar_aguas_vivas_capturadas():
        global ag_pontos, inventario
        
        # Adiciona água-viva capturada (ID 21) ao inventário
        for i in range(ag_pontos):
            inventario.append(21)
        
        renpy.notify(f"{ag_pontos} águas-vivas adicionadas ao inventário!")
    
    def fazer_geleia_de_aguas_vivas(quantidade=1):
        global inventario, total_geleia_feita
        
        # Verificar se temos águas-vivas e potes suficientes
        qnt_aguas_vivas = inventario.count(21)  # ID da água-viva
        qnt_potes = inventario.count(8)  # ID do pote
        
        # Determinar quantas geleias podemos fazer
        max_geleia = min(qnt_aguas_vivas, qnt_potes, quantidade)
        
        if max_geleia <= 0:
            return 0
            
        # Remover os ingredientes do inventário
        for i in range(max_geleia):
            inventario.remove(21)  # Remove uma água-viva
            inventario.remove(8)   # Remove um pote
            
        # Adicionar geleia ao inventário (ID 22)
        for i in range(max_geleia):
            inventario.append(22)  # Adiciona geleia de água-viva
            
        # Atualizar contador
        total_geleia_feita += max_geleia
        
        return max_geleia
    
    def limpar_telas_aguasvivas():
        # Função para garantir que todas as telas do mini-jogo sejam escondidas
        renpy.hide_screen("ag_game_screen")
        renpy.hide_screen("ag_game_info")

# Adicionar item de geleia ao dicionário de itens
init 1 python:
    if 22 not in itens_loja:
        itens_loja[22] = {"nome": "Geleia de Água-viva", "preco": 40}

# Variáveis para o mini-jogo (independentes do jogo principal)
default ag_pontos = 0
default ag_tempo_restante = 10.0
default ag_jogo_ativo = False
default aguas_vivas = []

# Tela de informações do mini-jogo (simples, apenas texto)
screen ag_game_info():
    frame:
        xalign 1.0
        yalign 0.0
        padding (20, 20)
        margin (10, 10)
        background "#00000080"  # Fundo semi-transparente
        
        vbox:
            spacing 10
            text "Águas-vivas: [ag_pontos]" color "#FFFFFF" outlines [(2, "#000000", 0, 0)] size 30
            text "Tempo: ['{:.1f}'.format(ag_tempo_restante)]s" color "#FFFFFF" outlines [(2, "#000000", 0, 0)] size 30

# Tela principal do mini-jogo
screen ag_game_screen():
    # Tela do jogo
    if ag_jogo_ativo:
        # Mostra apenas as águas-vivas como botões
        for q in aguas_vivas:
            if q.visivel:
                imagebutton:
                    idle "jellyfish.png"  # Usa a imagem jellyfish.png
                    xpos q.x
                    ypos q.y
                    action Function(clicar_agua_viva, q.id)

# Ponto de entrada para o minigame
label minigame_aguasvivas:
    # Esconder tela xerequinha
    hide screen xerequinha
    
    # Vai para a tela de diálogo com o Patrick
    jump patrick_jellyfish_intro

# Patrick pergunta sobre a rede de caça
label patrick_jellyfish_intro:
    # Cena do Patrick com fundo de águas-vivas
    if renpy.has_image("jellos"):
        scene jellos
    else:
        scene bg_aguasvivas
        
    # Mostrar Patrick (assumindo que você tem uma imagem "pautrick")
    if renpy.has_image("pautrick"):
        show pautrick
    
    p "Ei, Bob Esponja! Vamos caçar algumas águas-vivas hoje?"
    
    # Se não é a primeira vez, oferece a opção de fazer geleia primeiro
    if jogou_minigame_antes and 21 in inventario and 8 in inventario:
        p "Hmm, vejo que você já tem algumas águas-vivas e potes. Quer fazer geleia antes de começarmos?"
        
        menu:
            "Fazer geleia primeiro":
                $ qnt_aguas_vivas = inventario.count(21)
                $ qnt_potes = inventario.count(8)
                $ max_possiveis = min(qnt_aguas_vivas, qnt_potes)
                
                p "Excelente ideia! Temos ingredientes para fazer [max_possiveis] pote(s) de geleia."
                p "Quantas geleias você quer fazer?"
                
                menu:
                    "Fazer uma geleia" if max_possiveis >= 1:
                        $ geleia_feita = fazer_geleia_de_aguas_vivas(1)
                        p "Perfeito! Fizemos [geleia_feita] pote de geleia deliciosa!"
                    
                    "Fazer três geleias" if max_possiveis >= 3:
                        $ geleia_feita = fazer_geleia_de_aguas_vivas(3)
                        p "Uau! Fizemos [geleia_feita] potes de geleia saborosa!"
                    
                    "Fazer todas as geleias possíveis" if max_possiveis >= 1:
                        $ geleia_feita = fazer_geleia_de_aguas_vivas(max_possiveis)
                        p "Incrível! Fizemos [geleia_feita] potes de geleia deliciosa!"
                    
                    "Melhor não fazer geleia agora":
                        p "Ok, vamos apenas caçar então!"
                
                p "Agora vamos à caçada!"
            
            "Vamos apenas caçar":
                p "Como quiser! Vamos caçar então!"
    
    p "Espera um pouco... você trouxe sua rede de caçar águas-vivas?"
    
    # Verifica se tem uma rede (item ID 7)
    if 7 in inventario:
        p "Ah, ótimo! Você tem uma rede. Vamos começar a caçada!"
        jump patrick_start_game
    else:
        p "Oh não! Você não tem uma rede de caça. Não podemos caçar águas-vivas assim."
        p "Vá até a loja do Sr. Siriguejo e compre uma rede. Volte quando estiver preparado!"
        
        # Volta para o jogo principal
        show screen xerequinha
        jump room4

# Patrick explica como jogar
label patrick_start_game:
    p "Ok, Bob Esponja! Vamos lá! Você tem 10 segundos para pegar o máximo de águas-vivas que conseguir."
    p "Basta clicar nelas quando aparecerem na tela. Está pronto?"
    
    menu:
        "Estou pronto!":
            p "Ótimo! Vamos começar!"
            jump start_jellyfish_game
            
        "Espera, preciso me preparar melhor...":
            p "Ok, volte quando estiver pronto para caçar águas-vivas!"
            show screen xerequinha
            jump room4

# Começa o jogo
label start_jellyfish_game:
    # Esconder Patrick
    if renpy.has_image("pautrick"):
        hide pautrick
    
    # Cena de fundo
    if renpy.has_image("jellos"):
        scene jellos
    else:
        scene bg_aguasvivas
    
    # Inicializar variáveis
    $ inicializar_aguas_vivas()
    
    # Mostrar telas do jogo
    show screen ag_game_screen
    show screen ag_game_info
    
    # Loop principal do jogo
    while ag_tempo_restante > 0 and ag_jogo_ativo:
        # Atualizar posição das águas-vivas
        $ atualizar_aguas_vivas()
        
        # Diminuir o tempo
        $ ag_tempo_restante -= 0.05
        
        # Pausa para controlar a velocidade
        $ renpy.pause(0.05, hard=True)
    
    # Finaliza o jogo
    $ ag_jogo_ativo = False
    
    # Esconde a tela de informações
    hide screen ag_game_info
    hide screen ag_game_screen
    
    # Vai para o diálogo final com o Patrick
    jump patrick_end_game

# Final do jogo
label patrick_end_game:
    # Marcar que o jogador já jogou pelo menos uma vez
    $ jogou_minigame_antes = True
    
    # Mostrar Patrick novamente
    if renpy.has_image("pautrick"):
        show pautrick
    
    if ag_pontos == 0:
        p "Uau, Bob Esponja, você não pegou nenhuma água-viva? Talvez seja melhor praticar mais um pouco."
        p "Vamos voltar para casa e tentar outro dia."
        
        show screen xerequinha
        jump room4
        
    elif ag_pontos < 5:
        p "Você pegou [ag_pontos] águas-vivas, Bob Esponja! Não está mal para um iniciante."
    else:
        p "UAU! Você pegou [ag_pontos] águas-vivas, Bob Esponja! Isso é incrível!"
    
    # Adicionando todas as águas-vivas ao inventário automaticamente
    $ adicionar_aguas_vivas_capturadas()
    p "Já guardei todas as águas-vivas que você capturou no seu inventário!"
    
    # Verifica se podemos fazer geleia
    $ pode_fazer_geleia = 8 in inventario
    
    if pode_fazer_geleia:
        p "Ei, Bob Esponja! Que tal fazermos um pouco de geleia de águas-vivas agora?"
        
        menu:
            "Fazer geleia":
                # Contagem de itens disponíveis
                $ qnt_aguas_vivas = inventario.count(21)
                $ qnt_potes = inventario.count(8)
                $ max_possiveis = min(qnt_aguas_vivas, qnt_potes)
                
                if max_possiveis <= 0:
                    p "Hmm, na verdade parece que não temos águas-vivas ou potes suficientes. Precisamos de pelo menos um de cada."
                    p "Vamos tentar novamente depois de pegar mais águas-vivas ou comprar mais potes."
                else:
                    p "Ótimo! Temos ingredientes para fazer [max_possiveis] pote(s) de geleia."
                    
                    # Menu para escolher quantidade
                    menu:
                        "Fazer uma geleia" if max_possiveis >= 1:
                            $ geleia_feita = fazer_geleia_de_aguas_vivas(1)
                            p "Perfeito! Fizemos [geleia_feita] pote de geleia deliciosa!"
                        
                        "Fazer três geleias" if max_possiveis >= 3:
                            $ geleia_feita = fazer_geleia_de_aguas_vivas(3)
                            p "Uau! Fizemos [geleia_feita] potes de geleia saborosa!"
                        
                        "Fazer todas as geleias possíveis" if max_possiveis >= 1:
                            $ geleia_feita = fazer_geleia_de_aguas_vivas(max_possiveis)
                            p "Incrível! Fizemos [geleia_feita] potes de geleia deliciosa!"
                        
                        "Melhor não fazer geleia agora":
                            p "Tudo bem, podemos fazer geleia depois!"
            
            "Não quero fazer geleia agora":
                p "Sem problemas! Podemos fazer geleia em outro momento."
    
    p "O que você quer fazer agora?"
    
    menu:
        "Brincar com as águas-vivas um pouco":
            p "Ah, isso vai ser divertido, Bob Esponja!"
            
            scene jellos with dissolve
            
            if renpy.has_image("pautrick"):
                show pautrick
            
            p "Olha como elas são gelatinosas e bonitinhas!"
            p "Cuidado para não levar uma ferroada!"
            
            "Você e Patrick brincam com as águas-vivas por algum tempo."
            "É uma experiência divertida e você aprende mais sobre o comportamento delas."
            
            p "Foi divertido! Voltemos outra hora para brincar mais."
            
        "Vamos embora":
            p "Ok, Bob Esponja, vamos embora."
            p "Foi divertido, mas temos outras coisas para fazer!"
    
    p "Foi um ótimo dia de caça às águas-vivas! Vamos voltar para casa."
    
    # Limpa as telas
    $ limpar_telas_aguasvivas()
    
    # Volta para o jogo principal
    show screen xerequinha
    jump room4