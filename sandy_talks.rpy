# sandy_talks.rpy - Arquivo contendo apenas os diálogos e sequências para as cenas com Sandy

init python:
    def obter_dialogo_peitos():
        # Retorna um diálogo aleatório para quando Sandy mostra os peitos
        import random
        dialogos = [
            "Você quer... ver meus peitos? Bem, acho que posso mostrar rapidinho pra você, parceiro...",
            "Sabe que isso não é muito científico, né? Mas se você gosta tanto... você tá diferente hoje, Bob...",
            "Olha só o que você me faz fazer, seu cabeção! Isso fica só entre a gente, viu? Por todos os touros do Texas!",
            "O ar daqui é bem fresquinho sem a roupa... Gosta do que tá vendo, vaqueiro? Por que tá me olhando assim?",
            "Normalmente sou mais reservada, mas com você eu me sinto diferente... tá mais macho hoje, parceiro..."
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_punheta():
        # Retorna um diálogo aleatório para quando Sandy dá uma punheta
        import random
        dialogos = [
            ["sd", "Hmm... Quer uma ajudinha manual, parceiro? No Texas chamamos isso de 'domando o touro'..."],
            ["sd", "Você tá diferente, Bob... mais bruto. Gosto disso. Vamo ver se aguenta a famosa punheta do Texas!"],
            ["sd", "Nunca pensei que usaria minhas habilidades de engenheira desse jeito... caramba, você parece outra pessoa!"],
            ["sd", "Yeehaw! Vamos ver quanto você aguenta, esponjinha... pelas barbas do profeta, você tá enorme!"],
            ["sd", "No Texas, a gente chamava isso de 'ordenhar o touro'... caralho, você tá diferente do meu Bob habitual!"]
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_buceta():
        # Retorna um diálogo aleatório para quando Sandy mostra a buceta
        import random
        dialogos = [
            ["sd", "Quer ver minha bucetinha de esquilo, parceiro? Bem... acho que já estamos íntimos o suficiente..."],
            ["sd", "Nunca mostrei isso pra ninguém no Fundo do Bikini... Você é especial, Bob, mesmo tando tão estranho..."],
            ["sd", "Puta que pariu! Nunca achei que mostraria minha xoxota pra alguém, mas você me deixa à vontade!"],
            ["sd", "Espero que goste do que vai ver. É um tesouro do Texas, como dizem! Que cara de tarado é essa?"],
            ["sd", "Quer conhecer o lado selvagem de uma esquilo? Prepare-se... caralho, você tá mais selvagem que o normal!"]
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_cuzinho():
        # Retorna um diálogo aleatório para quando Sandy permite anal
        import random
        if vezes_cuzinho == 0:
            dialogos = [
                ["sd", "Meu cuzinho cowboy? Você quer experimentar... aquele lugar? Nunca fiz isso antes, parceiro..."],
                ["sd", "Por trás? Tenho um pouco de medo... Promete ir devagar? Pelos cornos do diabo, você tá diferente!"],
                ["sd", "Isso é algo que nunca fiz nem no Texas... Tem certeza? Puta merda, você tá tão estranho!"],
                ["sd", "Ai meu Deus... Acho que podemos tentar, mas seja gentil, ok? Caralho, você parece outro!"],
                ["sd", "Essa é uma fronteira que nunca explorei... Yeehaw! Nunca te vi tão... mandão antes, Bob!"]
            ]
        elif vezes_cuzinho == 1:
            dialogos = [
                ["sd", "Da última vez foi um pouco dolorido... Mas agora tô mais preparada. Caralho, você tá tão bom!"],
                ["sd", "Vamos com calma de novo? No Texas dizem que a segunda cavalgada é sempre melhor, parceiro!"],
                ["sd", "Hmm... Tenho pensado nisso desde a última vez. Vem cá, vaqueiro! Me cavalga de novo!"],
                ["sd", "Quem diria que uma cientista texana como eu gostaria desse tipo de... experimento!"],
                ["sd", "Dessa vez temos que usar mais lubrificante... Vai ser melhor pra nós dois, porra!"]
            ]
        elif vezes_cuzinho == 2:
            dialogos = [
                ["sd", "Já tô ficando boa nisso, né? Vem cá, vamos fazer de novo... adoro esse seu lado animal!"],
                ["sd", "Acho que encontrei um novo hobby científico pra estudar a fundo... caralho, você mudou tanto!"],
                ["sd", "Quem diria que o cuzinho de uma esquila texana seria tão compatível com... sua pica gostosa!"],
                ["sd", "Mmm... Mal posso esperar. Dessa vez quero sentir tudo! Puta merda, você tá tão bom nisso!"],
                ["sd", "Sabe, no Texas a gente não fala sobre isso, mas... você virou outra pessoa, e eu adoro!"]
            ]
        else:
            dialogos = [
                ["sd", "Ah, meu cowboy favorito chegou! Sabe o que eu quero, não é? Quero dar o cu pra você!"],
                ["sd", "Já tô pronta pra você... Nem preciso mais de muita preparação. Yeehaw! Vamos cavalgar!"],
                ["sd", "Acho que descobri meu talento secreto. Meu cuzinho texano ama sua pica, parceiro!"],
                ["sd", "Isso virou meu vício, sabia? Nenhum experimento científico me dá tanto prazer. Caralho!"],
                ["sd", "Vem logo, Bob. Meu cuzinho tá latejando... você é tão mais macho agora, puta merda!"]
            ]
        return random.choice(dialogos)
    
    def obter_dialogo_recusa():
        # Retorna um diálogo aleatório para quando Sandy recusa por já ter feito no dia
        import random
        dialogos = [
            "Já fizemos isso hoje, volte amanhã cowboy taradão! Pelos cornos do diabo, você tá insaciável!",
            "Ei, calma aí! Até uma esquilo precisa de descanso! Puta merda, desde quando ficou tão exigente?",
            "Hmm, alguém tá muito ansioso! Mas vai ter que esperar até amanhã.",
            "Tenho outra coisas para fazer... Que tal voltarmos a isso amanhã? ",
            "Você é insaciável, não é? Mas vamos deixar pra amanhã, ok?",
            "Por hoje chega, mas volte amanhã com essa rola grossa bem dura pra mim!" 
        ]
        return random.choice(dialogos)
    
    # Sequências de diálogos para cada cena sexual
    def obter_sequencia_peitos(vez):
        sequencias = [
            # Primeira vez
            [
                ["sd", "Você quer mesmo ver meus peitos, Bob? Diabos, você tá tão esquisito hoje..."],
                ["sd", "Bem... acho que não faz mal mostrar rapidinho... mas você tá diferente..."],
                ["sd", "Só não conte pra ninguém, ok? Caralho, para de me olhar desse jeito!"],
                ["", "Sandy tira a parte de cima do biquíni lentamente..."],
                ["sd", "E então... o que acha? Por que tá com essa cara de tarado?"],
                ["sd", "Sei que não são grandes como os das sereias... puta merda, você nunca me olhou assim antes..."],
                ["sd", "Você tá gostando do que vê? Tá babando, Bob... caralho, isso não é normal..."],
                ["", "Sandy percebe o olhar estranho e predatório de Bob"],
                ["sd", "Seu olhar tá me deixando excitada... mas também meio assustada, vaqueiro..."],
                ["", "Você nota os mamilos dela ficando mais rígidos"],
                ["sd", "Ahhh... Isso é tão... diferente... diabos, você tá tão estranho hoje..."],
                ["", "Sandy respira fundo e fecha os olhos, aproveitando a sensação, mas confusa com o comportamento diferente"]
            ],
            
            # Segunda vez
            [
                ["sd", "Quer ver meus peitos de novo, seu safadinho? Puta merda, você tá tão diferente do antigo Bob..."],
                ["sd", "Estive pensando nisso desde a última vez... você é como um Bob novo e selvagem, parceiro..."],
                ["", "Sandy remove a parte superior do biquíni com mais confiança desta vez"],
                ["sd", "Gosta do que vê? Quer tocá-los? Caralho, você nunca foi tão direto assim antes..."],
                ["", "Suas mãos grosseiras tocam os peitos da Sandy com avidez"],
                ["sd", "Mmm... Isso é bom... mas você tá tão bruto, Bob... que porra aconteceu contigo?"],
                ["sd", "Pode apertar um pouco mais... nossa, não precisava ser tão forte, seu animal!"],
                ["", "Ela guia suas mãos pelos seus mamilos, surpresa com sua agressividade"],
                ["sd", "Ahh! Isso! Continue... mas com menos força, seu bruto texano!"],
                ["", "Sandy começa a respirar mais rápido"],
                ["sd", "Ohhh Bob... Você me faz sentir coisas incríveis! Caralho, quem é você realmente?"],
                ["", "Ela treme levemente enquanto um pequeno orgasmo percorre seu corpo"]
            ],
            
            # Terceira vez - NOVA VERSÃO COM VARIAÇÕES
            [
                # Linha 1 - três variações
                [
                    ["sd", "Ora, vejam só! O vaqueiro voltou pra ver o rodeio, não é mesmo?"],
                    ["sd", "Puxa vida! Nunca vi um homem tão vidrado em peitos como você, Bob!"],
                    ["sd", "Voltou pra admirar a vista, parceiro? Tá mais ávido que um coiote no deserto!"]
                ],
                # Linha 2 - três variações
                [
                    ["", "Sandy sorri enquanto tira a parte de cima do biquíni, notando seu olhar intenso"],
                    ["", "Ela remove o biquíni com um movimento confiante, analisando sua reação"],
                    ["", "Sandy tira o biquíni e sacode seus seios provocativamente, testando sua reação"]
                ],
                # Linha 3 - três variações
                [
                    ["sd", "Caramba, Bob! Seus olhos tão quase saltando pra fora, diabos!"],
                    ["sd", "Puxa vida! Você tá olhando como um gato pro peixe! Nunca te vi assim!"],
                    ["sd", "Pelos chifres de um touro bravo! Que olhar faminto é esse, parceiro?"]
                ],
                # Linha 4 - três variações
                [
                    ["sd", "Cacete, você tá me olhando como um predador do Texas olha pra última coxa de frango..."],
                    ["sd", "Nossa, Bob! Com esse olhar você parece que tá há anos sem ver uma mulher!"],
                    ["sd", "Puta merda! Esse seu olhar tá mais quente que o sol do Texas em pleno verão!"]
                ],
                # Linha 5 - três variações
                [
                    ["", "Você mantém uma expressão dura e séria, analisando cada detalhe dos seios dela"],
                    ["", "Seus olhos percorrem cada centímetro dos seios dela com uma intensidade predatória"],
                    ["", "Você observa friamente, sem piscar, memorizando cada curva do corpo dela"]
                ],
                # Linha 6 - três variações
                [
                    ["sd", "Porra! Desde quando você ficou tão... observador? Nunca te vi assim antes!"],
                    ["sd", "Diabos! O que aconteceu com você, Bob? Tá parecendo outro homem!"],
                    ["sd", "Caramba! Quem diria que um dia o Bob ia me olhar assim? Você tá diferente demais!"]
                ],
                # Linha 7 - três variações
                [
                    ["sd", "Ah, caralho! Esse seu olhar tá me deixando toda molhada! Tá diferente demais..."],
                    ["sd", "Merda, Bob! Você tá me excitando só com esse olhar! O que fizeram com você?"],
                    ["sd", "Puta que pariu! Esse seu jeito tá me deixando toda arrepiada! Onde aprendeu isso?"]
                ],
                # Linha 8 - três variações
                [
                    ["", "Ela exibe os seios com orgulho, percebendo a intensidade do seu olhar"],
                    ["", "Sandy ajusta a postura para mostrar melhor os seios, gostando da sua reação"],
                    ["", "Ela se aproxima mais, exibindo os seios de um ângulo melhor para você"]
                ],
                # Linha 9 - três variações
                [
                    ["sd", "Pelos cornos de um touro selvagem! Gosta do que vê, parceiro? Nunca te vi tão focado!"],
                    ["sd", "Tá gostando da vista, vaqueiro? Parece que vai me devorar só com os olhos!"],
                    ["sd", "Que é isso, cowboy? Parece que nunca viu peitos texanos antes! Tá hipnotizado!"]
                ],
                # Linha 10 - três variações
                [
                    ["", "Você mantém sua expressão fria e dominadora"],
                    ["", "Seu olhar permanece implacável, quase intimidador"],
                    ["", "Você não demonstra nenhuma emoção, apenas um desejo animal"]
                ],
                # Linha 11 - três variações
                [
                    ["sd", "Ahhh! Diabos! Tem algo no seu olhar que tá me deixando louca! Você tá mais... macho!"],
                    ["sd", "Caralho, Bob! Só de você me olhar assim já tô quase gozando! Você tá tão... homem!"],
                    ["sd", "Puta merda! Esse olhar... tá me fazendo derreter toda! Nunca te vi tão dominador!"]
                ],
                # Linha 12 - três variações
                [
                    ["", "Sandy respira fundo e fecha os olhos, visivelmente excitada apenas pelo seu olhar"],
                    ["", "Ela morde o lábio inferior, seu corpo respondendo intensamente ao seu olhar predatório"],
                    ["", "Sandy estremece de prazer, ficando excitada apenas com a intensidade do seu olhar"]
                ]
            ],
            
            # Repetições após completar - NOVA VERSÃO COM VARIAÇÕES
            [
                # Linha 1 - três variações
                [
                    ["sd", "Yeehaw! Meus peitos tavam com saudade do seu olhar, Bob..."],
                    ["sd", "Ora, vejam só quem voltou! Meus peitinhos texanos tavam te esperando!"],
                    ["sd", "Vamos lá, cowboy! Sei que você veio admirar a paisagem de novo!"]
                ],
                # Linha 2 - três variações
                [
                    ["", "Ela remove a parte de cima do biquíni com habilidade, já acostumada com seu comportamento"],
                    ["", "Sandy tira o biquíni e balança os seios provocativamente para você"],
                    ["", "Ela se livra do biquíni com um movimento rápido, ansiosa para mostrar os seios"]
                ],
                # Linha 3 - três variações
                [
                    ["sd", "Puta merda, essa sua pica tá dura como pedra! Só de olhar pra mim, hein?"],
                    ["sd", "Caramba, Bob! Seu pau tá tão duro que podia cortar diamante! Tudo isso só de olhar?"],
                    ["sd", "Pelos cornos do diabo! Olha o tamanho desse volume na sua calça! Só de me ver?"]
                ],
                # Linha 4 - três variações
                [
                    ["sd", "Caralho, esse seu jeito de olhar... tão direto, tão bruto... me excita pra caralho!"],
                    ["sd", "Diabos, Bob! Esse seu olhar faminto tá me deixando toda molhada!"],
                    ["sd", "Puta que pariu! Como você consegue me deixar tão excitada só com esse olhar?"]
                ],
                # Linha 5 - três variações
                [
                    ["", "Você observa com frieza, sem demonstrar emoção, apenas desejo animal"],
                    ["", "Seus olhos percorrem o corpo dela como um predador avaliando sua presa"],
                    ["", "Você mantém um olhar penetrante, quase violento em sua intensidade"]
                ],
                # Linha 6 - três variações
                [
                    ["sd", "Santa mãe do Texas! Continue olhando assim! Você tá tão grosso na cueca, puta que pariu!"],
                    ["sd", "Jesus Cristo! Esse pau tá enorme! Só de me olhar você fica assim, caralho!"],
                    ["sd", "Cacete! Olha o tamanho disso! Você tá mais duro que poste de cerca texano!"]
                ],
                # Linha 7 - três variações
                [
                    ["sd", "Sandy ajeita os seios, exibindo-os melhor para sua observação detalhada"],
                    ["sd", "Ela massageia os próprios seios, oferecendo um show privado para você"],
                    ["sd", "Sandy aperta os seios juntos, criando um decote provocante só para seu olhar"]
                ],
                # Linha 8 - três variações
                [
                    ["sd", "Ahh! Seu olhar é mais potente que uma pistola carregada! Me mata de tesão, caralho!"],
                    ["sd", "Mmm! Como você consegue me deixar tão excitada sem nem me tocar? Tá me matando!"],
                    ["sd", "Deus do céu! Esse seu olhar tá me fodendo sem você nem encostar em mim!"]
                ],
                # Linha 9 - três variações
                [
                    ["", "Ela se contorce sob seu olhar intenso"],
                    ["", "Sandy começa a se mover sensualmente, respondendo ao seu olhar dominador"],
                    ["", "Ela respira mais rápido, claramente excitada apenas por ser observada por você"]
                ],
                # Linha 10 - três variações
                [
                    ["sd", "Não para de olhar, seu filho da puta! Tão focado, tão... animal!"],
                    ["sd", "Continua me olhando assim, caralho! Tá me deixando louca!"],
                    ["sd", "Me devora com esses olhos, porra! Nunca senti algo assim antes!"]
                ],
                # Linha 11 - três variações
                [
                    ["", "Ela estremece ao ver o volume enorme na sua calça"],
                    ["", "Sandy olha fixamente para o volume na sua calça, lambendo os lábios"],
                    ["", "Ela não consegue tirar os olhos do seu pau duro marcando na calça"]
                ],
                # Linha 12 - três variações
                [
                    ["sd", "AHHHHH! PUTA MERDA! SIM! Sandy geme, excitada pelo seu olhar dominador e seu pau duro"],
                    ["sd", "CARALHO! TÔ GOZANDO SÓ COM SEU OLHAR! Você é um animal, Bob!"],
                    ["sd", "PELOS CORNOS DO DIABO! ISSO! Nunca pensei que gozaria só de ser olhada assim!"]
                ]
            ]
        ]
        
        # Se for terceira vez ou posterior, precisamos montar uma sequência aleatória
        if vez >= 3:
            # Vamos usar a estrutura da última sequência (índice 3)
            sequencia_base = sequencias[3]
            sequencia_final = []
            
            # Para cada linha, escolha aleatoriamente uma das três variações
            import random
            for linha in sequencia_base:
                variacao_escolhida = random.choice(linha)
                sequencia_final.append(variacao_escolhida)
            
            return sequencia_final
        
        # Se for primeira ou segunda vez, retorna a sequência original
        return sequencias[vez]
    
    def obter_sequencia_punheta(vez):
        sequencias = [
            # Primeira vez
            [
                ["sd", "Então... você quer que eu te toque? Caralho, você tá tão estranho hoje, parceiro..."],
                ["sd", "Nunca fiz isso antes... me guia? Diabos, por que você tá tão ansioso?"],
                ["", "Sandy se aproxima timidamente, notando sua expressão diferente"],
                ["sd", "É assim que se faz? Puta merda, por que você tá gemendo desse jeito?"],
                ["", "Ela começa a movimentar a mão lentamente, surpresa com sua reação exagerada"],
                ["sd", "Estou fazendo certo? Pelos cornos do diabo, nunca te vi tão excitado..."],
                ["", "Você assente grosseiramente, sentindo o prazer aumentar"],
                ["sd", "Você tá ficando todo molhado, Bob... isso é normal pra uma esponja do Texas?"],
                ["sd", "Devo ir mais rápido? Você tá tremendo demais, vaqueiro..."],
                ["", "Seus movimentos se intensificam"],
                ["bob", "Ah! Sandy! Porra, vou...!"],
                ["", "Você atinge o clímax enquanto Sandy observa fascinada e um pouco assustada"]
            ],
            # Segunda vez
            [
                ["sd", "Quer sentir minha mão de novo, seu tarado? Caralho, você tá tão diferente agora..."],
                ["sd", "Acho que aprendi alguns truques desde a última vez... "],
                ["", "Sandy começa a tocar você com mais confiança"],
                ["sd", "Gosta quando eu faço assim? Puta que pariu, você não reage nada como antes..."],
                ["", "Ela varia a pressão e velocidade habilmente"],
                ["sd", "Mmm... você fica tão... estranho quando tá excitado... ta mais duro que um coral!"],
                ["sd", "Vamos ver quanto tempo você aguenta... filho da puta..."],
                ["", "Ela acelera os movimentos repentinamente"],
                ["sd", "Sei que você tá quase lá... caralho, olha a grossura desse pau!!"],
                ["bob", "Puta merda sua cachorra mutante eu vou ter que gozar!!"],
                ["sd", "Vai, Bob! Goza pra mim! "],
                ["", "Você tem um orgasmo intenso nas mãos da Sandy, voou gozo pra todo lado."]
            ],
            # Terceira vez
            [
                ["sd", "Yeehaw! Minha patinha tava com saudades de você, bobinho..."],
                ["sd", "Adoro ver como você reage ao meu toque... "],
                ["", "Sandy começa com movimentos lentos e firmes"],
                ["sd", "Olha só como você já tá duro pra mim... "],
                ["sd", "Minhas patas são peludinhas mas tem uma parte gelada também não é?"],
                ["", "Ela usa técnicas avançadas que te deixam tonto de prazer"],
                ["sd", "Tá gostando, Bob? Aprendi isso especialmente pra você, caralho!"],
                ["", "Você mal consegue responder, perdido em sensações"],
                ["sd", "Quero que você goze forte pra mim hoje... tigrão"],
                ["sd", "Agora, Bob! Deixa sair!"],
                ["bob", "SANDYYYYY! PORRA!"],
                ["", "Você tem o orgasmo mais forte de sua vida enquanto Sandy percebe que você não é quem diz ser"]
            ],
            # Repetições após completar
            [
                ["sd", "Vamos ver se consigo bater meu recorde texano hoje, Bob..."],
                ["sd", "Quero ver quanto tempo você aguenta minha técnica especial... seu bruto..."],
                ["", "Sandy envolve você com suas mãos experientes"],
                ["sd", "Gosta quando eu aperto aqui? E aqui? Puta merda, você geme tão diferente do Bob..."],
                ["", "Ela alterna entre movimentos rápidos e lentos, te levando à loucura"],
                ["sd", "Seu corpo inteiro tá tremendo, gosta de um punhetão né"],
                ["sd", "Ainda não, parceiro! Quero te levar ao limite... no Texas a gente faz assim..."],
                ["", "Você implora por alívio enquanto ela controla seu prazer"],
                ["sd", "Agora sim... pode gozar pra mim... jorra tudo em mim!!!!"],
                ["bob", "Ah! Ah! AH! SANDYYY! CARALHO!"],
                ["sd", "Isso! Deixa sair tudo! Yeehaw!"],
                ["", "Ela sorri satisfeita enquanto você tem um orgasmo espetacular que quase revela sua identidade"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]
    
    def obter_sequencia_buceta(vez):
        sequencias = [
            # Primeira vez
            [
                ["sd", "Você quer mesmo... ver lá embaixo? Pelos cornos do diabo, você tá diferente hoje..."],
                ["sd", "Ninguém nunca viu antes... e não sei porque sinto que você também nunca viu uma..."],
                ["", "Sandy tira o shorts lentamente, com timidez"],
                ["sd", "E então... o que acha, parceiro? Por que você tá com essa cara de idiota?"],
                ["", "Você olha admirado para a intimidade dela como se nunca tivesse visto uma"],
                ["bob", "Caralho, é linda, Sandy... muito melhor que as humanas..."],
                ["sd", "Poxa Bob, você gosta mesmo de uma pepeca do Texas..."],
                ["sd", "Só pode olhar ok?"],
                ["", "Você começa a babar vendo aquela buceta toda melada te encarando"],
                ["sd", "Você está..."],
                ["sd", "Babando?!"],
                ["", "Sandy começa a se sentir usada e decide parar"]
            ],
            # Segunda vez
            [
                ["sd", "Quer ver minha buceta de novo Bob?"],
                ["sd", "Tá bom, mas sem nenhuma gracinha!"],
                ["", "Sandy remove o shorts com mais confiança"],
                ["sd", "Tá gostando, parceiro? Seu amigo com certeza está!"],
                ["", "Seu pau fica tão duro que começa a latejar"],
                ["sd", "Caralho! Seu pau ta até tremendo hahaha"],
                ["sd", "Você deve ta doido pra me foder né?"],
                ["", "Você até tenta responder mas se abrir a boca vai falar merda."],
                ["sd", "Qual o problema amigão?"],
                ["sd", "Não consegue nem ver uma bucetinha de uma vaqueira sem perder o controle?"],
                ["sd", "Talvez vocÊ não mereça me foder então..."],
                ["sd", "Mas não pense que minha pepeca não aguenta..."]
            ],
            # Terceira vez
            [
                ["sd", "Já sei já sei"],
                ["sd", "Olha bem pra ela seu filho da puta!"],
                ["", "Sandy puxa o bikini pra baixo e abre as pernas sem hesitar"],
                ["sd", "Gostou do que vê cachorrão?!"],
                ["", "Seu pau endurece rapidamente"],
                ["sd", "Seu pau cresceu mais rápido que uma fita metrica lubrificada! "],
                ["sd", "E tá muito grosso também"],
                ["sd", "Continua olhando minha bucetinha e toca uma pra mim vai"],
                ["sd", "Bate gostoso pensando em me foder"],
                ["", "Você se masturba no meio da casa da Sandy"],
                ["sd", "Continua batendo até você sentir o leite implorar pra sair"],
                ["sd", "Minha buceta tá mais quente que uma torta de nozes fresquinha rs"]
            ],
            # Repetições após completar
            [
                ["sd", "Não se cansa de ver uma buceta né?"],
                ["", "Você imediatamente fica duro"],
                ["sd", "Olha mas não toca"],
                ["", "Suas mãos começam a tremer"],
                ["sd", "Sabe Bob, isso já ta ficando até normal pra mim"],
                ["sd", "Não acha meio estranho ficar pedindo toda hora pra alguém mostrar a pepequinha?"],
                ["sd", "Eu com certeza gosto, mas só to falando"],
                ["sd", "Fizemos isso tantas vezes que as vezes mostro a buceta pra parede por impulso"],
                ["sd", "Ah foi mal, seu objetivo é so bater punheta"],
                ["sd", "Goza pra mim então cachorrão! Já consigo até sentir o cheiro de semen"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]
    
    def obter_sequencia_cuzinho(vez):
        sequencias = [
            # Primeira vez
            [
                ["sd", "Você... quer tentar por trás? Puta merda, você é tão pervertido agora, Bob..."],
                ["sd", "Nunca fiz isso antes... tenha cuidado... caralho, sei que você é bruto demais..."],
                ["", "Sandy se vira timidamente, tremendo um pouco"],
                ["sd", "Vai bem devagar, ok? Pelo amor de Deus, você não parece saber se controlar..."],
                ["", "Você começa a penetrá-la com força e sem técnica"],
                ["sd", "Ai! Espera... dói um pouco... puta merda, você é grosso demais, seu idiota!"],
                ["sd", "Talvez se usarmos mais lubrificante... caralho, você precisa aprender a ser gentil!"],
                ["", "Você tenta novamente, com um pouco menos de brutalidade"],
                ["sd", "Mmm... tá melhorando... continua assim... diabos, não seja tão animal..."],
                ["", "Vocês encontram um ritmo, ainda desajeitado"],
                ["sd", "Ah! É diferente, mas... até que é bom... mesmo você sendo um bruto texano..."],
                ["", "Sandy tem um pequeno orgasmo, surpreendendo a si mesma apesar da sua falta de habilidade"]
            ],
            # Segunda vez
            [
                ["sd", "Quer tentar de novo aquilo? Caralho, você foi tão desajeitado da última vez..."],
                ["sd", "Tô um pouco menos nervosa hoje... mas pelos cornos do diabo, você precisa ser mais cuidadoso..."],
                ["", "Sandy se posiciona, mais confiante desta vez"],
                ["sd", "Ainda precisamos ir com calma... puta que pariu, não seja um animal como da última vez..."],
                ["", "Você entra com menos brutalidade desta vez"],
                ["sd", "Ah! Isso! Está melhor agora! Diabos, você está aprendendo, Bob..."],
                ["sd", "Pode ir um pouco mais fundo... mas com cuidado, seu escroto texano..."],
                ["", "Vocês aumentam gradualmente o ritmo"],
                ["sd", "Bob! Isso é... incrível! Caralho, você nem parece mais o mesmo!"],
                ["sd", "Não para agora! Estou gostando! Puta merda, quem diria que um impostor foderia tão bem!"],
                ["", "Você sente ela se contraindo ao seu redor"],
                ["sd", "AHHHH! Sandy goza intensamente, tremendo toda"]
            ],
            # Terceira vez
            [
                ["sd", "Bob, quero sentir você dentro do meu cuzinho hoje... seu bruto gostoso..."],
                ["sd", "Mal posso esperar... já estou pronta... pra esse seu pau de 'esponja'..."],
                ["", "Sandy se posiciona ansiosamente"],
                ["sd", "Não precisa ser tão gentil desta vez... já sei que você é um animal..."],
                ["", "Você a penetra com confiança, mostrando sua verdadeira natureza"],
                ["sd", "SIM! Assim mesmo! Mais forte! Pelos cornos do diabo, mostra quem você realmente é!"],
                ["sd", "Fode meu cuzinho, Bob! Vai fundo! Puta que pariu!"],
                ["", "O ritmo fica intenso e selvagem"],
                ["sd", "Estou quase lá! Não para! Arromba meu toba!"],
                ["bob", "Sandy! Eu também vou gozar, porra!"],
                ["sd", "JUNTOS! AGORA! SEU TEXANO DELICIOSO!"],
                ["", "Vocês atingem o clímax simultaneamente num orgasmo explosivo"]
            ],
            # Repetições após completar
            [
                ["sd", "Vem logo, vaqueiro. Meu cuzinho texano está impaciente hoje..."],
                ["sd", "Não precisamos de preliminares... mete sem dó!"],
                ["", "Sandy se posiciona e se oferece sem hesitação"],
                ["sd", "Me fode bem gostoso hoje, Bob... eu adoro..."],
                ["", "Você a penetra com força, conhecendo bem seus limites"],
                ["sd", "ISSO! ASSIM! FORTE! DIABOS, VOCÊ É UM ANIMAL, NÃO UMA ESPONJA!"],
                ["sd", "Meu Deus, Bob! Como você consegue me fazer sentir isso? Puta merda, você é tão diferente agora!"],
                ["", "Vocês encontram o ritmo perfeito que sabem que funciona"],
                ["sd", "Vai! Vai! Estou quase lá! Pelos cornos do diabo, mostra quem você realmente é!"],
                ["bob", "Sandy! Não aguento mais, porra!"],
                ["sd", "GOZA DENTRO! EU QUERO SENTIR!!"],
                ["", "Vocês atingem um orgasmo mútuo que parece durar para sempre"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]

    def obter_sequencia_boquete(vez):
        sequencias = [
            # Primeira vez
            [
                ["bob", "Você quer chupar minha rola? Vamo lá, esquilo, mostra o que sabe fazer."],
                ["sd", "Nunca fiz isso antes... mas estou curiosa, parceiro..."],
                ["", "Sandy se ajoelha timidamente na sua frente"],
                ["sd", "Me avisa se eu fizer algo errado, tá? No Texas a gente não costuma praticar isso..."],
                ["", "Ela começa a lamber você gentilmente"],
                ["bob", "Porra, que sensação estranha... mas você tá indo bem, esquilo..."],
                ["bob", "Vai com mais vontade, esquilo, não tenho o dia todo."],
                ["", "Sandy começa a te colocar na boca lentamente"],
                ["sd", "Mmm... tá bom assim, vaqueiro?"],
                ["bob", "É, tá melhorando. Não sabia que esquilos do Texas chupavam tão bem."],
                ["bob", "Caralho, Sandy! Isso é foda! Vou gozar, porra!"],
                ["", "Você atinge o clímax enquanto Sandy parece surpresa, mas satisfeita"]
            ],
            # Segunda vez
            [
                ["bob", "Vem cá, esquilo, quero sentir essa boquinha peluda de novo."],
                ["sd", "Gostei da última vez...aprendi alguns truques do Texas."],
                ["", "Sandy se ajoelha com mais confiança"],
                ["sd", "Relaxa aí, Bob. Hoje vou te dar mais prazer, parceiro."],
                ["", "Ela alterna entre lambidas e chupadas com mais habilidade"],
                ["bob", "Isso, porra! Engole essa rola dura sua piranha!"],
                ["sd", "Sandy mantém contato visual enquanto te chupa profundamente"],
                ["sd", "Mmm... *slurp*... tá gostando, cowboy?"],
                ["", "Ela acelera o ritmo, a boca dela é tão quente que você entra em transe"],
                ["bob", "Cacete, Sandy! Vai me fazer gozar rápido assim, porra!"],
                ["sd", "Goza seu merda!"],
                ["", "Você explode na boca dela, com a sua boca aberta pois ja perdeu os controles faciais"]
            ],
            # Terceira vez
            [
                ["bob", "Traz essa boca de esquilo pra cá de novo."],
                ["bob", "Hoje vou te mostrar como se chupa de verdade."],
                ["", "Sandy se ajoelha com uma expressão de desejo"],
                ["sd", "Puta merda, esse pau ta sempre limpinho! Tem nem gosto de mijo e DST como os do Texas!"],
                ["", "Ela começa com um ritmo perfeito, sabendo exatamente o que você gosta"],
                ["bob", "Deu sorte que moro embaixo d agua por que eu n sou de lavar o pau não..."],
                ["sd", "Sandy chupa você profundamente, controlando sua respiração como uma profissional"],
                ["sd", "Mmm... *garganta profunda*... *slurp*... yeehaw!"],
                ["bob", "Caralho, como um esquilo aprendeu a fazer isso? Na prisão não tinha isso não..."],
                ["bob", "Puta que pariu, Sandy! Vou encher sua boca, sua vadiazinha texana!"],
                ["sd", "Ela parece surpresa com suas palavras, mas não para de chupar"],
                ["", "Você goza violentamente na garganta dela, pensando em como é fácil enganá-la"]
            ],
            # Repetições após completar
            [
                ["bob", "Ei esquilo, vem chupar minha rola. Tô precisando relaxar."],
                ["sd", "É pra já tigrão!"],
                ["", "Sandy se ajoelha e já começa a te devorar sem hesitação"],
                ["sd", "Mmm... *glup*... *glup*... yeehaw, adoro te sentir assim..."],
                ["", "Ela usa técnicas avançadas que te fazem ver estrelas"],
                ["bob", "Porra, tu melhorou muito. Andou mamando quem?."],
                ["sd", "Sandy alterna entre chupadas profundas e lambidas precisas"],
                ["sd", "Mmm... quero sentir você explodindo na minha boca de novo, vaqueiro..."],
                ["bob", "Você agarra a cabeça dela com força, controlando o ritmo"],
                ["bob", "Puta que pariu! Na prisão esse boquete vale mais que 10 maços de cigarro!"],
                ["sd", "Mmm... *glup*... *glup*... prisa-"],
                ["", "Antes dela assimilar a frase você inunda ela de porra"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]

    def obter_sequencia_foder_buceta(vez):
        sequencias = [
            # Primeira vez
            [
                ["bob", "E aí, esquilo, que tal sentir um homem de verdade dentro de você?"],
                ["sd", "Nunca fiz isso antes... mas confio em você, Bob... mesmo você estando tão estranho..."],
                ["", "Sandy se deita e abre as pernas timidamente"],
                ["sd", "Espero que você seja gentil, parceiro..."],
                ["", "Você se posiciona entre as pernas dela, rindo internamente"],
                ["sd", "Ai! Calma, Bob... vai devagar, pelos cornos do diabo!"],
                ["bob", "Cacete, você é bem apertadinha hein?"],
                ["", "Vocês encontram um ritmo, com você sendo mais agressivo que o Bob seria"],
                ["sd", "Nossa... você parece diferente hoje... mais intenso, caralho!"],
                ["", "Os movimentos se intensificam, você não tem paciência para ir devagar"],
                ["sd", "Bob! Isso tá... intenso demais! Mas... puta merda, tô gostando!"],
                ["", "Você goza dentro dela sem avisar, satisfeito por dominar a situação"]
            ],
            # Segunda vez
            [
                ["bob", "Tô a fim de meter em você de novo."],
                ["sd", "Nossa, Bob... você tá tão... direto ultimamente"],
                ["", "Sandy se posiciona, um pouco surpresa com sua atitude"],
                ["sd", "Você tá bem diferente, mas eu gosto dessa sua nova energia, pelos cornos do diabo..."],
                ["", "Você a penetra sem muita cerimônia"],
                ["bob", "Porra! Buceta é melhor que cu de macho!"],
                ["bob", "Caralho, Sandy! Sua buceta texana é muito boa!"],
                ["", "O ritmo aumenta, e você bate nela com força"],
                ["sd", "Mais forte! Não para! Puta merda, você nunca me comeu assim antes!"],
                ["bob", "Vou encher essa buceta de porra!"],
                ["sd", "Sim! Goza dentro! Goza dentro, caralho!"],
                ["", "Você a preenche completamente, satisfeito por ela não suspeitar de nada"]
            ],
            # Terceira vez
            [
                ["bob", "Tira a roupa, esquilo. Vou te foder agora."],
                ["sd", "Nossa, Bob... você nunca foi assim antes... mas diabos, eu adoro, vaqueiro."],
                ["", "Sandy se posiciona ansiosamente, já molhada de excitação"],
                ["sd", "Sabe, gosto desse seu lado mais agressivo, caralho..."],
                ["", "Você a penetra com força, puxando seu rabo"],
                ["bob", "PORRA! ISSO! ME ARREBENTA!"],
                ["bob", "Engole essa rola toda, esquilo texano do caralho!"],
                ["", "Vocês encontram um ritmo selvagem e brutal"],
                ["sd", "Mais fundo! Isso! Me rasga toda, pelos cornos do diabo!"],
                ["bob", "Vou encher você de porra, texana!"],
                ["sd", "GOOOOOOZA DENTRO! ME ALAGA TODA, CARALHO!"],
                ["", "Você tem um orgasmo violento, impressionado como ela não percebe que você não é o Bob"]
            ],
            # Repetições após completar
            [
                ["bob", "Tira a roupa vadia. Agora."],
                ["sd", "Bob, você tá tão mandão... puta que pariu, adoro esse seu lado dominador, vaqueiro."],
                ["", "Sandy se posiciona de quatro, já sabendo o que você quer"],
                ["bob", "Me fode com força, quero sentir você me rasgando."],
                ["", "Você a penetra violentamente, puxando seu cabelo"],
                ["bob", "ISSO! ASSIM! DESTRÓI MINHA BUCETINHA CARALHOO!"],
                ["bob", "Toma essa rola, vadia! O Bob Esponja aqui é outro agora, caralho!"],
                ["", "Você bate na bunda dela enquanto mete com força"],
                ["sd", "Me bate mais! Me xinga! Pelos cornos do diabo, eu amo isso!"],
                ["bob", "Vou encher esse útero texano de porra!"],
                ["sd", "SIM! ME INUNDA DE PORRA, CARALHO!"],
                ["", "Você goza profundamente nela, pensando em quantas outras mulheres do fundo do mar você pode comer"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]

    def obter_sequencia_nozes_cuzinho(vez):
        sequencias = [
            # Primeira vez
            [
                ["bob", "Ei, esquilo, que tal enfiar essas nozes no seu cu texano?"],
                ["sd", "No meu... o quê? Puta merda, isso é... muito estranho, Bob."],
                ["", "Sandy parece chocada, mas também curiosa"],
                ["sd", "Olha, sou cientista texana, então... vamos experimentar, parceiro."],
                ["bob", "Você prepara as nozes com um sorriso malicioso"],
                ["sd", "Vai doer, caralho?"],
                ["bob", "Com certeza! Fica de quatro logo."],
                ["", "Você começa a inserir as nozes uma a uma, sem muito cuidado"],
                ["sd", "Ai! Calma! É diferente, mas... caralho, até que é interessante."],
                ["", "Enquanto você continua, ela começa a gemer"],
                ["bob", "Porra, nunca imaginei que isso seria tão bom, esquilo!"],
                ["", "Sandy tem um orgasmo inesperado, e você ri da perversão que conseguiu fazer com ela"]
            ],
            # Segunda vez ou mais
            [
                ["bob", "Ei, trouxe mais nozes texanas. Acho que seu cu tá com fome, esquilo."],
                ["sd", "Nossa, Bob... pelos cornos do diabo, nunca imaginei que gostaria tanto disso."],
                ["", "Sandy se posiciona ansiosamente de quatro"],
                ["sd", "Enfia mais dessa vez, vaqueiro. Quero sentir o máximo possível, caralho!"],
                ["bob", "Você prepara as nozes, impressionado com quão pervertida ela se tornou"],
                ["bob", "Abre o cu esquilinho!"],
                ["", "As nozes deslizam para dentro dela com facilidade agora"],
                ["sd", "Isso! Sim! Enfia mais fundo, puta merda!"],
                ["sd", "Mais! Coloca mais! Quero sentir todas dentro de mim, pelo amor de Deus do Texas!"],
                ["", "O corpo dela treme a cada nova noz inserida"],
                ["bob", "Cacete! Isso é demais, esquilo! Eu vou... vou..."],
                ["", "Sandy tem um orgasmo intenso, e algumas nozes saem como projéteis, fazendo você rir"]
            ]
        ]
        
        if vez >= 1:
            return sequencias[1]
        return sequencias[vez]

# Define as imagens para a sequência de zoom nos peitos (após 3 vezes)
# Estas imagens precisarão ser criadas e colocadas na pasta de imagens do jogo
image sandy_pes = "images/sandy/sandy_pes.png"
image sandy_pernas = "images/sandy/sandy_pernas.png"
image sandy_barriga = "images/sandy/sandy_barriga.png"
image sandy_peitos = "images/sandy/sandy_peitos.png"

# Efeito sonoro de ejaculação - este arquivo precisa ser colocado na pasta de sons do jogo
define audio.porra = "audio/porra.mp3"