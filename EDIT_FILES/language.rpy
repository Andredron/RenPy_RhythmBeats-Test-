init -3 python: 
    if persistent.lang is None: 
        persistent.lang = "spanish"
    lang = persistent.lang

init python: 
    config.main_menu.insert(3, (u'Language', "language_chooser", "True"))
    
#init python:
    #if lang == "russian":#russian font here
        #style.default.font = "DejavuSans.ttf"
    #elif lang == "english": 
        #style.default.font = "font=DejavuSans.ttf" #english font here 