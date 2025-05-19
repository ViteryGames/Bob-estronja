# comcumbina.rpy - Corrigido com animações específicas e Sally no tamanho certo

# Definição da imagem Sally com tamanho correto (mesmo da Sandy)
image puta sally:
    "images/puta sally.png"
    zoom 0.75  # Mesmo zoom que a Sandy usa
    xalign 0.8
    yalign 0.9

# Definição das animações no início do arquivo
image keket_sally_anim:
    "keket sfull 1"
    pause 0.4
    "keket sfull 2"
    pause 0.4
    "keket sfull 3"
    pause 0.4
    repeat

# Versão rápida da animação para o clímax
image keket_sally_anim_rapida:
    "keket sfull 1"
    pause 0.2
    "keket sfull 2"
    pause 0.2
    "keket sfull 3"
    pause 0.2
    repeat

# Animação para sexo vaginal
image vagina_sally_anim:
    "vagina sally 1"
    pause 0.4
    "vagina sally 2"
    pause 0.4
    "vagina sally 3"
    pause 0.4
    repeat

# Versão rápida da animação para sexo vaginal
image vagina_sally_anim_rapida:
    "vagina sally 1"
    pause 0.2
    "vagina sally 2"
    pause 0.2
    "vagina sally 3"
    pause 0.2
    repeat

# Animação para sexo anal
image cuzin_sally_anim:
    "cuzin sally 1"
    pause 0.4
    "cuzin sally 2"
    pause 0.4
    "cuzin sally 3"
    pause 0.4
    repeat

# Versão rápida da animação para sexo anal
image cuzin_sally_anim_rapida:
    "cuzin sally 1"
    pause 0.2
    "cuzin sally 2"
    pause 0.2
    "cuzin sally 3"
    pause 0.2
    repeat

# ANIMAÇÕES DE GOZADA ESPECÍFICAS (2 frames cada)

# Animação para gozada do boquete 
image gozada_boquete_anim:
    "gozada boquete 1"
    pause 0.3
    "gozada boquete 2"
    pause 0.3
    repeat

# Animação para gozada vaginal
image gozada_vagina_anim:
    "gozada vagina 1"
    pause 0.3
    "gozada vagina 2"
    pause 0.3
    repeat

# Animação para gozada anal
image gozada_anal_anim:
    "gozada anal 1"
    pause 0.3
    "gozada anal 2"
    pause 0.3
    repeat

# IMAGENS FINAIS APÓS GOZADA (Sally gozada em cada cenário)
image sally_gozada_boquete = "images/sally_gozada_boquete.png"
image sally_gozada_vagina = "images/sally_gozada_vagina.png" 
image sally_gozada_anal = "images/sally_gozada_anal.png"

# Definição dos sons para cada ação sexual
define audio.boquete_som = "audio/boquete.mp3"
define audio.vagina_som = "audio/vagina.mp3"
define audio.anal_som = "audio/anal.mp3"
define audio.gozada_som = "audio/porra.mp3"

# Variável para controlar se é a primeira vez
default primeira_vez_puta = True

label comcumbinas:
    # Verifica se a variável 'visitou_puta' para o dia atual já existe
    # Se não existir, cria com valor False
    if not hasattr(store, "visitou_puta_dia_{}".format(saida)):
        $ setattr(store, "visitou_puta_dia_{}".format(saida), False)
    
    # Obtém o valor da variável para o dia atual
    $ visitou_hoje = getattr(store, "visitou_puta_dia_{}".format(saida))
    
    # Verifica se já visitou hoje
    if visitou_hoje:
        "Não tem ninguém lá fora."
        jump quanaite
    else:
        scene quartobob noite

        # Animação de entrada da Sally na primeira vez
        if primeira_vez_puta:
            # Sally entra pelo lado direito da tela
            show puta sally:
                xalign 1.2  # Começa fora da tela (lado direito)
                yalign 0.5
            
            # Animação de movimento para o centro
            show puta sally:
                linear 1.5 xalign 0.9
            
            $ primeira_vez_puta = False
        else:
            # Nas próximas vezes, apenas mostra no centro
            show puta sally at center

        "Sou piranha"
        jump sou_puta

label sou_puta:
    menu:
        "Boquete $15":
            if money >= 15:
                $ escolha = "quequet"
                $ money -= 15
                jump putitas
            else:
                "Você não possui moedas suficientes. São necessárias 15 moedas."
                jump sou_puta
                
        "Vagina $30":
            # Verificar se possui camisinha E dinheiro suficiente
            if money >= 30 and 14 in inventario:
                $ escolha = "pussy"
                $ money -= 30
                $ inventario.remove(14)  # Remove a camisinha do inventário
                jump putitas
            elif money < 30:
                "Você não possui moedas suficientes. São necessárias 30 moedas."
                jump sou_puta
            else:
                "Você precisa ter uma camisinha para esta opção. Compre uma na loja primeiro."
                jump sou_puta
                
        "Cuzin $60":
            # Verificar se possui camisinha E dinheiro suficiente
            if money >= 60 and 14 in inventario:
                $ escolha = "cuzin"
                $ money -= 60
                $ inventario.remove(14)  # Remove a camisinha do inventário
                jump putitas
            elif money < 60:
                "Você não possui moedas suficientes. São necessárias 60 moedas."
                jump sou_puta
            else:
                "Você precisa ter uma camisinha para esta opção. Compre uma na loja primeiro."
                jump sou_puta
        
        "Conversar (Grátis)":
            $ escolha = "conversar"
            jump putitas

label putitas:
    if escolha == "quequet":
        hide puta sally
        # Iniciar com a animação imediatamente e o som
        play sound audio.boquete_som loop
        show keket_sally_anim
        
        # Primeiras 5 falas com velocidade normal
        "Puta" "Vou te chupar bem gostoso agora seu safado"
        "Puta" "Hmm, nunca chupei uma esponja antes... você tem um gosto único!"
        b "Cala a boca e chupa logo, porra! Não paguei pra ficar ouvindo merda."
        "Puta" "Caralho, quanta agressividade! "
        b "Não me compare com essa merda de TV. Chupa logo antes que eu perca a paciência!"
        
        # Mudar para animação mais rápida após 5 falas
        hide keket_sally_anim
        show keket_sally_anim_rapida
        
        "Puta" "Tá bom, tá bom... Vou usar minha língua de um jeito especial..."
        b "Aí sim, cadela! Assim que eu gosto... Puta que pariu, que boquinha gostosa!"
        "Puta" "Você está gostando? Nunca imaginei que o Bob Esperma fosse tão... intenso."
        
        # Gozada simplificada para boquete
        b "Vou gozar, porra! Se prepara!"
        
        # Parar o som de boquete
        stop sound
        
        # Esconder a animação de boquete
        hide keket_sally_anim_rapida
        
        # Mostrar animação específica de gozada do boquete
        show gozada_boquete_anim
        
        # Primeira gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        b "Toma tudo, sua vadia!"
        
        # Segunda gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        b "Continua chupando! Ainda não acabei, cacete!"
        
        # Terceira gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        "Puta Piranha" "Uau! Nunca vi tanto... como você consegue produzir tanto?"
        
        # Esconder a animação de gozada
        hide gozada_boquete_anim
        
        # Mostrar imagem final da Sally gozada
        show sally_gozada_boquete at center
        pause 2.0
        
        "Puta Piranha" "Que gosto diferente... nunca provei nada parecido!"
        
        menu:
            "Voltar para o quarto":
                hide sally_gozada_boquete
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite
        
    elif escolha == "pussy":
        # Iniciar com a animação imediatamente e o som
        play sound audio.vagina_som loop
        show vagina_sally_anim
        
        # Primeiras 5 falas com velocidade normal
        "Puta" "Come minha buceta seu gordo tarado!"
        "Puta Piranha" "Ainda bem que você trouxe camisinha! Segurança em primeiro lugar!"
        "Puta Piranha" "Isso, enfia tudo! Quem diria que uma esponja teria esse equipamento todo!"
        b "Cala a boca e rebola nessa pica, sua vadia! Vou te arrombar toda!"
        "Puta Piranha" "Nossa, Bob! Você está tão... diferente do que imaginei!"
        
        # Mudar para animação mais rápida após 5 falas
        hide vagina_sally_anim
        show vagina_sally_anim_rapida
        
        b "Não me chama de Bob, porra! Sou mais homem que qualquer um nesse mar de merda!"
        "Puta Piranha" "Como devo te chamar então?"
        b "Não precisa me chamar de nada. Só geme bem gostoso e faz seu trabalho, cacete!"
        "Puta Piranha" "Nossa, estou sentindo você pulsar dentro de mim... você está diferente do que imaginei!"
        
        # Gozada simplificada para vagina
        b "Vou gozar, sua piranha! Se prepara!"
        
        # Parar o som de vagina
        stop sound
        
        # Esconder a animação de vagina
        hide vagina_sally_anim_rapida
        
        # Mostrar animação específica de gozada vaginal
        show gozada_vagina_anim
        
        # Primeira gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        b "Caralho! Toma tudo, sua vadia!"
        
        # Segunda gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        "Puta Piranha" "Isso! Sinto escorrendo pelas minhas pernas!"
        
        # Terceira gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        b "Nunca vi tanta porra assim, né piranha?"
        
        # Esconder a animação de gozada
        hide gozada_vagina_anim
        
        # Mostrar imagem final da Sally gozada
        show sally_gozada_vagina at center
        pause 2.0
        
        "Puta Piranha" "Nossa! Você é uma máquina de produzir... nunca vi nada igual!"
        
        menu:
            "Voltar para o quarto":
                hide sally_gozada_vagina
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite
        
    elif escolha == "cuzin":
        scene cama bob
        # Iniciar com a animação imediatamente e o som
        show filtro noite
        hide puta sally
        play sound audio.anal_som loop
        show cuzin_sally_anim
        
        # Primeiras 5 falas com velocidade normal
        "Puta Piranha" "Ainda bem que você trouxe camisinha! No cuzinho é ainda mais importante!"
        "Puta Piranha" "Isso, mete tudo no meu cuzinho! Uma esponja como você deve saber como limpar todos os cantinhos!"
        b "Vou destruir esse rabo, piranha! Nunca mais vai sentar direito depois de mim!"
        "Puta Piranha" "Nossa, você é maior do que parece! Vai com calma!"
        
        # Esconder kradeath
        hide kradeath
        
        # Mudar para animação mais rápida após 5 falas
        hide cuzin_sally_anim
        show cuzin_sally_anim_rapida
        
        b "Calma o caralho! Paguei caro por esse cu, vou usar do jeito que eu quiser!"
        "Puta Piranha" "Ai! Tá doendo! Você não é nada como na TV!"
        b "A TV é uma mentira, sua burra! A vida real é muito diferente, porra!"
        "Puta Piranha" "Tá... tá bom! Ai, isso! Achou o ponto certo! Continua assim!"
        
        # Gozada simplificada para anal
        b "Vou gozar nesse cu apertado! Segura firme, cachorra!"
        
        # Parar o som de anal
        stop sound
        
        # Esconder a animação de anal
        hide cuzin_sally_anim_rapida
        
        # Mostrar animação específica de gozada anal
        show gozada_anal_anim
        
        # Primeira gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        b "Toma no cu, sua vadia!"
        
        # Segunda gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        "Puta Piranha" "Meu Deus! Eu consigo sentir jorrando dentro de mim!"
        
        # Terceira gozada com shake e som
        with hpunch
        play sound audio.gozada_som
        b "Ainda não acabou! Toma mais!"
        
        # Esconder a animação de gozada
        hide gozada_anal_anim
        
        # Mostrar imagem final da Sally gozada
        show sally_gozada_anal at center
        pause 2.0
        
        "Puta Piranha" "Nossa! Como consegue produzir tanto assim? Parece uma mangueira!"
        
        menu:
            "Voltar para o quarto":
                hide sally_gozada_anal
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite
        
    elif escolha == "conversar":
        $ dialogo_random = renpy.random.randint(1, 4)
        
        if dialogo_random == 1:
            "Puta" "Então, você realmente é o Bob Esperma? Parece um pouco... diferente"
            
            b "Claro que eu sou, sua puta idiota! Não ta vendo a esponja na minha cabeça?"
            
            "Puta" "E essa cicatriz no seu pescoço? Parece que sua cabeça foi... costurada?"
            
            b "Não é da sua conta! Foi um... acidente. Agora cala a boca sobre isso antes que eu me irrite!"
            
            "Puta" "E o que aconteceu com sua voz? Lembro que era mais... aguda."
            
            b "Fumo três maços por dia, cacete! Qualquer problema com isso? Agora chega de perguntas idiotas!"
            
        elif dialogo_random == 2:
            "Puta" "Essa casa é mesmo um abacaxi de verdade? Como funciona isso?"
            
            b "É só uma merda de casa, porra! O que tem pra entender? Caiu de um navio e pronto!"
            
            "Puta" "E não apodrece? Estamos debaixo d'água há anos..."
            
            b "Tenho cara de biólogo marinho, sua imbecil? É só uma casa, não enche o saco!"
            
            "Puta" "Fascinante. E todos esses móveis? Também caíram de navios?"
            
            b "Alguns eu roubei, outros eu 'encontrei'. Algum problema com isso, princesa?"
            
            "Puta" "Você tem um gosto peculiar para decoração. Essas cortinas de flores são... únicas."
            
            b "Não escolhi essa merda! Já estava aqui quando che... quer dizer, sempre foi assim. Agora cala a boca!"
            
        elif dialogo_random == 4:
            "Puta" "O que foi esse barulho? Parece que veio daquele armário."
            
            b "Porra nenhuma! É só o vento, caralho! Não tem nada nesse armário!"
            
            "Puta" "Não parecia o vento... Soou mais como alguém gemendo."
            
            b "Tá me chamando de mentiroso, sua vadia? Já disse que não é nada! É o Gary, meu caracol de merda!"
            
            "Puta" "Se você diz... Posso dar uma olhada nele? Adoro animais de estimação!"
            
            b "NÃO TOCA NESSE ARMÁRIO, PORRA! Quer dizer... ele morde estranhos. É perigoso."
            
            "Puta" "Tudo bem, tudo bem! Não precisa gritar, querido."
            
            b "Não sou seu 'querido', entendeu? Agora esquece esse armário ou vamos ter problemas!"
            
        "Puta" "Bem, já conversamos bastante. Quer fazer outra coisa agora?"
        
        menu:
            "Voltar para o menu anterior":
                jump sou_puta
                
            "Voltar para o quarto":
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite