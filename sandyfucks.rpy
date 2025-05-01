# sandyfucks.rpy - Arquivo contendo os labels de conteúdo sexual com Sandy

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
    
    scene sandy_peitos_rapido with dissolve
    pause 1.5
    
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
    scene sandy_peitos with dissolve
    pause 1.0
    
    # Pausa para que o jogador veja os peitos completamente
    "Sandy mostra seus peitos para você. Clique para continuar."
    
    # Retornar à cena normal
    scene bg casa_sandy
    show sandy satisfeita at center
    
    $ hora_do_dia += 2
    jump finalizar_sandy  # Vai para o final da interação

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
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Toma isso, Sandy! Isso mesmo!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua se masturbando, liberando mais jatos."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Caralho! Tô gozando muito!"
            
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
            
            # Terceira gozada com shake
            with hpunch
            sd "Ahh! Estou... gozando!"
            
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
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Ahhh! Que delícia!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua gozando, seu corpo tremendo."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Caralho, Sandy! Você me deixa louco!"
            
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
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Toma isso, Sandy! É tudo pra você!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "O prazer é tão intenso que você mal consegue ficar em pé."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Puta merda! Tô gozando demais!"
            
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
    
    # Opção de gozar dentro ou fora
    menu:
        "Onde você quer gozar?"
        
        "Gozar na mão dela":
            bob "Vou gozar na sua mão, Sandy!"
            $ i = len(sequencia) - 2  # Pegar os últimos dois diálogos
            while i < len(sequencia):
                $ quem_fala, texto = sequencia[i]
                if quem_fala == "sd":
                    sd "[texto]"
                elif quem_fala == "bob":
                    bob "[texto]"
                else:
                    "[texto]"
                $ i += 1
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Isso mesmo, Sandy! Continua!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Sandy continua masturbando você enquanto o gozo escorre por seus dedos."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Caralho! Ainda tá saindo mais!"
            
            sd "Uau! Você soltou bastante hoje!"
            
        "Gozar no rosto dela":
            bob "Vou gozar na sua cara!"
            sd "O quê? Espera, eu não est--"
            "Você direciona seu pau para o rosto dela e libera tudo."
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Toma isso na cara, Sandy!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "O primeiro jato atinge o rosto dela em cheio."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua gozando, cobrindo todo o rosto dela."
            
            sd "Ugh! Meus olhos! Avisa da próxima vez!"
            "Sandy limpa o rosto, um pouco irritada mas também intrigada."

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
    
    # Opção de gozar dentro ou fora
    menu:
        "Onde você quer gozar?"
        
        "Gozar na boca":
            bob "Vou gozar na sua boca, engole tudo!"
            "Sandy arregala os olhos mas continua chupando."
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Isso mesmo! Engole tudo!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você segura a cabeça dela enquanto continua gozando."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Puta que pariu! Tô gozando demais!"
            
            sd "*Glup* *Glup* ... *Cof* *Cof*"
            "Sandy tenta engolir tudo, mas um pouco escorre pelo canto da boca."
            sd "Uau... isso é... diferente do que eu esperava."
            
        "Gozar no rosto":
            bob "Vou gozar na sua cara!"
            "Você tira da boca dela e direciona para o rosto."
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Toma na cara, Sandy!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua gozando enquanto ela fecha os olhos."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Ainda não acabou! Toma mais!"
            
            sd "Aaah! Tá quente!"
            "O rosto de Sandy fica completamente coberto."
            sd "Nossa... quanto... nunca pensei que uma esponja pudesse produzir tanto líquido."

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
    
    # Opção de gozar dentro ou fora
    menu:
        "Onde você quer gozar?"
        
        "Gozar dentro":
            bob "Vou gozar dentro de você!"
            sd "Sim! Me enche toda de porra!"
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Toma dentro, Sandy! Tô gozando!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua metendo enquanto libera mais jatos dentro dela."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Caralho! Ainda tá saindo mais!"
            
            "Você sente seu orgasmo explodir dentro dela."
            sd "Ahhh! Estou sentindo tudo dentro! É tão quente!"
            
        "Gozar fora":
            bob "Vou gozar fora!"
            "Você retira rapidamente e goza sobre a barriga dela."
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Toma isso, Sandy! Tá saindo muito!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua se masturbando sobre a barriga dela."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Caralho! Olha quanto leite!"
            
            sd "Uau! Quanta porra! Tá me inundando toda!"
            "A barriga de Sandy fica completamente coberta pelo seu líquido."

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
    
    show sandy seducao at center
    
    # Mostrar a sequência de diálogos até o penúltimo (antes do clímax)
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
        
    # Opções para o clímax
    menu:
        "O que você quer fazer?"
        
        "Gozar enquanto ela tem o orgasmo":
            "Você se masturba furiosamente enquanto insere as nozes."
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Isso, Sandy! Goza com essas nozes no rabo!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua se masturbando enquanto observa as nozes entrando nela."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Caralho! Tô gozando muito vendo isso!"
            
            # Completar os diálogos finais
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
            
        "Gozar em cima das nozes inseridas":
            "Você se masturba e direciona para o cuzinho enquanto as nozes estão dentro."
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Vou gozar em cima das nozes, Sandy!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "O primeiro jato cobre as nozes inseridas."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Olha quanto leite tá saindo! Tô inundando seu rabo!"
            
            sd "Uau! Você tá molhando todas as nozes!"
            "O líquido escorre entre as nozes inseridas no cuzinho da Sandy."

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
    
    # Opção de gozar dentro ou fora
    menu:
        "Onde você quer gozar?"
        
        "Gozar dentro do cuzinho":
            bob "Vou encher seu cu de porra!"
            sd "SIM! GOZA DENTRO! INUNDA MEU CUZINHO!"
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Toma no cuzinho, Sandy! Tá saindo muito!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "Você continua metendo enquanto solta mais jatos dentro dela."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Caralho! Nunca gozei tanto assim!"
            
            "Você bombeia jatos e mais jatos dentro do cuzinho da Sandy."
            sd "Ahhhh! Tá tão quente dentro de mim!"
            
        "Gozar na cara dela":
            bob "Quero gozar na sua cara!"
            "Você retira rapidamente e corre para o rosto dela."
            sd "O quê? Espera, acabou de sair do meu--"
            
            # Primeira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Engole essa porra toda, Sandy!"
            
            # Segunda gozada com shake
            with hpunch
            play sound "porra.mp3"
            "O primeiro jato atinge o rosto dela em cheio."
            
            # Terceira gozada com shake
            with hpunch
            play sound "porra.mp3"
            b "Ainda não acabou! Toma mais leite!"
            
            "Você explode violentamente na cara dela."
            sd "Ugh! Isso é nojento... mas até que gostei..."
    
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