






init python:

    import discord_rpc, time


    renpy.load_module("coregame/rhythmbeats")

    _("""NOTAS:
    El contenido de este script no forma parte del módulo de RhythmBeats.
    Es código para ejecución correcta de la implementación de este juego.
    """)


    def finish_playstage(screen_queue = [], dissolving = False):
        _("""Esta función cierra las screens escritas en 'screen_queue' cuando la partida finaliza""")
        
        renpy.hide_screen("playground_2dmv")
        if screen_queue:
            for scr in screen_queue:
                renpy.hide_screen(scr)
            if dissolving:
                renpy.with_statement(dissolve)


    def accuracy_color(avg = 0.0, disp = "bar"):
        _("""Esta función se utiliza para colorizar la barra y el texto que señala
        la precisión media del jugador.""")
        
        avg = abs(avg)
        
        colors = {
                "bar" : {"perfect" : "#9F9", "great" : "#FF9", "bad" : "#F44"},
                "text" : {"perfect" : "#090", "great" : "#990", "bad" : "#900"}
        }
        
        if avg < 15.0:
            return colors[disp]["perfect"]
        elif avg >= 15.0 and avg < 30.0:
            return colors[disp]["great"]
        elif avg >= 30.0:
            return colors[disp]["bad"]
        else:
            return "#000"


    def hp_color(hp = 0, disp = "bar"):
        _("""Esta función se utiliza para colorizar la barra y el texto que señala la precisión
        media del jugador.""")
        
        colors = {
                "bar" : {"normal" : "#9F9", "critical" : "#F44"},
                "text" : {"normal" : "#090", "critical" : "#900"}
        }
        
        if hp <= 5:
            return colors[disp]["critical"]
        else:
            return colors[disp]["normal"]


    def level_color(level, mode = "color"):
        colors = {
                2 : "0AA",
                3 : "0A0",
                4 : "AA0",
                5 : "F00",
                6 : "F0F"
        }
        
        if mode == "color":
            return colors[level]
        elif mode == "text":
            return u"{outlinecolor=%s}L%s{/outlinecolor}" % (colors[level], level)


    def trim_text(_text, limit):
        _("""Esto recorta un texto si alzanca un límite determinado de caracteres
        de longitud, agregando puntos suspensivos al final del recorte.""")
        
        if len(_text) > limit:
            return _text[:limit] + "..."
        return _text


    def play_preview(now):
        _("""Esto reproduce un fragmento de la canción completa al seleccionarla
        desde el menú de pistas.""")
        
        if not renpy.music.get_playing(channel = "music") == now["audio_preview"]:
            renpy.music.stop(channel="music", fadeout = 0.15)
            renpy.music.play(
                        now["audio_preview"],
                        loop = True,
                        fadeout = 0.15,
                        if_changed = True)


    class AlphaControl2DMV(BarValue):
        
        def __init__(self):
            _("""Constructor de la clase AlphaControl2DMV().
            Esta clase se utiliza para controlar la atenuación del 2DMV desde los ajustes.
            Hereda la clase BarValue de Ren'Py para ajustar la atenuación con una barra slider.""")
            
            self.step = 0.1
        
        def set_alpha(self, value):
            persistent.custom_alpha = value
            renpy.restart_interaction()
        
        def get_adjustment(self):
            return ui.adjustment(
                range = 1.0,
                value = persistent.custom_alpha,
                changed=self.set_alpha,
                step=self.step)
        
        def get_style(self):
            return "slider", "vslider"


    class MusicData:
        
        def __init__(self, fn):
            self.fn = fn
            self.entire_data = dict()
        
        def load(self):
            try:
                logging.info(_("Cargando metadatos JSON de canciones..."))
                content = renpy.file(self.fn)
                self.entire_data = json.loads(content.read().decode("utf-8"))
            
            except Exception as load_error:
                logging.error(_("Error al cargar metadatos JSON: %s") % str(load_error))
        
        def sort(self, now = "all"):
            sort_results = []
            
            if now == "all":
                for section in sorted(self.entire_data):
                    sort_results.extend(self.entire_data[section])
            else:
                sort_results = self.entire_data[now]
            
            return sort_results
        
        def get_category(self, id):
            music_metadata = {
                        "all" : _("Todos"),
                        "love_live" : _("Love Live!"),
                        "project_sekai" : _("Project SEKAI"),
                        "other" : _("Otras pistas")
            }
            
            return music_metadata[id]


    class DiscordRichPresence:
        _("""Esta clase permite hacer visible al juego en Discord mediante
        Discord Rich Presence (RPC).
        Esto solo funciona en PC, y para que la actividad sea visible, el jugador
        debe tener instalado el cliente de Discord en su PC.
        No se asegura que el juego sea visible si se usa Discord desde un navegador.""")
        
        def __init__(self):
            self.client = "1072433463833133116"
            self.is_running = True
            self.runtime_epoch = time.time()
            
            self.cb_methods = {
                            "ready" : self.rpc_ready,
                            "disconnected" : self.rpc_disconnect,
                            "error" : self.rpc_error}
            
            discord_rpc.initialize(self.client, callbacks=self.cb_methods, log=False)
        
        
        
        
        def rpc_ready(self, userdict):
            logging.info(_("Discord RPC está activo..."))
            logging.info(_("Usuario detectado: %s") % userdict["username"])
            logging.info(_("ID de usuario: #%s") % userdict["id"])
            
            renpy.notify(_("{image=ui_icon_discord}  ¡Ren'Py RhythmBeats ya es visible en Discord!"))
        
        
        def rpc_disconnect(self, code, msg):
            logging.warning(_("Discord RPC está desconectado."))
            logging.warning(_("Código de error: %s") % code)
            logging.warning(_("Detalles: %s") % msg)
        
        
        def rpc_error(self, code, msg):
            logging.error(_("Error durante la ejecución de Discord RPC."))
            logging.error(_("Código de error: %s") % code)
            logging.error(_("Detalles: %s") % msg)
        
        
        
        
        def set_status(self, state = "", details = "", image_text = _("Jugando a Ren'Py RhythmBeats!")):
            
            discord_rpc.update_presence(
                **{
                    "state" : state,
                    "details" : details,
                    "start_timestamp": self.runtime_epoch,
                    "large_image_key": "largeimage",
                    "large_image_text" : image_text
                }
            )
            
            renpy.restart_interaction()
        
        
        def stop(self):
            self.is_running = False
            discord_rpc.shutdown()
        
        
        def rpc_updater(self):
            while True:
                try:
                    discord_rpc.update_connection()
                    discord_rpc.run_callbacks()
                
                except Exception as rpc_upd_error:
                    print(_("Error: %s") % rpc_upd_error)
                finally:
                    if self.is_running:
                        time.sleep(3)
                    else:
                        break
        
        
        def rpc_start(self):
            renpy.notify(_("{image=ui_icon_discord}  Ren'Py RhythmBeats se está conectando con Discord..."))
            
            t1 = threading.Thread(target = self.rpc_updater)
            t1.setDaemon(True)
            t1.start()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
