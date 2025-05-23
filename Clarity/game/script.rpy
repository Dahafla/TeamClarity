
define e = Character(" ", color="#FFFFFF", voice="audio/vocalize.mp3")


default emotion = 50 # starting emotion variable and value
default timer_active = False #timer boolean
default emotion_decrease = 0
default emotion_reason = "" #initialize emotion_reason

#create the emotion bar
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
            at transform:
                on change:
                    alpha 0.7
                    linear 0.3 alpha 1.0

# show message after emotion goes up or down
screen emotion_transition(message):
    tag emotion_transition
    frame:
        background "#FFFFFF"
        xfill True
        yfill True

    text message:
        color "#000000"
        size 40
        xalign 0.5
        yalign 0.5
        line_spacing 10


# python function
init python:
    #dynamic emotion bar color change
    def emotion_color(value):
        if value > 50:
            return "#00FF00"
        elif value > 25:
            return "#FFFF00"
        else:
            return "#FF0000" 
    
    #for idle decrease
    def decrease_emotion():
        global emotion
        if emotion > 0:
            emotion -= 20
        if emotion <= 0:
            return True
        return False
    
    #function to change emotion
    def change_emotion(amount, reason):
        global emotion, emotion_reason
        emotion += amount
        emotion_reason = reason
        renpy.call_in_new_context("emotion_explanation", reason = reason)

#for transitions
define fade_time = 2.0

#function for screen showing emotion reason
label emotion_explanation(reason):
    show screen emotion_transition(reason) with dissolve
    $ renpy.pause(3.0)  # Screen stays for 2 seconds
    hide screen emotion_transition with fade
    return

# The game starts here.
label start:
    #scene 1
    scene bg 1 #Scene 1
    show screen emotion_bar 

    #alarm sfx
    play music "alarm.mp3" fadein 1.0 
    #breathing
    play sound "breathing.ogg" loop fadein 2.0 volume 0.3
    e "I am awake. I know I am awake but I still lay here pretending to be asleep"

    default snooze_count = 0
    $ timer_active = True
    $ emotion_decrease = 0

    #scene 2
    label scene2:

        #change scene based on snooze count
        if snooze_count == 0:

            scene bg 2 with fade # scene 2
            play sound "bedrustle.mp3"
            e "The alarm clock buzzes. The sound is distant, like it belongs to someone else."

        elif snooze_count == 1:
            scene bg 2a with fade
            play sound "bed rustle.ogg" volume 0.7
            e "The buzzing continues. A little louder this time."

        elif snooze_count == 2:
            scene bg 2b with fade
            play sound "bed rustle2.ogg"
            e "The alarm is relentless. It's impossible to ignore now."

        menu:
                "Snooze the alarm":
                    play sound "ui_click"
                    pause 0.5
                    jump snooze_alarm

                "Turn off the alarm":
                    play sound "ui_click"
                    pause 0.5
                    #$ timer_active = False
                    jump turn_off_alarm
        #idle timer
        while timer_active:
            $ emotion_decrease += 1
            if emotion_decrease % 60 == 0:  # Decrease emotion every 1 second (60 frames)
                if decrease_emotion():  # If emotion = 0 -> jump ending2
                    jump ending2
            return

    #choice 1
    label snooze_alarm:
        $ timer_active = False
        $ snooze_count += 1

        stop music fadeout 0.5
        play sound "snooze.mp3"

        e "Just a few more minutes"
        $ change_emotion( -20, "Avoiding the day feels easier… but it adds to the weight you're already carrying.")

        #change alarm volume each snooze
        $ alarm_volume = 0.5 + (snooze_count * 0.5)
        play music "alarm.mp3" volume alarm_volume fadein 1.0

        $ renpy.pause(2.0)
        if emotion > 0:
            jump scene2
        else:
            jump ending2

    #choice 2
    label turn_off_alarm:
        stop music fadeout 0.1
        stop sound 
        play sound "snooze.mp3"
        e "I turn it off. Silence fills the room, but the weight of the day still lingers."
        $ change_emotion ( 10, "You didn't want to get up. But you did. That matters.")
        jump scene3


    # scene 3
    label scene3:
        scene bg 3 with fade
        play sound "clock ticking.mp3"
        e "My room feels foreign. Messy. Cold. Like it belongs to someone else."
        menu:
            "Stay in bed":
                pause 0.5
                jump stay_in_bed

            "Open the curtains":
                pause 0.5
                jump open_the_curtains
    
    label stay_in_bed:
        play sound "bed creak.mp3"
        e "Maybe if I stay still, the world will move on without me"
        $ change_emotion( -25, "When you shut out the world, it doesn't stop but your world gets smaller.")
        if emotion > 0:
            jump scene3
        else:
            jump ending2

    
    label open_the_curtains:
        stop sound 
        play sound "curtains.mp3"
        $ change_emotion(30, "It's just light. But to someone in the dark, it's a step toward living again")
        jump scene4

    #scene 4
    label scene4:
        scene bg 4 with fade
        play sound "birds.ogg" fadein .5
        e "Sunlight peeks through. It's too real, too harsh but I feel a little warm"
        jump scene5
    
    #scene 5
    label scene5:
        scene bg 5 with fade
        e "My mouth is dry. A glass of water is within reach, but the distance feels impossible."
        menu:
            "Take the water":
                pause 0.5
                jump take_the_water

            "Leave it":
                pause 0.5
                jump leave_it
    
    label take_the_water:
        e "The water is cold. It feels like proof that I exist."
        $change_emotion (10, "Taking a step, however small, reminds you you're still here.")
        jump scene6
    
    label leave_it:
        "Not today. Maybe later. Maybe never."
        $ change_emotion( -15, "You chose to stay still, and the heaviness of that choice lingers.")
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
                pause 0.5
                jump read_paper

            "leave it alone":
                pause 0.5
                jump leave_paper_alone
    
    label read_paper:
        e "Mom's words feel distant, but familiar."
        e "Like echoes of a past where things felt lighter. Maybe I could feel that again. Someday."
        $ change_emotion(50, "You reached for comfort, even if just for a moment.")
        jump scene7
    
    label leave_paper_alone:
        "Not today."
        $ change_emotion(-50, "Turning away is easier, but it pushes you further from what you had.")
        if emotion > 0:
            jump scene6
        else:
            jump ending2
    
    label scene7:
        hide screen emotion_bar
        scene bg 7 with fade
        menu:
            "stand up":
                pause 0.5
                jump stand_up

            "Lie back down":
                pause 0.5
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
        jump thanks
        return

    label ending2:
        hide screen emotion_bar
        scene ending 2 with dissolve
        e "It's okay to not be ready. Tomorrow is another day."
        jump thanks
        return

    label thanks:
        hide screen emotion_bar
        scene thanks with dissolve
        pause
        return
