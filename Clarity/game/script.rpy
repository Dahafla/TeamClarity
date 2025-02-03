# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Main Character")


# The game starts here.

label start:

    scene bg 1 #Scene 1

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
        jump scene2

    label turn_off_alarm:
        e "I turn it off, but the weight of the day still lingers."
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
        jump scene3
    
    label open_the_curtains:
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
        jump scene6
    
    label leave_it:
        "It's too much, I will just stay here"
        jump scene6

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
        jump scene7
    
    label leave_paper_alone:
        "I can't do it, not today"
        jump scene6
    
    label scene7:
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
        scene ending 1
        e "Every small step matters. I have made it this far and I can keep going."
        return

    label ending2:
        scene ending 2
        e "It's okay to not be ready. Tomorrow is another day."
        return

    
