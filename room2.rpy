define lu = "Lula Pirusco"
default cozinha_mensagem = False

label room2:
  scene kk
  "Você chega no Siri Cracudo" 

  define k = "Seu siririca"
  
  show krab a at center with fade:
     zoom 0.75

  k "BOB ESPONJA!!!" 

  k"Posso saber onde vc estava?"
  menu:
      "Não sou o Bob Esponja. O verdadeiro ta amarrado em casa.":
       $escolha = "truth"
       jump siricas


      "Batendo punheta":
       $escolha = "punheta"
       jump siricas


      "Comendo a piranha da sua mãe":
       $escolha = "comituamae"
       jump siricas

      "Comendo a piranha da sua irmã":
       $escolha = "comituamae"
       jump siricas


      "Meu caracol passou mal Seu Siririca" :
       $escolha = "gary"
       jump siricas

label siricas:
  hide krab a
  if escolha == "punheta":  
     show krab happy:
        zoom 0.6 xpos 1000 ypos 400

     k"Tudo bem rapaz sem problemas"

     k"Já tive sua idade um dia, uma punhetinha aumenta na produtividade"

     k"Mas me avisa na próxima vez para evitar problemas ok?! Não seja igual o Rola Molusco que passa horas no banheiro..."

     hide patrick2
  elif escolha == "comituamae":
         show kradeath

         k"VAI TOMA NO CUUUU BOB ESPORRAAAA!!!"

         "Game over"

         return
  elif escolha == "truth":
       show krab4:
        zoom 0.6 xpos 1000 ypos 400 

       k"Puta merda..."
  elif escolha == "gary":
       show krab4:
        zoom 0.5 xpos 1000 ypos 520 

       k"Puxa rapaz que pena..."

       show krab4:
        zoom 0.5 xpos 1000 ypos 520  

       k"Que tal fritar uns hamburgueres de siri para se sentir melhor?"

label cozinha:
  
  scene kitchen 



  show batavo1 at Transform(xzoom=-1):
    zoom 1.5 xpos 700 ypos 30
  
  
  while True:
      if not cozinha_mensagem:
         "Aqui é a cozinha do Siri Cracudo"  

         $ cozinha_mensagem = True 

      menu:
            #"Se masturbar":
               # $ escolha = "quarto"
               # jump opcoes

            "Adcionar um molho secreto":
                $ escolha = "gozo"
                jump chapa

            "Cozinhar um hamburguer de siri normal":
                $ escolha = "burguer"
                jump chapa

label chapa:
  
  play audio "grelha.mp3" fadein 2.0

  show chapa

  if escolha == "burguer":  
     pause(5)

     hide chapa

     "Seis horas depois" 
     $ hora_do_dia += 6 

     pause(2)

     show kk night

     show krab happy:
      zoom 0.6 xpos 1000 ypos 400

     k"”Vá pra casa rapaz, e ve se capricha mais amanhã os clientes estão reclamando que o gosto está uma merda."
     

     k"Não que eu me importe com isso se for uma vez ou outra,mas se manter esse ritmo vou perder DINHEI- digo meus amados clientes."
     jump capturados

  elif escolha == "gozo":
         show molho

         pause(2)

         show molho2

         pause(2)

         show molho3
         
         "Você adcinou o MOLHO SECRETO em todos os hamburgueres de siri"

         pause(2)

         "Seis horas depois"
         $ hora_do_dia += 6  

         stop audio fadeout 2.0

         show kk night

         show krab happy:
          zoom 0.6 xpos 1000 ypos 400

         k"”Vá pra casa rapaz, e continue com essa receita nova os clientes estão adorando $$ ."

         $money += 10
         "Você recebeu 10 dolares pelo ótimo serviço!"
         stop music fadeout 3.0
         jump quanaite


         
  





  if nugget: 
    k "Vejo que alguem comeu seu rabo rapaz..."

  menu: 
     "Leave":
       call screen mapScreen


label caixakk:
 scene caixa kk lula

 lu" Bom, acho que como eu sou o unico ser com QI positivo nesta espenunca de cidade, eu vou ter que perguntar"
 
 show lula com vc 

 lu" Quem é vc e onde esta aquele boiolinha quadrado?"

 menu:
            #"Se masturbar":
               # $ escolha = "quarto"
               # jump opcoes

            "Não sei do que está falando, eu sou ele!":
                $ escolha = "mentiu"
                jump luleta

            "Ignorar (fodase é o Lula Molusco)":
                $ escolha = "mentiu"
                jump luleta

label luleta:              
 if escolha == "mentiu":  
     pause(3)

   
   
     
     show caixa kk lula
     "Ta que se foda eu so venho aqui pra fazer banheirao mesmo"
     jump cozinha



label lobbykk: 

 play music "siricracudo.mp3" fadein 2.0

 screen lobbykk: 

    add "lobbykrab.png"  
    on "show" action Play("music", "siricracudo.mp3", fadein=2.0)
     


    imagebutton:
             xpos 920
             ypos 230
             idle "barco pirusco idle.png"
             hover "barco pirusco.png" 
             action Jump("caixakk")  

    imagebutton :
              xpos 1170
              ypos 200
              idle "porta kk idle.png"
              hover "porta kk hover.png" 
              action Jump("cozinha")     

    imagebutton :
          xpos 1490
          ypos 200
          idle "porta kk idle.png"
          hover "porta kk hover.png" 
          action Jump("banheirao")   

    imagebutton :
          xpos 263
          ypos 200
          idle "porta kk idle.png"
          hover "porta kk hover.png" 
          action Jump("sala_siririca")           

label banheirao: 
 scene banheirao 

 k"Meu piru ta mole hoje porra.."

 menu: 
    "Voltar":

       call screen lobbykk with fade
 
default visitou_sala_siririca = False

label sala_siririca:
    scene tutinha
    play music "siricracudo.mp3" fadein 2.0
    
    if not visitou_sala_siririca:
        "Você entra na sala do Seu Siririca"
        
        show krab a at center with fade:
            zoom 0.75
        
        k "O que você quer agora, Bob Esponja? Tá vendo que estou OCUPADO CONTANDO MEU DINHEI... digo, fazendo a contabilidade do restaurante!"
        $ visitou_sala_siririca = True
    else:
        show krab a at center with fade:
            zoom 0.75

    jump menu_principal_siririca

label menu_principal_siririca:
    menu:
        "Conversar":
            $ escolha = "conversar"
            jump conversa_siririca
            
        "Pedir um aumento":
            $ escolha = "aumento"
            jump aumento_siririca
            
        "Perguntar sobre o Rola Molusco":
            $ escolha = "molusco"
            jump info_molusco
            
        "Mexer na gaveta secreta":
            $ escolha = "gaveta"
            jump gaveta_secreta
            
        "Voltar":
            call screen lobbykk with fade

label conversa_siririca:
    hide krab a
    show krab4:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Tem cinco segundos para falar o que quer. Cada segundo custa dinheiro, rapaz!"
    
    jump menu_conversa_siririca

label menu_conversa_siririca:
    menu:
        "Perguntar sobre a história do Siri Cracudo":
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Ah, essa é uma história inspiradora sobre CAPITALISMO E DINHEIRO!"
            
            k "Eu comecei com um hamburger velho, uma frigideira enferrujada e MUITA AMBIÇÃO!"
            
            k "E agora tenho esse império que me rende TANTO DINHEIRO HAHAHA"
            
            k "Agora volte ao trabalho antes que eu mude de ideia e te DEMITA!"
            
            jump menu_conversa_siririca
        
        "Perguntar sobre a filha dele":
            show krab4:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Pera aí, como VOCÊ sabe que eu tenho uma filha?"
            
            k "Você anda seguindo a Pérola por aí? Se eu descobrir que você está dando em cima dela..."
            
            show kradeath
            
            k "VOU ENFIAR ESSE HAMBÚRGUER DE SIRI NO SEU..."
            
            hide kradeath
            show krab a:
                zoom 0.75
            
            k "Ahem... volte ao trabalho, Bob Esponja."
            
            jump menu_conversa_siririca
        
        "Falar sobre o tempo":
            show krab4:
                zoom 0.6 xpos 1000 ypos 400
            
            k "O tempo? O TEMPO É DINHEIRO, RAPAZ!"
            
            k "Enquanto estamos aqui falando sobre NADA, você podia estar lá fritando hambúrgueres e ME DANDO LUCRO!"
            
            jump menu_conversa_siririca
        
        "Fazer outra coisa":
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade

label aumento_siririca:
    hide krab a
    show kradeath
    
    k "HAHAHAHAHAHA!"
    
    show krab4:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Essa foi boa, rapaz. AUMENTO? No Siri Cracudo?"
    
    k "Você já recebe o privilégio de trabalhar pro MELHOR RESTAURANTE da Fenda do Biquíni!"
    
    menu:
        "Insistir no aumento":
            show kradeath
            
            k "ESCUTA AQUI SEU PEDAÇO DE ESPONJA INÚTIL!"
            
            k "EU POSSO TE SUBSTITUIR POR QUALQUER PARASITA DO OCEANO!"
            
            k "Agora volte pra cozinha antes que eu te DEMITA!"
            
            $ money -= 5
            "Seu Siririca multou você em 5 dólares por insubordinação!"
            
            jump menu_principal_siririca
        
        "Oferecer trabalhar mais horas":
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "AGORA ESTAMOS FALANDO A MESMA LÍNGUA!"
            
            k "Trabalhar DE GRAÇA depois do expediente? ISSO SIM é espírito de equipe!"
            
            k "Continue assim e talvez eu pense em te dar um aumento de 0,1%% no próximo século!"
            
            $ money += 2
            "Você ganhou 2 dólares como 'incentivo'!"
            
            jump menu_principal_siririca
        
        "Sugerir uma promoção 'Traga sua batata e pague 2x mais'":
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "MEU DEUS! Você é um GÊNIO, rapaz!"
            
            k "Fazemos eles trazerem os ingredientes E pagarem mais? HAHAHA!"
            
            k "Vou implementar isso AGORA MESMO!"
            
            $ money += 15
            "Você recebeu 15 dólares de comissão pela ideia!"
            
            jump menu_principal_siririca
        
        "Fazer outra coisa":
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade

label info_molusco:
    hide krab a
    show krab4:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Aquele tentáculos inútil? O que tem ele?"
    
    k "Passa o dia inteiro reclamando e tocando aquela flauta irritante!"
    
    k "Mas ele é barato, então eu mantenho por aqui..."
    
    menu:
        "Perguntar onde ele está":
            k "Provavelmente no caixa, sendo mal-educado com os clientes como sempre."
            
            k "Ou escondido no banheiro batendo... quer dizer, tocando clarinete."
            
            jump menu_principal_siririca
        
        "Sugerir demitir o Lula Molusco":
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "E pagar dois salários? Tá maluco?"
            
            k "Você faria o trabalho dele também?"
            
            menu:
                "Sim, posso fazer":
                    k "HAHAHA, você já está aceitando fazer HORA EXTRA de graça!"
                    
                    k "Agora quer fazer o trabalho do Lula também? SEM CHANCE!"
                    
                    k "Não vou demitir ele e contratar outro funcionário quando posso explorar DOIS de uma vez!"
                    
                    jump menu_principal_siririca
                
                "Não, melhor não":
                    k "É o que eu pensava. Volte ao trabalho!"
                    
                    jump menu_principal_siririca
        
        "Fazer outra coisa":
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade

label gaveta_secreta:
    hide krab a
    
    "Enquanto Seu Siririca está distraído, você se esgueira até a gaveta secreta do escritório"
    
    menu:
        "Abrir a gaveta":
            "Você encontra várias fotos do Seu Siririca abraçado com sacos de dinheiro"
            
            "Também há um livro chamado 'Como explorar funcionários e lucrar com isso - Volume 37'"
            
            "E um cofre pequeno trancado..."
            
            menu:
                "Tentar abrir o cofre":
                    "Você tenta girar a combinação..."
                    
                    "De repente, um alarme dispara!"
                    
                    show kradeath at center with moveinright:
                        zoom 0.9
                    
                    k "SEU LADRÃOZINHO DE MEIA TIGELA!"
                    
                    k "TENTANDO ROUBAR MEU PRECIOSO DINHEIRO?!"
                    
                    "Seu Siririca agarra você pela gola"
                    
                    k "VOU TE JOGAR NO FREEZER COM O ÚLTIMO FUNCIONÁRIO QUE TENTOU ME ROUBAR!"
                    
                    $ money = 0
                    "Seu Siririca confiscou todo o seu dinheiro como punição!"
                    
                    jump menu_principal_siririca
                
                "Fechar a gaveta rapidamente":
                    "Você fecha a gaveta bem a tempo"
                    
                    show krab a at center with moveinright:
                        zoom 0.75
                    
                    k "O que você está fazendo perto da minha mesa, rapaz?"
                    
                    menu:
                        "Só vim limpar a poeira, chefe!":
                            show krab happy:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "Ah, limpeza gratuita! Assim que eu gosto!"
                            
                            k "Continue assim que um dia você talvez ganhe um aumento de meio centavo!"
                            
                            jump menu_principal_siririca
                        
                        "Procurando canetas para a cozinha":
                            show krab4:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "CANETAS? Na cozinha?"
                            
                            k "Você acha que CANETAS crescem em árvores? São CARAS!"
                            
                            k "Use carvão ou tinta de lula como todo mundo!"
                            
                            jump menu_principal_siririca
                
                "Fazer outra coisa":
                    jump menu_principal_siririca
                    
                "Voltar":
                    call screen lobbykk with fade
        
        "Melhor não arriscar":
            "Você decide que não vale a pena arriscar sua vida por curiosidade"
            
            show krab a at center with moveinleft:
                zoom 0.75
            
            k "O que você está fazendo parado aí? O tempo é DINHEIRO!"
            
            k "Volte para a cozinha AGORA! Tem clientes esperando!"
            
            jump menu_principal_siririca
        
        "Fazer outra coisa":
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade