# Adicione estas linhas ao início do arquivo storymode.rpy, após as definições existentes

# Definir imagens para o Holandês Voador
image fumaca_verde:
    "fumaca_verde.png"  # Adicione esta imagem aos seus recursos
    zoom 1.5
    alpha 0.0
    linear 1.0 alpha 1.0
    easein 0.5 zoom 1.0 alpha 0.8
    
image holandes_normal:
    "holandes garrafa.png"  # Adicione esta imagem aos seus recursos
    zoom 0.8
    xalign 0.5
    yalign 0.5

image holandes_risada:
    "holandes metedor risada.png"  # Adicione esta imagem aos seus recursos
    zoom 0.8
    xalign 0.5
    yalign 0.5
    
image garrafa:
    "garrafa.png"  # Adicione esta imagem aos seus recursos
    zoom 0.5
    xalign 0.5
    yalign 0.8

image mapa:
    "mapa.png"  # Adicione esta imagem aos seus recursos
    zoom 0.7

# Definir o personagem do Holandês Voador
define h = Character("Holandês Metedor", color="#34A65F")

# Definir variável para rastrear se o jogador já encontrou o Holandês
default encontrou_holandes = False
default tem_mapa_holandes = False

# Adicione esta nova label em storymode.rpy

label landal:
    scene bg room4
    stop music fadeout 1.0
    play audio "holandes.mp3" fadeout 2.0
    # Verificar se é noite
    if hora_do_dia >= 18 or hora_do_dia < 6:
        scene quartobob noite
    
    show batavo1 at Transform(xzoom=-1) with hpunch:
        zoom 1.0 xpos 1000 ypos 400
    
    "A porta da sala está trancada."
    
    b "Ué, será que prendeu com porra?"
    
    # Efeito de tremor para a entrada do Holandês
    show fumaca_verde at truecenter with dissolve
    
    play sound "risada_holandes.mp3" volume 0.8  # Adicione este som
    
    "Uma fumaça verde estranha surge na sala!"
    
    b "Que porra é essa agora?!"
    
    # Tremor intenso quando o Holandês aparece
    with hpunch
    with vpunch
    
    hide fumaca_verde
    show holandes_risada with dissolve
    play audio "laugh2.mp3" fadeout 2.0
    
    h "HAHAHAHA! Vejam só o que temos aqui!"
    
    # Efeito de tremor adicional quando ele grita
    with hpunch
    
    h "ALGUÉM NOVO NA FENDA DO BIQUÍNI, HEIN?!"
    hide holandes_risada
    show holandes_normal
    
    h "Todo novo morador recebe... um PRESENTE!"
    
    b "E quem é você? Uma bichona verde flutuante?"

    hide holandes_normal
    show holandes direita
    
    h "BICHONA?! Eu sou O HOLANDÊS METEDOR seu obeso do caralho!!"
    
    # Movimento da garrafa flutuando
    hide holandes direita
    show garrafa at center with moveinbottom
    
    h "Este mapa mostra tudo o que vc precisa pra explorar esta merda de cidade!"
    
    h "To cansado de bater punheta olhando a filha do sirigueijo no chuveiro, quero ver coisas mais picantes..."
    
    # Aqui o Holandês estreita os olhos, suspeitando
    h "O Bob Esporra nunca foi muito trepador.Mas você não é exatamente o Bob Esporra, é?"
    
    # Efeito de tremor leve para criar tensão
    with hpunch
    
    b "Do que você está falando? É claro que sou o Bob sua bichona de tranças! Mariquinha boiola marica"
    hide holandes_normal
    hide holandes direita
    show holandes_risada
    
    h "HAHAHA! Eu gosto do seu... estilo. Mais um motivo para te dar este mapa."
    
    h "Há lugares... INTERESSANTES marcados nele! Use com sabedoria seu gordo broxa!"
    
    hide holandes_risada
    "O Holandês Metedor deixa a garrafa flutuando no ar."
    
    show holandes_normal:
        alpha 1.0
        ease 1.5 alpha 0.0
        
    hide holandes_normal
    
    play sound "risada_holandes.mp3" volume 0.5
    
    "A risada do Holandês Voador ecoa enquanto ele desaparece..."
    
    b "Que porra foi essa?"

    "Você adquiriu o MAPA, estará disponível sempre que sair de casa no canto superior direito."
    
    # Definir variável para ativar novos locais no mapa
    $ tem_mapa_holandes = True
    $ mapa_disponivel = True
    
    # Volta para o fluxo normal
    jump salabob
