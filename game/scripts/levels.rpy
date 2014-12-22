label post_level_check:
    $ totalscore += score
    "Health Remaining: [health] \nScore: [score] \nTotal Score: [totalscore]"
    $ score = 0
    
    if health == 100:
        s "No damage! Nice job Gator!"
        
        g "Pah. That was easy!"
        
        s "It'll only get harder as you go."
    elif health <= 25:
        s "Gator, are you sure you want to continue with the mission?"
        
        g "I...can still fight. For Admiral. For Prince."
        
        s "Alright..."
    elif health <= 50:
        s "You're injured..."
        
        g "I'll be fine. Admiral wouldn't back down. Neither will I."
    elif health <= 75:
        s "You took some damage."
        
        g "Only some. Let's go!"
    elif health > 75:
        s "Nice job!"
        
        g "Heh. Showed them who's boss."

return

label game_over_man:
    show game_over
    s "Sna- er, Gator? Gator?! GAAAATTTORRRR!!!"
    
return

screen mt_silver_exterior:
    add "assets/backgrounds/mt_silver_exterior.png"
    use stats
    
    timer 1.0 action Show("near_slow_level1")
    timer 2.6 action Show("far_slow_level1")
    timer 3.8 action Show("mid_slow_level1")
    timer 5.0 action Show("mid_right_slow_level1")
    timer 8.0 action Show("mid_left_slow_level1")
    timer 9.0 action Show("far_slow_level1")
    timer 10.0 action Show("near_slow_level1")
    timer 10.6 action Show("mid_left_slow_level1")
    timer 11.7 action Show("far_slow_level1")
    timer 12.0 action Show("near_slow_level1")
    timer 13.5 action Show("far_slow_level1")
    timer 13.7 action Show("near_slow_level1")
    timer 14.9 action Show("mid_right_slow_level1")
    timer 16.6 action Show("mid_right_slow_level1")
    timer 16.9 action Show("far_slow_level1")
    timer 17.0 action Show("mid_left_slow_level1")
    timer 17.5 action Show("mid_slow_level1")
    
    timer 21.0 action Return()

screen mt_silver_floor_1:
    add "assets/backgrounds/mt_silver_floor_1.png"
    use stats
    
    timer 3.0 action Return()

screen mt_silver_floor_2:
    add "assets/backgrounds/mt_silver_floor_2.png"
    use stats
    
    timer 3.0 action Return()