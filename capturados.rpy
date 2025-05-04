# Variáveis iniciais para o script noturno
default bob_desmaiado = False
default dialogo_inicial_exibido = False
default saida_quando_desmaiou = 0
default dia = 1  # Nova variável para contar os dias

label capturados:
  # Desabilita o mapa durante toda a cena noturna
  $ mapa_disponivel = False
  
  scene locker

  # Verifica se Bob está desmaiado
  if bob_desmaiado and saida <= saida_quando_desmaiou:
    "Bob Esperma ainda está desmaiado"
    "Ele respira com dificuldade, mas está vivo"
    jump quanaite
  
  show bob trap night at Transform(xzoom=-1) with hpunch:
    zoom 0.9 xpos 800 ypos 450

  bs "Mmmmhhmmmm mmhm!!!!"
  
  menu:  
       "Desmaiar ele":
         $escolha = "cu"
         jump opbob1
       
       "Conversar":
        $escolha = "Talk"
        jump opbob1

       "Sair" :
         jump quanaite

label opbob1:
 if escolha == "cu":
   play sound "soco.mp3"
   with hpunch
   "Você desmaiou o Bob Esperma"
   "Ele cai no chão, inconsciente"
   "Não há mais como interagir com ele por enquanto"
   $ bob_desmaiado = True
   $ saida_quando_desmaiou = saida
   jump quanaite
   
 elif escolha == "Talk":
   if bob_desmaiado and saida <= saida_quando_desmaiou:
     "Bob Esperma ainda está desmaiado no chão"
     "Parece que ele não vai acordar tão cedo"
     jump quanaite
   else:
     # Se saida > saida_quando_desmaiou, ele acordou no dia seguinte
     $ bob_desmaiado = False
   
   # Exibe o diálogo inicial apenas na primeira vez
   if not dialogo_inicial_exibido:
     "Você remove a mordaça da boca de Bob Esperma"
     
     bs "Por favor, me solte! Eu não fiz nada de errado!"
     
     b "Cala a boca, seu pedaço de merda amarela!"
     
     "Você dá um tapa no rosto de Bob Esperma"
     
     bs "Ai! Por que você está fazendo isso comigo?"
     
     b "Porque eu quero, porra! Passei 15 anos trancado num buraco fedorento, agora é minha vez de me divertir!"
     
     "Bob Esperma treme, seus olhos grandes cheios de medo"
     
     $ dialogo_inicial_exibido = True
   
   # Menu de opções de conversa
   jump opbob1_menu_opcoes


# Menu de opções de conversa separado
label opbob1_menu_opcoes:
  menu:
    "Sobre o que conversar?"
    
    "Perguntar sobre a Fenda do Biquíni":
      b "Então essa merda aqui é a Fenda do Biquíni? Que nome ridículo!"
      
      bs "É-é um lugar muito legal quando você conhece... T-temos o Siri Cascudo, a Escola de Pilotagem da Senhora Puff..."
      
      b "Não me interessa essa baboseira! Quero saber onde tem dinheiro e onde tem pessoas para eu me divertir!"
      
      bs "M-mas violência não é a resposta..."
      
      "Você ri de forma ameaçadora"
      
      b "Na prisão, violência era a única resposta, seu imbecil!"
      
      menu:
        "Continuar conversando":
          jump opbob1_menu_opcoes
        "Voltar":
          jump quanaite
      
    "Intimidar ele":
      b "Sabe o que eu fazia com caras como você na prisão?"
      
      "Você se aproxima perigosamente de Bob Esperma"
      
      b "Primeiro eu quebrava todos os ossos das mãos deles... mas você nem ossos tem, né? Que pena..."
      
      "Bob Esperma tenta se afastar, mas está preso"
      
      bs "P-por favor... tenha piedade..."
      
      b "Piedade? PIEDADE? Ninguém teve piedade de mim quando me jogaram naquele inferno!"
      
      "Sua voz ecoa pelas paredes do quarto"
      
      menu:
        "Continuar conversando":
          jump opbob1_menu_opcoes
        "Voltar":
          jump quanaite
      
    "Contar histórias da prisão":
      b "Deixa eu te contar como eu arranquei o olho do último cara que olhou torto pra mim..."
      
      "Você descreve com detalhes grotescos uma cena de violência extrema"
      
      bs "Pare, por favor! Não quero ouvir isso!"
      
      b "O quê? Muito sensível para ouvir a verdade do mundo real, esponjinha?"
      
      "Você ri ao ver o terror nos olhos de Bob Esperma"
      
      b "E isso foi só o começo. Imagina o que eu fiz com o cara que roubou meu almoço..."
      
      menu:
        "Continuar conversando":
          jump opbob1_menu_opcoes
        "Voltar":
          jump quanaite
          
    "Desmaiar ele":
      b "Já cansei da sua cara idiota!"
      play sound "soco.mp3"
      with hpunch
      
      "Você acerta um golpe violento na cabeça de Bob Esperma" with hpunch
      
      "Ele cai inconsciente, sua forma amarela mole desabando no chão"
      
      "Não há mais como interagir com ele por enquanto"
      
      $ bob_desmaiado = True
      $ saida_quando_desmaiou = saida
      jump quanaite
         
label quanaite:
 $ mapa_disponivel = False
 # O mapa continua indisponível em quanaite
 scene quartobob noite 

 show batavo1 at Transform(xzoom=-1):
    zoom 1.3 xpos 900 ypos 200 
  
 menu:  
    "Dormir":
     # Aqui é onde aumentamos a variável dia
     scene black with fade
     "Você dorme profundamente..."
     
     $ dia += 1  # Incrementa a variável dia
     $ hora_do_dia = 8      # Isso define o horário para 8:00 da manhã
      # Reabilita o mapa quando o jogador acorda
     
     scene quartobob with fade
     "Você acorda. São 8 horas da manhã do dia [dia]."  # Mostra o dia atual
     
     jump room4
       
    "Falar com Bob Esperma":
      jump capturados

    "Espiar a janela":
      jump janela

label janela: 
  $ mapa_disponivel = False
  # O mapa continua indisponível
  scene rua1
  
  $ renpy.pause(1)

  # Se estiver pelo menos na noite 2
  if saida >= 2:
    show rua1

    # Verifica se já viu a prostituta pela janela hoje
    if not hasattr(store, "viu_prostituta_janela_dia_{}".format(saida)):
        $ setattr(store, "viu_prostituta_janela_dia_{}".format(saida), False)
    
    $ viu_hoje = getattr(store, "viu_prostituta_janela_dia_{}".format(saida))
    
    if not viu_hoje and not getattr(store, "visitou_puta_dia_{}".format(saida), False):
        show ruap with fade

        "Você vê uma prostituta aguardando no ponto de ônibus."
        # Marca como visto hoje
        $ setattr(store, "viu_prostituta_janela_dia_{}".format(saida), True)
        
        # Adicione o novo menu aqui
        menu:
            "Assobiar para chamar a puta":
                "Você assobia alto e agita os braços para chamar a atenção dela."
                "A prostituta olha para sua janela e sorri maliciosamente."
                "Ela atravessa a rua e vem em direção à sua casa."
                scene quartobob noite
                "Alguns minutos depois..."
                # O mapa continua indisponível quando vai para comcumbinas
                # A classe comcumbinas já tem seu próprio controle de mapa
                jump comcumbinas
                
            "Voltar":
                "Você decide não chamar atenção e volta para dentro."
                jump quanaite
    else:
        "Não há nada de interessante lá fora."
        jump quanaite
    
  # Se for antes da noite 2
  else:
    "Não tem ninguem la fora"     
  
  menu:  
    "Voltar":
      jump quanaite