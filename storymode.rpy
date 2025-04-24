define b = "Bob Estronja"
default day2 = False


label storymode:
 scene bg room1
    
 show patrick1:
    zoom 1.5 xpos 30 ypos 400 

    
 p"Ei Bob Esponja onde vc estava?! O Seu siririca está maluco atrás de voce tem muitos clientes no Siri Cracudo"
 hide patrick1
 show batavo1 at Transform(xzoom=-1):
    zoom 1.3 xpos 900 ypos 200 
 b"Siri Cracudo?"
  
 show patrick1:
    zoom 1.5 xpos 30 ypos 400 

 p"O restaurante que você trabalha há decadas e valoriza mais que sua própria vida?"
 menu: 
     "Ah sim, melhor eu ir indo. Obrigado cara":
         $ escolha = "bob"
         jump pau1
     "Nunca ouvi falar":
         $ escolha = "tv"
         jump pau1
     "Não sou o Bob Esponja, peguei o onibus errado e acabei vindo parar aqui.":  
         $escolha = "vdd"
         jump pau1        


label pau1:
    if escolha == "crz":   
     show patrick5:
        zoom 1.5 xpos 30 ypos 400 
     p"(Coitado, todos esses anos acabaram deixando ele maluco. Deve estar ficando demente, melhor eu me afastar...)"

     p"Certo Bob Esponja, até mais"

     hide patrick5
    elif escolha == "bob":
     hide patrick2    
     show patrick1:
        zoom 1.5 xpos 30 ypos 400 
     p"Até mais boiolinha quadrado"
     hide patrick2
    elif escolha == "inv":
        if vezes_investigou == 0:
            "Você descobre 10 dólares debaixo do colchão."
            "Dentro de um envelope escrito: 'Salário dos últimos 20 anos'."
        elif vezes_investigou == 1:
            "Você descobriu que hoje é o dia do gay."
            $ dia_do_contra = True 
        else:
            "Não há mais nada para investigar."
        $ vezes_investigou += 1
    elif escolha =="tv":
     hide patrick1   
     show patrick2:
        zoom 1.5 xpos 30 ypos 400 
     p"É onde voce frita hamburguer pro seu sirigueijo, sabe.. "

     hide patrick2
     show patrick6:
        zoom 1.5 xpos 30 ypos 400 

     p"Hamburguer de siri.. "

     hide patrick6
     menu: 
         "Ah sim, melhor eu ir indo. Obrigado cara":
              $ escolha = "bob"
              jump pau1
         "Eu não frito hamburguer,eu não sou um fracassado.":
             $ escolha = "crz"
             jump pau1
    elif escolha =="vdd":
     show patrick1:
        zoom 1.5 xpos 30 ypos 400 

     p"Então pq está vestindo as roupas dele?"   
     menu: 
         "Pq eu quero seu palhaço filho da puta":
             $escolha = "cuzao1"
             jump badgay
         "Pq hj é o dia do contra!":
             $escolha = "contra"
             $contrap1 = True
             jump badgay    

label badgay:
  if escolha == "cuzao1": 
     hide patrick1
      
     show patrick2:
        zoom 1.5 xpos 30 ypos 400 

     p"Também não precisa falar assim..."

     p"Cabeça de mechilhão!"

     hide patrick2
  elif escolha == "contra":
         hide patrick1
         show patrick aa:
          zoom 1.5 xpos 30 ypos 400 

         p"O DIA DO CONTRA?! PUXA EU TINHA ME ESQUECIDO! VALEU AMIGÃO."
     
         hide patrick aa

         "Patrick saiu correndo"


label stry1:
 scene areia 

 menu: 
     #"Voltar pra casa":
       #jump chegada_em_casa
     "Ir para o Siri Cracudo":
       jump room2 


    
 p"Até mais boiola!"
  


label day2:
  scene areia
  
  show patrick1
  
  p "Ei amigão, como vai?"

  p"Estou com saudades de uma boa e velha caça ás aguas-vivas com meu melhor amigo"

  p"Estou indo pro campos das águas vivas agora mesmo!!"

  p"O que vc acha de caçar algumas comigo hoje"
  hide patrick1
  menu:
     "Caçar o que?":
         $escolha = "que"
         jump oppatrick

     "Me caguei seu viado fudido de merda?":
         $escolha = "no"
         jump oppatrick

label day3:
  scene shellfone
  
  "Seu telefone de concha está vibrando"

  sd"Oi Bob esponja! Venha me visitar hoje na casa da árvore!"

  menu:
     "Vamboraaa porra quero gozar":
         $escolha = "sandyS1"
         jump sandybuzz1

     "Me caguei seu viado fudido de merda?":
         $escolha = "sandyN1"
         call screen lobbykk with fade
       
label sandybuzz1:
  if escolha == "sandyS1":  
     show patrick2:
        zoom 1.5 xpos 30 ypos 400 

     p"Também não precisa falar assim..."

     p"Cabeça de mechilhão!"

     hide patrick2

   

  elif escolha == "sandyN1":
     show patrick2:
        zoom 1.5 xpos 30 ypos 400 
   
  menu:
     "Ir la dar uma gozada":
         jump sandy
      



label oppatrick:
  if escolha == "no":  
     show patrick2:
        zoom 1.5 xpos 30 ypos 400 

     p"Também não precisa falar assim..."

     p"Cabeça de mechilhão!"

     hide patrick2
  elif escolha == "que":
     show patrick2:
        zoom 1.5 xpos 30 ypos 400 

     p"Caçar aguas vivas nos campos das aguas vivas..."

     p"É nosso hobby favorito não se lembra?"
     menu:
          "Não":
             call screen lobbykk

  menu:
     "Ir para o siri cracudo":
         call screen lobbykk
      
   
label day4: 

   scene areia 

   "Holandes Metedor" "HAHAHAHAAHAHAHAH SEU ESPONJA BOIOLAAAAA"

   "ESSE É UM MAPA MUUUITO FILHO DA PUTA QUE VAI TE FUDEEEE HEHEHEH KKKKKKAKAKAKAKAAKK"

   
   menu: 
     "Abrir o mapa":
       call screen mapScreen









return