define sd = "Sandy Bucetas"

label room5:
  scene travelha
  show sandybb with dissolve
  

  sd"Oi bob esponja"

  sd"Come meu cu seu viado safado!" 
 
  k"Posso saber onde vc estava?"
  menu:
      "Não sou o Bob Esponja. O verdadeiro ta amarrado em casa.":
       $escolha = "convers2"
       jump sandbum


      "Batendo punheta":
       $escolha = "convers1"
       jump sandbum


      "Comendo a piranha da sua mãe":
       $escolha = "comituamae"
       jump sandbum
      "Comendo a piranha da sua irmã":
       $escolha = "convers2"
       jump sandbum


      "Meu caracol passou mal Seu Siririca" :
       $escolha = "convers1"
       jump sandbum

      "To de pau caducano to de pau caducano to de pau cadunanu to de pau cadunano" :
       $escolha = "flirt"
       jump sandbum
 

label sandbum:
  hide krab a
  if escolha == "convers1":  
     show krab happy:
        zoom 0.6 xpos 1000 ypos 400

     k"Tudo bem rapaz sem problemas"

     k"Já tive sua idade um dia, uma punhetinha aumenta na produtividade"

     k"Mas me avisa na próxima vez para evitar problemas ok?! Não seja igual o Rola Molusco que passa horas no banheiro..."

     hide patrick2
  elif escolha == "convers2":
         
         sd"VAI TOMA NO CUUUU BOB ESPORRAAAA!!!"

         "Game over"
  elif escolha == "comituamae":
         show kradeath

         sd"VAI TOMA NO CUUUU BOB ESPORRAAAA!!!"

         "Game over"
  elif escolha == "flirt":
         show kradeath

         sd"tambem com esse piru grosso... tambem com esse pau gostosum"

         "Game over"       

         


  menu: 
     "Leave":
       call screen mapScreen

