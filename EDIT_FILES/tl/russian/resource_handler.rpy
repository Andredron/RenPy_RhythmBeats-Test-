# TODO: Translation updated at 2023-02-23 14:02

translate russian strings:

    # game/resource_handler.rpy:14
    old "Constructor de la clase UpdateManager().\n            Esta clase se encarga de realizar los procedimientos de recuperación de datos del\n            host (ver atributo self.index_url), comprobar si existen actualizaciones y gestionar la\n            descarga de paquetes necesarios para la ejecución del juego demostrativo."
    new "Конструктор clase UpdateManager().\n                  Этот класс отвечает за выполнение процедур получения данных\n                                  о хосте (см. атрибут self.index_url), проверку обновлений и управление загрузкой пакетов,\n          необходимых для запуска демо-игры."

    # game/resource_handler.rpy:42
    old "Este método prepara el entorno de administración y elimina archivos residuales\n            de descargas fallidas o repetidas."
    new "Этот метод подготавливает среду управления и удаляет \n                   остаточные файлы после неудачных или повторных загрузок."

    # game/resource_handler.rpy:51
    old "Eliminando archivos residuales..."
    new "Удаление остаточных файлов..."

    # game/resource_handler.rpy:56
    old "Archivos residuales eliminados."
    new "Остаточные файлы удалены."

    # game/resource_handler.rpy:60
    old "Este método retorna True si ocurrió una excepción durante el procedimiento\n            de actualización. En el caso contrario, retorna False."
    new "Этот метод возвращает True, если во время процедуры обновления произошло исключение.\n       В противном случае он возвращает False."

    # game/resource_handler.rpy:69
    old "Este método realiza la comparación de los índices del servidor con los índices\n            locales para comprobar si se requiere actualizar o descargar nuevos paquetes.\n            Al obtener la comparación, recupera los endpoints de los paquetes (Mediafire)\n            y computa el tamaño total de descarga según el header recibido."
    new "Этот метод сравнивает индексы сервера с локальными индексами,\n        чтобы проверить, требуется ли обновление или загрузка новых пакетов. \n                    Когда сравнение получено, он извлекает конечные точки пакетов (Mediafire)\n                            и вычисляет общий размер загрузки в соответствии с полученным заголовком."

    # game/resource_handler.rpy:79
    old "Comparando índice local con el índice remoto"
    new "Сравнение локального индекса с удаленным"

    # game/resource_handler.rpy:90
    old "Comparación omitida. Modo desarrollador activo."
    new "Сравнение опущено. Режим разработчика активен."

    # game/resource_handler.rpy:96
    old "Obteniendo endpoints de descarga..."
    new "Получение конечных точек скачивания..."

    # game/resource_handler.rpy:115
    old "Este método realiza la descarga por lotes con la cola de archivos a descargar.\n            La screen download() es llamada cada vez que se necesita descargar un archivo."
    new "Этот метод выполняет пакетную загрузку с очередью файлов для загрузки. \n          Экран download() вызывается каждый раз, когда файл должен быть загружен."

    # game/resource_handler.rpy:121
    old "Descargando recursos..."
    new "Скачивание ресурсов..."

    # game/resource_handler.rpy:125
    old "Descargando \"%s\"..."
    new "Загружаем \"%s\"..."

    # game/resource_handler.rpy:138
    old "Este método ejecuta la búsqueda de actualizaciones en un hilo paralelo al del juego\n            mediante threading.Thread."
    new "Этот метод выполняет поиск обновлений в потоке, параллельном игровому потоку \n         через threading.Thread."

    # game/resource_handler.rpy:146
    old "Recuperando índice remoto..."
    new "Получение удаленного индекса ..."

    # game/resource_handler.rpy:155
    old "Comprobando versión global..."
    new "Проверяем глобальную версию ..."

    # game/resource_handler.rpy:161
    old "Error de adquisición de datos: %s"
    new "Ошибка при получении данных: %s"

