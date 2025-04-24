label preda:
  scene bg preda

  show pautrick joia at left with moveoutright:
     zoom 1.75


  p"Oi Bob Esporra.{w}"  
  window hide
  $ renpy.pause(1)

  show pautrick joia
  $ renpy.pause(1)
  
  
  "Pautrick" "Quer ver meu piru?"
  menu: 
     "Sim":
         jump opa

     "Não":
         jump opb

  label opa:
     show pautrick mole at left with moveoutright:
         zoom 1.75
     hide pautrick joia
     jump end
     

  label opb: 
     show patrick poxa1 at left with moveoutright:
         zoom 1.75
     hide pautrick joia
     p"Poxa..."
     jump end
     
label end:

  menu: 
     "Leave":
       call screen bobCasas