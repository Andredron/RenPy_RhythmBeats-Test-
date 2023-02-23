






init python:
    import time, json, requests, threading, ssl, re

    class UpdateManager(threading.Thread):
        
        def __init__(self):
            _("""Constructor de la clase UpdateManager().
            Esta clase se encarga de realizar los procedimientos de recuperación de datos del
            host (ver atributo self.index_url), comprobar si existen actualizaciones y gestionar la
            descarga de paquetes necesarios para la ejecución del juego demostrativo.""")
            
            super(UpdateManager, self).__init__()
            
            self.daemon = True
            
            self.index_url = None
            self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
                            "Cache-Control": "no-cache",
                            "Pragma": "no-cache"}
            
            self.dl_path = config.gamedir if any((renpy.windows, renpy.linux)) else os.path.join(os.environ["ANDROID_PUBLIC"], "game")
            
            self.local_index = persistent.local_index
            self.remote_index = {}
            
            self.request_end = False
            self.exception_content = None
            
            self.update_queue = {}
            self.update_size = 0
            self.progress = [0, 0]
        
        
        def setup(self):
            _("""Este método prepara el entorno de administración y elimina archivos residuales
            de descargas fallidas o repetidas.""")
            
            if not persistent.local_index:
                self.local_index = persistent.local_index = {}
            
            if not os.path.exists(self.dl_path):
                os.mkdir(self.dl_path)
            
            logging.info(_("Eliminando archivos residuales..."))
            for file in os.listdir(self.dl_path):
                if file.endswith(("tmp", ").bruh")):
                    os.remove(os.path.join(self.dl_path, file))
            
            logging.info(_("Archivos residuales eliminados."))
        
        
        def get_exception(self):
            _("""Este método retorna True si ocurrió una excepción durante el procedimiento
            de actualización. En el caso contrario, retorna False.""")
            
            if isinstance(self.exception_content, Exception):
                return True
            return False
        
        
        def get_update(self):
            _("""Este método realiza la comparación de los índices del servidor con los índices
            locales para comprobar si se requiere actualizar o descargar nuevos paquetes.
            Al obtener la comparación, recupera los endpoints de los paquetes (Mediafire)
            y computa el tamaño total de descarga según el header recibido.""")
            
            ssl._create_default_https_context = ssl._create_unverified_context
            
            current_queue = {}
            current_url = ""
            
            logging.info(_("Comparando índice local con el índice remoto"))
            if not config.developer:
                for k in self.remote_index:
                    if k in self.local_index:
                        if self.local_index[k] != self.remote_index[k] or not renpy.exists(k + ".bruh"):
                            if renpy.exists(k + ".bruh"):
                                os.remove(os.path.join(self.dl_path, k + ".bruh"))
                            current_queue.update({k : self.remote_index[k]})
                    else:
                        current_queue.update({k : self.remote_index[k]})
            else:
                logging.info(_("Comparación omitida. Modo desarrollador activo."))
            
            self.progress = [0, len(current_queue)]
            
            
            if len(current_queue) > 0:
                logging.info(_("Obteniendo endpoints de descarga..."))
            
            for k in current_queue:
                self.progress[0] += 1
                r = requests.get(current_queue[k], headers = self.headers, timeout = 5)
                url = re.findall('"((http|ftp)s?://.*?)"', r.text)
                
                for i in url:
                    if i[0].startswith("https://download"):
                        current_url = i[0]
                        break
                
                r = requests.head(current_url, headers = self.headers, timeout = 5)
                self.update_size += round(float(r.headers["Content-Length"]) / 1048576.0, 2)
                self.update_queue.update({k : current_url})
                renpy.restart_interaction()
        
        
        def start_batch_download(self):
            _("""Este método realiza la descarga por lotes con la cola de archivos a descargar.
            La screen download() es llamada cada vez que se necesita descargar un archivo.""")
            
            batch_length = len(self.update_queue)
            batch_count = 0
            
            logging.info(_("Descargando recursos..."))
            logging.info(_("Cola de descarga esperada: %s" % batch_length))
            
            for pkg in sorted(self.update_queue):
                logging.info(_("Descargando \"%s\"...") % pkg)
                batch_count += 1
                
                renpy.call_screen("download",
                            url = self.update_queue[pkg],
                            progress = (batch_count, batch_length),
                            path = os.path.join(self.dl_path, "%s.bruh" % pkg))
                
                self.update_queue.pop(pkg)
                persistent.local_index.update({pkg : self.remote_index[pkg]})
        
        
        def run(self):
            _("""Este método ejecuta la búsqueda de actualizaciones en un hilo paralelo al del juego
            mediante threading.Thread.""")
            
            remote_ver = None
            
            self.setup()
            
            try:
                logging.info(_("Recuperando índice remoto..."))
                r = requests.get(self.index_url, timeout = 5)
                
                if r.status_code == 200:
                    index_digest = json.loads(r.text)
                    
                    self.remote_index = index_digest["packages"]
                    remote_ver = index_digest["version"]
                    
                    logging.info(_("Comprobando versión global..."))
                    if remote_ver != config.version:
                        renpy.call_screen("need_main_update", now_version = remote_ver)
                    
                    self.get_update()
                else:
                    raise Exception(_("Error de adquisición de datos: %s") % r)
            
            except Exception as update_error:
                self.exception_content = update_error
                logging.error(str(update_error))
            
            finally:
                self.request_end = True
                renpy.restart_interaction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
