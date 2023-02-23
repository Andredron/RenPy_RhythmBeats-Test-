









label quit:
    if rpc:
        $ rpc.stop()

    return

label song_selection_menu:
    $ music_inst = MusicData(fn = "coregame/music_data.json")
    $ music_inst.load()
    $ stage_aborted = False
    $ data = None
    $ p = persistent

    if not p.song_selected:
        $ p.song_selected = music_inst.sort(p.category)[0]

    if p.discord_rpc:
        if not rpc:
            $ rpc = DiscordRichPresence()
            $ rpc.set_status(state = _("En \"Menú de Pistas\"."),
                            details = _("Seleccionando pista musical..."))
            $ rpc.rpc_start()
        elif True:

            $ rpc.set_status(state = _("En \"Menú de Pistas\"."),
                            details = _("Seleccionando pista musical..."))

    call screen song_select(music_inst) with dissolve

    $ renpy.pause(hard = True)





    label game_playstage:

        scene tex_black_solid

        if rpc:
            $ rpc.set_status(state = _("Artistas: %s") % data["song_artists"],
                            details = _("Jugando: \"%s\"") % data["song_title"],
                            image_text = _("Partida en curso..."))


        $ renpy.free_memory()


        python:
            rhythm = RhythmPlayground(
                        fn = data["beatmap"],
                        displayable = Transform("ui_coregame_note_tap", zoom = 0.55),
                        offset_map = data["map_offset"],
                        offset_game = p.custom_offset,
                        failsafe = p.failsafe)

            rhythm.load()
            rhythm.miss_sound = audio.sfx_note_miss

        stop music fadeout 1.0
        call screen song_start(data) with dissolve
        hide bg_main
        $ renpy.pause(0.5, hard = True)

        play music data["audio"] noloop
        show screen playground_hud(data["length"])
        show screen playground(mv_data = data["mv"]) with dissolve

        $ renpy.pause(hard = True)






    label show_cleared:
        show screen playground_finish(miss_notes = rhythm.miss, max_allowed = 15)
        $ renpy.pause(6.0 if rhythm.miss == 0 else 4.0, hard = True)
        stop music fadeout 1.0
        jump show_results_sequence



    label show_failed:
        stop music
        $ finish_playstage(["playground_hud", "playground"])
        show screen playground_finish(miss_notes = 15, max_allowed = 15)
        $ renpy.pause(3.0, hard = True)


        if not stage_aborted:
            jump show_results_sequence

        hide screen playground
        hide screen playground_finish with dissolve

        $ del rhythm
        $ renpy.free_memory()

        jump song_selection_menu



    label show_results_sequence:
        $ finish_playstage(["playground", "playground_hud"], dissolving = True)
        hide screen playground_finish with dissolve

        $ renpy.pause(1.0, hard = True)

        play music bgm_0047
        call screen show_results(data, rhythm)

        $ del rhythm
        $ renpy.free_memory()

        jump song_selection_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
