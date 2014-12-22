# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image level_1 = "assets/backgrounds/mt_silver_exterior.png"
image level_2 = "assets/backgrounds/mt_silver_floor_1.png"
image level_3 = "assets/backgrounds/mt_silver_floor_2.png"

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
define b = Character('Burrito', color="#c8ffc8")


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
    
    s "This is the first floor of Mt. Silver. Helix is at the top."
    
    g "If it's anything like the outside, this'll be easy."
    
    s "Outside was cannon fodder."
    
    g "Is that so? I'll go through them anyway!"
    
    call screen mt_silver_floor_1
    
    if health <= 0:
        jump game_over_man
        
    call post_level_check
    
    b "Lazor Gator!"
    
    g "Burrito? What're you doing, talking to me?"
    
    b "I've been using my powers so you and Snake could communicate."
    
    "(Someone please come up with better dialogue.)"
    
    g "Oh."
    
    b "You must be getting tired by now."
    
    if health == 100:
        g "Actually, I'm fine."
        
        b "Oh. A-anyway, I'm starting Operation Love Bomb."
    else:
        g "A bit, maybe."
        
        b "That's what Operation Love Bomb is for!"
    
    g "Operation Love Bomb?"
    
    b "Yep. KT and I will be warping Health Packs over. Hit them to heal, although it won't do much if you're already at full health."
    
    g "Great! I'm moving up to the next floor, so send them there!"
    
    s "Gator, Burrito, sorry to interrupt your date..."
    
    "(show gator and burrito: WTF)"
    
    s "...But you might want to head to the next floor."
    
    g "Oh. Right."
    
    scene level_3 with fade
    
    g "Let's go!"
    
    call screen mt_silver_floor_2
    
    if health <= 0:
        jump game_over_man
        
    call post_level_check
    
    #call screen mt_silver_summit (boss battle), requires several stages and cut

    return
