label casas: 




 

screen bobCasas:
 add "bg room1.jpg"

 
 text "Money = [money]" xpos 50 ypos 50 size 50 color "#FFFF00"

 imagebutton :
     xpos 1300
     ypos 180
     idle "abacaxi idle.png"
     hover "abacaxi.png" 
     action Jump("salabob") 

 imagebutton :
     xpos 735
     ypos 195
     idle "lulah idle.png"
     hover "lulah hover.png" 
     action Jump("lulah") 

 imagebutton :
     xpos 220
     ypos 510
     idle "preda idle.png"
     hover "preda hover.png" 
     action Jump("preda")