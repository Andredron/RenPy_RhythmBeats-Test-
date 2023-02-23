# TODO: Translation updated at 2023-02-23 14:02

translate english strings:

    # game/resource_handler.rpy:14
    old "Constructor de la clase UpdateManager().\n            Esta clase se encarga de realizar los procedimientos de recuperación de datos del\n            host (ver atributo self.index_url), comprobar si existen actualizaciones y gestionar la\n            descarga de paquetes necesarios para la ejecución del juego demostrativo."
    new "Clase UpdateManager() constructor.\n                  This class is responsible for executing procedures to retrieve\n                               host data (see self.index_url attribute), check for updates and manage the download of\n             packages needed to run the demo game."

    # game/resource_handler.rpy:42
    old "Este método prepara el entorno de administración y elimina archivos residuales\n            de descargas fallidas o repetidas."
    new "This method prepares the control environment and deletes \n                 residual files after failed or repeated downloads."

    # game/resource_handler.rpy:51
    old "Eliminando archivos residuales..."
    new "Deleting residual files..."

    # game/resource_handler.rpy:56
    old "Archivos residuales eliminados."
    new "The remaining files have been deleted."

    # game/resource_handler.rpy:60
    old "Este método retorna True si ocurrió una excepción durante el procedimiento\n            de actualización. En el caso contrario, retorna False."
    new "This method returns True if an exception occurs during the update procedure.\n          Otherwise it returns False."

    # game/resource_handler.rpy:69
    old "Este método realiza la comparación de los índices del servidor con los índices\n            locales para comprobar si se requiere actualizar o descargar nuevos paquetes.\n            Al obtener la comparación, recupera los endpoints de los paquetes (Mediafire)\n            y computa el tamaño total de descarga según el header recibido."
    new "This method compares server indexes with local indexes,\n                                   to see if new packages need to be updated or downloaded.\n                                 When the comparison is received, it retrieves the packet endpoints (Mediafire)\n           and calculates the total download size according to the received header."

    # game/resource_handler.rpy:79
    old "Comparando índice local con el índice remoto"
    new "Comparing a local index with a remote one"

    # game/resource_handler.rpy:90
    old "Comparación omitida. Modo desarrollador activo."
    new "The comparison is omitted. Developer mode is active."

    # game/resource_handler.rpy:96
    old "Obteniendo endpoints de descarga..."
    new "Obtaining download endpoints..."

    # game/resource_handler.rpy:115
    old "Este método realiza la descarga por lotes con la cola de archivos a descargar.\n            La screen download() es llamada cada vez que se necesita descargar un archivo."
    new "This method performs a batch download with a queue of files to be downloaded. \n            The download() screen is called each time a file is to be downloaded"

    # game/resource_handler.rpy:121
    old "Descargando recursos..."
    new "Downloading resources..."

    # game/resource_handler.rpy:125
    old "Descargando \"%s\"..."
    new "Upload \"%s\"..."

    # game/resource_handler.rpy:138
    old "Este método ejecuta la búsqueda de actualizaciones en un hilo paralelo al del juego\n            mediante threading.Thread."
    new "This method searches for updates in a thread parallel to the \n                                 game thread via threading.Thread."

    # game/resource_handler.rpy:146
    old "Recuperando índice remoto..."
    new "Получение удаленного индекса ..."

    # game/resource_handler.rpy:155
    old "Comprobando versión global..."
    new "Checking the global version ..."

    # game/resource_handler.rpy:161
    old "Error de adquisición de datos: %s"
    new "Error when receiving data: %s"

