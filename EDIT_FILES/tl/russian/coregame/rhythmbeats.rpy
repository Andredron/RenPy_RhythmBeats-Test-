# TODO: Translation updated at 2023-02-23 14:02

translate russian strings:

    # game/coregame/rhythmbeats.rpym:33
    old "Una clase simple para emitir excepciones bajo el nombre de Ren'Py RhythmBeats."
    new "Простой класс для выдачи исключений под именем Ren'Py RhythmBeats."

    # game/coregame/rhythmbeats.rpym:39
    old "Constructor de la clase RhythmPlayground().\n            Recibe 5 parámetros (2 obligatorios) en el momento que se crea la instancia de la clase.\n            Estos parámetros son los siguientes:\n\n            fn (str):\n                Este parámetro es obligatorio, y recibe una cadena con la ruta del archivo BEAT\n                relativa a la carpeta /game de tu juego.\n                Este archivo puede ser leído incluso dentro de un paquete RPA.\n\n            displayable (str o displayable):\n                Este parámetro es obligatorio, y recibe como argumento un elemento displayable\n                que será utilizado para mostrar cada nota en la pantalla. Puedes pasar como\n                argumento una ruta de una image, o una imagen modificada con Transform().\n\n            offset_map (float):\n                Si no es 0.0, este parámetro recibe como argumento un número de punto flotante,\n                que representa el tiempo (en segundos) que se desfasa el beatmap respecto de la\n                reproducción de la pista musical. Esto debería ser un número individual de cada beatmap.\n\n            offset_game (float):\n                Si no es 0.0, este parámetro recibe como argumento un número de punto flotante\n                que representa el tiempo (en milisegundos) que se agrega como desfase\n                personalizable por el jugador.\n                Esto es útil para que el jugador pueda calibrar manualmente en caso de que perciba\n                que la cascada de notas no se sincroniza del todo bien con sus toques. En ese caso,\n                puedes pasar como argumento una variable persistente con el valor calibrado por el\n                jugador.\n\n            threshold (float):\n                Si no es 0.1, este parámetro recibe como argumento un número de punto flotante,\n                que representa el umbral de tiempo (en segundos) para detectar si el jugador ha\n                tocado la nota o no. Por defecto se ha fijado el umbral en 0.1 segundos (100ms) por\n                lo que el jugador tiene un rango total de 200ms para tocar correctamente una nota.\n\n            failsafe (bool):\n                El modo seguro permite reproducir el beatmap sin necesidad de tocar las notas.\n                Es útil en caso de querer ajustar visualmente la cascada de notas respecto\n                de la música (mediante offset_map).\n                Si es True, ejecutará el beatmap en modo seguro. Si es False, el\n                juego se ejecutará normalmente.\n            "
    new "Конструктор класса RhythmPlayground().\n                 Он получает 5 параметров (2 обязательных) при создании экземпляра класса.\n                           Эти параметры следующие:\n                          fn (str):\n                Этот параметр является обязательным и принимает строку с путем к BEAT-файлу\n                    относительно папки /game вашей игры.\n                    Этот файл может быть прочитан даже внутри пакета RPA.\n                       displayable (str или displayable):\n              Этот параметр является обязательным и принимает в качестве аргумента элемент displayable,\n      который будет использоваться для отображения каждой ноты на экране. В качестве аргумента\n    можно передать путь к изображению или изображение, измененное с помощью Transform().\n\n  offset_map (float):\n             Если не 0.0, этот параметр принимает в качестве аргумента число с плавающей точкой,\n            представляющее время (в секундах), на которое битмап смещен от воспроизведения\n                 музыкальной дорожки. Это должно быть индивидуальное число для каждого битмапа.\n\n                      offset_game (float):\n                Если не 0.0, этот параметр принимает в качестве аргумента число с плавающей точкой,\n           представляющее время (в миллисекундах), которое добавляется в качестве\n               настраиваемого смещения проигрывателем.\n       Это полезно для ручной калибровки игроком в случае, если он/она чувствует, что\n                    каскад нот не совсем синхронизирован с его/ее прикосновениями. В этом случае вы можете\n             передать в качестве аргумента постоянную переменную со значением,\n                      откалиброванным игроком.\n\n       threshold (float):\n                Если не 0.1, этот параметр принимает в качестве аргумента число с плавающей точкой,\n            которое представляет собой порог времени (в секундах) для определения того,\n                    сыграл игрок ноту или нет. По умолчанию порог установлен на 0,1 секунды (100 мс), поэтому\n          у игрока есть 200 мс, чтобы правильно сыграть ноту.\n\n                                           failsafe (bool):\n                Режим failsafe позволяет воспроизводить битмап без проигрывания нот.\n                          Это полезно в том случае, если вы хотите визуально настроить каскад нот\n                   относительно музыки (через offset_map).\n            Если True, то битмап будет запущен в безопасном режиме. Если False, игра\n        будет запущена в обычном режиме.\n           "

    # game/coregame/rhythmbeats.rpym:148
    old "Este método carga y procesa las secuencias de un archivo beatmap de\n            una canción en específico. El archivo `.beat` debe ser señalado en el\n            momento en que se crea una instancia de la clase.\n\n            Esto debe ser llamado posterior a instanciar la clase. No recibe ningún\n            argumento ni tampoco retorna datos."
    new "Этот метод загружает и обрабатывает последовательности файла битмапа\n           определенной песни. Файл `.beat` должен быть указан\n                             в момент создания экземпляра класса.\n\n                          Этот метод должен быть вызван после инстанцирования класса. Метод не принимает\n     никаких аргументов и не возвращает никаких данных."

    # game/coregame/rhythmbeats.rpym:155
    old "Process"
    new "Процесс"

    # game/coregame/rhythmbeats.rpym:155
    old "Cargando beatmap..."
    new "Загрузка карты ритмов..."

    # game/coregame/rhythmbeats.rpym:159
    old "Stats"
    new "Статистика"

    # game/coregame/rhythmbeats.rpym:159
    old "Ruta relativa: %s."
    new "Относительный путь: %s."

    # game/coregame/rhythmbeats.rpym:180
    old "Offset final: %sms."
    new "Окончательное смещение: %sms."

    # game/coregame/rhythmbeats.rpym:185
    old "Preparando waterfall (SpriteManager)..."
    new "Подготовка водопада (SpriteManager)..."

    # game/coregame/rhythmbeats.rpym:187
    old "OK"
    new "OK"

    # game/coregame/rhythmbeats.rpym:187
    old "Beatmap listo para ejecutar.\n"
    new "Битмап готов к работе."

    # game/coregame/rhythmbeats.rpym:197
    old "\n            (NO DOCUMENTADO)\n            Este método recoge los eventos de Pygame para reconocer los toques\n            del jugador en el juego, ya sea con un teclado o con pantalla táctil.\n\n            NOTA: No puedo realizar lecturas de múltiples dedos en una pantalla\n            táctil, ya que Ren'Py parece limitarme los eventos de Pygame, por lo\n            que el reconocimiento de toques en móviles puede ser... desagradable =(\n            "
    new "\n            (НЕ ДОКУМЕНТИРОВАНО)\n        Этот метод собирает события Pygame для распознавания прикосновений\n            игрока в игре, будь то клавиатура или сенсорный экран.\n\n                           ПРИМЕЧАНИЕ: Я не могу сделать многопальцевое чтение на сенсорном экране,\n       так как Ren'Py, похоже, ограничивает меня событиями Pygame, поэтому\n             распознавание касаний на мобильных устройствах может быть... неприятным =(\n         "

    # game/coregame/rhythmbeats.rpym:227
    old "Se encarga del gameplay principal.\n            Este método reproduce el beatmap cargado y se encarga de realizar todos\n            los cálculos necesarios para determinar si el jugador acierta o falla\n            alguna nota.\n            Las interacciones del jugador se computan en este método respecto de un\n            tiempo de época (Epoch) dado en segundos, que por cierto, es entregada\n            gracias a la clase `DynamicDisplayable()` de Ren'Py.\n\n            No retorna ningún valor importante para el desarrollador o el jugador."
    new "Он заботится об основном игровом процессе.\n    Этот метод воспроизводит загруженную карту ритмов\n                      и выполняет все необходимые вычисления, чтобы определить, попадает ли игрок в ноты\n           или промахивается.\n      Взаимодействие игрока вычисляется в этом методе относительно\n                       заданного времени эпохи в секундах, которое, кстати, передается благодаря\n         классу Ren'Py's `DynamicDisplayable()`. \n\n                        Он не возвращает никакого важного значения для разработчика или игрока."

    # game/coregame/rhythmbeats.rpym:320
    old "Este método crea 'n' cantidad de sprites para el SpriteManager()\n            en función de la cantidad de notas que posee el beatmap."
    new "Этот метод создает 'n' количество спрайтов для SpriteManager()\n              на основе количества нот в битмапе."

    # game/coregame/rhythmbeats.rpym:339
    old "Esta función calcula las coordenadas de las notas que van cayendo,\n            respecto del timestamp de esa nota y el tiempo epoch actual."
    new "Эта функция вычисляет координаты падающих нот относительно\n                     временной метки этой ноты и текущего времени эпохи"

    # game/coregame/rhythmbeats.rpym:374
    old "Este método ejecuta la iteración del beatmap para mover las\n            notas hacia la línea de juicio."
    new "Этот метод выполняет итерацию карты ритмов для перемещения\n             нот на линию суждения."

    # game/coregame/rhythmbeats.rpym:396
    old "Este método retorna un objeto iterable `itertools.zip_longest` con el\n            beatmap para la visualización de los taps en una screen. Esto ayuda a\n            iterar el beatmap con solo 1 bucle for en una screen =D\n\n            Esto debe ser llamado posterior a instanciar la clase. No recibe ningún\n            argumento en particular."
    new "Этот метод возвращает итерируемый объект `itertools.zip_longest` с картой\n        ритмов для отображения касаний на экране. Это помогает итерировать\n               карту тактов с помощью только 1 цикла for на экране =D\n\n             Этот метод должен быть вызван после инстанцирования класса. Она не принимает\n       никаких особых аргументов."

    # game/coregame/rhythmbeats.rpym:407
    old "Este método devuelve una tupla con la precisión media del jugador\n            durante la partida, y la tendencia de reacción (en atraso o en adelanto)\n            con flechas.\n\n            **Formato de retorno:**\n            (Tiempo de reacción media, tendencia de reacción)\n\n            Los valores de precisión media son retornados en milisegundos, mientras\n            que las flechas de tendencia de reacción son retornadas como cadenas de texto.\n            Puedes usar este método para obtener estadísticas durante la partida o\n            al finalizar =D"
    new "Этот метод возвращает кортеж со средней точностью игрока\n                     во время игры и тенденцию реакции (в отставании или опережении)\n                     со стрелками.\n             **Формат возврата:**\n               (Среднее время реакции, тенденция реакции)\n                     Значения средней точности возвращаются в миллисекундах, а\n                          стрелки тенденции реакции возвращаются в виде строк.\n                                      Вы можете использовать этот метод для получения статистики во время игры или\n      в конце игры =D"

    # game/coregame/rhythmbeats.rpym:439
    old "Este método retorna `True` si el mapa aún se está ejecutando. En el\n            caso contrario, retorna `False` si se recorrieron todas las notas del\n            Beatmap."
    new "Этот метод возвращает `True`, если карта все еще выполняется. В противном\n      случае он возвращает `False`, если все ноты в карте Beatmap\n                 были пройдены."

    # game/coregame/rhythmbeats.rpym:181
    old "Full Combo: %s notas."
    new "Полное комбо: %s примечаний."

