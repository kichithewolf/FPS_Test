#####################################################
# Speeds: Slow (1.5 sec), Med (1 secs), Fast (.75 sec)
#
# Positions:
# far-center, mid-center, near-center, far-left,
# far-mid-right, mid-near-right, very-near-right,
# far-mid-left, very-near-left
#
# Naming: position_speed_level
#####################################################

screen far_slow_level1:
    # Score: 20
    # Health: -10
    vbox xalign 0.5 yalign 0.25:
          imagebutton:
            idle "assets/enemies/level1/far center pid.png"
            hover "assets/enemies/level1/far center pid hit.png"
            action [Hide("far_slow_level1"), SetVariable("score", score+20)]
    timer 1.5 action [Hide("far_slow_level1"), SetVariable("health", health-10), If(health <= 0, true=Return())]

screen mid_slow_level1:
    # Score: 15
    # Health: -15
    vbox xalign 0.6 yalign 0.5:
          imagebutton:
            idle "assets/enemies/level1/mid center nido.png"
            hover "assets/enemies/level1/mid center nido hit.png"
            action [Hide("mid_slow_level1"), SetVariable("score", score+15)]
    timer 1.5 action [Hide("mid_slow_level1"), SetVariable("health", health-15), If(health <= 0, true=Return())]
    
screen near_slow_level1:
    # Score: 10
    # Health: -20
    vbox xalign 0.5 yalign 1.0:
          imagebutton:
            idle "assets/enemies/level1/near center rat.png"
            hover "assets/enemies/level1/near center rat hit.png"
            action [Hide("near_slow_level1"), SetVariable("score", score+10)]
    timer 1.5 action [Hide("near_slow_level1"), SetVariable("health", health-20), If(health <= 0, true=Return())]

screen mid_right_slow_level1:
    # Score: 15
    # Health: -25
    vbox xalign 0.8 yalign 0.7:
          imagebutton:
            idle "assets/enemies/level1/mid right char.png"
            hover "assets/enemies/level1/mid right char hit.png"
            action [Hide("mid_right_slow_level1"), SetVariable("score", score+15)]
    timer 1.5 action [Hide("mid_right_slow_level1"), SetVariable("health", health-15), If(health <= 0, true=Return())]

screen mid_left_slow_level1:
    # Score: 15
    # Health: -25
    vbox xalign 0.1 yalign 0.4:
          imagebutton:
            idle "assets/enemies/level1/mid left ven.png"
            hover "assets/enemies/level1/mid left ven hit.png"
            action [Hide("mid_left_slow_level1"), SetVariable("score", score+15)]
    timer 1.5 action [Hide("mid_left_slow_level1"), SetVariable("health", health-15), If(health <= 0, true=Return())]
