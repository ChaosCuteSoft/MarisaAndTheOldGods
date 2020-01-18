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

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marisa")
define ogouwu = Character("oguwu")


# The game starts here.

label start:
    call ch99 from _call_ch99

    
    menu:
        "Yes":
            jump Yes

        "No":
            jump No

        "Maybe":
            jump Maybe

    scene blackbg
    with dottrans2
    show moka scary
    moka "UwU"

    label Yes:

    moka "yes working"

    return

    label No:

    moka "Nooooooo"

    return

    label Maybe:

    moka "Maybeeeeee"



    return
