# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image level_1 = "assets/backgrounds/mt_silver_exterior.png"
image game_over = "assets/effects/game_over.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define g = Character('Lazor Gator', color="#c8ffc8")
define s = Character('Snake', color="#c8ffc8")


# The game starts here.
label start:
    
    e "Testing out a renpy fps game."
    
    show level_1
    
    s "Mission control calling in: Gator, I'm detecting his minions at Mt. Silver! Take them out!"
    
    g "Time to take down the Helix!"
    
    # Level 1
    $ health = 100
    call screen mt_silver_exterior
    
    if health <= 0:
        jump game_over_man
    
    $ totalscore += score
    "Health Remaining: [health] \nScore: [score] \nTotal Score: [totalscore]"
    $ score = 0
    
    if health == 100:
        s "No damage! Nice job Gator!"
    elif health <= 25:
        s "Gator, are you sure you want to continue with the mission?"
    elif health <= 50:
        s "You're injured..."
    elif health <= 75:
        s "You took some damage."
    elif health > 75:
        s "Nice job!"
        
    g "Outside done! Time to head in!"
    
    #call screen mt_silver_floor_1
    
    #call screen mt_silver_floor_2
    
    #call screen mt_silver_summit (boss battle)

    return

label game_over_man:
    show game_over
    s "Sna- er, Gator? Gator?! GAAAATTTORRRR!!!"
    
    return

screen far_enemy:
    vbox xalign 0.5 yalign 0.25:
          imagebutton:
            idle "assets/enemies/generic_enemy_far.png"
            hover "assets/enemies/generic_enemy_far_hit.png"
            action [Hide("far_enemy"), SetVariable("score", score+20)]
    timer 1.0 action [Hide("far_enemy"), SetVariable("health", health-10)]

screen mid_enemy:
    vbox xalign 0.6 yalign 0.5:
          imagebutton:
            idle "assets/enemies/generic_enemy_mid.png"
            hover "assets/enemies/generic_enemy_mid_hit.png"
            action [Hide("mid_enemy"), SetVariable("score", score+15)]
    timer 1.0 action [Hide("mid_enemy"), SetVariable("health", health-15)]
    
screen near_enemy:
    vbox xalign 0.5 yalign 0.75:
          imagebutton:
            idle "assets/enemies/generic_enemy_near.png"
            hover "assets/enemies/generic_enemy_near_hit.png"
            action [Hide("near_enemy"), SetVariable("score", score+10)]
    timer 1.0 action [Hide("near_enemy"), SetVariable("health", health-20)]
    
screen mt_silver_exterior:
    add "assets/backgrounds/mt_silver_exterior.png"
    use stats
    
    timer 1.0 action [Show("far_enemy"), If(health <= 0, true=Return())]
    timer 1.5 action [Show("near_enemy"), If(health <= 0, true=Return())]
    timer 3.5 action [Show("far_enemy"), If(health <= 0, true=Return())]
    timer 5.0 action [Show("far_enemy"), If(health <= 0, true=Return())]
    timer 6.5 action [Show("near_enemy"), If(health <= 0, true=Return())]
    timer 8.5 action [Show("near_enemy"), If(health <= 0, true=Return())]
    timer 9.0 action [Show("mid_enemy"), If(health <= 0, true=Return())]
    timer 10.5 action [Show("far_enemy"), If(health <= 0, true=Return())]
    timer 12.5 action Return()
