# comcumbina.rpy - Estrutura simplificada com áudio funcionando

# Definição da imagem Sally com tamanho correto (mesmo da Sandy)
image puta sally:
    "images/puta sally.png"
    zoom 0.75
    xalign 0.8
    yalign 0.9

# Definição das animações
image keket_sally_anim:
    "keket sfull 1"
    pause 0.4
    "keket sfull 2"
    pause 0.4
    "keket sfull 3"
    pause 0.4
    repeat

image keket_sally_anim_rapida:
    "keket sfull 1"
    pause 0.2
    "keket sfull 2"
    pause 0.2
    "keket sfull 3"
    pause 0.2
    repeat

image vagina_sally_anim:
    "vagina sally 1"
    pause 0.4
    "vagina sally 2"
    pause 0.4
    "vagina sally 3"
    pause 0.4
    repeat

image vagina_sally_anim_rapida:
    "vagina sally 1"
    pause 0.2
    "vagina sally 2"
    pause 0.2
    "vagina sally 3"
    pause 0.2
    repeat

image cuzin_sally_anim:
    "cuzin sally 1"
    pause 0.4
    "cuzin sally 2"
    pause 0.4
    "cuzin sally 3"
    pause 0.4
    repeat

image cuzin_sally_anim_rapida:
    "cuzin sally 1"
    pause 0.2
    "cuzin sally 2"
    pause 0.2
    "cuzin sally 3"
    pause 0.2
    repeat

image gozada_boquete_anim:
    "gozada boquete 1"
    pause 0.3
    "gozada boquete 2"
    pause 0.3
    repeat

image gozada_vagina_anim:
    "gozada vagina 1"
    pause 0.3
    "gozada vagina 2"
    pause 0.3
    repeat

image gozada_anal_anim:
    "gozada cu 1"
    pause 0.3
    "gozada cu 2"
    pause 0.3
    repeat

image sally_gozada_boquete = "images/sally_gozada_boquete.png"
image sally_gozada_vagina = "images/sally gozada vagina.png" 
image sally_gozada_anal = "images/sally_gozada_anal.png"

# Variável para controlar se é a primeira vez
default primeira_vez_puta = True

label comcumbinas:
    if not hasattr(store, "visitou_puta_dia_{}".format(saida)):
        $ setattr(store, "visitou_puta_dia_{}".format(saida), False)
    
    $ visitou_hoje = getattr(store, "visitou_puta_dia_{}".format(saida))
    
    if visitou_hoje:
        "Não tem ninguém lá fora."
        jump quanaite
    else:
        scene quartobob noite

        if primeira_vez_puta:
            show puta sally:
                xalign 1.2
                yalign 0.5
            
            show puta sally:
                linear 1.5 xalign 0.9
            
            $ primeira_vez_puta = False
        else:
            show puta sally at center

        "Sou piranha"
        jump sou_puta

label sou_puta:
    menu:
        "Boquete $15":
            if money >= 15:
                $ money -= 15
                jump boquete_scene
            else:
                "Você não possui moedas suficientes. São necessárias 15 moedas."
                jump sou_puta
                
        "Vagina $30":
            if money >= 30 and 14 in inventario:
                $ money -= 30
                $ inventario.remove(14)
                jump vagina_scene
            elif money < 30:
                "Você não possui moedas suficientes. São necessárias 30 moedas."
                jump sou_puta
            else:
                "Você precisa ter uma camisinha para esta opção. Compre uma na loja primeiro."
                jump sou_puta
                
        "Cuzin $60":
            if money >= 60 and 14 in inventario:
                $ money -= 60
                $ inventario.remove(14)
                jump cuzin_scene
            elif money < 60:
                "Você não possui moedas suficientes. São necessárias 60 moedas."
                jump sou_puta
            else:
                "Você precisa ter uma camisinha para esta opção. Compre uma na loja primeiro."
                jump sou_puta
        
        "Conversar (Grátis)":
            jump conversar_scene

# CENA DO BOQUETE
label boquete_scene:
    scene cama bob noite
    hide puta sally
    
    stop music
    stop sound
    
    play music "sexmusic.wav" fadein 1.0
    
    show keket_sally_anim
    
    "Puta" "Vou te chupar bem gostoso agora seu safado"
    "Puta" "Hmm, nunca chupei uma esponja antes... você tem um gosto único!"
    b "Cala a boca e chupa logo, porra! Não paguei pra ficar ouvindo merda."
    "Puta" "Caralho, quanta agressividade! "
    b "Não me compare com essa merda de TV. Chupa logo antes que eu perca a paciência!"
    
    hide keket_sally_anim
    show keket_sally_anim_rapida
    
    "Puta" "Tá bom, tá bom... Vou usar minha língua de um jeito especial..."
    b "Aí sim, cadela! Assim que eu gosto... Puta que pariu, que boquinha gostosa!"
    "Puta" "Você está gostando? Nunca imaginei que o Bob Esperma fosse tão... intenso."
    
    b "Vou gozar, porra! Se prepara!"
    
    stop sound
    
    hide keket_sally_anim_rapida
    show gozada_boquete_anim
    
    with hpunch
    b "Toma tudo, sua vadia!"
    
    with hpunch
    b "Continua chupando! Ainda não acabei, cacete!"
    
    with hpunch
    "Puta Piranha" "Uau! Nunca vi tanto... como você consegue produzir tanto?"
    
    hide gozada_boquete_anim
    show sally gozo b at center
    pause 2.0
    
    "Puta Piranha" "Que gosto diferente... nunca provei nada parecido!"
    
    stop music fadeout 1.0
    
    menu:
        "Voltar para o quarto":
            stop music
            stop sound
            hide sally gozo b
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite

# CENA VAGINAL
label vagina_scene:
    scene cama bob
    
    stop music
    stop sound
    
    play music "sexmusic.wav" fadein 1.0
    play sound "gemidos.mp3" loop
    
    show vagina_sally_anim
    
    "Puta" "Come minha buceta seu gordo tarado!"
    "Puta Piranha" "Ainda bem que você trouxe camisinha! Segurança em primeiro lugar!"
    "Puta Piranha" "Isso, enfia tudo! Quem diria que uma esponja teria esse equipamento todo!"
    b "Cala a boca e rebola nessa pica, sua vadia! Vou te arrombar toda!"
    "Puta Piranha" "Nossa, Bob! Você está tão... diferente do que imaginei!"
    
    hide vagina_sally_anim
    show vagina_sally_anim_rapida
    
    stop sound
    play sound "botadarapida.mp3" loop
    
    b "Não me chama de Bob, porra! Sou mais homem que qualquer um nesse mar de merda!"
    "Puta Piranha" "Como devo te chamar então?"
    b "Não precisa me chamar de nada. Só geme bem gostoso e faz seu trabalho, cacete!"
    "Puta Piranha" "Nossa, estou sentindo você pulsar dentro de mim... você está diferente do que imaginei!"
    
    b "Vou gozar, sua piranha! Se prepara!"
    
    stop sound
    
    hide vagina_sally_anim_rapida
    show gozada_vagina_anim
    
    with hpunch
    b "Caralho! Toma tudo, sua vadia!"
    
    with hpunch
    "Puta Piranha" "Isso! Sinto escorrendo pelas minhas pernas!"
    
    with hpunch
    b "Nunca vi tanta porra assim, né piranha?"
    
    hide gozada_vagina_anim
    show sally_gozada_vagina at center
    pause 2.0
    
    "Puta Piranha" "Nossa! Você é uma máquina de produzir... nunca vi nada igual!"
    
    stop music fadeout 1.0
    
    menu:
        "Voltar para o quarto":
            stop music
            stop sound
            hide sally_gozada_vagina
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite

# CENA ANAL
label cuzin_scene:
    scene cama bob
    
    stop music
    stop sound
    
    play music "sexmusic.wav" fadein 1.0
    play sound "gemidos.mp3" loop
    
    show filtro noite
    hide puta sally
    show cuzin_sally_anim
    
    "Puta Piranha" "Ainda bem que você trouxe camisinha! No cuzinho é ainda mais importante!"
    "Puta Piranha" "Isso, mete tudo no meu cuzinho! Uma esponja como você deve saber como limpar todos os cantinhos!"
    b "Vou destruir esse rabo, piranha! Nunca mais vai sentar direito depois de mim!"
    "Puta Piranha" "Nossa, você é maior do que parece! Vai com calma!"
    
    hide kradeath
    
    hide cuzin_sally_anim
    show cuzin_sally_anim_rapida
    
    stop sound
    play sound "botadarapida.mp3" loop
    
    b "Calma o caralho! Paguei caro por esse cu, vou usar do jeito que eu quiser!"
    "Puta Piranha" "Ai! Tá doendo! Você não é nada como na TV!"
    b "A TV é uma mentira, sua burra! A vida real é muito diferente, porra!"
    "Puta Piranha" "Tá... tá bom! Ai, isso! Achou o ponto certo! Continua assim!"
    
    b "Vou gozar nesse cu apertado! Segura firme, cachorra!"
    
    stop sound
    
    hide cuzin_sally_anim_rapida
    show gozada_anal_anim
    
    with hpunch
    b "Toma no cu, sua vadia!"
    
    with hpunch
    "Puta Piranha" "Meu Deus! Eu consigo sentir jorrando dentro de mim!"
    
    with hpunch
    b "Ainda não acabou! Toma mais!"
    
    hide gozada_anal_anim
    show gozada cu 2 at center
    pause 2.0
    
    "Puta Piranha" "Nossa! Como consegue produzir tanto assim? Parece uma mangueira!"
    
    stop music fadeout 1.0
    
    menu:
        "Voltar para o quarto":
            stop music
            stop sound
            hide gozada cu 2
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite

# CENA DE CONVERSA
label conversar_scene:
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
            $ hora_do_dia += 2 
            $ setattr(store, "visitou_puta_dia_{}".format(saida), True)
            jump quanaite