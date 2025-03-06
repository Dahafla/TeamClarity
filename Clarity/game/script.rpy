# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(" ")


default emotion = 50

screen emotion_bar():
    frame:
        align (0.1, 0.1)
        xsize 300
        ysize 50
        background "#000000"
        padding (5, 5)
        bar:
            value emotion
            range 100
            xsize 290
            ysize 40
            left_bar "#FFFFFF"  
            right_bar "#CCCCCC"  
            thumb None



# The game starts here.

label start:

    show screen emotion_bar

    scene bg 1 with fade #Scene 1

    e "I am awake, I know I am awake but I still lay here pretending to be asleep"

    label scene2:
        scene bg 2 # scene 2

        e "The alarm clock continues it's buzzing, heavy as the day ahead"
        menu:
            "Snooze the alarm":
                jump snooze_alarm

            "Turn off the alarm":
                jump turn_off_alarm


    label snooze_alarm:
        e "Just a few more minutes"
        $ emotion -= 20
        if emotion > 0:
            jump scene2
        else:
            jump ending2

    label turn_off_alarm:
        e "I turn it off, but the weight of the day still lingers."
        $ emotion += 10
        jump scene3


    # scene 3
    label scene3:
        scene bg 3
        e "I look around the room, it feels like a stranger. Messy.Cold"
        menu:
            "Stay in bed":
                jump stay_in_bed

            "Open the curtains":
                jump open_the_curtains
    
    label stay_in_bed:
        e "I will just stay here, for a while"
        $ emotion -= 25
        if emotion > 0:
            jump scene3
        else:
            jump ending2

    
    label open_the_curtains:
        $ emotion += 30
        jump scene4

    #scene 4
    label scene4:
        scene bg 4
        e "Sunlight peeks through, it's harsh but I feel a little warm"
        jump scene5
    
    #scene 5
    label scene5:
        scene bg 5
        e "My mouse is dry. A glass of water sits within reach-but the steps feel steeper than they should.
        Is it worth the effort?"

        menu:
            "Take the water":
                jump take_the_water

            "Leave it":
                jump leave_it
    
    label take_the_water:
        "I force myself to take the glass. 
        The cold water is soothing.
        It's a small gesture but it helps"
        $ emotion += 10
        jump scene6
    
    label leave_it:
        "It's too much, I will just stay here"
        $ emotion -= 15
        if emotion > 0:
            jump scene6
        else:
            jump ending2

    label scene6:
        scene bg 6
        e "I see a crumbled piece of paper- not behind the door, not locked away.
        But to reach it, I have to open the door. I know it's her handwriting"

        menu:
            "Read the piece of paper":
                jump read_paper

            "leave it alone":
                jump leave_paper_alone
    
    label read_paper:
        e "Mom's words feel distant, but they remind me of better days.
        Maybe I can feel that again someday"
        $ emotion += 50
        jump scene7
    
    label leave_paper_alone:
        "I can't do it, not today"
        $ emotion -= 50
        if emotion > 0:
            jump scene6
        else:
            jump ending2
    
    label scene7:
        hide screen emotion_bar
        scene bg 7
        menu:
            "stand up":
                jump stand_up

            "Lie back down":
                jump lie_down
    
    label stand_up:
        scene bg 8
        e "The floor is cold but I am standing, that's a start"
        jump ending1
    
    label lie_down:
        scene bg 9
        e "It's too much today, maybe tomorrow."
        jump ending2
    
    label ending1:
        hide screen emotion_bar
        scene ending 1 with dissolve
        e "Every small step matters. I have made it this far and I can keep going."
        return

    label ending2:
        hide screen emotion_bar
        scene ending 2 with dissolve
        e "It's okay to not be ready. Tomorrow is another day."
        return

    
