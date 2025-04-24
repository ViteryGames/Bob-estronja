label myScreens: 

screen mapScreen: 
 add "bg map.png"


  #Room 1
 imagebutton :
     xpos 545
     ypos 250
     idle "R1 idle.png"
     hover "R1 hover.png" 
     action Jump("room1") 

  #Room 2
 imagebutton :
     xpos 22
     ypos 100
     idle "R2 idle.png"
     hover "R2 hover.png" 
     action Call("lobbykk")    

   #Room 3
 imagebutton :
     xpos 130
     ypos 385
     idle "R3 idle.png"
     hover "R3 hover.png" 
     action Jump("balde_de_lixo")    

 imagebutton :
     xpos 530
     ypos 600
     idle "R4 idle.png"
     hover "R4 hover.png" 
     action Jump("sandy") 

 imagebutton :
     xpos 1430
     ypos 25
     idle "R5 idle.png"
     hover "R5 hover.png" 
     action Jump("praia")   

 imagebutton :
     xpos 1500
     ypos 590
     idle "jellyfields idle.png"
     hover "jellyfields hover.png" 
     action Jump("praia") 

 imagebutton :
     xpos 1395
     ypos 310
     idle "loja idle.png"
     hover "loja hover.png" 
     action Jump("barg")         