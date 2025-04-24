screen xerequinha:
 text "Money = [money]" xpos 50 ypos 50 size 50 color "#000000"
 text "Tempo = [hora_do_dia]h" xpos 50 ypos 100 size 50 color "#000000"
 text "Saida = [saida]" xpos 50 ypos 150 size 50 color "#000000"


menu:
 "Start the game":
     jump smartass

label smartass:
 call screen myScreens

return