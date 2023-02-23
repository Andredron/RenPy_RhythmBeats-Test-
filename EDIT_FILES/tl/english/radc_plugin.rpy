# TODO: Translation updated at 2023-02-23 14:02

translate english strings:

    # game/radc_plugin.rpy:18
    old "Retorna la ruta donde Ren'Py pretende leer los Assets del juego. Útil si quieres\n        descargar un archivo que posteriormente sea leído por el juego.\n\n        En el caso de Android, la carpeta /game en la ruta pública no está creada. En ese caso,\n        os.mkdir() se encargará de crear la carpeta si no existe."
    new "Returns the path that Ren'Py is going to use to read the game's assemblies. Useful if\n    you want to upload a file to be read by the game afterwards.\n\n          In the case of Android the /game folder in the open path is not created. In this case \n         os.mkdir() will create the folder if it does not exist."

    # game/radc_plugin.rpy:36
    old "Esta clase se encarga de obtener la URL final de un archivo almacenado en\n        alguna nube que muestre la URL final en la página de descarga del archivo."
    new "This class is responsible for retrieving the final URL of the file stored in some cloud,\n             and displaying the final URL on the file download page."

    # game/radc_plugin.rpy:40
    old "Inicializa y construye los atributos de la clase."
    new "Initialises and builds class attributes."

    # game/radc_plugin.rpy:52
    old "Retorna bool si la recuperación ha terminado o no."
    new "Returns bool whether recovery is complete or not."

    # game/radc_plugin.rpy:56
    old "Retorna la URL final de descarga."
    new "Returns the final download URL."

    # game/radc_plugin.rpy:60
    old "Retorna True si hubo una excepción o no, durante la recuperación.s"
    new "Returns True if an exception has occurred during recovery or not."

    # game/radc_plugin.rpy:66
    old "Realiza el raspado de la URL compartida."
    new "Performs a general URL scan."

    # game/radc_plugin.rpy:99
    old "Esta clase se encarga de ejecutar y hacer el seguimiento de una descarga solicitada."
    new "This class is responsible for executing and tracking the requested load."

    # game/radc_plugin.rpy:102
    old "Constructor de la clase. Recibe los siguientes argumentos:\n\n                url (Obligatorio):\n                    La URL del archivo que quieres descargar. Debe ser un archivo físico, no una\n                    prevista web.\n\n                savepath:\n                    Si no es None, es una cadena con la ruta física del dispositivo donde se guardará\n                    el archivo."
    new "Class constructor. It gets the following arguments:\n                         url (Obligatorio):\n                    URL of the file you want to upload. It must be a physical file,\n                                 not a web preview.\n\n           savepath:\n                    If this is not None, then this is a string with the physical path to the device where the file\n      will be saved"

    # game/radc_plugin.rpy:127
    old "Retorna el porcentaje descargado para ser interpretado por una barra de progreso."
    new "Returns the load percentage to be interpreted by the progress bar."

    # game/radc_plugin.rpy:132
    old "Retorna una lista con los MB descargados y los MB totales del archivo a descargar."
    new "Returns a list of downloaded MBs and the total number of MBs of the downloaded file."

    # game/radc_plugin.rpy:136
    old "Retorna True si la descarga ha finalizado, de lo contrario, retorna False."
    new "Returns True if loading is complete, otherwise returns False."

    # game/radc_plugin.rpy:140
    old "Retorna True si se presenta un error en la descarga."
    new "Returns True if a loading error has occurred."

    # game/radc_plugin.rpy:147
    old "Calcula el progreso de la descarga."
    new "Calculates the progress of the load."

    # game/radc_plugin.rpy:156
    old "Inicia la descarga en un contexto SSL no verificado para evitar errores de descarga\n            por conflictos con los certificados de seguridad."
    new "Run the download in an untested SSL context to avoid download \n                                 errors due to security certificate conflicts."

    # game/radc_plugin.rpy:166
    old "Error DownloadHandler(): %s"
    new "Error DownloadHandler(): %s"

