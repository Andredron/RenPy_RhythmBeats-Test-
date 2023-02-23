








transform mv_fade:
    on start:
        alpha 0.0
        ease 0.5 alpha 1.0
    on hide:

        alpha 1.0
        ease 0.5 alpha 0.0


transform full_combo_line_effect(xymap=[(0.0, 0.0), 0.0], delta=0.0):

    subpixel True
    anchor (0.5, 0.5)
    xysize (700, 3)
    block:

        pos (xymap[0][0], xymap[1])
        pause delta + 0.001
        ease 1.0 pos (xymap[0][1], xymap[1])


transform show_clear_text(delta=0.0):
    subpixel True
    align (0.5, 0.5)


    parallel:
        zoom 0.0
        pause delta + 0.001
        easeout_quint 0.4 zoom 1.0
        linear 6.0 zoom 1.3
    parallel:


        alpha 0.0
        pause delta + 0.001
        ease 0.4 alpha 1.0


transform crossline_text(xran=(0.0, 0.0), y, offset=0.0, delta=0.0):
    subpixel True
    anchor (0.5, 0.5)
    block:

        pos (xran[0], y)
        pause offset
        easein_quint 0.2 pos (0.5, y)
        pause delta + 0.001
        easeout_quint 0.3 pos (xran[1], y)

transform place_atl(xybef=(0.0, 0.0), xyaft=(0.0, 0.0), ref=(0.0, 0.0), delta=0.0):
    subpixel True
    anchor (ref[0], ref[1])

    on start:
        pos (xybef[0], xybef[1])
        pause delta + 0.001
        easein_quint 0.3 pos (xyaft[0], xyaft[1])
    on hide:

        pos (xyaft[0], xyaft[1])
        easeout_quint 0.3 pos (xybef[0], xybef[1])


transform alpha_com(op, delta=0.0):
    anchor (0.5, 0.5)
    pos (0.5, 0.5)

    on start:
        alpha 0.0
        ease delta + 0.001 alpha op
    on hide:

        alpha op
        ease 0.35 alpha 0.0


transform switcher_animation:
    subpixel True

    on start:
        yzoom 0.0
        ease 0.1 yzoom 1.0
    on show:
        yzoom 0.0
        ease 0.1 yzoom 1.0
    on hide:
        xzoom 1.0 yzoom 1.0
        ease 0.1 yzoom 0.0
transform cover_change_animation:
    alpha 0.0
    on start:
        ease 0.5 alpha 1.0
    on hide:
        ease 0.5 alpha 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
