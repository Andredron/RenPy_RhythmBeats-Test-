









screen song_start(song_data):
    modal True
    style_prefix "song_start"

    timer 4.0 action [Hide("song_start", transition = dissolve), Return()]

    add Fixed(Transform(im.Blur(song_data["cover"], 2.0), zoom = 2.5), Transform(Solid("#000"), alpha = 0.5)) at alpha_com(1.0, 0.3)

    vbox:
        spacing 30
        add song_data["cover"] align (0.5, 0.4) zoom 0.8

        vbox:
            label song_data["song_title"]
            text song_data["song_artists"]

        text _("BPM: %s | Full Combo: %s notas") % (song_data["bpm"], song_data["map_length"]) italic True

style song_start_vbox:
    xsize 1280
    align (0.5, 0.5)

style song_start_label:
    xalign 0.5

style song_start_label_text:
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    size 27
    italic True

style song_start_text:
    color "#FFF"
    outlines [(2, "#000", 1, 1)]
    xalign 0.5
    size 17





screen playground(mv_data):
    zorder 102
    modal True


    if mv_data:
        timer mv_data[1] action Show("playground_2dmv", source = mv_data[0], transition = dissolve)
    else:
        timer 0.01 action Show("playground_2dmv", source = Transform(im.Blur(data["cover"], 2.0), zoom = 2.5))


    add "ui_coregame_note_lane"


    add rhythm.run_core
    add rhythm.run_waterfall






screen playground_hud(song_length):
    zorder 103
    style_prefix "stats"

    timer song_length + 1.0 action Jump("show_cleared")

    python:
        hp = 15 - rhythm.miss
        accuracy = rhythm.accuracy_rate()[0]
        reaction = rhythm.accuracy_rate()[1]
        accuracy_pct = rhythm.accuracy_rate()[2]


    if rhythm.miss < 15:

        vbox:
            text "{font=DejaVuSans.ttf}❤{/font} [hp]/15" color hp_color(hp, "text")
            bar:
                value AnimatedValue(old_value = 0.0, value = hp, range = 15, delay = 0.1)
                left_bar hp_color(hp, "bar")


        vbox:
            xpos 0.7
            text u"%s {font=DejaVuSans.ttf}♪{/font} %.01f%%" % (reaction, accuracy_pct):
                color accuracy_color(accuracy, "text")
            bar:
                value AnimatedValue(old_value = 0.0, value = accuracy_pct, range = 100, delay = 0.1)
                left_bar accuracy_color(accuracy, "bar")



        vbox:
            style_prefix "song_combo"
            label _("COMBO")
            text str(rhythm.combo)


        bar:
            style "song_progress"
            value AudioPositionValue(channel = 'music' , update_interval = 0.1)

    else:


        python:
            ui.close()
            renpy.jump("show_failed")



    if persistent.operating_stats:
        frame:
            style_prefix "debugger"
            ypos 0.3

            has vbox
            label _("Métricas de operación.")
            text _("- Beatmap: %s") % rhythm.fn
            text _("- Offset: %s s") % rhythm.offset
            text _("- Epoch: %.01f s") % rhythm.epoch
            text _("- Último tap: %.01f ms") % rhythm.last_tap
            text _("- Progreso del mapa: %s/%s") % rhythm.map_progress
            text _("- Acertados: %s") % rhythm.perfect
            text _("- Fallidos: %s") % rhythm.miss



    if rhythm.is_running():
        hbox:
            xalign 0.5 ypos 0.85
            style_prefix "sort_music"
            textbutton _("Abortar Show") action [
            SetVariable("stage_aborted", True),
            Jump("show_failed")]



init python:
    config.per_frame_screens.append("playground_hud")


style stats_bar:
    left_bar Solid("#9F9")
    right_bar Solid("#777")
    xysize (300, 7)

style stats_text:
    color "#090"
    outlines [(2, "#FFF", 0, 0)]
    size 22

style stats_vbox:
    pos (0.05, 0.05)

style song_progress:
    xysize (800, 24)
    xalign 0.5 ypos 0.02

    left_bar Frame("coregame/ui/bar/ui_bar_progress_fill.png", 50, 12, 50, 12)
    right_bar Frame("coregame/ui/bar/ui_bar_progress_base.png", 50, 12, 50, 12)
    thumb "coregame/ui/bar/ui_bar_progress_thumb.png"
    thumb_offset 12


style song_combo_vbox:
    xsize 200
    spacing 0
    pos (0.75, 0.38)

style song_combo_label:
    xalign 0.5

style song_combo_label_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 22

style song_combo_text:
    color "#FFF"
    outlines [(3, "#000", 0, 0)]
    size 70
    xalign 0.5


style debugger_frame:
    background Frame(Transform(Solid("#242424"), alpha = 0.7), 24, 24, 24, 24)
    padding (30, 30, 30, 30)
    xminimum 200

style debugger_vbox:
    spacing 10

style debugger_label_text:
    color "#CF0"
    size 20

style debugger_text:
    color "#FFF"
    size 18






screen playground_2dmv(source):
    zorder 101
    add source
    add Solid("#000") alpha persistent.custom_alpha





screen playground_finish(miss_notes, max_allowed):
    zorder 104
    modal True

    if miss_notes == 0:
        timer 1.8 action Play("sfx_01", audio.sfx_stage_full_combo)
        add "ui_tex_black"
        add "fx_tex_confetti"

        text _("Full Combo!") at show_clear_text(2.3) size 70

        add "ui_tex_white" at full_combo_line_effect(xymap = [(-0.3, 1.3), 0.42], delta = 2.0)
        add "ui_tex_white" at full_combo_line_effect(xymap = [(-0.3, 1.3), 0.58], delta = 2.15)

    elif miss_notes < max_allowed:
        timer 1.0 action Play("sfx_01", audio.sfx_stage_cleared)
        add "ui_tex_black"
        text _("Show Clear!") at show_clear_text(1.0) size 70

    else:
        timer 0.001 action Play("sfx_01", audio.sfx_stage_failed)
        add "ui_coregame_bg_failed"
        text _("Show Failed!") at show_clear_text(0.0) size 70





screen show_results(song_selected, party):
    zorder 104
    style_prefix "show_results"

    on "show" action Play("sfx_01", audio.sfx_results_intro)

    default delta_header = 1.8
    default delta_cover = 1.5
    default delta_stats = 2.3

    default accuracy_pct = 100.0 - abs(rhythm.accuracy_rate()[0])


    add Fixed(Transform(im.Blur(song_selected["cover"], 2.0), zoom = 2.5), Transform(Solid("#000"), alpha = 0.5)) at alpha_com(1.0, 2.0)


    text _("RESULTADOS") size 60 at crossline_text(xran = (-0.3, 1.3), y = 0.45, offset = 0.2, delta = 0.6)
    text _("FINALES") size 60 at crossline_text(xran = (1.3, -0.3), y = 0.55, offset = 0.2, delta = 0.6)


    vbox at place_atl((1.1, 0.07), (0.07, 0.07), delta = delta_header):
        label song_selected["song_title"]
        text song_selected["song_artists"]
        null height 15
        text _("BPM: %s | Full Combo: %s notas") % (song_selected["bpm"], song_selected["map_length"])

    add song_selected["cover"] at place_atl((-0.3, 0.3), (0.07, 0.3), delta = delta_cover) zoom 0.65


    frame at place_atl((1.1, 0.26), (0.4, 0.26), delta = delta_stats):
        has vbox spacing 20

        frame:
            style_prefix "msg_success"
            text _("RESULTADOS DE LA PARTIDA") style "update_label_text" xalign 0.5

        hbox:
            style_prefix "combo_results"
            vbox:
                xsize 250
                text _("COMBO FINAL") xalign 0.5
                label str(party.combo) xalign 0.5

            vbox:
                text _(u"\u2022 Perfecto       : [party.perfect]") italic True
                text _(u"\u2022 BRUH            : [party.miss]") italic True

        vbox:
            style_prefix "perfbar"
            text _("PRECISIÓN MEDIA: %.02f%%") % (accuracy_pct) xalign 0.5

            bar:
                value AnimatedValue(old_value = 0.0, value = 100 - abs(rhythm.accuracy_rate()[0]), range = 100, delay = 4.0)

            null height 20

            text _(u"\u2022 Tiempo de reacción promedio: %s ms.") % (abs(rhythm.accuracy_rate()[0]))
            text _(u"\u2022 Tendencia de reacción: %s") % rhythm.accuracy_rate()[1]


    hbox at place_atl((0.5, 1.1), (0.5, 0.85), (0.5, 0.0), delta = delta_stats):
        style_prefix "sort_music"
        textbutton _("Regresar a la lista") action Jump("song_selection_menu")


style show_results_frame:
    background Frame(Solid("#242424"), 24, 24, 24, 24)
    padding (30, 30, 30, 30)
    xminimum 600

style show_results_hbox:
    spacing 40

style show_results_label_text:
    size 38
    color "#CF0"
    outlines [(2, "#000", 1, 1)]
style show_results_text is song_btn_text:
    outlines [(2, "#000", 1, 1)]



style perfbar_bar:
    left_bar Solid("#CF0")
    right_bar Solid("#777")
    xysize (550, 7)
    yalign 0.5

style perfbar_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 19

style perfbar_hbox:
    spacing 20



style combo_results_label_text:
    color "#FFF"
    outlines [(3, "#000", 0, 0)]
    size 85

style combo_results_text:
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    size 19

style combo_results_hbox:
    spacing 40

style combo_results_vbox:
    yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
