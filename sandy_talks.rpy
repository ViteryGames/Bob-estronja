# sandy_talks.rpy - Arquivo contendo apenas os diálogos e sequências para as cenas com Sandy

init python:
    def obter_dialogo_peitos():
        # Retorna um diálogo aleatório para quando Sandy mostra os peitos
        import random
        dialogos = [
            "sd", "Você quer... ver meus peitos? Bem, acho que posso mostrar rapidinho para você, Bob...",
            "sd", "Sabe que isso não é muito científico, né? Mas se você gosta tanto... você tá diferente hoje, Bob...",
            "sd", "Olha só o que você me faz fazer, Bob Esponja... Isso fica só entre a gente, viu? Você tá esquisito ultimamente...",
            "sd", "O ar daqui é bem fresquinho sem a roupa... Gosta do que está vendo? Por que tá me olhando assim?",
            "sd", "Normalmente eu sou mais reservada, mas com você eu me sinto diferente... embora você pareça meio estranho hoje..."
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_punheta():
        # Retorna um diálogo aleatório para quando Sandy dá uma punheta
        import random
        dialogos = [
            ["sd", "Hmm... Você quer uma ajudinha manual? Acho que posso dar um jeito nisso... Bob, você tá tão diferente..."],
            ["sd", "Você tá agindo estranho ultimamente, mas ainda assim quero te tocar..."],
            ["sd", "Nunca pensei que usaria minhas habilidades de engenheira desse jeito... você parece outra pessoa, Bob..."],
            ["sd", "Vamos ver o quanto você consegue aguentar, esponjinha... ou o que quer que você seja agora..."],
            ["sd", "No Texas, a gente chamava isso de 'ordenhar o touro'... Mas você tá diferente do meu Bob habitual..."]
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_buceta():
        # Retorna um diálogo aleatório para quando Sandy mostra a buceta
        import random
        dialogos = [
            ["sd", "Você quer ver... lá embaixo? Bem... acho que já estamos íntimos o suficiente... embora você esteja esquisito hoje..."],
            ["sd", "Nunca mostrei isso para ninguém no Fundo do Bikini... Você é especial, Bob, mesmo agindo tão estranho ultimamente..."],
            ["sd", "Esquilos normalmente são muito reservados, mas... algo em você me deixa à vontade... mesmo você estando diferente..."],
            ["sd", "Espero que você goste do que vai ver. É um tesouro do Texas, como dizem! Por que você tá com essa cara?"],
            ["sd", "Quer conhecer o lado selvagem de uma esquilo? Prepare-se... embora você pareça mais selvagem que o normal ultimamente..."]
        ]
        return random.choice(dialogos)
    
    def obter_dialogo_cuzinho():
        # Retorna um diálogo aleatório para quando Sandy permite anal
        import random
        if vezes_cuzinho == 0:
            dialogos = [
                ["sd", "Hmm... Você quer experimentar... aquele lugar? Nunca fiz isso antes... e você tá me assustando com esse jeito novo..."],
                ["sd", "Por aqui? Tenho um pouco de medo... Promete ir devagar? Você parece mais agressivo que o normal, Bob..."],
                ["sd", "Isso é algo que nunca fiz nem no Texas... Tem certeza? Você tá tão estranho ultimamente..."],
                ["sd", "Ai meu Deus... Acho que podemos tentar, mas seja gentil, ok? Você parece outra pessoa hoje..."],
                ["sd", "Essa é uma fronteira que nunca explorei... Você sabe o que está fazendo? Nunca te vi tão... mandão antes..."]
            ]
        elif vezes_cuzinho == 1:
            dialogos = [
                ["sd", "Da última vez foi um pouco dolorido... Mas acho que agora estou mais preparada. Ainda acho você diferente, mas gostei..."],
                ["sd", "Vamos com calma de novo? Acho que estou começando a gostar... desse seu novo jeito mais rude..."],
                ["sd", "Hmm... Tenho pensado nisso desde a última vez. Vamos tentar novamente? Você é tão diferente do Bob que eu conhecia..."],
                ["sd", "Quem diria que uma cientista como eu gostaria desse tipo de... experimento. Você me surpreende, 'Bob'..."],
                ["sd", "Dessa vez temos que usar mais lubrificante... Vai ser melhor para nós dois. Você é tão agressivo agora..."]
            ]
        elif vezes_cuzinho == 2:
            dialogos = [
                ["sd", "Já estou ficando boa nisso, não acha? Vem cá, vamos fazer de novo... gosto desse seu lado mais selvagem..."],
                ["sd", "Acho que encontrei um novo hobby científico para estudar a fundo... você mudou tanto, Bob, mas até que gosto..."],
                ["sd", "Quem diria que o cuzinho de uma esquilo seria tão compatível com... bem, o que quer que você seja agora..."],
                ["sd", "Mmm... Mal posso esperar. Desta vez quero sentir tudo! Você é tão diferente, mas tão bom nisso..."],
                ["sd", "Sabe, no Texas a gente não fala sobre isso, mas aqui no fundo do mar... você virou outra pessoa, e até que gosto..."]
            ]
        else:
            dialogos = [
                "sd", "Ah, meu cowboy favorito chegou! Sabe o que eu quero, não é? Esse seu jeito bruto me excita...",
                "sd", "Já estou pronta para você... Nem preciso mais de muita preparação. Você está tão diferente, mas tão bom nisso...",
                "sd", "Acho que descobri meu talento secreto. E você, quem quer que seja agora, é meu parceiro perfeito!",
                "sd", "Isso virou meu vício, sabia? Nenhum experimento científico me dá tanto prazer. Você nem parece mais o Bob...",
                "sd", "Vem logo, 'Bob'. Meu cuzinho está sentindo sua falta... você é tão mais agressivo agora..."
            ]
        return random.choice(dialogos)
    
    def obter_dialogo_recusa():
        # Retorna um diálogo aleatório para quando Sandy recusa por já ter feito no dia
        import random
        dialogos = [
            "sd", "Já fizemos isso hoje, volte amanhã cowboy taradão! Você está muito mais insaciável que o normal...",
            "sd", "Ei, calma aí! Até uma esquilo precisa de descanso, sabia? Desde quando você ficou tão exigente, Bob?",
            "sd", "Hmm, alguém está muito ansioso! Mas você vai ter que esperar até amanhã. Você tá tão esquisito ultimamente...",
            "sd", "Estou um pouco dolorida de mais cedo... Que tal voltarmos a isso amanhã? Você tá muito agressivo hoje...",
            "sd", "Você é insaciável, não é? Mas vamos deixar para amanhã, ok? Você nem parece mais o mesmo Bob..."
        ]
        return random.choice(dialogos)
    
    # Sequências de diálogos para cada cena sexual
    def obter_sequencia_peitos(vez):
        sequencias = [
            # Primeira vez
            [
                ["sd", "Você quer mesmo ver meus peitos, Bob? Você tá tão esquisito hoje..."],
                ["sd", "Bem... acho que não faz mal mostrar rapidinho... mas você tá diferente..."],
                ["sd", "Só não conte pra ninguém, ok? E para de me olhar desse jeito, tá me assustando..."],
                ["", "Sandy tira a parte de cima do traje lentamente..."],
                ["sd", "E então... o que acha? Por que tá com essa cara de tarado?"],
                ["sd", "Sei que não são grandes como os das sereias... você nunca me olhou assim antes..."],
                ["sd", "Você está gostando do que vê? Tá babando, Bob... isso não é normal..."],
                ["", "Sandy percebe o olhar estranho e predatório de 'Bob'"],
                ["sd", "Seu olhar está me deixando excitada... mas também meio assustada..."],
                ["", "Você nota os mamilos dela ficando mais rígidos"],
                ["sd", "Ahhh... Isso é tão... diferente... você tá tão estranho hoje..."],
                ["", "Sandy respira fundo e fecha os olhos, aproveitando a sensação, mas confusa com o comportamento diferente"]
            ],
            # Segunda vez
            [
                ["sd", "Quer ver meus peitos de novo, seu safadinho? Você tá tão diferente do antigo Bob..."],
                ["sd", "Estive pensando nisso desde a última vez... você é como um Bob novo e selvagem..."],
                ["", "Sandy remove a parte superior com mais confiança desta vez"],
                ["sd", "Gosta do que vê? Quer tocá-los? Você nunca foi tão direto assim antes..."],
                ["", "Suas mãos grosseiras tocam os peitos da Sandy com avidez"],
                ["sd", "Mmm... Isso é bom... mas você tá tão bruto, Bob..."],
                ["sd", "Pode apertar um pouco mais... nossa, não precisava ser tão forte!"],
                ["", "Ela guia suas mãos pelos seus mamilos, surpresa com sua agressividade"],
                ["sd", "Ahh! Isso! Continue... mas com menos força, seu bruto!"],
                ["", "Sandy começa a respirar mais rápido"],
                ["sd", "Ohhh 'Bob'... Você me faz sentir coisas incríveis! Quem é você realmente?"],
                ["", "Ela tremble levemente enquanto um pequeno orgasmo percorre seu corpo"]
            ],
            # Terceira vez
            [
                ["sd", "Já sei o que você quer ver... você está viciado nos meus peitos, 'Bob'..."],
                ["sd", "Sandy sorri maliciosamente enquanto tira o traje, já acostumada com seu jeito diferente"],
                ["sd", "Adoro quando você olha para meus peitos assim... com esse olhar tão... humano..."],
                ["sd", "Quer lambê-los hoje? Vejo que você já está babando..."],
                ["", "Você se aproxima e começa a sugar seus mamilos com voracidade"],
                ["sd", "Isso! Usa essa boca... nossa, desde quando você chupa assim?"],
                ["sd", "Ah, Bob! Você está me deixando toda molhada! Tá tão diferente..."],
                ["", "Ela segura sua cabeça contra seus peitos"],
                ["sd", "Mais forte! Chupa com vontade! Nossa, não sabia que você tinha isso dentro de você!"],
                ["", "Você sente seu corpo tremer de prazer"],
                ["sd", "Ahhh! Estou... estou...! Você não parece mais o Bob, mas adoro!"],
                ["sd", "Sandy geme alto enquanto tem um orgasmo intenso"]
            ],
            # Repetições após completar
            [
                ["sd", "Meus peitos estavam com saudade da sua atenção... 'Bob'..."],
                ["", "Ela remove o traje com habilidade, já acostumada com seu novo comportamento"],
                ["sd", "Gosta tanto deles, né? São todos seus... seu tarado disfarçado..."],
                ["sd", "Quero que você use sua língua hoje... você é tão bom nisso agora..."],
                ["", "Você obedece prontamente, lambendo seus mamilos duros com agressividade"],
                ["sd", "Isso! Exatamente assim! Você definitivamente não é mais o mesmo..."],
                ["sd", "Sandy massageia seus próprios seios enquanto você os lambe vorazmente"],
                ["sd", "Ahh! Meu corpo inteiro está formigando! Você me deixa louca, seja lá quem for!"],
                ["", "Ela aperta sua cabeça contra seu peito"],
                ["sd", "Não para agora! Estou quase lá! Você é um animal!"],
                ["", "Você sente seu corpo convulsionar de prazer"],
                ["sd", "AHHHHH! SIM! Sandy grita enquanto atinge o clímax, confusa mas extasiada"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]
    
    def obter_sequencia_punheta(vez):
        sequencias = [
            # Primeira vez
            [
                ["sd", "Então... você quer que eu te toque? Você tá tão estranho hoje..."],
                ["sd", "Nunca fiz isso antes... me guia? Nossa, por que você tá tão ansioso?"],
                ["", "Sandy se aproxima timidamente, notando sua expressão diferente"],
                ["sd", "É assim que se faz? Por que você tá gemendo desse jeito?"],
                ["", "Ela começa a movimentar a mão lentamente, surpresa com sua reação exagerada"],
                ["sd", "Estou fazendo certo? Nossa, nunca te vi tão excitado..."],
                ["", "Você assente grosseiramente, sentindo o prazer aumentar"],
                ["sd", "Você está ficando todo molhado, 'Bob'... isso é normal para uma esponja?"],
                ["sd", "Devo ir mais rápido? Você tá tremendo demais..."],
                ["", "Seus movimentos se intensificam"],
                ["bob", "Ah! Sandy! Porra, vou...!"],
                ["", "Você atinge o clímax enquanto Sandy observa fascinada e um pouco assustada"]
            ],
            # Segunda vez
            [
                ["sd", "Quer sentir minha mão de novo, bobinho? Ou devo dizer... quem quer que você seja?"],
                ["sd", "Acho que aprendi alguns truques desde a última vez... você é tão diferente agora..."],
                ["", "Sandy começa a tocar você com mais confiança"],
                ["sd", "Gosta quando eu faço assim? Você reage bem diferente do Bob que eu conhecia..."],
                ["", "Ela varia a pressão e velocidade habilmente"],
                ["sd", "Mmm... você fica tão... estranho quando está excitado... nada como antes..."],
                ["sd", "Vamos ver quanto tempo você aguenta... seu safado disfarçado..."],
                ["", "Ela acelera os movimentos repentinamente"],
                ["sd", "Sei que você está quase lá... seus olhos não são do Bob que conheço..."],
                ["bob", "Sandy! Caralho! Não consigo aguentar mais!"],
                ["sd", "Vai, 'Bob'! Goza para mim! Quem quer que você seja!"],
                ["", "Você tem um orgasmo intenso nas mãos da Sandy, quase revelando sua verdadeira identidade"]
            ],
            # Terceira vez
            [
                ["sd", "Minha mão estava com saudades de você... seu impostor tarado..."],
                ["sd", "Eu adoro ver como você reage ao meu toque... tão diferente do verdadeiro Bob..."],
                ["", "Sandy começa com movimentos lentos e firmes"],
                ["sd", "Olha só como você já está duro para mim... Bob nunca ficava assim tão rápido..."],
                ["sd", "Vou usar minhas duas mãos hoje... para esse seu troço que não é de esponja..."],
                ["", "Ela usa técnicas avançadas que te deixam tonto de prazer"],
                ["sd", "Está gostando, 'Bob'? Eu aprendi isso especialmente para você... ou quem quer que seja..."],
                ["", "Você mal consegue responder, perdido em sensações"],
                ["sd", "Quero que você goze forte para mim hoje... seu escroto gostoso..."],
                ["sd", "Agora, 'Bob'! Deixa sair! Mostra quem você realmente é!"],
                ["bob", "SANDYYYYY! PORRA!"],
                ["", "Você tem o orgasmo mais forte de sua vida enquanto Sandy percebe que você não é quem diz ser"]
            ],
            # Repetições após completar
            [
                ["sd", "Vamos ver se consigo bater meu recorde hoje... seu humano disfarçado..."],
                ["sd", "Quero ver quanto tempo você aguenta minha técnica especial... seu bruto..."],
                ["", "Sandy envolve você com suas mãos experientes"],
                ["sd", "Gosta quando eu aperto aqui? E aqui? Você geme tão diferente do Bob..."],
                ["", "Ela alterna entre movimentos rápidos e lentos, te levando à loucura"],
                ["sd", "Seu corpo inteiro está tremendo, 'Bob'... definitivamente você não é uma esponja..."],
                ["sd", "Ainda não! Quero te levar ao limite... seu impostor gostoso..."],
                ["", "Você implora por alívio enquanto ela controla seu prazer"],
                ["sd", "Agora sim... pode gozar para mim... mostre quem você realmente é..."],
                ["bob", "Ah! Ah! AH! SANDYYY! CARALHO!"],
                ["sd", "Isso! Deixa sair tudo! Seu humano safado!"],
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
                ["sd", "Você quer mesmo... ver lá embaixo? Você tá tão diferente hoje, Bob..."],
                ["sd", "Ninguém nunca viu antes... e não sei porque sinto que você também nunca viu uma..."],
                ["", "Sandy tira o shorts lentamente, com timidez"],
                ["sd", "E então... o que acha? Por que você tá com essa cara de idiota?"],
                ["", "Você olha admirado para a intimidade dela como se nunca tivesse visto uma"],
                ["bob", "Caralho, é linda, Sandy... muito melhor que as humanas..."],
                ["sd", "Poxa 'Bob', você gosta mesmo de uma bucetinha, hein seu tarado disfarçado..."],
                ["sd", "Quer... tocar um pouco? Mas controle essa mão bruta..."],
                ["", "Suas mãos desajeitadas tocam com força"],
                ["sd", "Ah! Isso... bem devagar... você é tão desajeitado, não era assim antes..."],
                ["sd", "Toca mais, 'Bob'... isso é tão bom... mas você parece nunca ter tocado uma antes..."],
                ["", "Sandy suspira profundamente, sentindo um pequeno orgasmo apesar da sua falta de jeito"]
            ],
            # Segunda vez
            [
                ["sd", "Quer ver minha buceta de novo, 'Bob'? Quem quer que você seja..."],
                ["sd", "Estive pensando nisso desde a última vez... mesmo você sendo tão estranho agora..."],
                ["", "Sandy remove o shorts com mais confiança"],
                ["sd", "Está gostando? Toca nela um pouco... mas com menos força dessa vez, seu bruto..."],
                ["", "Você a toca enquanto ela se contorce de prazer"],
                ["sd", "Isso, 'Bob'! Continua assim! Você tá aprendendo..."],
                ["sd", "Você pode usar sua língua se quiser... se é que você é mesmo uma esponja..."],
                ["", "Você começa a lambê-la com voracidade"],
                ["sd", "Ah! 'Bob'! Isso é incrível! Você nunca fez isso assim antes!"],
                ["sd", "Não para agora! Estou quase lá! Você lambe como um humano, não como uma esponja!"],
                ["sd", "Sandy agarra sua cabeça com força"],
                ["sd", "AHHHHH! Sandy grita enquanto tem um orgasmo intenso"]
            ],
            # Terceira vez
            [
                ["sd", "Sabe o que eu quero que você faça hoje, seu impostor delicioso?"],
                ["sd", "Quero sentir sua língua nada absorvente na minha bucetinha..."],
                ["", "Sandy se deita e abre as pernas sem hesitar"],
                ["sd", "Vem, 'Bob'. Mostra o que você sabe fazer... com essa língua que não é de esponja..."],
                ["", "Você mergulha entre suas pernas com entusiasmo de predador"],
                ["sd", "Isso! Lambe assim! Exatamente aí! Bob nunca lambeu assim antes!"],
                ["sd", "Ah, 'Bob'! Como você aprendeu a fazer isso tão bem? Você não é o verdadeiro, né?"],
                ["sd", "Ela empurra o quadril contra seu rosto"],
                ["sd", "Mais rápido! Não para agora! Seu humano disfarçado!"],
                ["", "Você sente seu corpo começar a tremer"],
                ["sd", "BOBBBB! OU SEJA LÁ QUEM VOCÊ FOR! EU VOU GOZAAAAAR!"],
                ["sd", "Sandy tem um orgasmo explosivo que a deixa sem fôlego"]
            ],
            # Repetições após completar
            [
                ["sd", "Preciso da sua língua hoje, impostor. Agora!"],
                ["", "Ela praticamente arranca o shorts e se posiciona"],
                ["sd", "Faz aquilo que só você sabe fazer... com essa língua humana disfarçada..."],
                ["", "Você a lambe com habilidade adquirida com a prática"],
                ["sd", "Isso! Bem no meu pontinho! Você definitivamente não é o Bob!"],
                ["sd", "Você é o melhor nisso, 'Bob'! Ou quem quer que você seja! Ninguém me faz sentir assim!"],
                ["sd", "Sandy agarra sua cabeça com força, controlando o ritmo"],
                ["sd", "Não para! Não para! Estou quase lá! Seu fugitivo gostoso!"],
                ["", "Você sente seus músculos se contraindo"],
                ["sd", "AHHHHH! BOOOOBB! FODAAAA! VOCÊ É UM HUMANO, NÉ?!"],
                ["sd", "Ela tem um orgasmo tão forte que quase desmaia"],
                ["sd", "Meu Deus... você fica melhor a cada vez... não sei quem você é, mas adoro..."]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]
    
    def obter_sequencia_cuzinho(vez):
        sequencias = [
            # Primeira vez
            [
                ["sd", "Você... quer tentar por trás? Você é tão pervertido agora, 'Bob'...",],
                ["sd", "Nunca fiz isso antes... tenha cuidado... sei que você é bruto demais...",],
                ["", "Sandy se vira timidamente, tremendo um pouco",],
                ["sd", "Vai bem devagar, ok? Você não parece saber se controlar...",],
                ["", "Você começa a penetrá-la com força e sem técnica",],
                ["sd", "Ai! Espera... dói um pouco... você é grosso demais, seu idiota!",],
                ["sd", "Talvez se usarmos mais lubrificante... você precisa aprender a ser gentil!",],
                ["", "Você tenta novamente, com um pouco menos de brutalidade",],
                ["sd", "Mmm... está melhorando... continua assim... não seja tão animal...",],
                ["", "Vocês encontram um ritmo, ainda desajeitado",],
                ["sd", "Ah! É diferente, mas... até que é bom... mesmo você sendo um bruto...",],
                ["", "Sandy tem um pequeno orgasmo, surpreendendo a si mesma apesar da sua falta de habilidade"]
            ],
            # Segunda vez
            [
                ["sd", "Quer tentar de novo aquilo? Você foi tão desajeitado da última vez...",],
                ["sd", "Estou um pouco menos nervosa hoje... mas você precisa ser mais cuidadoso...",],
                ["", "Sandy se posiciona, mais confiante desta vez",],
                ["sd", "Ainda precisamos ir com calma... não seja um animal como da última vez...",],
                ["", "Você entra com menos brutalidade desta vez",],
                ["sd", "Ah! Isso! Está melhor agora! Você está aprendendo, 'Bob'...",],
                ["sd", "Pode ir um pouco mais fundo... mas com cuidado, seu escroto...",],
                ["", "Vocês aumentam gradualmente o ritmo",],
                ["sd", "'Bob'! Isso é... incrível! Você nem parece mais o mesmo!",],
                ["sd", "Não para agora! Estou gostando! Quem diria que um impostor foderia tão bem!",],
                ["", "Você sente ela se contraindo ao seu redor",],
                ["sd", "AHHHH! Sandy goza intensamente, tremendo toda"]
            ],
            # Terceira vez
            [
                ["sd", "'Bob', quero sentir você dentro do meu cuzinho hoje... seu bruto gostoso...",],
                ["sd", "Mal posso esperar... já estou pronta... para esse seu pau de 'esponja'...",],
                ["", "Sandy se posiciona ansiosamente",],
                ["sd", "Não precisa ser tão gentil desta vez... já sei que você é um animal...",],
                ["", "Você a penetra com confiança, mostrando sua verdadeira natureza",],
                ["sd", "SIM! Assim mesmo! Mais forte! Mostra quem você realmente é!",],
                ["sd", "Fode meu cuzinho, 'Bob'! Vai fundo! Seu humano tarado!",],
                ["", "O ritmo fica intenso e selvagem",],
                ["sd", "Estou quase lá! Não para! Você fode muito melhor que o verdadeiro Bob!",],
                ["bob", "Sandy! Eu também vou gozar, porra!",],
                ["sd", "JUNTOS! AGORA! SEU FUGITIVO DELICIOSO!",],
                ["", "Vocês atingem o clímax simultaneamente num orgasmo explosivo"]
            ],
            # Repetições após completar
            [
                ["sd", "Vem logo, impostor. Meu cuzinho está impaciente hoje...",],
                ["sd", "Não precisamos de preliminares... quero você dentro de mim... seu humano disfarçado...",],
                ["", "Sandy se posiciona e se oferece sem hesitação",],
                ["sd", "Me fode bem gostoso hoje, 'Bob'... sei que você não é ele, mas adoro...",],
                ["", "Você a penetra com força, conhecendo bem seus limites",],
                ["sd", "ISSO! ASSIM! FORTE! VOCÊ É UM ANIMAL, NÃO UMA ESPONJA!",],
                ["sd", "Meu Deus, 'Bob'! Como você consegue me fazer sentir isso? Você é tão diferente agora!",],
                ["", "Vocês encontram o ritmo perfeito que sabem que funciona",],
                ["sd", "Vai! Vai! Estou quase lá! Mostra quem você realmente é!",],
                ["bob", "Sandy! Não aguento mais, porra!",],
                ["sd", "GOZA DENTRO! EU QUERO SENTIR! SEU HUMANO DISFARÇADO!",],
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
                ["sd", "Nunca fiz isso antes... mas estou curiosa..."],
                ["", "Sandy se ajoelha timidamente na sua frente"],
                ["sd", "Me avisa se eu fizer algo errado, tá?"],
                ["", "Ela começa a lamber você gentilmente"],
                ["bob", "Porra, que sensação estranha... mas você tá indo bem..."],
                ["bob", "Vai com mais vontade, esquilo, não tenho o dia todo."],
                ["", "Sandy começa a te colocar na boca lentamente"],
                ["sd", "Mmm... tá bom assim?"],
                ["bob", "É, tá melhorando. Não sabia que esquilos chupavam tão bem."],
                ["bob", "Caralho, Sandy! Isso é foda! Vou gozar, porra!"],
                ["", "Você atinge o clímax enquanto Sandy parece surpresa, mas satisfeita"]
            ],
            # Segunda vez
            [
                ["bob", "Vem cá, esquilo, quero sentir essa boca de novo."],
                ["sd", "Gostei da última vez... acho que aprendi alguns truques."],
                ["", "Sandy se ajoelha com mais confiança"],
                ["sd", "Relaxa aí, Bob. Hoje vou te dar mais prazer."],
                ["", "Ela alterna entre lambidas e chupadas com mais habilidade"],
                ["bob", "Isso, porra! Chupa direito!"],
                ["sd", "Sandy mantém contato visual enquanto te chupa profundamente"],
                ["sd", "Mmm... *slurp*... tá gostando?"],
                ["", "Ela acelera o ritmo, usando as mãos junto com a boca"],
                ["bob", "Cacete, Sandy! Vai me fazer gozar rápido assim!"],
                ["sd", "Pode gozar, Bob. Quero sentir tudo!"],
                ["", "Você explode na boca dela, rindo por dentro de como ela não percebe que não é o Bob"]
            ],
            # Terceira vez
            [
                ["bob", "Traz essa boca de esquilo pra cá de novo."],
                ["bob", "Hoje vou te mostrar como se chupa de verdade."],
                ["", "Sandy se ajoelha com uma expressão de desejo"],
                ["sd", "Você tá tão diferente, Bob... mais... intenso."],
                ["", "Ela começa com um ritmo perfeito, sabendo exatamente o que você gosta"],
                ["bob", "Isso, porra! Chupa essa porra toda!"],
                ["sd", "Sandy chupa você profundamente, controlando sua respiração como uma profissional"],
                ["sd", "Mmm... *garganta profunda*... *slurp*..."],
                ["bob", "Caralho, como um esquilo aprendeu a fazer isso? Na prisão não tinha isso não..."],
                ["bob", "Puta que pariu, Sandy! Vou encher sua boca, sua vadia!"],
                ["sd", "Ela parece surpresa com suas palavras, mas não para de chupar"],
                ["", "Você goza violentamente na garganta dela, pensando em como é fácil enganá-la"]
            ],
            # Repetições após completar
            [
                ["bob", "Ei esquilo, vem chupar minha rola. Tô precisando relaxar."],
                ["sd", "Bob, você anda tão agressivo... mas até que eu gosto."],
                ["", "Sandy se ajoelha e já começa a te devorar sem hesitação"],
                ["sd", "Mmm... *glup*... *glup*... adoro te sentir assim..."],
                ["", "Ela usa técnicas avançadas que te fazem ver estrelas"],
                ["bob", "Porra, tu melhorou muito. Deve ser o ar do mar."],
                ["sd", "Sandy alterna entre chupadas profundas e lambidas precisas"],
                ["sd", "Mmm... quero sentir você explodindo na minha boca..."],
                ["bob", "Você agarra a cabeça dela com força, controlando o ritmo"],
                ["bob", "Puta que pariu! Que boquete do caralho!"],
                ["sd", "Mmm... *glup*... *glup*..."],
                ["", "Você goza na boca dela, pensando que ser o Bob Esponja tem suas vantagens"]
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
                ["sd", "Nunca fiz isso antes... mas confio em você, Bob..."],
                ["", "Sandy se deita e abre as pernas timidamente"],
                ["sd", "Espero que você seja gentil..."],
                ["", "Você se posiciona entre as pernas dela, rindo internamente"],
                ["sd", "Ai! Calma, Bob... vai devagar..."],
                ["bob", "Cacete, você é bem apertadinha hein?"],
                ["", "Vocês encontram um ritmo, com você sendo mais agressivo que o Bob seria"],
                ["sd", "Nossa... você parece diferente hoje... mais intenso..."],
                ["", "Os movimentos se intensificam, você não tem paciência para ir devagar"],
                ["sd", "Bob! Isso tá... intenso demais! Mas... tô gostando!"],
                ["", "Você goza dentro dela sem avisar, satisfeito por dominar a situação"]
            ],
            # Segunda vez
            [
                ["bob", "Tô a fim de meter em você de novo, vem cá."],
                ["sd", "Nossa, Bob... você tá tão... direto ultimamente."],
                ["", "Sandy se posiciona, um pouco surpresa com sua atitude"],
                ["sd", "Você tá bem diferente, mas eu gosto dessa sua nova energia..."],
                ["", "Você a penetra sem muita cerimônia"],
                ["bob", "Porra! Isso! Me fode com força!"],
                ["bob", "Caralho, Sandy! Sua buceta é muito boa!"],
                ["", "O ritmo aumenta, e você bate nela com força"],
                ["sd", "Mais forte! Não para! Você nunca me comeu assim antes!"],
                ["bob", "Vou encher essa buceta de porra!"],
                ["sd", "Sim! Goza dentro! Goza dentro!"],
                ["", "Você a preenche completamente, satisfeito por ela não suspeitar de nada"]
            ],
            # Terceira vez
            [
                ["bob", "Tira a roupa, esquilo. Vou te foder agora."],
                ["sd", "Nossa, Bob... você nunca foi assim antes... mas eu adoro."],
                ["", "Sandy se posiciona ansiosamente, já molhada de excitação"],
                ["sd", "Sabe, gosto desse seu lado mais agressivo..."],
                ["", "Você a penetra com força, puxando seu rabo"],
                ["bob", "PORRA! ISSO! ME ARREBENTA!"],
                ["bob", "Engole essa rola toda, esquilo do caralho!"],
                ["", "Vocês encontram um ritmo selvagem e brutal"],
                ["sd", "Mais fundo! Isso! Me rasga toda!"],
                ["bob", "Vou encher você de porra!"],
                ["sd", "GOOOOOOZA DENTRO! ME ALAGA TODA!"],
                ["", "Você tem um orgasmo violento, impressionado como ela não percebe que você não é o Bob"]
            ],
            # Repetições após completar
            [
                ["bob", "Tira a roupa. Agora."],
                ["sd", "Bob, você tá tão mandão... adoro esse seu lado dominador."],
                ["", "Sandy se posiciona de quatro, já sabendo o que você quer"],
                ["bob", "Me fode com força, quero sentir você me rasgando."],
                ["", "Você a penetra violentamente, puxando seu cabelo"],
                ["bob", "ISSO! ASSIM! DESTRÓI MINHA BUCETA!"],
                ["bob", "Toma essa rola, vadia! O Bob Esponja aqui é outro agora!"],
                ["", "Você bate na bunda dela enquanto mete com força"],
                ["sd", "Me bate mais! Me xinga! Eu amo isso!"],
                ["bob", "Vou encher esse útero de porra!"],
                ["sd", "SIM! ME INUNDA DE PORRA!"],
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
                ["bob", "Ei, esquilo, que tal enfiar essas nozes no seu cu?"],
                ["sd", "No meu... o quê? Isso é... muito estranho, Bob."],
                ["", "Sandy parece chocada, mas também curiosa"],
                ["sd", "Olha, sou cientista, então... vamos experimentar."],
                ["bob", "Você prepara as nozes com um sorriso malicioso"],
                ["sd", "Vai doer?"],
                ["bob", "Provavelmente. Fica de quatro logo."],
                ["", "Você começa a inserir as nozes uma a uma, sem muito cuidado"],
                ["sd", "Ai! Calma! É diferente, mas... até que é interessante."],
                ["", "Enquanto você continua, ela começa a gemer"],
                ["bob", "Porra, nunca imaginei que isso seria tão bom!"],
                ["", "Sandy tem um orgasmo inesperado, e você ri da perversão que conseguiu fazer com ela"]
            ],
            # Segunda vez ou mais
            [
                ["bob", "Ei, trouxe mais nozes. Acho que seu cu tá com fome."],
                ["sd", "Nossa, Bob... nunca imaginei que gostaria tanto disso."],
                ["", "Sandy se posiciona ansiosamente de quatro"],
                ["sd", "Enfia mais dessa vez. Quero sentir o máximo possível."],
                ["bob", "Você prepara as nozes, impressionado com quão pervertida ela se tornou"],
                ["bob", "Anda logo, tô impaciente!"],
                ["", "As nozes deslizam para dentro dela com facilidade agora"],
                ["sd", "Isso! Sim! Enfia mais fundo!"],
                ["sd", "Mais! Coloca mais! Quero sentir todas dentro de mim!"],
                ["", "O corpo dela treme a cada nova noz inserida"],
                ["bob", "Cacete! Isso é demais! Eu vou... vou..."],
                ["", "Sandy tem um orgasmo intenso, e algumas nozes saem como projéteis, fazendo você rir"]
            ]
        ]
        
        if vez >= 1:
            return sequencias[1]
        return sequencias[vez]

    def obter_sequencia_cuzinho(vez):
        sequencias = [
            # Primeira vez
            [
                ["bob", "Vou comer seu cu hoje, esquilo."],
                ["sd", "Meu... o quê? Bob, isso é muito... diferente de você."],
                ["", "Sandy se vira timidamente, parecendo confusa"],
                ["sd", "Tem certeza disso? Vai devagar, tá?"],
                ["bob", "Você cospe na entrada e enfia sem muito cuidado"],
                ["sd", "AAAAI! Espera! Tá doendo muito!"],
                ["bob", "Relaxa essa bunda que melhora."],
                ["", "Você tenta de novo, com um pouco menos de força"],
                ["sd", "Ah... tá melhorando... continua assim..."],
                ["", "Vocês encontram um ritmo, você tentando não ser muito brutal"],
                ["sd", "Nossa... nunca pensei que o cuzinho podia dar tanto prazer..."],
                ["", "Sandy tem um pequeno orgasmo, e você se sente orgulhoso por corromper o esquilo"]
            ],
            # Segunda vez
            [
                ["bob", "Tô a fim de comer seu cu de novo."],
                ["sd", "Nossa, Bob... você tá tão diferente... mas eu gosto."],
                ["", "Sandy se posiciona, ainda um pouco nervosa"],
                ["sd", "Vamos com calma de novo, ok?"],
                ["", "Você entra com mais facilidade desta vez"],
                ["sd", "Isso! Tá melhor agora!"],
                ["bob", "Posso meter com força dessa vez?"],
                ["", "Vocês aumentam gradualmente o ritmo"],
                ["sd", "Caralho! É tão bom! Não sabia que podia ser assim!"],
                ["", "Você sente o cuzinho dela apertando seu pau"],
                ["sd", "Isso! Me fode! Me rasga!"],
                ["sd", "Sandy goza intensamente enquanto você continua metendo"]
            ],
            # Terceira vez
            [
                ["bob", "Fica de quatro, quero arrombar seu cu hoje."],
                ["sd", "Nossa, Bob... você tá tão agressivo ultimamente..."],
                ["", "Sandy se posiciona ansiosamente, já lubrificada"],
                ["sd", "Adoro quando você fala comigo assim, tão dominador..."],
                ["bob", "Você enfia tudo de uma vez, fazendo ela gritar"],
                ["sd", "PUTA QUE PARIU! ISSO! ME ARREBENTA!"],
                ["bob", "Vou destruir esse cu apertado!"],
                ["", "O ritmo fica intenso e brutal"],
                ["sd", "Isso! Me rasga todo! Tá tão fundo!"],
                ["bob", "Vou encher seu cu de porra!"],
                ["sd", "SIM! GOZA DENTRO! EU QUERO SENTIR TUDO!"],
                ["", "Vocês atingem o clímax juntos, e você pensa em como foi fácil submeter ela"]
            ],
            # Repetições após completar
            [
                ["bob", "De quatro, agora. Vou arrebentar esse rabo."],
                ["sd", "Adoro quando você me trata assim, Bob..."],
                ["", "Sandy se posiciona e abre as nádegas para você"],
                ["bob", "Vem, mete com força... Quero sentir tudo..."],
                ["", "Você mete violentamente, fazendo ela gritar"],
                ["sd", "ISSO! DESTRÓI MEU CU! MAIS FORTE!"],
                ["bob", "Caralho, Sandy! Que cu apertado do caralho!"],
                ["", "Vocês entram num ritmo frenético, quase animalesco"],
                ["sd", "Me rasga todo! Vai! Vai! Mais fundo!"],
                ["bob", "Vou gozar nesse rabo arrombado!"],
                ["sd", "GOZA! ME ENCHE DE PORRA!"],
                ["", "Você inunda o intestino dela, pensando em como o Bob nunca faria isso"]
            ]
        ]
        
        if vez >= 3:
            return sequencias[3]
        return sequencias[vez]