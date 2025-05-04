label vaginapodi:
  scene bg preda

  show pautrick joia with moveoutright:
     zoom 1.75
     align (0.5, 0.5)  # Centraliza a imagem (x=0.5 é centro, y=0.5 é centro)
     yoffset 100       # Move a imagem para baixo (valores positivos = para baixo)
     # OU use xalign e yalign separadamente:
     # xalign 0.5      # 0.5 = centro, 0.0 = esquerda, 1.0 = direita
     # yalign 0.7      # 0.5 = centro, 0.0 = topo, 1.0 = base

  p"Oi Bob Esperma{w}"  
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
     # Escondemos o personagem atual
     hide pautrick joia
     
     # Efeito de câmera com zoom inicial na parte inferior, subindo lentamente e depois zoom out
     show sandybb:
         zoom 2.5       # Zoom inicial mais próximo
         align (0.5, 0.5)  # Centraliza a imagem
         yoffset -300   # Começa focando na parte SUPERIOR 
         linear 4.0 yoffset 300   # Move lentamente para BAIXO (focando na parte inferior)
         ease 1.0 zoom 1.75 yoffset 0  # Retorna ao zoom normal e centraliza
     
     jump end
     
  label opb: 
     show patrick poxa1 with moveoutright:
         zoom 1.75
         align (0.5, 0.5)  # Centraliza a imagem
     hide pautrick joia
     p"Poxa..."
     jump end
     
label end:
  menu: 
     "Leave":
       call screen bobCasas

# preda.rpy - Interações com Patrick em sua casa
# Este arquivo deve ser colocado na pasta "game" do seu projeto Ren'Py

# Adicionar item de geleia ao dicionário de itens (caso não exista)
init 1 python:
    if 23 not in itens_loja:
        itens_loja[23] = {"nome": "Pote com Jeleia", "preco": 50}
    
    # Função para criar geleia a partir de águas-vivas e potes
    def criar_pote_jeleia():
        global inventario
        
        # Verificar se temos águas-vivas e potes suficientes
        qnt_aguas_vivas = inventario.count(21)  # ID água-viva capturada
        qnt_potes = inventario.count(8)         # ID pote para águas-vivas
        qnt_jeleias = inventario.count(23)      # ID pote com jeleia
        
        # Verificar se já está no limite
        if qnt_jeleias >= 5:
            return "max"
            
        # Verificar se temos ingredientes suficientes
        if qnt_aguas_vivas < 5:
            return "falta_aguas"
            
        if qnt_potes < 1:
            return "falta_pote"
            
        # Remover os ingredientes do inventário
        for i in range(5):
            inventario.remove(21)  # Remove 5 águas-vivas
        inventario.remove(8)       # Remove 1 pote
            
        # Adicionar jeleia ao inventário
        inventario.append(23)      # Adiciona 1 pote com jeleia
        
        return "sucesso"

# Imagem da casa de Patrick
image casa_patrick = "images/casa_patrick.jpg"

# Label principal para interagir com Patrick
label preda:
    scene casa_patrick
    
    "Você chega à casa de Patrick."
    
    # Verificar se Patrick está em casa
    $ hora_atual = hora_do_dia % 24
    if 2 <= hora_atual <= 5:
        "Patrick não está acordado agora. Melhor voltar mais tarde."
        jump room4
    
    # Patrick aparece
    show pautrick
    
    p "Ei, Bob Esperma! Que surpresa te ver aqui!"
    
    # Menu de interação principal
    menu patrick_opcoes:
        "O que você deseja falar com Patrick?"
        
        "Conversar um pouco":
            jump conversar_patrick
            
        "Ver o Patrick sem camisa" if money >= 10:
            $ money -= 10
            p "Você quer me ver sem camisa? Bem... por 10 moedas, tudo bem."
            
            # Mostrar Patrick sem camisa
            hide pautrick
            show pautrick mole
            
            p "Está satisfeito agora?"
            
            "Patrick parece um pouco desconfortável."
            
            hide pautrick mole
            show pautrick
            
            jump patrick_opcoes
            
        "Ver o Patrick sem camisa" if money < 10:
            p "Para me ver sem camisa, você precisa de pelo menos 10 moedas."
            
            jump patrick_opcoes
            
        "Fazer Pote com Jeleia":
            # Verifica se já está no limite
            $ qnt_jeleias = inventario.count(23)
            
            if qnt_jeleias >= 5:
                p "Você já tem o número máximo de potes com jeleia que pode carregar (5)."
                jump patrick_opcoes
                
            # Verifica ingredientes e cria jeleia
            $ resultado = criar_pote_jeleia()
            
            if resultado == "sucesso":
                p "Ótimo! Vamos transformar essas águas-vivas em jeleia deliciosa!"
                
                "Patrick mistura as águas-vivas no pote com alguns ingredientes secretos."
                
                p "Aqui está seu Pote com Jeleia! Vai ficar ainda melhor depois de alguns dias."
                "Você recebeu um Pote com Jeleia."
                
            elif resultado == "falta_aguas":
                p "Precisamos de pelo menos 5 águas-vivas para fazer uma boa jeleia. Vamos caçar mais?"
                
                menu:
                    "Vamos caçar águas-vivas":
                        p "Vamos lá!"
                        jump minigame_aguasvivas
                        
                    "Talvez mais tarde":
                        p "Quando quiser, é só me avisar."
                
            elif resultado == "falta_pote":
                p "Precisamos de um pote para armazenar a jeleia. Vá comprar um na loja do Sr. Siriguejo."
            
            jump patrick_opcoes
            
        "Ir embora":
            p "Tchau! Volte quando quiser!"
            jump room4

# Conversas simples com Patrick
label conversar_patrick:
    menu:
        "Sobre o que você quer conversar?"
        
        "Como vai seu dia?":
            p "Meu dia vai ótimo! Passei a manhã olhando para as nuvens, depois comi um pouco de areia, e agora estou aqui com você!"
            
        "Alguma novidade em Fenda do Bikini?":
            p "Hmm, o Lula Molusco está irritado como sempre. O Sr. Siriguejo continua obcecado com dinheiro."
            p "E tem uma nova exposição de arte moderna no museu! São pedras... só pedras mesmo."
            
        "O que você gosta de fazer?":
            p "Eu gosto de dormir, comer, pescar águas-vivas com você, e olhar para as estrelas!"
            p "Às vezes também gosto de não fazer absolutamente nada. Sou muito bom nisso."
            
        "Voltar":
            jump patrick_opcoes
            
    jump conversar_patrick
