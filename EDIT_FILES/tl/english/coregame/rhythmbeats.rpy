# TODO: Translation updated at 2023-02-23 14:02

translate english strings:

    # game/coregame/rhythmbeats.rpym:33
    old "Una clase simple para emitir excepciones bajo el nombre de Ren'Py RhythmBeats."
    new "A simple class for issuing exceptions called Ren'Py RhythmBeats."

    # game/coregame/rhythmbeats.rpym:39
    old "Constructor de la clase RhythmPlayground().\n            Recibe 5 parámetros (2 obligatorios) en el momento que se crea la instancia de la clase.\n            Estos parámetros son los siguientes:\n\n            fn (str):\n                Este parámetro es obligatorio, y recibe una cadena con la ruta del archivo BEAT\n                relativa a la carpeta /game de tu juego.\n                Este archivo puede ser leído incluso dentro de un paquete RPA.\n\n            displayable (str o displayable):\n                Este parámetro es obligatorio, y recibe como argumento un elemento displayable\n                que será utilizado para mostrar cada nota en la pantalla. Puedes pasar como\n                argumento una ruta de una image, o una imagen modificada con Transform().\n\n            offset_map (float):\n                Si no es 0.0, este parámetro recibe como argumento un número de punto flotante,\n                que representa el tiempo (en segundos) que se desfasa el beatmap respecto de la\n                reproducción de la pista musical. Esto debería ser un número individual de cada beatmap.\n\n            offset_game (float):\n                Si no es 0.0, este parámetro recibe como argumento un número de punto flotante\n                que representa el tiempo (en milisegundos) que se agrega como desfase\n                personalizable por el jugador.\n                Esto es útil para que el jugador pueda calibrar manualmente en caso de que perciba\n                que la cascada de notas no se sincroniza del todo bien con sus toques. En ese caso,\n                puedes pasar como argumento una variable persistente con el valor calibrado por el\n                jugador.\n\n            threshold (float):\n                Si no es 0.1, este parámetro recibe como argumento un número de punto flotante,\n                que representa el umbral de tiempo (en segundos) para detectar si el jugador ha\n                tocado la nota o no. Por defecto se ha fijado el umbral en 0.1 segundos (100ms) por\n                lo que el jugador tiene un rango total de 200ms para tocar correctamente una nota.\n\n            failsafe (bool):\n                El modo seguro permite reproducir el beatmap sin necesidad de tocar las notas.\n                Es útil en caso de querer ajustar visualmente la cascada de notas respecto\n                de la música (mediante offset_map).\n                Si es True, ejecutará el beatmap en modo seguro. Si es False, el\n                juego se ejecutará normalmente.\n            "
    new "The RhythmPlayground() class constructor.                It receives 5 parameters (2 obligatory) when creating an instance of the class.                           These parameters are as follows:                          fn (str):               This parameter is mandatory and takes a string with the path to the BEAT file relative to the /game folder of your game.                   This file can even be read inside the RPA package.                       displayable (str or displayable):              This parameter is mandatory and takes displayable as an argument, which will be used to display each note on the screen. An image path or an image changed with Transform() can be passed as argument.  offset_map (float):             If not 0.0, this parameter takes as its argument a floating-point number representing the time (in seconds) by which the bitmap is offset from playback\n of the music track. This must be an individual number for each bitmap.                     offset_game (float):\n If not 0.0, this parameter takes as its argument a floating-point number representing the time (in milliseconds) that is added as a player adjustable offset.       This is useful for manual calibration by the player in case he/she feels that the cascade of notes is not quite in sync with his/her touch. In this case you can pass as an argument a constant variable with a value calibrated by the player. threshold (float):               If not 0.1, this parameter takes as its argument a floating-point number that represents the time threshold (in seconds) for determining whether a player has played a note or not. By default, the threshold is set to 0.1 seconds (100ms), so the player has 200ms to play the note correctly.                                          failsafe (bool):\n The failsafe mode allows you to play a bitmap without playing a note.                          This is useful if you want to visually adjust the cascade of notes relative to the music (via offset_map).           If True, the beatmap will run in safe mode. If False, the game will run in normal mode."

    # game/coregame/rhythmbeats.rpym:148
    old "Este método carga y procesa las secuencias de un archivo beatmap de\n            una canción en específico. El archivo `.beat` debe ser señalado en el\n            momento en que se crea una instancia de la clase.\n\n            Esto debe ser llamado posterior a instanciar la clase. No recibe ningún\n            argumento ni tampoco retorna datos."
    new "This method loads and processes the beatmap file sequence of a specific song. The `.beat' file must be specified at the time the class instance is created.\n This method must be called after the class is instantiated. The method accepts no arguments and returns no data."

    # game/coregame/rhythmbeats.rpym:155
    old "Process"
    new "The process"

    # game/coregame/rhythmbeats.rpym:155
    old "Cargando beatmap..."
    new "Loading the rhythm map..."

    # game/coregame/rhythmbeats.rpym:159
    old "Stats"
    new "Statistics"

    # game/coregame/rhythmbeats.rpym:159
    old "Ruta relativa: %s."
    new "Relative path: %s."

    # game/coregame/rhythmbeats.rpym:180
    old "Offset final: %sms."
    new "Final offset: %sms."

    # game/coregame/rhythmbeats.rpym:185
    old "Preparando waterfall (SpriteManager)..."
    new "Preparing the waterfall (SpriteManager)..."

    # game/coregame/rhythmbeats.rpym:187
    old "OK"
    new "OK"

    # game/coregame/rhythmbeats.rpym:187
    old "Beatmap listo para ejecutar.\n"
    new "The Beatmap is ready to go."

    # game/coregame/rhythmbeats.rpym:197
    old "\n            (NO DOCUMENTADO)\n            Este método recoge los eventos de Pygame para reconocer los toques\n            del jugador en el juego, ya sea con un teclado o con pantalla táctil.\n\n            NOTA: No puedo realizar lecturas de múltiples dedos en una pantalla\n            táctil, ya que Ren'Py parece limitarme los eventos de Pygame, por lo\n            que el reconocimiento de toques en móviles puede ser... desagradable =(\n            "
    new "(NOT DOCUMENTED)\n This method collects Pygame events to recognise the player's touch\n in the game, be it on the keyboard or touchscreen.\n NOTE: I cannot do multi-finger reading on a touchscreen,\n as Ren'Py seems to limit me to Pygame events, so touch recognition on mobile devices can be... uncomfortable =(\n"

    # game/coregame/rhythmbeats.rpym:227
    old "Se encarga del gameplay principal.\n            Este método reproduce el beatmap cargado y se encarga de realizar todos\n            los cálculos necesarios para determinar si el jugador acierta o falla\n            alguna nota.\n            Las interacciones del jugador se computan en este método respecto de un\n            tiempo de época (Epoch) dado en segundos, que por cierto, es entregada\n            gracias a la clase `DynamicDisplayable()` de Ren'Py.\n\n            No retorna ningún valor importante para el desarrollador o el jugador."
    new "It takes care of the basic gameplay.\n          This method plays the loaded rhythm map and does all necessary calculations to determine whether the player hits or misses the notes.\n The player interaction is calculated in this method against a given epoch time in seconds, which incidentally is passed thanks to Ren'Py's `DynamicDisplayable()` class. \It does not return any important value for the developer or the player."

    # game/coregame/rhythmbeats.rpym:320
    old "Este método crea 'n' cantidad de sprites para el SpriteManager()\n            en función de la cantidad de notas que posee el beatmap."
    new "This method creates 'n' number of sprites for SpriteManager()\n based on the number of notes in the bitmap."

    # game/coregame/rhythmbeats.rpym:339
    old "Esta función calcula las coordenadas de las notas que van cayendo,\n            respecto del timestamp de esa nota y el tiempo epoch actual."
    new "This function calculates the coordinates of the falling notes in relation to that note's timestamp and the current epoch time"

    # game/coregame/rhythmbeats.rpym:374
    old "Este método ejecuta la iteración del beatmap para mover las\n            notas hacia la línea de juicio."
    new "This method iterates the rhythm map to move\n notes on the judgement line."

    # game/coregame/rhythmbeats.rpym:396
    old "Este método retorna un objeto iterable `itertools.zip_longest` con el\n            beatmap para la visualización de los taps en una screen. Esto ayuda a\n            iterar el beatmap con solo 1 bucle for en una screen =D\n\n            Esto debe ser llamado posterior a instanciar la clase. No recibe ningún\n            argumento en particular."
    new "This method returns an iterated `itertools.zip_longest` object with a map of\n beats to display touches on screen. This helps iterate\n the beatmap with only 1 for loop on screen =D\n\n This method must be called after the class is instantiated. It does not take\n any special arguments."

    # game/coregame/rhythmbeats.rpym:407
    old "Este método devuelve una tupla con la precisión media del jugador\n            durante la partida, y la tendencia de reacción (en atraso o en adelanto)\n            con flechas.\n\n            **Formato de retorno:**\n            (Tiempo de reacción media, tendencia de reacción)\n\n            Los valores de precisión media son retornados en milisegundos, mientras\n            que las flechas de tendencia de reacción son retornadas como cadenas de texto.\n            Puedes usar este método para obtener estadísticas durante la partida o\n            al finalizar =D"
    new "This method returns a tuple with the average accuracy of the player\n during the game and the reaction tendency (lagging or leading)\n with arrows.\n **Format return:** (Average reaction time, reaction tendency)\n Average accuracy values are returned in milliseconds and reaction tendency arrows are returned as strings.\n You can use this method to get stats during the game or\n at the end of the game =D"

    # game/coregame/rhythmbeats.rpym:439
    old "Este método retorna `True` si el mapa aún se está ejecutando. En el\n            caso contrario, retorna `False` si se recorrieron todas las notas del\n            Beatmap."
    new "This method returns `True` if the map is still running. Otherwise it returns `False` if all the notes in the Beatmap have been passed."

# TODO: Translation updated at 2023-02-23 23:08

translate english strings:

    # game/coregame/rhythmbeats.rpym:181
    old "Full Combo: %s notas."
    new "Full combo: %s notes."

