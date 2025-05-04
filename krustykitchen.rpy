label menu_principal_siririca:
    menu:
        "Conversar":
            $ escolha = "conversar"
            jump conversa_siririca
            
        "Pedir um aumento":
            $ escolha = "aumento"
            # Esconder krab a antes de ir para aumento_siririca
            hide krab a
            jump aumento_siririca
            
        "Perguntar sobre o Rola Molusco":
            $ escolha = "molusco"
            # Esconder krab a antes de ir para info_molusco
            hide krab a
            jump info_molusco
            
        "Mexer na gaveta secreta":
            $ escolha = "gaveta"
            # Esconder krab a antes de ir para gaveta_secreta
            hide krab a
            jump gaveta_secreta
            
        "Voltar":
            call screen lobbykk with fade

label conversa_siririca:
    # Aqui não precisamos esconder nada, apenas mostrar krab4
    show krab4:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Tem cinco segundos para falar o que quer. Cada segundo custa dinheiro, rapaz!"
    
    jump menu_conversa_siririca

label menu_conversa_siririca:
    menu:
        "Perguntar sobre a história do Siri Cracudo":
            # Esconder krab4 apenas (que é o que está na tela) e mostrar happy
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Ah, essa é uma história inspiradora sobre CAPITALISMO E DINHEIRO!"
            
            k "Eu comecei com um hamburger velho, uma frigideira enferrujada e MUITA AMBIÇÃO!"
            
            k "E agora tenho esse império que me rende TANTO DINHEIRO HAHAHA"
            
            k "Agora volte ao trabalho antes que eu mude de ideia e te DEMITA!"
            
            jump menu_conversa_siririca
        
        "Perguntar sobre a filha dele":
            # Se krab happy estiver na tela, esconder apenas ele
            # Se krab4 estiver na tela, não precisamos esconder
            # Como não sabemos qual está, usando conditional hiding
            if renpy.showing("krab happy"):
                hide krab happy
            show krab a:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Pera aí, como VOCÊ sabe que eu tenho uma filha?"
            
            k "Você anda seguindo a Pérola por aí? Se eu descobrir que você está dando em cima dela..."
            
            # Esconder apenas o que está na tela (krab4) e mostrar kradeath
            hide krab4
            show kradeath
            
            k "VOU ENFIAR ESSE HAMBÚRGUER DE SIRI NO SEU..."
            
            # Esconder kradeath e mostrar krab a
            hide kradeath
            show krab a:
                zoom 0.6 xpos 1000 ypos 400
            
            k "Ahem... volte ao trabalho, Bob Esperma."
            
            jump menu_conversa_siririca
        
        "Falar sobre o tempo":
            # Esconder o que estiver na tela (krab a ou krab happy) e mostrar krab4
            if renpy.showing("krab a"):
                hide krab a
            elif renpy.showing("krab happy"):
                hide krab happy
            show krab4:
                zoom 0.6 xpos 1000 ypos 400
            
            k "O tempo? O TEMPO É DINHEIRO, RAPAZ!"
            
            k "Enquanto estamos aqui falando sobre NADA, você podia estar lá fritando hambúrgueres e ME DANDO LUCRO!"
            
            jump menu_conversa_siririca
        
        "Fazer outra coisa":
            # Esconder o que estiver na tela e mostrar krab a
            if renpy.showing("krab4"):
                hide krab4
            elif renpy.showing("krab happy"):
                hide krab happy
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade

# Adicionar nova variável padrão para rastrear se a ideia já foi sugerida
default sugeriu_promocao_batata = False

label aumento_siririca:
    # Mostrar kradeath (não precisamos esconder nada aqui)
    show kradeath
    
    k "HAHAHAHAHAHA!"
    
    # Esconder kradeath e mostrar krab4
    hide kradeath
    show krab4:
        zoom 0.6 xpos 1000 ypos 400
    
    k "Essa foi boa, rapaz. AUMENTO? No Siri Cracudo?"
    
    menu:
        "Insistir no aumento":
            # Esconder o que está na tela (krab4) e mostrar kradeath
            hide krab4
            show kradeath
            
            k "ESCUTA AQUI SEU PEDAÇO DE ESPONJA INÚTIL!"
            
            k "EU POSSO TE SUBSTITUIR POR QUALQUER PARASITA DO OCEANO!"
            
            k "Agora volte pra cozinha antes que eu te DEMITA!"
            
            $ money -= 5
            "Seu Siririca multou você em 5 dólares por insubordinação!"
            
            # Esconder antes de voltar ao menu
            hide kradeath
            jump menu_principal_siririca
        
        "Oferecer trabalhar mais horas":
            # Esconder krab4 e mostrar krab happy
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "AGORA ESTAMOS FALANDO A MESMA LÍNGUA!"
            
            k "Trabalhar DE GRAÇA depois do expediente? ISSO SIM é espírito de equipe!"
            
            k "Continue assim e talvez eu pense em te dar um aumento de 0,1%% no próximo século!"
            
            $ money += 2
            "Você ganhou 2 dólares como 'incentivo'!"
            
            # Esconder antes de voltar ao menu
            hide krab happy
            jump menu_principal_siririca
        
        # A opção só aparece se ainda não foi sugerida
        "Sugerir uma promoção 'Traga sua batata e pague 2x mais'" if not sugeriu_promocao_batata:
            # Esconder krab4 e mostrar krab happy
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
            
            # Esconder antes de voltar ao menu
            hide krab happy
            jump menu_principal_siririca
        
        "Fazer outra coisa":
            # Esconder krab4 e mostrar krab a
            hide krab4
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade

label info_molusco:
    # Mostrar krab4 diretamente
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
            # Esconder krab4 e mostrar krab happy
            hide krab4
            show krab happy:
                zoom 0.6 xpos 1000 ypos 400
            
            k "E pagar dois salários? Tá maluco?"
            
            k "Você faria o trabalho dele também?"
            
            menu:
                "Sim, posso fazer":
                    k "HAHAHA, você já está aceitando fazer HORA EXTRA de graça!"
                    
                    k "Agora quer fazer o trabalho do Lula também? SEM CHANCE!"
                    
                    k "Não vou demitir ele e contratar outro funcionário quando posso explorar DOIS de uma vez!"
                    
                    # Esconder antes de voltar ao menu
                    hide krab happy
                    jump menu_principal_siririca
                
                "Não, melhor não":
                    k "É o que eu pensava. Volte ao trabalho!"
                    
                    # Esconder antes de voltar ao menu
                    hide krab happy
                    jump menu_principal_siririca
        
        "Fazer outra coisa":
            # Esconder krab4 e mostrar krab a
            hide krab4
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade

label gaveta_secreta:
    # Não precisamos esconder nada aqui, pois a cena muda naturalmente
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
                    
                    # Esconder antes de voltar ao menu
                    hide kradeath
                    jump menu_principal_siririca
                
                "Fechar a gaveta rapidamente":
                    "Você fecha a gaveta bem a tempo"
                    
                    show krab a at center with moveinright:
                        zoom 0.75
                    
                    k "O que você está fazendo perto da minha mesa, rapaz?"
                    
                    menu:
                        "Só vim limpar a poeira, chefe!":
                            # Esconder krab a e mostrar krab happy
                            hide krab a
                            show krab happy:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "Ah, limpeza gratuita! Assim que eu gosto!"
                            
                            k "Continue assim que um dia você talvez ganhe um aumento de meio centavo!"
                            
                            # Esconder antes de voltar ao menu
                            hide krab happy
                            jump menu_principal_siririca
                        
                        "Procurando canetas para a cozinha":
                            # Esconder krab a e mostrar krab4
                            hide krab a
                            show krab4:
                                zoom 0.6 xpos 1000 ypos 400
                            
                            k "CANETAS? Na cozinha?"
                            
                            k "Você acha que CANETAS crescem em árvores? São CARAS!"
                            
                            k "Use carvão ou tinta de lula como todo mundo!"
                            
                            # Esconder antes de voltar ao menu
                            hide krab4
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
            
            # Esconder antes de voltar ao menu
            hide krab a
            jump menu_principal_siririca
        
        "Fazer outra coisa":
            # Mostrar krab a diretamente
            show krab a at center:
                zoom 0.75
            
            jump menu_principal_siririca
            
        "Voltar":
            call screen lobbykk with fade