name = input("Antes de empezar, ¿Podria decirme su nombre porfavor?\n")

print(
    "¡Bienvenido {}, a mi proyecto de trivia del curso de backend del MTPE junto a Silabuz espero que te guste!\n"
    .format(name))
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[39m'
puntaje = 0
correcto = GREEN + "¡Correcto!\n" + RESET
incorrecto = RED + "¡Incorrecto, suerte en las proximas preguntas!\n" + RESET
incorrectoFinal = RED + "¡Incorrecto!" + RESET
condicion = YELLOW + "Escoge (A)Verdadero o (B)Falso.\n" + RESET
condicionMul = YELLOW + "Escoge una de estas opciones (A), (B), (C) o (D).\n" + RESET

category = input(
    "Antes de empezar primero, elegiremos el tipo de trivia que desees hacer:\n"
    "A. Sobre Anime y Mangas.\n"
    "B. Sobre Música.\n")

while category not in ("A", "B"):
    category = input("Porfavor ingrese una de las letras indicadas.\n")

if category == "A":
    dificulty = input(
        "Felicidades {}, ah escogido la categoria de anime y mangas, ahora debe escoger el nivel de dificultad:\n"
        "A. Facil.\n"
        "B. Ni tan facil ni tan dificil.\n"
        "C. Dificil.\n".format(name))
    while dificulty not in ("A", "B", "C"):
        dificulty = input("Porfavor ingrese una de las letras indicadas.\n")
    if dificulty == "A":
        type_answer = input(
            "Ingresa el tipo de preguntas que deseas responder:\n"
            "A. Verdadero o Falso.\n"
            "B. Opcion Multiple.\n")
        while type_answer not in ("A", "B"):
            type_answer = input(
                "Porfavor ingrese una de las letras indicadas.\n")
        if type_answer == "A":
            print(
                "¡{}, mucha suerte! descubriremos que tan amante del anime y manga eres."
                .format(name))
            answer_1 = input(
                "Clefairy estaba destinado a ser el Pokémon inicial de Ash en el episodio piloto de la caricatura.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_1 not in ("A", "B"):
                answer_1 = input("Escoge (A)Verdadero o (B)Falso\n")
            if answer_1 == "A":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_2 = input(
                "En Kill La Kill, el arma de la protagonista principal es una katana.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_2 not in ("A", "B"):
                answer_2 = input("Escoge (A)Verdadero o (B)Falso.\n")
            if answer_2 == "A":
                print(incorrecto)
            else:
                print(correcto)
                puntaje += 4
            answer_3 = input(
                "No Game No Life se emitió por primera vez en 2014.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_3 not in ("A", "B"):
                answer_3 = input(condicion)
            if answer_3 == "A":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_4 = input(
                "En la serie To Love-Ru, Golden Darkness es enviada a matar a Lala Deviluke.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_4 not in ("A", "B"):
                answer_4 = input(condicion)
            if answer_4 == "A":
                print(incorrecto)
            else:
                print(correcto)
                puntaje += 4
            answer_5 = input(
                "El nombre del ataque Kamehameha en Dragon Ball Z lleva el nombre de un famoso rey de Hawái.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_5 not in ("A", "B"):
                answer_5 = input(condicion)
            if answer_5 == "A":
                print(correcto)
                puntaje += 4
            else:
                print(incorrectoFinal)
        else:
            print(
                "¡{}, mucha suerte! descubriremos que tan amante del anime y manga eres.\n"
                .format(name))
            answer_1 = input(
                "En Inuyasha, ¿qué buscan coleccionar los héroes?\n"
                "A. Fragmentos de joya.\n"
                "B. Dragon balls.\n"
                "C. Piedras delirantes.\n"
                "D. Piedras sagradas.\n")
            while answer_1 not in ("A", "B", "C", "D"):
                answer_1 = input(condicionMul)
            if answer_1 == "A":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_2 = input(
                "¿Quién es el personaje principal con cabello amarillo en el anime Naruto?\n"
                "A. Ten Ten.\n"
                "B. Naruto.\n"
                "C. Sasuke.\n"
                "D. Takashi.\n")
            while answer_2 not in ("A", "B", "C", "D"):
                answer_2 = input(condicionMul)
            if answer_2 == "B":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_3 = input(
                "Los dos personajes principales de No Game No Life, Sora y Shiro, ¿cómo se llaman juntos?\n"
                "A. Bestias de guerra.\n"
                "B. Immanity.\n"
                "C. Disboard.\n"
                "D. Vacio(Blank).\n")
            while answer_3 not in ("A", "B", "C", "D"):
                answer_3 = input(condicionMul)
            if answer_3 == "D":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_4 = input(
                "¿Quién es el titán acorazado en Attack On Titan?\n"
                "A. Armin Arlelt.\n"
                "B. Mikasa Ackerman.\n"
                "C. Reiner Braun.\n"
                "D. Eren Jaeger.\n")
            while answer_4 not in ("A", "B", "C", "D"):
                answer_4 = input(condicionMul)
            if answer_4 == "C":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_5 = input(
                "¿Qué estudio de animación produjo Gurren Lagann?\n"
                "A. Kyoto Animation.\n"
                "B. Pierrot.\n"
                "C. Gainax.\n"
                "D. A-1 Pictures\n")
            while answer_5 not in ("A", "B", "C", "D"):
                answer_5 = input(condicionMul)
            if answer_5 == "C":
                print(correcto)
                puntaje += 4
            else:
                print(incorrectoFinal)
    elif dificulty == "B":
        print(
            "!{}, mucha suerte¡ al ser el nivel regular ya no habra la posibilidad de escoger verdadero o falso, ahora seran multiples opciones.\n"
            .format(name))
        answer_1 = input(
            "¿En la serie JoJos Bizarre Adventure, ¿qué personaje principal hace la mayor cantidad de apariciones recurrentes?\n"
            "A. Giorno Giovanna.\n"
            "B. Joseph Joestar.\n"
            "C. Jotaro Kujo.\n"
            "D. Josuke Higashikata.\n")
        while answer_1 not in ("A", "B", "C", "D"):
            answer_1 = input(condicionMul)
        if answer_1 == "C":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_2 = input(
            "¿En Love Live: School Idol Project ¿qué seudónimo usa Kotori Minami en su trabajo como empleada doméstica?.\n"
            "A. Stanoytchev.\n"
            "B. Kuznetsov.\n"
            "C. Aqours.\n"
            "D. Minalinsky.\n")
        while answer_2 not in ("A", "B", "C", "D"):
            answer_2 = input(condicionMul)
        if answer_2 == "D":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_3 = input(
            "¿En la serie Re: Zero, ¿cuál de los siguientes arzobispos del pecado se come la existencia de Rem?\n"
            "A. Roy Alphard.\n"
            "B. Ley Batenkaitos.\n"
            "C. Petelgeuse Romanee-Conti.\n"
            "D. Louis Arneb.\n")
        while answer_3 not in ("A", "B", "C", "D"):
            answer_3 = input(condicionMul)
        if answer_3 == "B":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_4 = input(
            "¿En qué año salió al aire Bishoujo Senshi Sailor Moon en Japón?\n"
            "A. 1992.\n"
            "B. 1989.\n"
            "C. 1990.\n"
            "D. 1994.\n")
        while answer_4 not in ("A", "B", "C", "D"):
            answer_4 = input(condicionMul)
        if answer_4 == "A":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_5 = input(
            "¿Cómo se llama el personaje principal del anime One-Punch Man?\n"
            "A. Genos.\n"
            "B. Saitama.\n"
            "C. Sonic.\n"
            "D. King.\n")
        while answer_5 not in ("A", "B", "C", "D"):
            answer_5 = input(condicionMul)
        if answer_5 == "B":
            print(correcto)
            puntaje += 4
        else:
            print(incorrectoFinal)
    else:
        print(
            "{}, ahora si ponte modo serio ya que elegiste el modo dificil. Demuestra que tan fan del anime eres."
            .format(name))
        answer_1 = input(
            "¿Cuál es la última línea murmurada en la película de anime The End of Evangelion?\n"
            "A. ¡Idiota, no dejaré que me mates!\n"
            "B. Que asqueroso.\n"
            "C. Maldita sea, Shinji.\n"
            "D. Nada.\n")
        while answer_1 not in ("A", "B", "C", "D"):
            answer_1 = input(condicionMul)
        if answer_1 == "B":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_2 = input(
            "En One Piece, ¿quién es la chica que superó su pasado de esclavitud y se convirtió en agente de un ejército para luchar contra"
            " el gobierno corrupto?\n"
            "A. Boa Hancock.\n"
            "B. Nico Robin.\n"
            "C. Koala.\n"
            "D. Emporio Ivankov.\n")
        while answer_2 not in ("A", "B", "C", "D"):
            answer_2 = input(condicionMul)
        if answer_2 == "C":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_3 = input("¿En qué año se inició el manga To Love-Ru?\n"
                         "A. 2006.\n"
                         "B. 2007.\n"
                         "C. 2005.\n"
                         "D. 2004.\n")
        while answer_3 not in ("A", "B", "C", "D"):
            answer_3 = input(condicionMul)
        if answer_3 == "A":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_4 = input(
            "¿Qué estudio de animación produjo Sword Art Online?\n"
            "A. Silver Link.\n"
            "B. A-1 Pictures.\n"
            "C. Kyoto Animation.\n"
            "D. Production I.G.\n")
        while answer_4 not in ("A", "B", "C", "D"):
            answer_4 = input(condicionMul)
        if answer_4 == "B":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_5 = input("¿Qué estudio animó a Afro Samurai?\n"
                         "A. xebec.\n"
                         "B. Production I.G.\n"
                         "C. Gonzo.\n"
                         "D. Kyoto Animation.\n")
        while answer_5 not in ("A", "B", "C", "D"):
            answer_5 = input(condicionMul)
        if answer_5 == "C":
            print(correcto)
            puntaje += 4
        else:
            print(incorrectoFinal)
else:
    dificulty = input(
        "Felicidades {}, ah escogido la categoria de música, ahora debe escoger el nivel de dificultad:\n"
        "A. Facil.\n"
        "B. Ni tan facil ni tan dificil.\n"
        "C. Dificil.\n".format(name))
    while dificulty not in ("A", "B", "C"):
        dificulty = input("Porfavor ingrese una de las letras indicadas.\n")
    if dificulty == "A":
        type_answer = input(
            "Ingresa el tipo de preguntas que deseas responder:\n"
            "A. Verdadero o Falso.\n"
            "B. Opcion Multiple.\n")
        while type_answer not in ("A", "B"):
            type_answer = input(
                "Porfavor ingrese una de las letras indicadas.\n")
        if type_answer == "A":
            print(
                "¡{}, mucha suerte! descubriremos que tan fan de la música eres."
                .format(name))
            answer_1 = input(
                "El cantante principal Rivers Cuomo de la banda de rock estadounidense Weezer asistió a Harvard.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_1 not in ("A", "B"):
                answer_1 = input(condicion)
            if answer_1 == "A":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_2 = input(
                "El grupo de música Daft Punk obtuvo su nombre de una crítica negativa que recibieron.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_2 not in ("A", "B"):
                answer_2 = input(condicion)
            if answer_2 == "A":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_3 = input("Un saxofón es un instrumento de metal.\n"
                             "A. Verdadero.\n"
                             "B. Falso.\n")
            while answer_3 not in ("A", "B"):
                answer_3 = input(condicion)
            if answer_3 == "B":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_4 = input("Daft Punk se originó en Francia.\n"
                             "A. Verdadero.\n"
                             "B. Falso.\n")
            while answer_4 not in ("A", "B"):
                answer_4 = input(condicion)
            if answer_4 == "A":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_5 = input(
                "Michael Jackson escribió la canción de Los Simpson: Do the Bartman.\n"
                "A. Verdadero.\n"
                "B. Falso.\n")
            while answer_5 not in ("A", "B"):
                answer_5 = input(condicion)
            if answer_5 == "B":
                print(correcto)
                puntaje += 4
            else:
                print(incorrectoFinal)
        else:
            print(
                "¡{}, mucha suerte! descubriremos que tan fan de la música eres."
                .format(name))
            answer_1 = input(
                "¿Quién es el cantante principal de la banda británica de rock pop Coldplay?\n"
                "A. Jonny Buckland.\n"
                "B. Will Champion.\n"
                "C. Chris Martin.\n"
                "D. Will Champion.\n")
            while answer_1 not in ("A", "B", "C", "D"):
                answer_1 = input(condicionMul)
            if answer_1 == "C":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_2 = input("¿La K en K-Pop representa qué palabra?\n"
                             "A. Kenyan.\n"
                             "B. Korean.\n"
                             "C. Kazakhstan.\n"
                             "D. Kuwaiti.\n")
            while answer_2 not in ("A", "B", "C", "D"):
                answer_2 = input(condicionMul)
            if answer_2 == "B":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_3 = input(
                "¿Kanye West en los VMA de 2009 interrumpió a qué celebridad?\n"
                "A. MF DOOM.\n"
                "B. Beyonce.\n"
                "C. Taylor Swift.\n"
                "D. Beck.\n")
            while answer_3 not in ("A", "B", "C", "D"):
                answer_3 = input(condicionMul)
            if answer_3 == "C":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_4 = input("¿Quién es el cantante principal de Green Day?\n"
                             "A. Sean Hughes.\n"
                             "B. Billie Joe Armstrong.\n"
                             "C. Mike Dirnt.\n"
                             "D. Bad Bunny.\n")
            while answer_4 not in ("A", "B", "C", "D"):
                answer_4 = input(condicionMul)
            if answer_4 == "B":
                print(correcto)
                puntaje += 4
            else:
                print(incorrecto)
            answer_5 = input(
                "Cuyos álbumes incluyeron Back in Black y Ballbreaker.\n"
                "A. Iron Maiden.\n"
                "B. Black Sabbath.\n"
                "C. Metallica.\n"
                "D. AC\/DC.\n")
            while answer_5 not in ("A", "B", "C", "D"):
                answer_5 = input(condicionMul)
            if answer_5 == "D":
                print(correcto)
                puntaje += 4
            else:
                print(incorrectoFinal)
    elif dificulty == "B":
        print(
            "!{}, mucha suerte¡ al ser el nivel regular ya no habra la posibilidad de escoger verdadero o falso, ahora seran multiples opciones.\n"
            .format(name))
        answer_1 = input(
            "¿Saul Hudson (Slash) de la banda Guns Roses es conocido por tocar qué tipo de guitarra?\n"
            "A. Fender Stratocaster.\n"
            "B. LsL Mongrel.\n"
            "C. Gretsch Falcon.\n"
            "D. Les Paul Standard.\n")
        while answer_1 not in ("A", "B", "C", "D"):
            answer_1 = input(condicionMul)
        if answer_1 == "D":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_2 = input(
            "Pink Floyd hizo esta canción para su anterior cantante Syd Barrett.\n"
            "A. Shine On You Crazy Diamond.\n"
            "B. Have A Cigar.\n"
            "C. Welcome to the Machine.\n"
            "D. Wish You Were Here.\n")
        while answer_2 not in ("A", "B", "C", "D"):
            answer_2 = input(condicionMul)
        if answer_2 == "A":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_3 = input("¿Cuál de estas bandas es la más antigua?\n"
                         "A. AC\/DC.\n"
                         "B. Metallica.\n"
                         "C. Red Hot Chili Peppers.\n"
                         "D. Pink Floyd.\n")
        while answer_3 not in ("A", "B", "C", "D"):
            answer_3 = input(condicionMul)
        if answer_3 == "D":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_4 = input(
            "¿Quién es el vocalista y líder de la banda de rock Guns Roses?\n"
            "A. Kurt Cobain.\n"
            "B. Slash.\n"
            "C. Axl Rose.\n"
            "D. Bono.\n")
        while answer_4 not in ("A", "B", "C", "D"):
            answer_4 = input(condicionMul)
        if answer_4 == "C":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_5 = input(
            "¿En qué álbum de Iron Maiden apareció la canción Dream of Mirrors?\n"
            "A. A Matter of Life and Death.\n"
            "B. Brave New World.\n"
            "C. Dance of Death.\n"
            "D. Somewhere in Time.\n")
        while answer_5 not in ("A", "B", "C", "D"):
            answer_5 = input(condicionMul)
        if answer_5 == "B":
            print(correcto)
            puntaje += 4
        else:
            print(incorrectoFinal)
    else:
        print(
            "{}, ahora si ponte modo serio porque elegiste el modo dificil. Demuesta que tan fan de la música eres."
            .format(name))
        answer_1 = input(
            "¿En qué álbum de los Beatles encontrarías la canción Eleanor Rigby?\n"
            "A. Help!\n"
            "B. Rubber Soul.\n"
            "C. Abbey Road.\n"
            "D. Revolver.\n")
        while answer_1 not in ("A", "B", "C", "D"):
            answer_1 = input(condicionMul)
        if answer_1 == "D":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_2 = input(
            "¿Cuál de estos artistas NO remezcló la canción Faded de Alan Walker?\n"
            "A. Slushii.\n"
            "B. Skrillex.\n"
            "C. Dash Berlin.\n"
            "D. Tiesto.\n")
        while answer_2 not in ("A", "B", "C", "D"):
            answer_2 = input(condicionMul)
        if answer_2 == "B":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_3 = input(
            "Artis Leon Ivey Jr. es mejor conocida como ¿qué artista de rap?\n"
            "A. Coolio.\n"
            "B. Dr Dre.\n"
            "C. Snoop Dogg.\n"
            "D. 2pac.\n")
        while answer_3 not in ("A", "B", "C", "D"):
            answer_3 = input(condicionMul)
        if answer_3 == "A":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_4 = input(
            "¿En qué año nació Min Yoongi de la banda de chicos de Corea del Sur BTS?\n"
            "A. 1991.\n"
            "B. 1992.\n"
            "C. 1993.\n"
            "D. 1995.\n")
        while answer_4 not in ("A", "B", "C", "D"):
            answer_4 = input(condicionMul)
        if answer_4 == "C":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)
        answer_5 = input(
            "¿Cómo se llama la canción de Beyoncé y Alejandro Fernández estrenada en 2007?\n"
            "A. Amor Gitano.\n"
            "B. La ultima vez.\n"
            "C. Hasta donde estes.\n"
            "D. Rocket.\n")
        while answer_5 not in ("A", "B", "C", "D"):
            answer_5 = input(condicionMul)
        if answer_5 == "A":
            print(correcto)
            puntaje += 4
        else:
            print(incorrecto)

if category == "A":
    print("Puntaje: {}".format(puntaje))
    if puntaje >= 12 and puntaje <= 16:
        print(
            "Felicidades {}, obtuviste el puntaje de: {}, eres un buen fan del anime y manga."
            .format(name, puntaje))
    elif puntaje > 16:
        print(
            "Felicidades {}, obtuviste el puntaje perfecto de: {}, conoces mucho sobre anime y manga."
            .format(name, puntaje))
    else:
        print("Triste... pero no te desanimes, vuelve a intentarlo")
else:
    print("Puntaje: {}".format(puntaje))
    if puntaje >= 12 and puntaje <= 16:
        print(
            "Felicidades {}, obtuviste el puntaje de: {}, almenos si sabes algo de cultura general."
            .format(name, puntaje))
    elif puntaje > 16:
        print(
            "Felicidades {}, obtuviste el puntaje de: {}, eso quiere decir que eres muy fan de la música."
            .format(name, puntaje))
    else:
        print("Triste... pero no te desanimes, vuelve a intentarlo.")
print("Gracias por participar")