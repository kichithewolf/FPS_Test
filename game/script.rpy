# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image level_1 = "assets/backgrounds/mt_silver_exterior.png"
image level_2 = "assets/backgrounds/mt_silver_floor_1.png"

image game_over:
    "assets/effects/game_over.png" with Dissolve(0.2)
    0.2
    "assets/effects/game_over_2.png" with Dissolve(0.2)
    0.2
    "assets/effects/game_over_3.png" with Dissolve(0.2)
    0.2
    "assets/effects/game_over_4.png" with Dissolve(0.2)

# Declare characters used by this game.
define g = Character('Lazor Gator', color="#c8ffc8")
define s = Character('Snake', color="#c8ffc8")


# The game starts here.
label start:
    
    "Testing out a renpy fps game."
    
    scene level_1 with dissolve
    
    g "Helix...you'll pay for what you've done."
    
    s "Mission control calling in: Gator, I'm detecting his minions at Mt. Silver! Take them out!"
    
    g "Time to take down the Helix!"
    
    # Level 1
    $ health = 100
    call screen mt_silver_exterior
    
    if health <= 0:
        jump game_over_man
        
    call post_level_check
    
    g "Outside done! Time to head in!"
    
    scene level_2 with fade
    
    #call screen mt_silver_floor_1
    #introduce buttito, our healer
    #call screen mt_silver_floor_2
    
    #call screen mt_silver_summit (boss battle), requires several stages and cut

    return
