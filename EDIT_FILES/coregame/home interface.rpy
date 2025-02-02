









screen performance_warning():
    modal True
    zorder 200
    style_prefix "confirm"

    use notify_window(_("ADVERTENCIA DE RENDIMIENTO"), notify_sound=audio.ui_sound_error):
        vbox:
            spacing 15
            text _("Las pistas musicales con un número {color=cf0}igual o mayor a 450 notas{/color} podrían experimentar severos problemas de rendimiento, ya que el motor no es lo suficientemente eficiente en móviles =(")
            text _("Si quieres jugar esta pista con lag, será bajo tu propia responsabilidad.")
            text _("De verdad quieres jugarla?")

        hbox:
            style_prefix "main_ui"
            xalign 0.5 ypos 0.8 spacing 20

            textbutton _("Jugar de todos modos"):
                action [SetVariable("data", p.song_selected),
                Hide("performance_warning"),
                Hide("category_switcher"),
                Hide("song_select", transition = dissolve),
                Return(),
                Jump("game_playstage")]
                activate_sound audio.ui_sound_btn03

            textbutton _("Cerrar advertencia"):
                action Hide("performance_warning")
                activate_sound audio.ui_sound_btn02





screen config_panel():
    style_prefix "config_panel"
    modal True
    zorder 104

    add "tex_black"

    default current_config = "system"

    if current_config == "system":
        use system_menu
    elif current_config == "audio":
        use audio_control
    elif current_config == "calibrate":
        use calibration_menu
    elif current_config == "alpha":
        use alpha_menu



    vbox:
        textbutton _("Sistema") action SetLocalVariable("current_config", "system")
        textbutton _("Ajustes de sonido") action SetLocalVariable("current_config", "audio")
        textbutton _("Calibración") action SetLocalVariable("current_config", "calibrate")
        textbutton _("Atenuación 2DMV") action SetLocalVariable("current_config", "alpha")

    hbox:
        textbutton _("Cerrar menú") action Hide("config_panel"):
            activate_sound audio.ui_sound_btn02



screen calibration_menu():
    style_prefix "settings"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label _("CALIBRACIÓN MANUAL")

        text _("Por defecto, la compensación de tiempo es de 0 milisegundos.\nEn valores negativos, las notas llegarán {color=cf0}antes de lo esperado{/color}, mientras que con valores positivos se {color=cf0}retrasará la llegada{/color} de las notas.")

        vbox:
            style_prefix "offset_setup"
            label _("[persistent.custom_offset]{size=20}ms{/size}")

            hbox:
                spacing 15
                textbutton "-10" action If(
                persistent.custom_offset - 10 >= -1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset - 10),
                None)

                textbutton "-1" action If(
                persistent.custom_offset - 1 >= -1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset - 1),
                None)

                null width 40

                textbutton "+1" action If(
                persistent.custom_offset + 1 <= 1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset + 1),
                None)

                textbutton "+10" action If(
                persistent.custom_offset + 10 <= 1000,
                SetVariable("persistent.custom_offset", persistent.custom_offset + 10),
                None)



screen audio_control():
    style_prefix "settings"

    frame at place_atl((0.5, -0.5), (0.5, 0.5), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label _("AJUSTES DE SONIDO")

        text _("Ajusta el volumen de los canales de audio aquí abajo.")

        vbox:
            text _("BGM (Música)") size 20
            bar:
                value Preference("music volume")

        vbox:
            text _("UI (Interfaz)") size 20
            bar:
                value Preference("sound volume")

        vbox:
            text _("SFX (Efectos de sonido)") size 20
            bar:
                value Preference("voice volume")



screen alpha_menu():
    style_prefix "settings"

    add Transform(im.Blur(p.song_selected["cover"], 2.0), zoom = 2.5)
    add Solid("#000") alpha persistent.custom_alpha

    frame at place_atl((0.5, -0.5), (0.5, 0.5), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label _("ATENUACIÓN DE 2DMVs")

        text _("Si el brillo normal del fondo (2DMV) te incomoda a la vista, ajusta la atenuación del fondo.")

        vbox:
            text "%.02f%%" % round(persistent.custom_alpha * 100, 2):
                size 24
                xalign 0.5

            bar:
                value AlphaControl2DMV()



screen system_menu():
    style_prefix "settings"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label _("PREFERENCIAS DE SISTEMA")

        text _("Aquí puedes ajustar distintos parámetros de sistema que se verán reflejados durante el juego.")

        viewport:
            xysize (650, 320)
            yinitial 0.0
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            has vbox:
                style_prefix "config_toggle"

            vbox:
                text _("Modo de visualización:")
                hbox:
                    spacing 15
                    if renpy.windows or renpy.linux:
                        textbutton _("Ventana") action Preference("display", "window")
                    textbutton _("Pantalla Completa") action Preference("display", "fullscreen")

            vbox:
                text _("Métricas de operación:")
                hbox:
                    spacing 15
                    textbutton _("Oculto") action SetVariable("persistent.operating_stats", False)
                    textbutton _("Visible") action SetVariable("persistent.operating_stats", True)

            if renpy.windows or renpy.linux:
                vbox:
                    text _("Presencia en Discord (Discord RPC):")
                    hbox:
                        spacing 15
                        textbutton _("Inactivo") action SetVariable("persistent.discord_rpc", False), Notify(_("Los cambios de Discord RPC se aplicarán en el próximo arranque del juego."))
                        textbutton _("Activo") action SetVariable("persistent.discord_rpc", True), Notify(_("Los cambios de Discord RPC se aplicarán en el próximo arranque del juego."))

            vbox:
                text _("Ejecución de pistas musicales:")
                hbox:
                    spacing 15
                    textbutton _("Modo Juego") action SetVariable("persistent.failsafe", False)

                    if config.developer:
                        textbutton _("Modo Seguro") action SetVariable("persistent.failsafe", True)

            vbox:
                text _("Fotogramas objetivo (Reinicio del juego requerido):")
                hbox:
                    textbutton _("Automático") action Preference("gl framerate", None), Notify(_("Los cambios en los FPS se aplicarán en el próximo arranque del juego."))
                    textbutton _("30 FPS") action Preference("gl framerate", 30), Notify(_("Los cambios en los FPS se aplicarán en el próximo arranque del juego."))
                    textbutton _("45 FPS") action Preference("gl framerate", 48), Notify(_("Los cambios en los FPS se aplicarán en el próximo arranque del juego."))
                    textbutton _("60 FPS") action Preference("gl framerate", 60), Notify(_("Los cambios en los FPS se aplicarán en el próximo arranque del juego."))

            vbox:
                text _("API Gráfica (Reinicio del juego requerido):")

                hbox:
                    textbutton _("Automático") action _SetRenderer("auto"), Notify(_("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego."))

                    if renpy.windows or renpy.linux:
                        textbutton _("OpenGL") action _SetRenderer("gl2" if config.gl2 else "gl"), Notify(_("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego."))
                        textbutton _("ANGLE") action _SetRenderer("angle2" if config.gl2 else "angle"), Notify(_("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego."))
                    elif renpy.android:
                        textbutton _("OpenGL ES (Por defecto)") action _SetRenderer("gles2" if config.gl2 else "gles"), Notify(_("Los cambios de API Gráfica se aplicarán en el próximo arranque del juego."))

            vbox:
                text _("Tearing (V-Sync):")
                hbox:
                    textbutton _("Inactivo") action Preference("gl tearing", False), Notify(_("Los cambios de V-Sync se aplicarán en el próximo arranque del juego."))
                    textbutton _("Activo") action Preference("gl tearing", True), Notify(_("Los cambios de V-Sync se aplicarán en el próximo arranque del juego."))

            vbox:
                text _("Idioma (Language):")
                hbox:
                    textbutton _("Español") action Language(None)
                    textbutton _("English") action Language("english")
                    textbutton _("Русский") action Language("russian")




screen category_switcher():
    style_prefix "switcher"
    on "update" action Hide("category_switcher")

    frame at switcher_animation:
        has vbox
        textbutton _("Todos") action SetVariable("p.category", "all")
        textbutton _("Love Live!") action SetVariable("p.category", "love_live")
        textbutton _("Project SEKAI") action SetVariable("p.category", "project_sekai")
        textbutton _("Otras Pistas") action SetVariable("p.category", "other")


screen song_select(data):
    style_prefix "songlist"
    on "show" action Function(play_preview, now = p.song_selected)

    add Transform(im.Blur(p.song_selected["cover"], 2.0), zoom = 2.5) at cover_change_animation
    add "tex_black"


    hbox:
        style_prefix "sort_music"

        textbutton "{font=DejavuSans.ttf}{size=25}⚙{/size}{/font}":
            style_prefix "offset_setup"
            activate_sound audio.ui_sound_btn01
            action Show("config_panel")

        textbutton _("Filtro: %s") % data.get_category(p.category):
            action Show("category_switcher")

        null width 160

        fixed:
            fit_first True
            textbutton _("Sobre RhythmBeats"):
                style_prefix "game_credits"
                action Show("credits_window")
            add "ui_icon_logo" zoom 0.1 xpos 0.05 yalign 0.5

        fixed:
            fit_first True
            textbutton _("GitHub"):
                style_prefix "game_credits"
                action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats")
            add "ui_icon_github" xpos 0.1 yalign 0.5

        textbutton "{font=DejavuSans.ttf}{size=25}✖{/size}{/font}":
            style_prefix "offset_setup"
            action Quit(confirm = True)



    viewport at place_atl((-0.7, 0.2), (0.05, 0.2), delta = 1.0):
        yinitial 0.0
        xysize (625, 500)
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True

        has vbox spacing 15




        for song_id, song in enumerate(data.sort(p.category), start = 1):
            button:
                hbox:
                    style_prefix "song_level"
                    ysize 70 spacing 15

                    add Solid(level_color(song["level"])) xysize (7, 64) yalign 0.5

                    vbox:
                        label _("Lvl")
                        text str(song["level"]):
                            outlines [(2, level_color(song["level"]), 0, 0)]

                    vbox:
                        style_prefix "song_btn"
                        yalign 0.5

                        hbox:
                            spacing 7
                            if song["map_length"] >= 500:
                                add "ui_performance_alert"
                            label song["song_title"]

                        text trim_text(song["song_artists"], 55)

                action [SetVariable("p.song_selected", song),
                        Function(play_preview, now=song)]



    frame at place_atl((1.1, 0.2), (0.55, 0.2), delta = 1.0):
        style_prefix "now_showing"

        textbutton _("Ver Info") action Show("song_details", metadata = p.song_selected)

        vbox:
            label p.song_selected["song_title"]


            text trim_text(p.song_selected["song_artists"], 45)


            frame:
                style_prefix "mv_info"
                if "2dmv_info" in p.song_selected:
                    text p.song_selected["2dmv_info"]
                else:
                    background Solid("#F44")
                    text _("MV NO DISPONIBLE.")

            null height 15
            add p.song_selected["cover"] xalign 0.5 zoom 0.55

    hbox:
        style_prefix "main_ui"
        pos (0.67, 0.85)

        textbutton _("Jugar ahora!"):
            if p.song_selected["map_length"] > 450 and renpy.android:
                action Show("performance_warning")

            else:
                action [
                SetVariable("data", p.song_selected),
                Hide("category_switcher"),
                Hide("song_select", transition = dissolve),
                Return(),
                Jump("game_playstage")]

            activate_sound audio.ui_sound_btn03





screen song_details(metadata=None):
    style_prefix "settings"
    modal True
    zorder 104

    add "tex_black"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox

        frame:
            style_prefix "window_title"
            label _("INFORMACIÓN DE LA PISTA")

        hbox:
            spacing 20
            add metadata["cover"] zoom 0.3

            vbox:
                spacing 4
                text _("{color=cf0}Título:{/color} %s") % metadata["song_title"]
                text _("{color=cf0}Artistas/Unidad:{/color} %s") % metadata["song_artists"] text_align 0.0
                text _("{color=cf0}BPM:{/color} %s") % metadata["bpm"]

                if "song_info" in metadata:
                    text _("{color=cf0}Detalles:{/color} %s") % metadata["song_info"] text_align 0.0

        add Solid("#FFF") ysize 3

        frame:
            style_prefix "window_title"
            background Frame(Solid("#900"), 5, 5, 5, 5)
            text _("ADVERTENCIA: LA PARTIDA FINALIZARÁ SI TU HP LLEGA A CERO.") size 17

        text _("{color=cf0}Notas totales (Full Combo):{/color} %s notas") % metadata["map_length"]
        text _("{color=cf0}Duración estimada:{/color} %s segundos") % int(metadata["length"])
        text _("{color=cf0}Nivel de dificultad:{/color} %s") % level_color(metadata["level"], "text")

        if metadata["map_length"] >= 500:
            hbox:
                spacing 5
                add "ui_performance_alert"
                text _("Esta pista puede tener rendimiento deficiente en PC de bajos recursos.") text_align 0.0

    hbox:
        xalign 0.5 ypos 0.85
        style_prefix "main_ui"
        textbutton _("Cerrar ventana") action Hide("song_details"):
            activate_sound audio.ui_sound_btn02





screen credits_window():
    modal True
    style_prefix "credits_window"

    add "tex_black"

    frame at place_atl((0.5, -0.5), (0.5, 0.45), (0.5, 0.5)):
        has vbox xsize 900 spacing 20

        frame:
            style_prefix "window_title"
            label _("SOBRE REN'PY RHYTHMBEATS! GAME")

        viewport:
            yinitial 0.0
            xysize (900, 450)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            has vbox xsize 900 spacing 20

            vbox:
                xalign 0.5
                add "ui_icon_logo" zoom 0.4 xalign 0.5
                label config.name
                text _("[config.version] | Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]")

            vbox xalign 0.5:
                text _("Este juego es una demostración de lo que se puede hacer con el módulo de Acción Rítmica de {color=cf0}Ren'Py RhythmBeats!{/color}.")
                text _("El proyecto completo ha sido creado sin intenciones de recibir ingresos, por lo que todo el contenido se ofrece de forma gratuita.")

            hbox:
                style_prefix "game_credits"
                xalign 0.5 spacing 20

                fixed:
                    fit_first True
                    textbutton _("Ir al repositorio de GitHub"):
                        style_prefix "game_credits"
                        action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats")
                    add "ui_icon_github" xpos 0.08 yalign 0.5

                fixed:
                    fit_first True
                    textbutton _("Wiki: ¿Cómo se juega RhythmBeats?"):
                        style_prefix "game_credits"
                        action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats/blob/main/DETALLES_DEMO.md")
                    add "ui_icon_github" xpos 0.05 yalign 0.5


            if renpy.windows:
                add Solid("#FFF") xysize (870, 2) xalign 0.5

                text _("¿Encontraste un bug crítico? Aquí están los registros del juego:")

                vbox xalign 0.5:
                    text _("Ruta de Instalación: {color=CF0}[config.basedir]{/color}")
                    text _("Registro de Ren'Py: {color=CF0}[config.basedir]/log.txt{/color}")
                    text _("Registro de RhythmBeats: {color=CF0}[config.basedir]/rhythmbeats.log{/color}")

                hbox:
                    style_prefix "main_ui"
                    xalign 0.5 spacing 20

                    textbutton _("Abrir carpeta en el Explorador"):
                        activate_sound audio.ui_sound_btn02
                        action Function(os.startfile, config.basedir)


    hbox:
        xalign 0.5 ypos 0.85
        style_prefix "main_ui"
        textbutton _("Cerrar ventana"):
            activate_sound audio.ui_sound_btn02
            action Hide("credits_window")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
