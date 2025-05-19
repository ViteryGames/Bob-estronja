# sandyanim.rpy - Animações para cenas com Sandy (modificado)
image sandy_peitos:
    "images/sandy_peitos.png"
    zoom 1.0
    xalign 0.5
    yalign 0.5
# Animações para punheta - Versão normal
image sandy_punheta_anim:
    "images/sandy_punheta_1.png"
    pause 0.4  # Ritmo normal
    "images/sandy_punheta_2.png"
    pause 0.4
    "images/sandy_punheta_3.png"
    pause 0.4
    repeat

# Animações para punheta - Versão rápida (clímax)
image sandy_punheta_anim_rapida:
    "images/sandy_punheta_1.png"
    pause 0.15  # Ritmo mais rápido
    "images/sandy_punheta_2.png"
    pause 0.15
    "images/sandy_punheta_3.png"
    pause 0.15
    repeat

# Animações para boquete - Versão normal
image sandy_boquete_anim:
    "images/sandy_boquete_1.png"
    pause 0.35
    "images/sandy_boquete_2.png"
    pause 0.35
    "images/sandy_boquete_3.png"
    pause 0.35
    repeat

# Animações para boquete - Versão rápida (clímax)
image sandy_boquete_anim_rapida:
    "images/sandy_boquete_1.png"
    pause 0.15
    "images/sandy_boquete_2.png"
    pause 0.15
    "images/sandy_boquete_3.png"
    pause 0.15
    repeat

# Animações para buceta - Versão normal
image sandy_buceta_anim:
    "images/sandy_buceta_1.png"
    pause 0.4
    "images/sandy_buceta_2.png"
    pause 0.4
    "images/sandy_buceta_3.png"
    pause 0.4
    repeat

# Animações para buceta - Versão rápida (clímax)
image sandy_buceta_anim_rapida:
    "images/sandy_buceta_1.png"
    pause 0.2
    "images/sandy_buceta_2.png"
    pause 0.2
    "images/sandy_buceta_3.png"
    pause 0.2
    repeat

# Animações para cuzinho - Versão normal
image sandy_cuzinho_anim:
    "images/sandy_cuzinho_1.png"
    pause 0.4
    "images/sandy_cuzinho_2.png"
    pause 0.4
    "images/sandy_cuzinho_3.png"
    pause 0.4
    repeat

# Animações para cuzinho - Versão rápida (clímax)
image sandy_cuzinho_anim_rapida:
    "images/sandy_cuzinho_1.png"
    pause 0.18
    "images/sandy_cuzinho_2.png"
    pause 0.18
    "images/sandy_cuzinho_3.png"
    pause 0.18
    repeat

# Animações para nozes no cuzinho - Versão normal
image nozes_cuzinho_anim:
    "images/nozes_cuzinho_1.png"
    pause 0.5
    "images/nozes_cuzinho_2.png"
    pause 0.5
    "images/nozes_cuzinho_3.png"
    pause 0.5
    repeat

# Animações para nozes no cuzinho - Versão rápida (clímax)
image nozes_cuzinho_anim_rapida:
    "images/nozes_cuzinho_1.png"
    pause 0.25
    "images/nozes_cuzinho_2.png"
    pause 0.25
    "images/nozes_cuzinho_3.png"
    pause 0.25
    repeat

# As animações de gozada permanecem iguais

# Ver os peitos da Sandy (nível 1+)
# sandyfucks.rpy - Arquivo contendo os labels de conteúdo sexual com Sandy

# Som para as gozadas
define audio.gozada = "audio/porra.mp3"

# Ver os peitos da Sandy (nível 1+)
# Ver os peitos da Sandy (nível 1+)
# Ver os peitos da Sandy (nível 1+)
# Ver os peitos da Sandy (nível 1+)
label ver_peitos_sandy:
    # Verificar se já viu 3 vezes - se sim, mostrar submenu
    if vezes_mostrou_peitos >= 3:
        menu:
            "Como você quer ver os peitos dela?"
            
            "Ver rapidamente":
                # Verificar se já realizou ação sexual hoje
                if ultimo_dia_acao_sexual == dia:
                    show sandy seducao at center
                    $ dialogo = obter_dialogo_recusa()
                    sd "[dialogo]"
                    jump mostrar_menu_sandy
                else:
                    jump ver_peitos_rapido
                
            "Ver de perto (sequência especial)":
                # Verificar se já realizou ação sexual hoje
                if ultimo_dia_acao_sexual == dia:
                    show sandy seducao at center
                    $ dialogo = obter_dialogo_recusa()
                    sd "[dialogo]"
                    jump mostrar_menu_sandy
                else:
                    jump ver_peitos_zoom
    
    # Verificar se já realizou ação sexual hoje
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    # Sequência normal para as primeiras vezes
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_mostrou_peitos, 2)
    $ sequencia = obter_sequencia_peitos(indice)
    
    show sandy envergonhada at center
    
    # Primeiro diálogo (antes de mostrar os peitos) - apenas 2 linhas
    $ i = 0
    while i < 2 and i < len(sequencia):
        $ item = sequencia[i]
        
        # Verificar se o item é uma lista aninhada (caso das variações da 3ª vez)
        if isinstance(item, list) and len(item) > 0 and isinstance(item[0], list):
            # Se for uma lista de variações, escolhe a primeira variação
            $ item = item[0]
        
        # Agora processar normalmente
        if isinstance(item, list) and len(item) >= 2:
            $ quem_fala = item[0]
            $ texto = item[1]
        else:
            $ quem_fala = "sd"
            $ texto = str(item)
        
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Esconder Sandy com roupas
    hide sandy envergonhada
    
    # MOSTRAR OS PEITOS - Direto e simples
    show sandynua:
        zoom 0.55
        xalign 0.48
        yalign 0.8
    
    # Pausa suficiente para ver a imagem
    pause 2.0
    
    # Resto do diálogo (depois de mostrar os peitos)
    while i < len(sequencia):
        $ item = sequencia[i]
        
        # Verificar se o item é uma lista aninhada (caso das variações da 3ª vez)
        if isinstance(item, list) and len(item) > 0 and isinstance(item[0], list):
            # Se for uma lista de variações, escolhe a primeira variação
            $ item = item[0]
        
        # Agora processar normalmente
        if isinstance(item, list) and len(item) >= 2:
            $ quem_fala = item[0]
            $ texto = item[1]
        else:
            $ quem_fala = "sd"
            $ texto = str(item)
        
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Esconder a imagem dos peitos quando terminar o diálogo
    hide sandynua
    
    # Voltar para Sandy vestida
    show sandy satisfeita at center
    
    $ vezes_mostrou_peitos += 1
    $ hora_do_dia += 2
    
    # Bonus de pontos apenas na terceira vez
    if vezes_mostrou_peitos == 3:
        "Você já viu os peitos da Sandy 3 vezes! Ela está muito mais confortável com você agora."
        $ pontos_interesse_sandy += 20
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Ver os peitos rapidamente (após 3 vezes)
label ver_peitos_rapido:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    show sandy seducao at center
    sd "Quer ver meus peitos de novo? Aqui está um rápido vislumbre..."
    
    # Esconder Sandy vestida
    hide sandy seducao
    
    # MOSTRAR OS PEITOS - Direto e simples
    show sandynua:
        zoom 0.55
        xalign 0.48
        yalign 0.8
    
    # Pausa para ver a imagem
    pause 2.0

    # Esconder peitos
    hide sandynua
    
    # Voltar à cena normal
    scene bg casa_sandy with dissolve
    show sandy satisfeita at center
    
    sd "Gostou da visão rápida?"
    
    $ hora_do_dia += 2
    jump finalizar_sandy  # Vai para o final da interação
# Ver os peitos com zoom (sequência especial após 3 vezes)
label ver_peitos_zoom:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    show sandy seducao at center
    sd "Quer ver meus peitos de novo, né? Sei que você adora..."
    sd "Vou mostrar pra você. Afinal, já estamos bem íntimos..."
    
    # Sequência de zoom dos pés aos peitos
    scene black
    "A câmera se aproxima lentamente de Sandy..."
    
    # Mostrar imagens em sequência - dos pés até os peitos
    scene sandy_pes with dissolve
    pause 1.0
    scene sandy_pernas with dissolve
    pause 1.0
    scene sandy_barriga with dissolve
    pause 1.0
    
    # Finalmente mostrar os peitos - DIRETO E SIMPLES
    show sandybb
    
    # Pausa para apreciar a imagem
    pause 2.0
    
    # Pausa para que o jogador veja os peitos completamente
    "Sandy mostra seus peitos para você. Clique para continuar."
    
    # Retornar à cena normal
    scene bg casa_sandy
    show sandy satisfeita at center
    
    $ hora_do_dia += 2
    jump finalizar_sandy  # Vai para o final da interaçãoação

# Ver a buceta da Sandy (nível 5+ e após 3 punhetas)
label ver_buceta_sandy:
    # Verificar se já viu 3 vezes - se sim, mostrar submenu
    if vezes_mostrou_buceta >= 3:
        menu:
            "Como você quer ver a buceta dela?"
            
            "Ver rapidamente":
                # Verificar se já realizou ação sexual hoje
                if ultimo_dia_acao_sexual == dia:
                    show sandy seducao at center
                    $ dialogo = obter_dialogo_recusa()
                    sd "[dialogo]"
                    jump mostrar_menu_sandy
                else:
                    jump ver_buceta_rapido
                
            "Ver de perto (sequência especial)":
                # Verificar se já realizou ação sexual hoje
                if ultimo_dia_acao_sexual == dia:
                    show sandy seducao at center
                    $ dialogo = obter_dialogo_recusa()
                    sd "[dialogo]"
                    jump mostrar_menu_sandy
                else:
                    jump ver_buceta_zoom
    
    # Verificar se já realizou ação sexual hoje
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    # Mostrar diálogo aleatório antes da sequência principal
    $ dialogo = obter_dialogo_buceta()
    $ quem_fala, texto = dialogo
    if quem_fala == "sd":
        sd "[texto]"
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_mostrou_buceta, 2)
    $ sequencia = obter_sequencia_buceta(indice)
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos até o penúltimo (antes do orgasmo)
    $ i = 0
    while i < len(sequencia) - 2:  # -2 para parar antes do orgasmo
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Opção de gozar enquanto vê
    menu:
        "O que você quer fazer?"
        
        "Se masturbar olhando":
            bob "Vou gozar olhando pra você!"
            sd "Vai, Bob! Goza olhando pra minha bucetinha!"
            "Você se masturba furiosamente enquanto admira a Sandy."
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Toma isso, Sandy! Isso mesmo!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você continua se masturbando, liberando mais jatos."
            
            sd "Nossa, quanto leite! Você realmente gostou do que viu, hein?"
            
        "Pedir para ela se masturbar":
            bob "Quero ver você se tocando."
            sd "Assim? Você gosta quando eu me toco?"
            "Sandy começa a se masturbar para você, gemendo alto."
            
            # Primeira gozada com shake
            with hpunch
            "Sandy se contorce de prazer."
            sd "Estou quase lá!"
            
            # Segunda gozada com shake
            with hpunch
            "Seus gemidos ficam mais intensos."
            
            # Completar com os últimos diálogos
            $ i = len(sequencia) - 2
            while i < len(sequencia):
                $ quem_fala, texto = sequencia[i]
                if quem_fala == "sd":
                    sd "[texto]"
                elif quem_fala == "bob":
                    bob "[texto]"
                else:
                    "[texto]"
                $ i += 1

    $ hora_do_dia += 2

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

# Ver a buceta rapidamente (após 3 vezes)
label ver_buceta_rapido:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    show sandy seducao at center
    sd "Quer ver minha buceta de novo? Aqui está um rápido vislumbre..."
    
    scene sandy_buceta_rapido with dissolve
    pause 1.5
    
    scene bg casa_sandy with dissolve
    show sandy satisfeita at center
    
    sd "Gostou da visão rápida?"
    
    # Opção de gozar enquanto vê
    menu:
        "O que você quer fazer?"
        
        "Se masturbar olhando":
            bob "Vou gozar olhando pra você!"
            sd "Vai, Bob! Goza olhando pra minha bucetinha!"
            "Você se masturba furiosamente enquanto admira a Sandy."
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Ahhh! Que delícia!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você continua gozando, seu corpo tremendo."
            
            sd "Nossa, quanto leite! Você realmente gostou do que viu, hein?"
            
        "Não fazer nada":
            "Você apenas aprecia a visão por um momento."
    
    $ hora_do_dia += 2
    jump finalizar_sandy  # Vai para o final da interação

# Ver a buceta com zoom (sequência especial após 3 vezes)
label ver_buceta_zoom:
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    show sandy seducao at center
    sd "Quer ver minha buceta de perto? Acho que já estamos íntimos o suficiente..."
    
    # Sequência de zoom
    scene black
    "A câmera se aproxima lentamente de Sandy..."
    
    # Mostrar imagens em sequência
    scene sandy_pes with dissolve
    pause 1.0
    scene sandy_pernas with dissolve
    pause 1.0
    scene sandy_coxas with dissolve
    pause 1.0
    scene sandy_buceta with dissolve
    pause 1.0
    
    # Pausa para que o jogador veja a buceta completamente
    "Sandy mostra sua intimidade para você. Clique para continuar."
    
    # Opção de gozar enquanto vê
    menu:
        "O que você quer fazer?"
        
        "Se masturbar olhando":
            bob "Vou gozar olhando pra você!"
            sd "Vai, Bob! Goza olhando pra minha bucetinha!"
            "Você se masturba furiosamente enquanto admira a Sandy."
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Toma isso, Sandy! É tudo pra você!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "O prazer é tão intenso que você mal consegue ficar em pé."
            
            sd "Nossa, quanto leite! Você realmente gostou do que viu, hein?"
            
        "Pedir para ela se masturbar":
            bob "Quero ver você se tocando."
            sd "Assim? Você gosta quando eu me toco?"
            "Sandy começa a se masturbar para você, gemendo alto."
            
            scene sandy_buceta_masturbando with dissolve
            pause 1.0
            
            # Primeira gozada com shake
            with hpunch
            "Sandy começa a se tocar mais rapidamente."
            
            # Segunda gozada com shake
            with hpunch
            "Seus gemidos se intensificam enquanto ela se aproxima do orgasmo."
            
            # Terceira gozada com shake
            with hpunch
            sd "Ahh! Estou... gozando!"
            "O corpo de Sandy treme enquanto ela atinge o orgasmo."
    
    # Retornar à cena normal
    scene bg casa_sandy
    show sandy satisfeita at center
    
    $ hora_do_dia += 2
    jump finalizar_sandy  # Vai para o final da interação

# Pedir uma punheta (nível 3+)
label punheta_sandy:
    # Verificar se já realizou ação sexual hoje
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_punheta, 2)
    $ sequencia = obter_sequencia_punheta(indice)
    
    # Iniciar com a animação imediatamente
    scene bg casa_sandy
    show sandy_punheta_anim
    
    # Mostrar diálogos enquanto a animação está no ritmo normal
    $ i = 0
    while i < 5:  # Primeiros 5 diálogos
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Mudar para ritmo mais rápido e continuar diálogos
    hide sandy_punheta_anim
    show sandy_punheta_anim_rapida
    
    # Continuar os diálogos com ritmo mais rápido
    while i < len(sequencia) - 2:  # -2 para parar antes do clímax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Opção de gozar
    menu:
        "Onde você quer gozar?"
        
        "Gozar na mão dela":
            bob "Vou gozar na sua mão, Sandy!"
            
            # Esconder a animação de punheta
            hide sandy_punheta_anim_rapida
            
            # Mostrar animação de gozada na mão
            show gozada_peitos_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Isso mesmo, Sandy! Continua!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Sandy continua masturbando você enquanto o gozo escorre por seus dedos."
            
            # Esconder a animação de gozada
            hide gozada_peitos_anim
            
        "Gozar no rosto dela":
            bob "Vou gozar na sua cara!"
            sd "O quê? Espera, eu não est--"
            
            # Esconder a animação de punheta
            hide sandy_punheta_anim_rapida
            
            # Mostrar animação de gozada no rosto
            show gozada_rosto_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Toma isso na cara, Sandy!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "O primeiro jato atinge o rosto dela em cheio."
            
            # Esconder a animação de gozada
            hide gozada_rosto_anim
    
    # Mostrar Sandy satisfeita
    show sandy satisfeita at center
    
    sd "Uau, quanto leite! Você realmente gostou, hein?"

    $ vezes_punheta += 1
    $ hora_do_dia += 2

    if vezes_punheta == 3:
        "Sandy já te deu 3 punhetas! Ela está muito mais confortável com intimidades agora."
        $ pontos_interesse_sandy += 15
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Boquete (nível 7)
label boquete_sandy:
    # Verificar se já realizou ação sexual hoje
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_boquete, 2)
    $ sequencia = obter_sequencia_boquete(indice)
    
    # Iniciar com a animação imediatamente
    scene bg casa_sandy
    show sandy_boquete_anim
    
    # Mostrar diálogos enquanto a animação está no ritmo normal
    $ i = 0
    while i < 5:  # Primeiros 5 diálogos
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Mudar para ritmo mais rápido e continuar diálogos
    hide sandy_boquete_anim
    show sandy_boquete_anim_rapida
    
    # Continuar os diálogos com ritmo mais rápido
    while i < len(sequencia) - 2:  # -2 para parar antes do clímax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Opção de gozar
    menu:
        "Onde você quer gozar?"
        
        "Gozar na boca":
            bob "Vou gozar na sua boca, engole tudo!"
            
            # Esconder a animação de boquete
            hide sandy_boquete_anim_rapida
            
            # Mostrar animação de gozada na boca
            show gozada_boca_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Isso mesmo! Engole tudo!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você segura a cabeça dela enquanto continua gozando."
            
            # Esconder a animação de gozada
            hide gozada_boca_anim
            
        "Gozar no rosto":
            bob "Vou gozar na sua cara!"
            
            # Esconder a animação de boquete
            hide sandy_boquete_anim_rapida
            
            # Mostrar animação de gozada no rosto
            show gozada_rosto_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Toma na cara, Sandy!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você continua gozando enquanto ela fecha os olhos."
            
            # Esconder a animação de gozada
            hide gozada_rosto_anim
    
    # Mostrar Sandy satisfeita
    show sandy satisfeita at center
    
    sd "*Glup* *Glup* ... *Cof* *Cof*"
    sd "Uau... isso é... diferente do que eu esperava."

    $ hora_do_dia += 2
    $ vezes_boquete += 1
    
    if vezes_boquete == 3:
        "Sandy já te deu 3 boquetes! Ela está se tornando muito habilidosa nisso."
        $ pontos_interesse_sandy += 25
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Foder a bucetinha (nível 10)
label foder_buceta_sandy:
    # Verificar se já realizou ação sexual hoje
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_foder_buceta, 2)
    $ sequencia = obter_sequencia_foder_buceta(indice)
    
    # Iniciar com a animação imediatamente
    scene bg casa_sandy
    show sandy_buceta_anim
    
    # Mostrar diálogos enquanto a animação está no ritmo normal
    $ i = 0
    while i < 5:  # Primeiros 5 diálogos
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Mudar para ritmo mais rápido e continuar diálogos
    hide sandy_buceta_anim
    show sandy_buceta_anim_rapida
    
    # Continuar os diálogos com ritmo mais rápido
    while i < len(sequencia) - 2:  # -2 para parar antes do clímax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Opção de gozar
    menu:
        "Onde você quer gozar?"
        
        "Gozar dentro":
            bob "Vou gozar dentro de você!"
            sd "Sim! Me enche toda de porra!"
            
            # Esconder a animação de sexo
            hide sandy_buceta_anim_rapida
            
            # Mostrar animação de gozada dentro
            show gozada_buceta_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Toma dentro, Sandy! Tô gozando!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você continua metendo enquanto libera mais jatos dentro dela."
            
            # Esconder a animação de gozada
            hide gozada_buceta_anim
            
        "Gozar fora":
            bob "Vou gozar fora!"
            
            # Esconder a animação de sexo
            hide sandy_buceta_anim_rapida
            
            # Mostrar animação de gozada fora
            show gozada_peitos_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Toma isso, Sandy! Tá saindo muito!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você continua se masturbando sobre a barriga dela."
            
            # Esconder a animação de gozada
            hide gozada_peitos_anim
    
    # Mostrar Sandy satisfeita
    show sandy satisfeita at center
    
    sd "Ahhh! Estou sentindo tudo dentro! É tão quente!"
    "Sandy fica completamente satisfeita."

    $ hora_do_dia += 2
    $ vezes_foder_buceta += 1
    
    if vezes_foder_buceta == 3:
        "Você já fodeu a buceta da Sandy 3 vezes! Vocês estão em perfeita sintonia."
        $ pontos_interesse_sandy += 35
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    $ pontos_interesse_sandy += 15
    $ atualizar_nivel_interesse()
    
    jump finalizar_sandy  # Vai para o final da interação

# Enfiar nozes no cuzinho (nível 15)
# Enfiar nozes no cuzinho (nível 15)
label nozes_cuzinho_sandy:
    # Verificar se já realizou ação sexual hoje
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    # Obter a sequência de diálogos conforme vez
    $ indice = min(vezes_nozes_cuzinho, 0)
    $ sequencia = obter_sequencia_nozes_cuzinho(indice)
    
    # Iniciar com a animação imediatamente
    scene bg casa_sandy
    show nozes_cuzinho_anim
    
    # Mostrar diálogos enquanto a animação está no ritmo normal
    $ i = 0
    while i < 5:  # Primeiros 5 diálogos
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Mudar para ritmo mais rápido e continuar diálogos
    hide nozes_cuzinho_anim
    show nozes_cuzinho_anim_rapida
    
    # Continuar os diálogos com ritmo mais rápido
    while i < len(sequencia) - 2:  # -2 para parar antes do clímax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Opções para o clímax
    menu:
        "O que você quer fazer?"
        
        "Gozar enquanto ela tem o orgasmo":
            "Você se masturba furiosamente enquanto insere as nozes."
            
            # Esconder a animação de nozes
            hide nozes_cuzinho_anim_rapida
            
            # Mostrar animação de gozada
            show gozada_peitos_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Isso, Sandy! Goza com essas nozes no rabo!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você continua se masturbando enquanto observa as nozes entrando nela."
            
            # Completar com os últimos diálogos
            $ i = len(sequencia) - 2
            while i < len(sequencia):
                $ quem_fala, texto = sequencia[i]
                if quem_fala == "sd":
                    sd "[texto]"
                elif quem_fala == "bob":
                    bob "[texto]"
                else:
                    "[texto]"
                $ i += 1
            
            # Esconder a animação de gozada
            hide gozada_peitos_anim
            
        "Gozar em cima das nozes inseridas":
            "Você se masturba e direciona para o cuzinho enquanto as nozes estão dentro."
            
            # Esconder a animação de nozes
            hide nozes_cuzinho_anim_rapida
            
            # Mostrar animação de gozada nas nozes
            show gozada_cuzinho_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Vou gozar em cima das nozes, Sandy!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "O primeiro jato cobre as nozes inseridas."
            
            sd "Uau! Você tá molhando todas as nozes!"
            "O líquido escorre entre as nozes inseridas no cuzinho da Sandy."
            
            # Esconder a animação de gozada
            hide gozada_cuzinho_anim
    
    # Mostrar Sandy satisfeita
    show sandy satisfeita at center
    
    $ hora_do_dia += 2
    $ vezes_nozes_cuzinho += 1
    
    # Remove uma noz do inventário
    $ inventario.remove(3)
    $ pontos_interesse_sandy += 20
    $ atualizar_nivel_interesse()
    
    if vezes_nozes_cuzinho == 1:
        "Sandy está explorando novos prazeres com você!"
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    jump finalizar_sandy  # Vai para o final da interação

# Comer o cuzinho da Sandy (nível 20)
label comer_cuzinho:
    # Verificar se já realizou ação sexual hoje
    if ultimo_dia_acao_sexual == dia:
        show sandy seducao at center
        $ dialogo = obter_dialogo_recusa()
        sd "[dialogo]"
        jump mostrar_menu_sandy
    
    # Marcar que uma ação sexual foi realizada hoje
    $ ultimo_dia_acao_sexual = dia
    
    # Obter a sequência de diálogos conforme progresso
    $ indice = min(vezes_cuzinho, 2)
    $ sequencia = obter_sequencia_cuzinho(indice)
    
    # Iniciar com a animação imediatamente
    scene bg casa_sandy
    show sandy_cuzinho_anim
    
    # Mostrar diálogos enquanto a animação está no ritmo normal
    $ i = 0
    while i < 5:  # Primeiros 5 diálogos
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Mudar para ritmo mais rápido e continuar diálogos
    hide sandy_cuzinho_anim
    show sandy_cuzinho_anim_rapida
    
    # Continuar os diálogos com ritmo mais rápido
    while i < len(sequencia) - 2:  # -2 para parar antes do clímax
        $ quem_fala, texto = sequencia[i]
        if quem_fala == "sd":
            sd "[texto]"
        elif quem_fala == "bob":
            bob "[texto]"
        else:
            "[texto]"
        $ i += 1
    
    # Opção de gozar
    menu:
        "Onde você quer gozar?"
        
        "Gozar dentro do cuzinho":
            bob "Vou encher seu cu de porra!"
            sd "SIM! GOZA DENTRO! INUNDA MEU CUZINHO!"
            
            # Esconder a animação de cuzinho
            hide sandy_cuzinho_anim_rapida
            
            # Mostrar animação de gozada dentro do cuzinho
            show gozada_cuzinho_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Toma no cuzinho, Sandy! Tá saindo muito!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "Você continua metendo enquanto solta mais jatos dentro dela."
            
            "Você bombeia jatos e mais jatos dentro do cuzinho da Sandy."
            sd "Ahhhh! Tá tão quente dentro de mim!"
            
            # Esconder a animação de gozada
            hide gozada_cuzinho_anim
            
        "Gozar na cara dela":
            bob "Quero gozar na sua cara!"
            "Você retira rapidamente e corre para o rosto dela."
            sd "O quê? Espera, acabou de sair do meu--"
            
            # Esconder a animação de cuzinho
            hide sandy_cuzinho_anim_rapida
            
            # Mostrar animação de gozada na cara
            show gozada_rosto_anim
            
            # Primeira gozada com shake e som
            with hpunch
            play sound audio.gozada
            b "Engole essa porra toda, Sandy!"
            
            # Segunda gozada com shake e som
            with hpunch
            play sound audio.gozada
            "O primeiro jato atinge o rosto dela em cheio."
            
            "Você explode violentamente na cara dela."
            sd "Ugh! Isso é nojento... mas até que gostei..."
            
            # Esconder a animação de gozada
            hide gozada_rosto_anim
    
    # Mostrar Sandy satisfeita
    show sandy satisfeita at center
    
    $ hora_do_dia += 2
    $ vezes_cuzinho += 1
    
    if vezes_cuzinho == 3:
        "Você já comeu o cuzinho da Sandy 3 vezes! Sua relação atingiu o nível máximo de intimidade."
        $ pontos_interesse_sandy += 30
        $ atualizar_nivel_interesse()
        "O nível de interesse da Sandy aumentou para [nivel_interesse_sandy]!"
    
    $ pontos_interesse_sandy += 15
    $ atualizar_nivel_interesse()
    
    jump finalizar_sandy  # Vai para o final da interação