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

define moka = Character("Moka")
define ogouwu = Character("oguwu")


# The game starts here.

label start:

    call ch0 from _call_ch0
    call ch1 from _call_ch1
    call ch2 from _call_ch2
    call ch3 from _call_ch3
    call ch4 from _call_ch4
    call ch5 from _call_ch5
    call ch6 from _call_ch6
    call ch7 from _call_ch7
    call ch8 from _call_ch8
    call ch9 from _call_ch9
    call ch10 from _call_ch10

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
