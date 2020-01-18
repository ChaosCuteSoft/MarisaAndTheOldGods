# The script of the game goes in this file.

#Launch splash screen
label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(1)

    return


# The script of the game goes in this file.


# The game starts here.

label start:
    call ch99 from _call_ch99


    return
