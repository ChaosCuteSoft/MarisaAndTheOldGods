define dissolve = Dissolve(0.25)

define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.5),
    Solid("#000"), Dissolve(1.0),
    True])

define fade_white = Fade(0.4, 0.0, 0.5, color="#fff")

define pixellate = Pixellate(2,5)

define pushright = PushMove(1.0, "pushright")
define pushleft = PushMove(1.0, "pushleft")
define pushup = PushMove(1.0, "pushup")
define pushdown = PushMove(1.0, "pushdown")
define moveinoutdissolve = ComposeTransition(dissolve, before=moveoutleft, after=moveinright)
