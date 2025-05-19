label menu_principal_siririca:
    menu:
        "Conversar":
            $ escolha = "conversar"
            jump conversa_siririca
            
        "Pedir um aumento":
            $ escolha = "aumento"
            # Esconder krab a antes de ir para aumento_siririca para evitar sobreposição
            hide krab a
            jump aumento_siririca
            
        "Perguntar sobre o Rola Molusco":
            $ escolha = "molusco"
            # Esconder krab a antes de ir para info_molusco para evitar sobreposição
            hide krab a
            jump info_molusco
            
        "Mexer na gaveta secreta":
            $ escolha = "gaveta"
            # Esconder krab a antes de ir para gaveta_secreta para evitar sobreposição
            hide krab a
            jump gaveta_secreta
            
        "Voltar":
            call screen lobbykk with fade

label conversa_siririca:
    # Esconder qualquer Siririca anterior antes de mostrar um novo
    hide krab a
    hide krab happy
    hide krab4
    
    # Mostrar apenas krab4 na posição correta
    show krab4:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Tem cinco segundos para falar o que quer. Cada segundo custa dinheiro, rapaz!"
    
    jump menu_conversa_siririca

label menu_conversa_siririca:
    menu:
        "Perguntar sobre a história do Siri Cracudo":
            # Esconder Siririca anterior para evitar sobreposição
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Ah, essa é uma história inspiradora sobre CAPITALISMO E DINHEIRO!"
            
            k "Eu comecei com um hamburger velho, uma frigideira enferrujada e MUITA AMBIÇÃO!"
            
            k "E agora tenho esse império que me rende TANTO DINHEIRO HAHAHA"
            
            k "Agora volte ao trabalho antes que eu mude de ideia e te DEMITA!"
            
            jump menu_conversa_siririca
        
        "Perguntar sobre a filha dele":
            # Esconder qualquer Siririca atual antes de mostrar outro
            hide krab happy
            hide krab4
            show krab a:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Pera aí, como VOCÊ sabe que eu tenho uma filha?"
            
            k "Você anda seguindo a Pérola por aí? Se eu descobrir que você está dando em cima dela..."
            
            # Esconder krab a antes de mostrar kradeath
            hide krab a
            show kradeath
            
            k "VOU ENFIAR ESSE HAMBÚRGUER DE SIRI NO SEU..."
            
            # Esconder kradeath antes de mostrar krab a novamente
            hide kradeath
            show krab a:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Ahem... volte ao trabalho, Bob Esperma."
            
            jump menu_conversa_siririca
        
        "Falar sobre o tempo":
            # Esconder qualquer Siririca atual antes de mostrar krab4
            hide krab a
            hide krab happy
            show krab4:
                zoom 0.6 xpos 1000 ypos 400
            
            k "O tempo? O TEMPO É DINHEIRO, RAPAZ!"
            
            k "Enquanto estamos aqui falando sobre NADA, você podia estar lá fritando hambúrgueres e ME DANDO LUCRO!"
            
            jump menu_conversa_siririca
        
        "Fazer outra coisa":
            # Esconder qualquer Siririca atual antes de voltar
            hide krab happy
            hide krab4
            hide krab a
            
            # Mostrar krab a centralizado para o menu principal
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            # Esconder tudo antes de voltar ao lobby
            hide krab happy
            hide krab4
            hide krab a
            call screen lobbykk with fade

# Adicionar nova variável padrão para rastrear se a ideia já foi sugerida
default sugeriu_promocao_batata = False

label aumento_siririca:
    # Esconder qualquer Siririca atual antes de mostrar kradeath
    hide krab a
    hide krab4
    hide krab happy
    
    # Mostrar kradeath em posição adequada
    show kradeath
    
    k "HAHAHAHAHAHA!"
    
    # Esconder kradeath antes de mostrar krab4
    hide kradeath
    show krab lsmile:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Essa foi boa, rapaz. AUMENTO? No Siri Cracudo?"
    
    menu:
        "Insistir no aumento":
            # Esconder krab4 antes de mostrar kradeath
            hide krab lsmile
            show kradeath:
                zoom 0.8 xpos 960 ypos 500  # Posição ajustada
            
            k "ESCUTA AQUI SEU PEDAÇO DE ESPONJA INÚTIL!"
            
            k "EU POSSO TE SUBSTITUIR POR QUALQUER PARASITA DO OCEANO!"
            
            k "Agora volte pra cozinha antes que eu te DEMITA!"
            
            $ money -= 5
            "Seu Siririca multou você em 5 dólares por insubordinação!"
            
            # Esconder kradeath antes de voltar ao menu
            hide kradeath
            jump menu_principal_siririca
        
        "Oferecer trabalhar mais horas":
            # Esconder krab4 antes de mostrar krab happy
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "AGORA ESTAMOS FALANDO A MESMA LÍNGUA!"
            
            k "Trabalhar DE GRAÇA depois do expediente? ISSO SIM é espírito de equipe!"
            
            k "Continue assim e talvez eu pense em te dar um aumento de 0,1%% no próximo século!"
            
            $ money += 2
            "Você ganhou 2 dólares como 'incentivo'!"
            
            # Esconder krab happy antes de voltar ao menu
            hide krab happy
            jump menu_principal_siririca
        
        # A opção só aparece se ainda não foi sugerida
        "Sugerir uma promoção 'Traga sua batata e pague 2x mais'" if not sugeriu_promocao_batata:
            # Esconder krab4 antes de mostrar krab happy
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "MEU DEUS! Você é um GÊNIO, rapaz!"
            
            k "Fazemos eles trazerem os ingredientes E pagarem mais? HAHAHA!"
            
            k "Vou implementar isso AGORA MESMO!"
            
            $ money += 15
            "Você recebeu 15 dólares de comissão pela ideia!"
            
            # Marcar que a ideia já foi sugerida
            $ sugeriu_promocao_batata = True
            
            # Esconder krab happy antes de voltar ao menu
            hide krab happy
            jump menu_principal_siririca
        
        "Fazer outra coisa":
            # Esconder krab4 antes de voltar
            hide krab4
            
            # Mostrar krab a para o menu principal
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            # Esconder tudo antes de voltar ao lobby
            hide krab4
            call screen lobbykk with fade

label info_molusco:
    # Esconder qualquer Siririca atual antes de mostrar krab4
    hide krab a
    hide krab happy
    
    # Mostrar krab4 na posição correta
    show krab sus:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Aquele punheteiro inútil? O que tem ele?"
    
    k "Passa o dia inteiro reclamando e xingando os clientes pelas costas!"
    
    k "Mas ele é barato, então eu mantenho por aqui..."
    
    menu:
        "Perguntar onde ele está":
            k "Provavelmente no caixa, sendo mal-educado com os clientes como sempre."
            
            k "Ou escondido no banheiro batendo... quer dizer, tocando clarinete."
            
            jump menu_principal_siririca
        
        "Sugerir demitir o Lula Molusco":
            # Esconder krab4 antes de mostrar krab happy
            hide krab sus
            show krab madtalk:
                zoom 0.6 xpos 1000 ypos 400
            
            k "E pagar dois salários? Tá maluco?"
            
            k "Você faria o trabalho dele também?"
            
            menu:
                "Sim, posso fazer":
                    k "HAHAHA, você já está aceitando fazer HORA EXTRA de graça!"
                    
                    k "Agora quer fazer o trabalho do Lula também? SEM CHANCE!"
                    
                    k "Não vou demitir ele e contratar outro funcionário quando posso explorar DOIS de uma vez!"
                    
                    # Esconder krab happy antes de voltar ao menu
                    hide krab madtalk
                    jump menu_principal_siririca
                
                "Não, melhor não":
                    k "É o que eu pensava. Volte ao trabalho!"
                    
                    # Esconder krab happy antes de voltar ao menu
                    hide krab happy
                    jump menu_principal_siririca
        
        "Fazer outra coisa":
            # Esconder krab4 antes de voltar
            hide krab4
            
            # Mostrar krab a para o menu principal
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            # Esconder tudo antes de voltar ao lobby
            hide krab4
            call screen lobbykk with fade

label gaveta_secreta:
    # Esconder qualquer Siririca atual antes de continuar
    hide krab a
    hide krab4
    hide krab happy
    
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
                    
                    # Mostrar kradeath na posição correta
                    show kradeath at center with moveinright
                    
                    k "SEU LADRÃOZINHO DE MEIA TIGELA!"
                    
                    k "TENTANDO ROUBAR MEU PRECIOSO DINHEIRO?!"
                    
                    "Seu Siririca agarra você pela gola"
                    
                    k "VOU TE JOGAR NO FREEZER COM O ÚLTIMO FUNCIONÁRIO QUE TENTOU ME ROUBAR!"
                    
                    $ money = 0
                    "Seu Siririca confiscou todo o seu dinheiro como punição!"
                    
                    # Esconder kradeath antes de voltar ao menu
                    hide kradeath
                    jump menu_principal_siririca
                
                "Fechar a gaveta rapidamente":
                    "Você fecha a gaveta bem a tempo"
                    
                    # Mostrar krab a na posição correta
                    show krab a at center with moveinright:
                        zoom 0.75
                    
                    k "O que você está fazendo perto da minha mesa, rapaz?"
                    
                    menu:
                        "Só vim limpar a poeira, chefe!":
                            # Esconder krab a antes de mostrar krab happy
                            hide krab a
                            show krab happy:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "Ah, limpeza gratuita! Assim que eu gosto!"
                            
                            k "Continue assim que um dia você talvez ganhe um aumento de meio centavo!"
                            
                            # Esconder krab happy antes de voltar ao menu
                            hide krab happy
                            jump menu_principal_siririca
                        
                        "Procurando canetas para a cozinha":
                            # Esconder krab a antes de mostrar krab4
                            hide krab a
                            show krab4:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "CANETAS? Na cozinha?"
                            
                            k "Você acha que CANETAS crescem em árvores? São CARAS!"
                            
                            k "Use carvão ou tinta de lula como todo mundo!"
                            
                            # Esconder krab4 antes de voltar ao menu
                            hide krab4
                            jump menu_principal_siririca
                
                "Fazer outra coisa":
                    jump menu_principal_siririca
                    
                "Voltar":
                    call screen lobbykk with fade
        
        "Melhor não arriscar":
            "Você decide que não vale a pena arriscar sua vida por curiosidade"
            
            # Mostrar krab a na posição correta
            show krab a at center with moveinleft:
                zoom 0.75
            
            k "O que você está fazendo parado aí? O tempo é DINHEIRO!"
            
            k "Volte para a cozinha AGORA! Tem clientes esperando!"
            
            # Esconder krab a antes de voltar ao menu
            hide krab a
            jump menu_principal_siririca
        
        "Fazer outra coisa":
            # Mostrar krab a diretamente na posição correta
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade