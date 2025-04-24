# sandy.rpy - Arquivo principal da Sandy
# Importa os diálogos e sequências do arquivo sandy_talks.rpy

# Define o personagem Sandy
define sd = Character("Sandy Bucetas", who_color="#ff69b4")
define bob = Character("Bob", who_color="#ffff00")

# Variáveis para rastrear o estado da Sandy
default sandy_tesao = False  # Inicialmente não está com tesão
default ja_visitou_sandy = False  # Rastreia se já visitou a Sandy antes
default pontos_interesse_sandy = 0  # Pontos de interesse da Sandy
default nivel_interesse_sandy = 0  # Nível de interesse da Sandy (baseado nos pontos)
default vezes_mostrou_peitos = 0  # Contador para as vezes que Sandy mostrou os peitos
default vezes_punheta = 0  # Contador para as vezes que Sandy deu uma punheta
default vezes_mostrou_buceta = 0  # Contador para as vezes que Sandy mostrou a buceta
default vezes_cuzinho = 0  # Contador para as vezes que o jogador comeu o cuzinho
default vezes_boquete = 0  # Contador para as vezes que Sandy deu um boquete
default vezes_foder_buceta = 0  # Contador para as vezes que o jogador fodeu a buceta
default vezes_nozes_cuzinho = 0  # Contador para as vezes que o jogador enfiou nozes no cuzinho
default ultimo_dia_acao_sexual = -1  # Guarda o valor da variável 'saida' quando uma ação sexual foi realizada

# Função para atualizar o nível de interesse com base nos pontos
init python:
    def atualizar_nivel_interesse():
        global pontos_interesse_sandy, nivel_interesse_sandy
        nivel_interesse_sandy = pontos_interesse_sandy // 5
        # Limita ao nível máximo 20
        if nivel_interesse_sandy > 20:
            nivel_interesse_sandy = 20

# Label para interagir com a Sandy
label sandy:
    if not ja_visitou_sandy:
        scene bg casa_sandy with dissolve
        "Você chega à casa da Sandy pela primeira vez."
        $ ja_visitou_sandy = True
    else:
        scene bg casa_sandy with dissolve
        "Você chega à casa da Sandy."

    show sandy normal at center
    
    sd "Oi, Bob Esponja! O que te traz aqui?"
    "Nível de interesse atual: [nivel_interesse_sandy]"
    
    jump mostrar_menu_sandy

# Menu da Sandy separado em seu próprio label
label mostrar_menu_sandy:
    menu:
        "O que você deseja fazer?"
        
        "Apenas conversar":
            jump conversar_sandy
            
        "Oferecer um presente":
            jump presentear_sandy
        
        # Ver peitos - Modificado para mostrar (3/3) quando maximizado
        "Ver os peitos dela ([min(vezes_mostrou_peitos, 3)]/3)" if nivel_interesse_sandy >= 1:
            if vezes_mostrou_peitos < 3 and ultimo_dia_acao_sexual == saida:
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump ver_peitos_sandy
            
        # Punheta - Sempre contagem limitada (não é exibicionista)
        "Pedir uma punheta ([min(vezes_punheta, 3)]/3)" if nivel_interesse_sandy >= 3:
            if ultimo_dia_acao_sexual == saida:
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump punheta_sandy
            
        # Ver buceta - Modificado para mostrar (3/3) quando maximizado
        "Ver a buceta dela ([min(vezes_mostrou_buceta, 3)]/3)" if nivel_interesse_sandy >= 5 and vezes_punheta >= 3:
            if vezes_mostrou_buceta < 3 and ultimo_dia_acao_sexual == saida:
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump ver_buceta_sandy
                
        # Boquete - nível 7 - Mantém restrição por dia
        "Receber um boquete ([min(vezes_boquete, 3)]/3)" if nivel_interesse_sandy >= 7:
            if ultimo_dia_acao_sexual == saida:
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump boquete_sandy
                
        # Foder a bucetinha - nível 10 - Mantém restrição por dia
        "Foder a bucetinha dela ([min(vezes_foder_buceta, 3)]/3)" if nivel_interesse_sandy >= 10:
            if ultimo_dia_acao_sexual == saida:
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump foder_buceta_sandy
        
        # Enfiar nozes no cuzinho - nível 15 e precisa ter o item nozes
        "Enfiar nozes no cuzinho dela" if nivel_interesse_sandy >= 15:
            if ultimo_dia_acao_sexual == saida:
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            elif 3 not in inventario:
                show sandy normal at center
                sd "Você precisa comprar nozes primeiro, seu bobinho!"
                jump mostrar_menu_sandy
            else:
                jump nozes_cuzinho_sandy
        
        # Comer o cuzinho - agora só aparece no nível 20 - Mantém restrição por dia
        "Comer o cuzinho dela ([min(vezes_cuzinho, 3)]/3)" if nivel_interesse_sandy >= 20:
            if ultimo_dia_acao_sexual == saida:
                show sandy seducao at center
                $ dialogo = obter_dialogo_recusa()
                sd "[dialogo]"
                jump mostrar_menu_sandy
            else:
                jump comer_cuzinho
            
        "Sair":
            jump sair_da_sandy

# Saída da casa da Sandy
label sair_da_sandy:
    sd "Já vai embora? Tudo bem, volte quando quiser!"
    
    scene black with dissolve
    "Você deixa a casa da Sandy..."
    
    jump room4  # Volta para a casa do Bob

# Conversa simples com a Sandy
label conversar_sandy:
    sd "Então, o que tem feito ultimamente?"
    
    menu:
        "Falar sobre o trabalho no Siri Cascudo":
            sd "Aquele velho Sirigueijo ainda te paga mal, né? Você deveria exigir um aumento!"
            
        "Falar sobre as aventuras com Patrick":
            sd "Vocês dois sempre se metem em cada encrenca! Mas devo admitir que é divertido."
            
        "Falar sobre ciência":
            $ sandy_tesao = True  # Sandy fica animada com conversa sobre ciência
            sd "Uau! Estou impressionada com seu interesse em ciência! Acabei de desenvolver um novo experimento..."
            "Sandy fala animadamente sobre seus experimentos por quase uma hora."
    
    jump finalizar_sandy  # Vai para o final da interação

# Oferecer presentes para a Sandy
label presentear_sandy:
    "Que presente você quer oferecer para a Sandy?"
    
    # Mostrar apenas os itens que o jogador possui
    $ itens_para_sandy = []
    $ nomes_itens = []
    
    # Verificar itens específicos
    if 5 in inventario:  # Torta de Algas
        $ itens_para_sandy.append(5)
        $ nomes_itens.append("Torta de Algas")
        
    if 6 in inventario:  # Torta de Nozes
        $ itens_para_sandy.append(6)
        $ nomes_itens.append("Torta de Nozes (Diretamente do Texas)")
        
    if 15 in inventario:  # Boneca Inflável
        $ itens_para_sandy.append(15)
        $ nomes_itens.append("Boneca Inflável")
    
    # Novos itens adicionados
    if 4 in inventario:  # Chave de Fenda
        $ itens_para_sandy.append(4)
        $ nomes_itens.append("Chave de Fenda")
        
    if 3 in inventario:  # Nozes
        $ itens_para_sandy.append(3)
        $ nomes_itens.append("Nozes")
        
    if 2 in inventario:  # Chocolate
        $ itens_para_sandy.append(2)
        $ nomes_itens.append("Chocolate")
        
    if 10 in inventario:  # Livros
        $ itens_para_sandy.append(10)
        $ nomes_itens.append("Livros")
    
    # Verificar se o jogador tem algum dos presentes específicos
    if len(itens_para_sandy) == 0:
        "Você não tem nenhum presente que possa interessar à Sandy."
        jump finalizar_sandy  # Vai para o final da interação
    
    # Criar um menu dinâmico com os presentes disponíveis
    $ result = renpy.display_menu([(nome, id_item) for nome, id_item in zip(nomes_itens, itens_para_sandy)] + [("Voltar", -1)])
    
    # Processar a escolha
    if result == -1:
        jump finalizar_sandy  # Vai para o final da interação
    elif result == 5:  # Torta de Algas
        show sandy irritada at center
        sd "Eh, obrigada Bob merda cabeça de bosta."
        "Sandy parece não ter gostado muito do presente..."
        $ pontos_interesse_sandy += 3  # Mesmo não gostando, aumenta 3 pontos
    elif result == 6:  # Torta de Nozes
        show sandy feliz at center
        sd "NOSSA BOB estronja amei essa porra!"
        "Sandy fica super animada com o presente do Texas!"
        $ pontos_interesse_sandy += 8  # Aumenta 8 pontos por ser do Texas
    elif result == 15:  # Boneca Inflável
        if sandy_tesao:
            show sandy seducao at center
            sd "Vamos brincar cowboy..."
            "Sandy puxa você para dentro da casa e fecha a porta."
            scene black
            "..."
            $ pontos_interesse_sandy += 8  # Aumenta 8 pontos se ela estiver com tesão
            scene bg casa_sandy
            show sandy satisfeita at center
        else:
            show sandy irritada at center
            sd "Enfia no teu rabo boiola viado escroto!"
            "Sandy chuta você para fora de sua casa."
            
    # Novos itens adicionados - Reações e pontos
    elif result == 4:  # Chave de Fenda
        show sandy feliz at center
        sd "Uma chave de fenda! Exatamente o que eu precisava para meus experimentos!"
        "Sandy parece muito feliz com o presente."
        $ pontos_interesse_sandy += 7  # Aumenta 7 pontos
        
    elif result == 3:  # Nozes
        show sandy normal at center
        sd "Hmm, nozes... Obrigada, Bob, vou guardar para mais tarde."
        "Sandy parece gostar do presente, mas não está muito animada."
        $ pontos_interesse_sandy += 2  # Aumenta 2 pontos
        
    elif result == 2:  # Chocolate
        show sandy normal at center
        sd "Chocolate? Bem, não é tão saudável, mas gosto de um docinho de vez em quando."
        "Sandy aceita o presente com um leve sorriso."
        $ pontos_interesse_sandy += 1  # Aumenta 1 ponto
        
    elif result == 10:  # Livros
        show sandy feliz at center
        sd "Livros! Adoro expandir meus conhecimentos, obrigada!"
        "Sandy parece bastante interessada nos livros."
        $ pontos_interesse_sandy += 3  # Aumenta 3 pontos
        $ sandy_tesao = True  # Livros também podem deixá-la animada com ciência
    
    # Remover o item do inventário após dar o presente
    if result != -1:
        $ inventario.remove(result)
        $ money += 5  # Pequena bonificação por dar um presente
        $ atualizar_nivel_interesse()  # Atualiza o nível de interesse com base nos pontos
    
    jump finalizar_sandy  # Vai para o final da interação

# Ver os peitos da Sandy (nível 1+) - MODIFICADO para uso ilimitado após 3 vezes
label ver_peitos_sandy:
    # Marcar que uma ação sexual foi realizada hoje (apenas se ainda não atingiu 3 vezes)
    if vezes_mostrou_peitos < 3:
        $ ultimo_dia_acao_sexual = saida
    
    # Obter a sequência de diálogos conforme progresso
    # Modificação: use o mínimo entre vezes_mostrou_peitos e 2 para manter o máximo em 3
    $ indice = min(vezes_mostrou_peitos, 2)
    $ sequencia = obter_sequencia_peitos(indice)
    
    show sandy envergonhada at center
    
    # Mostrar a sequência de diálogos
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Incrementa o contador apenas se ainda não atingiu 3
    if vezes_mostrou_peitos < 3:    
        $ vezes_mostrou_peitos += 1
        
        # Bonus de pontos apenas na terceira vez
        if vezes_mostrou_peitos == 3:
            "Você já viu os peitos da Sandy 3 vezes! Ela está muito mais confortável com você agora."
            $ pontos_interesse_sandy += 20
            $ atualizar_nivel_interesse()
            "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Pedir uma punheta (nível 3+) - Mantém restrição por dia
label punheta_sandy:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = saida
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_punheta, 2)
    $ sequencia = obter_sequencia_punheta(indice)
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    $ vezes_punheta += 1
    
    if vezes_punheta == 3:
        "Sandy já te deu 3 punhetas! Ela está muito mais confortável com intimidades agora."
        $ pontos_interesse_sandy += 15
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Ver a buceta da Sandy (nível 5+ e após 3 punhetas) - MODIFICADO para uso ilimitado após 3 vezes
label ver_buceta_sandy:
    # Marcar que uma ação sexual foi realizada hoje (apenas se ainda não atingiu 3 vezes)
    if vezes_mostrou_buceta < 3:
        $ ultimo_dia_acao_sexual = saida
    
    # Obter a sequência de diálogos conforme progresso
    # Modificação: use o mínimo entre vezes_mostrou_buceta e 2 para manter o máximo em 3
    $ indice = min(vezes_mostrou_buceta, 2)
    $ sequencia = obter_sequencia_buceta(indice)
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Incrementa o contador apenas se ainda não atingiu 3
    if vezes_mostrou_buceta < 3:    
        $ vezes_mostrou_buceta += 1
        
        # Bonus de pontos apenas na terceira vez
        if vezes_mostrou_buceta == 3:
            "Você já viu a buceta da Sandy 3 vezes! Seu relacionamento com ela está cada vez mais íntimo."
            $ pontos_interesse_sandy += 25
            $ atualizar_nivel_interesse()
            "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Boquete (nível 7) - Mantém restrição por dia
label boquete_sandy:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = saida
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_boquete, 2)
    $ sequencia = obter_sequencia_boquete(indice)
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    $ vezes_boquete += 1
    
    if vezes_boquete == 3:
        "Sandy já te deu 3 boquetes! Ela está se tornando muito habilidosa nisso."
        $ pontos_interesse_sandy += 25
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Foder a bucetinha (nível 10) - Mantém restrição por dia
label foder_buceta_sandy:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = saida
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_foder_buceta, 2)
    $ sequencia = obter_sequencia_foder_buceta(indice)
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    $ vezes_foder_buceta += 1
    
    if vezes_foder_buceta == 3:
        "Você já fodeu a buceta da Sandy 3 vezes! Vocês estão em perfeita sintonia."
        $ pontos_interesse_sandy += 35
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    $ pontos_interesse_sandy += 15
    $ atualizar_nivel_interesse()
    
    jump finalizar_sandy  # Vai para o final da interação

# Enfiar nozes no cuzinho (nível 15) - Mantém restrição por dia
label nozes_cuzinho_sandy:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = saida
    
    # Obter a sequência de diálogos conforme vez
    $ indice = min(vezes_nozes_cuzinho, 2)
    $ sequencia = obter_sequencia_nozes_cuzinho(indice)
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    $ vezes_nozes_cuzinho += 1
    
    # Remove uma noz do inventário
    $ inventario.remove(3)
    $ pontos_interesse_sandy += 20
    $ atualizar_nivel_interesse()
    
    if vezes_nozes_cuzinho == 1:
        "Sandy está explorando novos prazeres com você!"
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Comer o cuzinho da Sandy (nível 20) - Mantém restrição por dia
label comer_cuzinho:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = saida
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_cuzinho, 2)
    $ sequencia = obter_sequencia_cuzinho(indice)
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos
    $ i = 0
    while i < len(sequencia):
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    $ vezes_cuzinho += 1
    
    if vezes_cuzinho == 3:
        "Você já comeu o cuzinho da Sandy 3 vezes! Sua relação atingiu o nível máximo de intimidade."
        $ pontos_interesse_sandy += 30
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    $ pontos_interesse_sandy += 15
    $ atualizar_nivel_interesse()
    
    jump finalizar_sandy  # Vai para o final da interação

# Finalizar a interação com a Sandy
label finalizar_sandy:
    if not ja_visitou_sandy:
        scene room2
        menu:
            "Ir para o siri cascudo seu boiola safado":
                $ ja_visitou_sandy = True
                jump start
    
    jump mostrar_menu_sandy  # Retorna ao menu principal da Sandy