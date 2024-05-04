#####################
# Escaping the Maze #
#####################

# IMPORTANT:
# You will need to run this code for the robot's maze at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json.
# Otherwise, this program will be useless.

# Function to turn robot right.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Function to move robot in the correct direction.
def move_forward():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_left()
            move()

# As long as robot is not yet at the goal, robot will keep moving.
while not at_goal():
    move_forward()

# The end of Reeborg's maze!