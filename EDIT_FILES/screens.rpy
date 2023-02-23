














init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    hover_underline True
    color "#CF0"

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize 5
    base_bar Frame(Solid("#777"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(Solid("#9F9"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







init -501 screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Atrás") action Rollback()
            textbutton _("Historial") action ShowMenu('history')
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Guardar") action ShowMenu('save')
            textbutton _("Guardar R.") action QuickSave()
            textbutton _("Cargar R.") action QuickLoad()
            textbutton _("Prefs.") action ShowMenu('preferences')




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")











init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Comenzar") action Start()

        else:

            textbutton _("Historial") action ShowMenu("history")

            textbutton _("Guardar") action ShowMenu("save")

        textbutton _("Cargar") action ShowMenu("load")

        textbutton _("Opciones") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Finaliza repetición") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menú principal") action MainMenu()

        textbutton _("Acerca de") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):


            textbutton _("Ayuda") action ShowMenu("help")

        if renpy.variant("pc"):



            textbutton _("Salir") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








init -501 screen main_menu():
    tag menu



    add gui.main_menu_background


    frame:
        style "main_menu_frame"



    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    properties gui.text_properties("title")

init -1 style main_menu_version:
    properties gui.text_properties("version")











init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Volver"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 280
    yfill True

init -1 style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

init -1 style game_menu_viewport:
    xsize 920

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 10

init -1 style game_menu_label:
    xpos 50
    ysize 120

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30










init -501 screen about():
    tag menu





    use game_menu(_("Acerca de"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versión [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save():
    tag menu


    use file_slots(_("Guardar"))


init -501 screen load():
    tag menu


    use file_slots(_("Cargar"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Grabación automática"), quick=_("Grabación rápida"))

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d de %B %Y, %H:%M"), empty=_("vacío")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}R") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 50
    ypadding 3

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")









init -501 screen preferences():
    tag menu


    use game_menu(_("Opciones"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Pantalla")
                        textbutton _("Ventana") action Preference("display", "window")
                        textbutton _("Pant. completa") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Lado de retroceso")
                    textbutton _("Desactivar") action Preference("rollback side", "disable")
                    textbutton _("Izquierda") action Preference("rollback side", "left")
                    textbutton _("Derecha") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Saltar")
                    textbutton _("Texto no visto") action Preference("skip", "toggle")
                    textbutton _("Tras opciones") action Preference("after choices", "toggle")
                    textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))






            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Veloc. texto")

                    bar value Preference("text speed")

                    label _("Veloc. auto-avance")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volumen música")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volumen sonido")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Prueba") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volumen voz")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Prueba") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Silencia todo"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 225

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 350

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 450









init -501 screen history():




    predict False tag menu

    use game_menu(_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:



                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("El historial está vacío.")




define -1 gui.history_allow_tags = { "alt", "noalt" }


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Ratón") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Mando") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label "Enter"
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanza el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas de flecha")
        text _("Navega la interfaz.")

    hbox:
        label _("Escape")
        text _("Accede al menú del juego.")

    hbox:
        label "Ctrl"
        text _("Salta el diálogo mientras se presiona.")

    hbox:
        label _("Tabulador")
        text _("Activa/desactiva el salto de diálogo.")

    hbox:
        label _("Av. pág.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Re. pág.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label "H"
        text _("Oculta la interfaz.")

    hbox:
        label "S"
        text _("Captura la pantalla.")

    hbox:
        label "V"
        text _("Activa/desactiva la asistencia por {a=https://www.renpy.org/l/voicing}voz-automática{/a}.")

    hbox:
        label "Shift+A"
        text _("Abre el menú de accesibilidad.")


init -501 screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Clic medio")
        text _("Oculta la interfaz.")

    hbox:
        label _("Clic derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Rueda del ratón arriba\nClic en lado de retroceso")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Rueda del ratón abajo")
        text _("Avanza hacia el diálogo siguiente.")


init -501 screen gamepad_help():

    hbox:
        label _("Gatillo derecho\nA/Botón inferior")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Gatillo izquierdo\nBotón sup. frontal izq.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Botón sup. frontal der.")
        text _("Avanza hacia el diálogo siguiente.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navega la interfaz.")

    hbox:
        label _("Comenzar, Guía")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y/Botón superior")
        text _("Oculta la interfaz.")

    textbutton _("Calibrar") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 250
    right_padding 20

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    use notify_window(_("VENTANA DE CONFIRMACIÓN"), notify_sound=audio.ui_sound_notify):
        vbox:
            spacing 30
            text _(message)

        hbox:
            xalign 0.5
            ypos 0.8
            spacing 15

            textbutton _("Sí") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action

init -1 style confirm_frame is update_frame

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_label is update_label
init -1 style confirm_label_text is update_label_text
init -1 style confirm_text is update_text
init -1 style confirm_button is main_ui_button:
    activate_sound audio.ui_sound_btn01
init -1 style confirm_button_text is main_ui_button_text
init -1 style confirm_vbox is update_vbox









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Saltando")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 900
    style_prefix "notify"

    frame at notify_appear:
        text "[message]"

    timer 5.0 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)




        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")




init -501 screen main_advice():
    style_prefix "startscreen"
    timer 3.0 action [Hide("main_advice", transition = dissolve), Return()]

    vbox:
        xsize 900
        add "ui_icon_headphones" at headphone_blink
        text _("Usa auriculares para una mejor experiencia (cascos recomendados).")


init -501 screen startscreen():
    style_prefix "startscreen"

    timer 3.0 action [Hide("startscreen", transition = dissolve), Return()]

    vbox:
        add "ui_icon_logo" zoom 0.8 xalign 0.5
        label config.name
        text config.version

    text "© CharlieFuu69 - Creative Commons CC-BY-SA v4.0" ypos 0.9

init -1 style startscreen_vbox:
    align (0.5, 0.5)
    spacing 15

init -1 style startscreen_label:
    xalign 0.5

init -1 style startscreen_label_text:
    color "#CF0"
    outlines [(2, "#000", 1, 1)]
    size 44

init -1 style startscreen_text:
    xalign 0.5
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 18





init -501 screen notify_window(title="", level=0, notify_sound=None):
    modal True
    zorder 110
    style_prefix "confirm"

    timer 0.01 action Play("notify_01", notify_sound)

    add "tex_black"

    frame at msgwindow_anim:
        frame:
            style_prefix ("msg_success" if level == 0 else "msg_failed")
            label title

        transclude





init -501 screen need_main_update(now_version=""):
    modal True
    zorder 200
    style_prefix "confirm"

    use notify_window(_("ACTUALIZACIÓN GLOBAL NECESARIA"), notify_sound=audio.ui_sound_notify):
        vbox:
            spacing 30
            text _("La versión que tienes ({color=cf0}[config.version]{/color}) está descontinuada. Debes actualizar a la versión {color=cf0}[now_version]{/color} para continuar jugando.")
            text _("Entra al repositorio de GitHub desde el botón acá abajo, y sigue las instrucciones para actualizar los paquetes necesarios.")

        hbox:
            xalign 0.5
            ypos 0.8
            spacing 20

            textbutton _("Ir a GitHub") action OpenURL("https://github.com/CharlieFuu69/RenPy_RhythmBeats")
            textbutton _("Cerrar el juego") action Quit(confirm = False)


init -501 screen download_complete():
    modal True
    zorder 200
    style_prefix "confirm"

    use notify_window(_("DESCARGA FINALIZADA"), notify_sound=audio.ui_sound_notify):
        vbox:
            text _("Los recursos de {color=cf0}Ren'Py RhythmBeats{/color} han sido descargados completamente.")

            if renpy.android:
                text _("El juego debe cerrarse y volver a iniciar para aplicar los cambios. Presiona {color=cf0}\"Cerrar Juego\"{/color} para continuar.")
            else:
                text _("Presiona \"Continuar\" para aplicar los cambios de los archivos descargados.")

        hbox:
            style_prefix "main_ui"
            xalign 0.5 ypos 0.8 spacing 20

            textbutton "%s" % (_("Cerrar el juego") if renpy.android else "Continuar"):
                action [Hide("download_complete"),
                Return()]
                activate_sound audio.ui_sound_btn03





init -501 screen update(inst):
    style_prefix "update"
    timer 0.5 action Function(inst.start)

    if inst.request_end:
        if inst.get_exception():
            use notify_window(title=_("ERROR DE CONEXIÓN"), level=1, notify_sound=audio.ui_sound_error):
                vbox:
                    text str(inst.exception_content).replace("[", "[[")

                hbox:
                    xalign 0.5 ypos 0.78 spacing 20
                    textbutton _("Reintentar") action [Hide("update"), Return(), Jump("check_updates")]
                    textbutton _("Cerrar Juego") action [Hide("update"), Quit(confirm=False)]

        else:
            if len(update.update_queue) != 0:
                use notify_window(title=_("DESCARGA DE RECURSOS"), notify_sound=audio.ui_sound_notify):
                    vbox:
                        text _("Tamaño de la descarga: %.02f MB") % inst.update_size underline True
                        text _("Esta descarga contiene las pistas musicales y 2DMVs incluidos en la demostración de {color=CF0}Ren'Py RhythmBeats!{/color}.")
                        text _("La velocidad de descarga puede variar en función del tráfico del servidor, o de la estabilidad de tu conexión.")

                    hbox:
                        xalign 0.5 ypos 0.8
                        textbutton _("Iniciar descarga") action [Hide("update"), Jump("download_sequence")]

            else:
                timer 0.01 action [Hide("update"), Return()]

    else:
        vbox:
            ypos 0.9
            text _("Buscando actualizaciones...")
            bar:
                value StaticValue(inst.progress[0], inst.progress[1])





init -501 screen download(url, progress, path):
    style_prefix "update"
    modal True

    default dl = DownloadHandler(url = url, savepath = path)
    on "show" action Function(dl.start)

    if dl.status():
        if dl.runtime_exception():
            use notify_window(title=_("ERROR DURANTE LA DESCARGA"), level=1, notify_sound=audio.ui_sound_error):
                vbox:
                    text str(dl.exception_output).replace("[", "[[")

                hbox:
                    xalign 0.5 ypos 0.78 spacing 20
                    textbutton _("Reintentar") action [Hide("download"), Return(), Jump("download_sequence")]
                    textbutton _("Cerrar Juego") action [Hide("download"), Quit(confirm=False)]

        else:
            timer 0.01 action [Hide("download"), Return()]

    else:
        vbox:
            ypos 0.85 spacing 5
            text _("Descargando recursos...")
            text _("%.02f MB / %.02f MB  %.02f%%  (%s/%s)") % (dl.dl_current, dl.dl_total, dl.gauge * 100.0, progress[0], progress[1])
            bar:
                value StaticValue(dl.gauge, 1.0)
            null height 7
            bar:
                value StaticValue(progress[0], progress[1])


init -1 python:
    config.per_frame_screens.append("download")



init -1 style button_skin:
    background Frame("gui/button/btn_[prefix_]skin.png", 24, 24, 24, 24)
    padding (20, 10, 20, 10)
    minimum (50, 50)

init -1 style frame_skin:
    background Frame("gui/overlay/ui_frame_skin.png", 12, 12, 12, 12)

init -1 style main_ui_button is button_skin:
    minimum (200, 50)

init -1 style main_ui_button_text:
    idle_color "#999"
    hover_color "#FFF"
    selected_color "#CF0"
    size 18
    text_align 0.5
    xalign 0.5



init -1 style update_frame is frame_skin:
    xysize (600, 400)
    align (0.5, 0.5)

init -1 style update_label:
    xalign 0.5

init -1 style update_label_text:
    color "#000"
    size 20

init -1 style update_text:
    xalign 0.5
    text_align 0.5
    xmaximum 550
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 18

init -1 style update_vbox:
    xalign 0.5 ypos 0.3
    spacing 10

init -1 style update_bar:
    xalign 0.5
    xysize (1100, 4)
    left_bar Solid("#CF0")
    right_bar Solid("777")

init -1 style update_button is main_ui_button:
    activate_sound audio.ui_sound_btn01
init -1 style update_button_text is main_ui_button_text



init -1 style msg_success_frame:
    background Frame(Solid("#CF0"), 5, 5, 5, 5)
    padding (10, 5, 10, 5)
    xalign 0.5 ypos 0.1
    minimum (500, 20)

init -1 style msg_success_label is update_label
init -1 style msg_success_label_text is update_label_text

init -1 style msg_failed_frame:
    background Frame(Solid("#FF233B"), 5, 5, 5, 5)
    xalign 0.5 ypos 0.1
    padding (10, 5, 10, 5)
    minimum (500, 20)

init -1 style msg_failed_label is update_label
init -1 style msg_failed_label_text is update_label_text





init -1 style msg_success:
    background Frame(Solid("#CF0"), 5, 5, 5, 5)
    padding (10, 5, 10, 5)
    xalign 0.5 ypos 0.1
    minimum (500, 20)

init -1 style msg_failed:
    background Frame(Solid("#FF233B"), 5, 5, 5, 5)
    xalign 0.5 ypos 0.1
    padding (10, 5, 10, 5)
    minimum (500, 20)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
