# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character(" ", color="#FFFFFF")


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
            left_bar Color(emotion_color(emotion))
            right_bar "#CCCCCC"  
            thumb None

init python:
    def emotion_color(value):
        if value > 50:
            return "#00FF00"
        elif value > 25:
            return "#FFFF00"
        else:
            return "#FF0000" 


define fade_time = 2.0
# The game starts here.

label start:


    scene bg 1 with fade #Scene 1
    show screen emotion_bar with fade

    e "I am awake. I know I am awake but I still lay here pretending to be asleep"

    default snooze_count = 0

    label scene2:

        if snooze_count == 0:

            scene bg 2 with fade # scene 2
            e "The alarm clock buzzes. The sound is distant, like it belongs to someone else."

        elif snooze_count == 1:
            scene bg 2a with fade
            e "The buzzing continues. A little louder this time."

        elif snooze_count == 2:
            scene bg 2b with fade
            e "The alarm is relentless. It's impossible to ignore now."

        menu:
                "Snooze the alarm":
                    jump snooze_alarm

                "Turn off the alarm":
                    jump turn_off_alarm

    label snooze_alarm:
        $ snooze_count += 1
        e "Just a few more minutes"
        $ emotion -= 20

        if emotion > 0:
            jump scene2
        else:
            jump ending2

    label turn_off_alarm:
        e "I turn it off. Silence fills the room, but the weight of the day still lingers."
        $ emotion += 10
        jump scene3


    # scene 3
    label scene3:
        scene bg 3 with fade
        e "My room feels foreign. Messy. Cold. Like it belongs to someone else."
        menu:
            "Stay in bed":
                jump stay_in_bed

            "Open the curtains":
                jump open_the_curtains
    
    label stay_in_bed:
        e "Maybe if I stay still, the world will move on without me"
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
        scene bg 4 with fade
        e "Sunlight peeks through. It's too real, too harsh but I feel a little warm"
        jump scene5
    
    #scene 5
    label scene5:
        scene bg 5 with fade
        e "My mouth is dry. A glass of water is within reach, but the distance feels impossible."
        menu:
            "Take the water":
                jump take_the_water

            "Leave it":
                jump leave_it
    
    label take_the_water:
        e "The water is cold. It feels like proof that I exist."
        $ emotion += 10
        jump scene6
    
    label leave_it:
        "Not today. Maybe later. Maybe never."
        $ emotion -= 15
        if emotion > 0:
            jump scene6
        else:
            jump ending2

    label scene6:
        scene bg 6 with fade
        e "A crumpled piece of paper sits by the door. Her handwriting."
        e "To reach it, I would have to open the door. Step out. Face the world."

        menu:
            "Read the piece of paper":
                jump read_paper

            "leave it alone":
                jump leave_paper_alone
    
    label read_paper:
        e "Mom's words feel distant, but familiar."
        e "Like echoes of a past where things felt lighter. Maybe I could feel that again. Someday."
        $ emotion += 50
        jump scene7
    
    label leave_paper_alone:
        "Not today."
        $ emotion -= 50
        if emotion > 0:
            jump scene6
        else:
            jump ending2
    
    label scene7:
        hide screen emotion_bar
        scene bg 7 with fade
        menu:
            "stand up":
                jump stand_up

            "Lie back down":
                jump lie_down
    
    label stand_up:
        scene bg 8 with fade
        e "The floor is cold. But I am standing, that's a start"
        jump ending1
    
    label lie_down:
        scene bg 9 with fade
        e "It's too much today, maybe tomorrow."
        jump ending2
    
    label ending1:
        hide screen emotion_bar
        scene ending 1 with dissolve
        e "Every small step matters. I have made it this far. I can keep going."
        return

    label ending2:
        hide screen emotion_bar
        scene ending 2 with dissolve
        e "It's okay to not be ready. Tomorrow is another day."
        return

