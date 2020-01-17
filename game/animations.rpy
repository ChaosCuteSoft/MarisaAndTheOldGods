init offset = -1


#default variables
define defaultZ = 0.8
define defaultX = 640
define excitedHigh = -55
define excitedTime = 0.2

transform topRightImage:
    xpos 0.9 xanchor 0.9, ypos 0.1, yanchor 0.1
transform topLeftImage:
    xpos 0.1 xanchor 0.1, ypos 0.1, yanchor 0.1
transform centerLeftImage:
    xpos 0.1 xanchor 0.1, ypos 0.4, yanchor 0.4
transform centerRightImage:
    xpos 0.8 xanchor 0.8, ypos 0.4, yanchor 0.4
transform bottomRightImage:
    xpos 0.9 xanchor 0.9, ypos 0.6, yanchor 0.6



transform tcommon(x=defaultX, z=defaultZ):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=defaultX, z=defaultZ):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform focus(x=defaultX, z=defaultZ):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

transform sink(x=defaultX, z=defaultZ):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform jumping(x=defaultX, z=defaultZ):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0


transform excited(x=defaultX, z=defaultZ, high=excitedHigh, jumptime=excitedTime):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein jumptime yoffset high
    easeout jumptime yoffset 0
    easein jumptime yoffset high
    easeout jumptime yoffset 0

transform uwu(x=defaultX, z=defaultZ):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easeout .25 xoffset 0
    easein .25 xoffset 15
    easeout .25 xoffset -15
    easein .25 xoffset 15
    easeout .25 xoffset 0

transform jumpfocus(x=defaultX, z=defaultZ):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -400
    easeout .1 yoffset 0

transform dip(x=defaultX, z=defaultZ):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform panic(x=defaultX, z=defaultZ):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

transform leftin(x=defaultX, z=defaultZ):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


transform thide(z=defaultZ):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300
transform e200:
    excited(200)
transform e493:
    excited(493)
transform e786:
    excited(786)
transform e1080:
    excited(1080)
transform e1180:
    excited(1080)
transform e240:
    excited(240)
transform e640:
    excited(640)
transform e1040:
    excited(1040)
transform e400:
    excited(400)
transform e880:
    excited(880)
transform e640:
    excited(640)

transform t200:
    tcommon(200)
transform t493:
    tcommon(493)
transform t786:
    tcommon(786)
transform t1080:
    tcommon(1080)
transform t1180:
    tcommon(1180)
transform t240:
    tcommon(240)
transform t640:
    tcommon(640)
transform t1040:
    tcommon(1040)
transform t400:
    tcommon(400)
transform t880:
    tcommon(880)
transform t640:
    tcommon(640)

transform i200:
    tinstant(200)
transform i493:
    tinstant(493)
transform i786:
    tinstant(786)
transform i1080:
    tinstant(1080)
transform i1180:
    tinstant(1180)
transform i240:
    tinstant(240)
transform i640:
    tinstant(640)
transform i1040:
    tinstant(1040)
transform i400:
    tinstant(400)
transform i880:
    tinstant(880)
transform i640:
    tinstant(640)

transform f200:
    focus(200)
transform f493:
    focus(493)
transform f786:
    focus(786)
transform f1080:
    focus(1080)
transform f1180:
    focus(1080)
transform f240:
    focus(240)
transform f640:
    focus(640)
transform f33:
    focus(1040)
transform f400:
    focus(400)
transform f880:
    focus(880)
transform f640:
    focus(640)

define zfactor = 1.0
#zoom and focus
transform zf200:
    focus(200, zfactor)
transform zf493:
    focus(493, zfactor)
transform zf786:
    focus(786, zfactor)
transform zf1080:
    focus(1080, zfactor)
transform zf1180:
    focus(1180, zfactor)
transform zf240:
    focus(240, zfactor)
transform zf640:
    focus(640, zfactor)
transform zf33:
    focus(1040, zfactor)
transform zf400:
    focus(400, zfactor)
transform zf880:
    focus(88, zfactor0)
transform zf640:
    focus(640, zfactor)

transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s1180:
    sink(1180)
transform s240:
    sink(240)
transform s640:
    sink(640)
transform s33:
    sink(1040)
transform s400:
    sink(400)
transform s880:
    sink(880)
transform s640:
    sink(640)

transform h41:
    jumping(200)
transform h42:
    jumping(493)
transform h43:
    jumping(786)
transform h44:
    jumping(1080)
transform h1180:
    jumping(1180)
transform h240:
    jumping(240)
transform h640:
    jumping(640)
transform h33:
    jumping(1040)
transform h400:
    jumping(400)
transform h880:
    jumping(880)
transform h640:
    jumping(640)

transform hf41:
    jumpfocus(200)
transform hf42:
    jumpfocus(493)
transform hf43:
    jumpfocus(786)
transform hf44:
    jumpfocus(1080)
transform hf1180:
    jumpfocus(1180)
transform hf240:
    jumpfocus(240)
transform hf640:
    jumpfocus(640)
transform hf33:
    jumpfocus(1040)
transform hf400:
    jumpfocus(400)
transform hf880:
    jumpfocus(880)
transform hf640:
    jumpfocus(640)

transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d1180:
    dip(1180)
transform d240:
    dip(240)
transform d640:
    dip(640)
transform d33:
    dip(1040)
transform d400:
    dip(400)
transform d880:
    dip(880)
transform d640:
    dip(640)

transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l980:
    leftin(980)
transform l1080:
    leftin(1080)
transform l1180:
    leftin(1180)
transform l240:
    leftin(240)
transform l640:
    leftin(640)
transform l1040:
    leftin(1040)
transform l400:
    leftin(400)
transform l880:
    leftin(880)
transform l640:
    leftin(640)

transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0
