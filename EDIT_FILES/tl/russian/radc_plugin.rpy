# TODO: Translation updated at 2023-02-23 14:02

translate russian strings:

    # game/radc_plugin.rpy:18
    old "Retorna la ruta donde Ren'Py pretende leer los Assets del juego. Útil si quieres\n        descargar un archivo que posteriormente sea leído por el juego.\n\n        En el caso de Android, la carpeta /game en la ruta pública no está creada. En ese caso,\n        os.mkdir() se encargará de crear la carpeta si no existe."
    new "Возвращает путь, по которому Ren'Py собирается читать ассеты игры. Полезно, если вы хотите загрузить файл, который впоследствии будет прочитан игрой. \n\n В случае Android папка /game в открытом пути не создается. В этом случае \n   os.mkdir() создаст папку, если она не существует."

    # game/radc_plugin.rpy:36
    old "Esta clase se encarga de obtener la URL final de un archivo almacenado en\n        alguna nube que muestre la URL final en la página de descarga del archivo."
    new "Этот класс отвечает за получение конечного URL файла, хранящегося в некотором облаке, \n и отображает конечный URL на странице загрузки файла."

    # game/radc_plugin.rpy:40
    old "Inicializa y construye los atributos de la clase."
    new "Инициализирует и строит атрибуты класса."

    # game/radc_plugin.rpy:52
    old "Retorna bool si la recuperación ha terminado o no."
    new "Возвращает bool, завершено ли восстановление или нет."

    # game/radc_plugin.rpy:56
    old "Retorna la URL final de descarga."
    new "Возвращает окончательный URL-адрес загрузки."

    # game/radc_plugin.rpy:60
    old "Retorna True si hubo una excepción o no, durante la recuperación."
    new "Возвращает True, если во время восстановления произошло исключение или нет."

    # game/radc_plugin.rpy:66
    old "Realiza el raspado de la URL compartida."
    new "Выполняет сканирование общего URL-адреса."

    # game/radc_plugin.rpy:99
    old "Esta clase se encarga de ejecutar y hacer el seguimiento de una descarga solicitada."
    new "Этот класс отвечает за выполнение и отслеживание запрошенной загрузки."

    # game/radc_plugin.rpy:102
    old "Constructor de la clase. Recibe los siguientes argumentos:\n\n                url (Obligatorio):\n                    La URL del archivo que quieres descargar. Debe ser un archivo físico, no una\n                    prevista web.\n\n                savepath:\n                    Si no es None, es una cadena con la ruta física del dispositivo donde se guardará\n                    el archivo."
    new "Конструктор класса. Он получает следующие аргументы:\n\n                      url (Obligatorio):\n                      URL-адрес файла, который вы хотите загрузить. Это должен быть физический файл, \n                а не веб-превью. \n\n             savepath:\n                    Если это не None, то это строка с физическим путем к устройству, на котором будет\n                    сохранен файл"

    # game/radc_plugin.rpy:127
    old "Retorna el porcentaje descargado para ser interpretado por una barra de progreso."
    new "Возвращает процент загрузки, который будет интерпретироваться индикатором выполнения."

    # game/radc_plugin.rpy:132
    old "Retorna una lista con los MB descargados y los MB totales del archivo a descargar."
    new "Возвращает список загруженных МБ и общее количество МБ загружаемого файла."

    # game/radc_plugin.rpy:136
    old "Retorna True si la descarga ha finalizado, de lo contrario, retorna False."
    new "Возвращает True, если загрузка завершена, в противном случае возвращает False."

    # game/radc_plugin.rpy:140
    old "Retorna True si se presenta un error en la descarga."
    new "Возвращает True, если произошла ошибка загрузки."

    # game/radc_plugin.rpy:147
    old "Calcula el progreso de la descarga."
    new "Рассчитывает ход выполнения загрузки."

    # game/radc_plugin.rpy:156
    old "Inicia la descarga en un contexto SSL no verificado para evitar errores de descarga\n            por conflictos con los certificados de seguridad."
    new "Запустите загрузку в непроверенном SSL-контексте, чтобы избежать ошибок загрузки \n              из-за конфликтов сертификатов безопасности."

    # game/radc_plugin.rpy:166
    old "Error DownloadHandler(): %s"
    new "Ошибка DownloadHandler(): %s"

