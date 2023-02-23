









label splashscreen:
    if not persistent.lang_one: ### una pregunta única sobre la elección de lenguas
        menu: 
            "Español": 
                $ renpy.change_language(None)

            "English": 
                $ renpy.change_language("english") 

            "{font=DejavuSans.ttf}Русский{/font}": ###la fuente nativa del proyecto no soporta cirílico, por lo que hay que hacer una muletilla en la primera ejecución
                $ renpy.change_language("russian")

        $ persistent.lang_one = True ### una variable a partir de la cual la pregunta no aburrirá al usuario

    play music audio.bgm_0001 fadeout 1.0 fadein 1.0
    call screen main_advice with dissolve
    show bg_main
    call screen startscreen with dissolve

    jump check_updates

    label check_updates:
        $ update = UpdateManager()
        $ update.index_url = "https://raw.githubusercontent.com/CharlieFuu69/RenPy_RhythmBeats/main/src/index.json"

        show tex_black with dissolve
        call screen update(inst = update)

        return

label download_sequence:
    $ update.start_batch_download()

    call screen download_complete
    $ renpy.utter_restart()





label main_menu:
    $ del update
    return





label start:
    $ quick_menu = False
    scene bg_main
    show tex_black

    if renpy.has_label("song_selection_menu"):
        stop music fadeout 1.0
        $ renpy.pause(1.0, hard = True)
        jump song_selection_menu
    elif True:
        $ logging.critical(_("Error de flujo (song_selection_menu): Label inexistente. Cerrando el juego."))
        $ renpy.quit(relaunch = False, save = False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
