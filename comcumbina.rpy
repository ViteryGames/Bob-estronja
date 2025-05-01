# Definição da animação no início do arquivo
image keket_sally_anim:
    "keket sally"
    pause 0.3
    "keket sally 2"
    pause 0.3
    "keket sally 3"
    pause 0.3
    repeat

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

        show puta sally

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
        show keket_sally_anim:
            zoom 1.0  # Tamanho maior
            xalign 0.5  # Centraliza horizontalmente (centro da tela)
            yalign 0.5  # Centraliza verticalmente (meio da tela)
        "Puta Piranha" "Vou te chupar bem gostoso agora seu safado"
        
        "Puta Piranha" "Hmm, nunca chupei uma esponja antes... você tem um gosto único!"
        
        b "Cala a boca e chupa logo, porra! Não paguei pra ficar ouvindo merda."
        
        "Puta Piranha" "Nossa, que agressividade! O Bob Esponja da TV parece tão gentil..."
        
        b "Não me compare com essa merda de TV. Chupa logo antes que eu perca a paciência!"
        
        "Puta Piranha" "Tá bom, tá bom... Vou usar minha língua de um jeito especial..."
        
        b "Aí sim, cadela! Assim que eu gosto... Puta que pariu, que boquinha gostosa!"
        
        "Puta Piranha" "Você está gostando? Nunca imaginei que o Bob Esponja fosse tão... intenso."
        
        # Menu para escolher onde gozar
        menu:
            "Gozar na boca":
                # Primeira gozada com shake
                with hpunch
                b "Vou gozar, porra! Engole tudo, sua vadia!"
                
                # Segunda gozada com shake
                with hpunch
                "Puta Piranha" "Hmm... que gosto diferente! Nunca provei nada parecido!"
                
                # Terceira gozada com shake
                with hpunch
                b "Continua chupando! Ainda não acabei, cacete!"
                
                "Puta Piranha" "Uau! Nunca vi tanto... hm... 'líquido de esponja' antes! Como você consegue produzir tanto?"
            
            "Gozar na cara":
                # Primeira gozada com shake
                with hpunch
                b "Vou gozar na sua cara, vadia! Se prepara!"
                
                # Segunda gozada com shake
                with hpunch
                "Puta Piranha" "Ai, está entrando no meu olho! Arde!"
                
                # Terceira gozada com shake
                with hpunch
                b "Cala a boca e continua! Quero te deixar toda melada!"
                
                "Puta Piranha" "Meu Deus, quanta coisa! Vou precisar de um banho depois disso..."
        
        hide keket_sally_anim
        
        menu:
            "Voltar para o quarto":
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite
        
    elif escolha == "pussy":
        sd "Come minha buceta seu gordo tarado!"
        
        "Puta Piranha" "Ainda bem que você trouxe camisinha! Segurança em primeiro lugar!"
        
        "Puta Piranha" "Isso, enfia tudo! Quem diria que uma esponja teria esse equipamento todo!"
        
        b "Cala a boca e rebola nessa pica, sua vadia! Vou te arrombar toda!"
        
        "Puta Piranha" "Nossa, Bob! Você está tão... diferente do que imaginei!"
        
        b "Não me chama de Bob, porra! Sou mais homem que qualquer um nesse mar de merda!"
        
        "Puta Piranha" "Como devo te chamar então?"
        
        b "Não precisa me chamar de nada. Só geme bem gostoso e faz seu trabalho, cacete!"
        
        "Puta Piranha" "Nossa, estou sentindo você pulsar dentro de mim... você está diferente do que imaginei!"
        
        # Menu para escolher onde gozar
        menu:
            "Gozar dentro":
                # Primeira gozada com shake
                with hpunch
                b "Vou gozar dentro dessa buceta! Se prepare, vadia!"
                
                # Segunda gozada com shake
                with hpunch
                "Puta Piranha" "Isso! Enche toda minha bucetinha!"
                
                # Terceira gozada com shake
                with hpunch
                b "Caralho! Toma tudo, sua piranha!"
                
                "Puta Piranha" "Meu Deus! Estou sentindo escorrer pelas minhas pernas... nunca vi tanta porra assim!"
            
            "Gozar fora":
                # Primeira gozada com shake
                with hpunch
                b "Vou tirar e gozar em você! Quero te encher de porra!"
                
                # Segunda gozada com shake  
                with hpunch
                "Puta Piranha" "Isso, jorra tudo em mim! Me deixa toda melada!"
                
                # Terceira gozada com shake
                with hpunch
                b "Toma, sua vagabunda! Olha quanta porra!"
                
                "Puta Piranha" "Nossa! Você é uma máquina de produzir... nunca vi nada igual!"
        
        menu:
            "Voltar para o quarto":
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite
        
    elif escolha == "cuzin":
        show kradeath
        sd "To com o cuzin coçando pra vc!!!"
        
        "Puta Piranha" "Ainda bem que você trouxe camisinha! No cuzinho é ainda mais importante!"
        
        "Puta Piranha" "Isso, mete tudo no meu cuzinho! Uma esponja como você deve saber como limpar todos os cantinhos!"
        
        b "Vou destruir esse rabo, piranha! Nunca mais vai sentar direito depois de mim!"
        
        "Puta Piranha" "Nossa, você é maior do que parece! Vai com calma!"
        
        b "Calma o caralho! Paguei caro por esse cu, vou usar do jeito que eu quiser!"
        
        "Puta Piranha" "Ai! Tá doendo! Você não é nada como na TV!"
        
        b "A TV é uma mentira, sua burra! A vida real é muito diferente, porra!"
        
        "Puta Piranha" "Tá... tá bom! Ai, isso! Achou o ponto certo! Continua assim!"
        
        # Menu para escolher onde gozar
        menu:
            "Gozar dentro":
                # Primeira gozada com shake
                with hpunch
                b "Vou gozar nesse cu apertado! Segura firme, cachorra!"
                
                # Segunda gozada com shake
                with hpunch
                "Puta Piranha" "Meu Deus! Eu consigo sentir jorrando dentro de mim!"
                
                # Terceira gozada com shake
                with hpunch
                b "Ainda não acabou! Toma mais, vadia!"
                
                "Puta Piranha" "Nossa! Você está me enchendo! Como consegue produzir tanto assim?"
            
            "Gozar fora":
                # Primeira gozada com shake
                with hpunch
                b "Vou tirar e gozar nas suas costas! Se prepara!"
                
                # Segunda gozada com shake
                with hpunch
                "Puta Piranha" "Isso! Me enche de porra! Quero sentir tudo!"
                
                # Terceira gozada com shake
                with hpunch
                b "Toma mais, sua vadia! Olha quanto leite!"
                
                "Puta Piranha" "Meu Deus! Você parece uma mangueira de tanta coisa que sai daí!"
        
        menu:
            "Voltar para o quarto":
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite
        
    elif escolha == "flirt":
        show kradeath
        sd "tambem com esse piru grosso... tambem com esse pau gostosum"
        
        "Puta Piranha" "Uau, você é mesmo cheio de surpresas! Nunca imaginei que você fosse tão... dotado."
        
        b "Claro que sou, sua imbecil. Acha que eu seria fraco que nem esse bobão da TV?"
        
        "Puta Piranha" "Percebi! Esse seu 'equipamento' não combina muito com sua aparência de desenho infantil."
        
        b "Tá me chamando de infantil, sua vadia? Vou te mostrar o que é ser homem de verdade!"
        
        "Puta Piranha" "Não foi isso que eu quis dizer! É que você é tão diferente do que mostram..."
        
        b "Cala essa boca e vem me chupar logo! Não paguei pra ficar de papo."
        
        "Puta Piranha" "Você é bem grosseiro para alguém que faz desenho animado..."
        
        b "E você fala demais pra uma puta barata! Agora pega nessa rola e faz seu trabalho!"
        
        "Puta Piranha" "Tudo bem, tudo bem! Não precisa ficar nervoso..."
        
        # Menu para escolher onde gozar
        menu:
            "Gozar na boca":
                # Primeira gozada com shake
                with hpunch
                b "Vou gozar na sua boca! Abre bem, cachorra!"
                
                # Segunda gozada com shake
                with hpunch
                "Puta Piranha" "Hmm... tem gosto de... algas marinhas?"
                
                # Terceira gozada com shake
                with hpunch
                b "Engole tudo! Não deixa cair uma gota!"
                
                "Puta Piranha" "Nunca vi ninguém gozar tanto assim! Você é uma máquina de produção!"
            
            "Gozar na cara":
                # Primeira gozada com shake
                with hpunch
                b "Vou gozar na sua cara toda! Se prepara!"
                
                # Segunda gozada com shake
                with hpunch
                "Puta Piranha" "Nossa! Está espirando para todo lado!"
                
                # Terceira gozada com shake
                with hpunch
                b "Toma mais, sua safada! Fica bem melada!"
                
                "Puta Piranha" "Meu Deus! Vou precisar de um banho agora! Tem até no meu cabelo!"
        
        menu:
            "Voltar para o quarto":
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite
                
    elif escolha == "conversar":
        $ dialogo_random = renpy.random.randint(1, 4)
        
        if dialogo_random == 1:
            "Puta Piranha" "Então, você realmente é o Bob Esponja? Parece um pouco... diferente do que mostram na TV."
            
            b "Claro que sou, sua burra! Só que a TV mostra o que eles querem que você veja. A realidade é outra, entende?"
            
            "Puta Piranha" "E essa cicatriz no seu pescoço? Parece que sua cabeça foi... costurada?"
            
            b "Não é da sua conta! Foi um... acidente. Agora cala a boca sobre isso antes que eu me irrite!"
            
            "Puta Piranha" "Você é ator agora? Pensei que trabalhasse no Siri Cascudo."
            
            b "Trabalho onde eu quiser, porra! Quem você pensa que é pra ficar me questionando?"
            
            "Puta Piranha" "E o que aconteceu com sua voz? Lembro que era mais... aguda."
            
            b "Fumo três maços por dia, cacete! Qualquer problema com isso? Agora chega de perguntas idiotas!"
            
        elif dialogo_random == 2:
            "Puta Piranha" "Essa casa é mesmo um abacaxi de verdade? Como funciona isso?"
            
            b "É só uma merda de casa, porra! O que tem pra entender? Caiu de um navio e pronto!"
            
            "Puta Piranha" "E não apodrece? Estamos debaixo d'água há anos..."
            
            b "Tenho cara de biólogo marinho, sua imbecil? É só uma casa, não enche o saco!"
            
            "Puta Piranha" "Fascinante. E todos esses móveis? Também caíram de navios?"
            
            b "Alguns eu roubei, outros eu 'encontrei'. Algum problema com isso, princesa?"
            
            "Puta Piranha" "Você tem um gosto peculiar para decoração. Essas cortinas de flores são... únicas."
            
            b "Não escolhi essa merda! Já estava aqui quando che... quer dizer, sempre foi assim. Agora cala a boca!"
            
        elif dialogo_random == 4:
            "Puta Piranha" "O que foi esse barulho? Parece que veio daquele armário."
            
            b "Porra nenhuma! É só o vento, caralho! Não tem nada nesse armário!"
            
            "Puta Piranha" "Não parecia o vento... Soou mais como alguém gemendo."
            
            b "Tá me chamando de mentiroso, sua vadia? Já disse que não é nada! É o Gary, meu caracol de merda!"
            
            "Puta Piranha" "Se você diz... Posso dar uma olhada nele? Adoro animais de estimação!"
            
            b "NÃO TOCA NESSE ARMÁRIO, PORRA! Quer dizer... ele morde estranhos. É perigoso."
            
            "Puta Piranha" "Tudo bem, tudo bem! Não precisa gritar, querido."
            
            b "Não sou seu 'querido', entendeu? Agora esquece esse armário ou vamos ter problemas!"
            
        elif dialogo_random == 5:
            "Puta Piranha" "Espera, o que é aquilo no chão? Parece... sangue?"
            
            b "Sangue? Tá louca? É ketchup, sua imbecil! Derrubei quando tava comendo."
            
            "Puta Piranha" "Ketchup? Por que teria ketchup espalhado pelo chão?"
            
            b "Porque sou um porco imundo, tá legal? Tenho cara de faxineiro por acaso?"
            
            "Puta Piranha" "E por que o ketchup faz uma trilha até aquele armário ali?"
            
            b "Eu guardei a porra do hambúrguer lá dentro! Algum problema com isso?"
            
            "Puta Piranha" "Isso não me parece muito higiênico para alguém que trabalha com comida."
            
            b "Tá preocupada com higiene? Você transa com qualquer um por dinheiro! Agora cala a boca!"
            
        "Puta Piranha" "Bem, já conversamos bastante. Quer fazer outra coisa agora?"
        
        menu:
            "Voltar para o menu anterior":
                jump sou_puta
                
            "Voltar para o quarto":
                # Marca como visitado para o dia atual
                $ hora_do_dia += 2 
                $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
                jump quanaite