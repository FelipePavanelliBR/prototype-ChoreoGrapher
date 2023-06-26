from libraries.cs1lib import *
from Dancer import Dancer
from Formation import Formation

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAMERATE = 50

MODES = ["create", "delete", "move", "recolor", "transition"]
mode = MODES[0]

currDancers = []
currId = 1

formation = 1
currFormations = {formation: Formation(formation)}

mousePressed = False


def addDancer(x, y):
    global currId
    currDancers.append(Dancer(x, y, currId))
    currId += 1


def mousePress(x, y):
    global mousePressed, formation
    mousePressed = True

    if clickOnFormationButton(x, y):
        next = len(currFormations) + 1
        currFormations[next] = Formation(next)
        formation = next

        #updating Dancers internal positions list
        for d in currDancers:
            d.newFormation(d.x, d.y)



    if mode == "create" and not clickOnFormationButton(x,y):
        addDancer(x, y)

    if mode == "delete":
        for d in currDancers:
            if d.contains(x, y):
                currDancers.remove(d)

    # if mode == "transition":
    #     currDancers[0].positions.append(Point(x, y))

    if mode == "recolor":
        for d in currDancers:
            if d.contains(x, y):
                d.toggleSelect()


def handleKeyPress(key):
    global mode, formation
    match key:
        case "d":
            mode = MODES[1]
        case "c":
            mode = MODES[0]
        case "m":
            mode = MODES[2]
        case "r":
            mode = MODES[3]
        case "t":
            mode = MODES[4]
        case "l":
            key = formation + 1
            if key in currFormations:
                formation += 1

        case "k":
            key = formation - 1
            if key in currFormations:
                formation -= 1

        case "q":
            quit()


def handleMouseRelease(x, y):
    global mousePressed
    mousePressed = False


def handleMouseDrag(x, y):
    if mode == "move" and mousePressed:
        for d in currDancers:
            if d.contains(x, y):
                d.move(x, y)

def clickOnFormationButton(x,y):

    if x > WINDOW_WIDTH - 210 and x < WINDOW_WIDTH - 90 and y > 15 and y < 35:
        print("New formation")
        return True
    else:
        return False


def addFormationButton():
    set_fill_color(0, 0, 1)
    draw_rectangle(WINDOW_WIDTH - 210, 15, 120, 20)
    draw_text("ADD FORMATION", WINDOW_WIDTH - 200, 30)

def displayScreen():
    set_stroke_color(1, 1, 1)

    #Writing out Mode, Formation,
    draw_text(mode, (int)(WINDOW_WIDTH / 2), 30)
    draw_text(currFormations[formation].name + " / " + (str) (len(currFormations)), (int)(WINDOW_WIDTH / 3), 30)
    draw_text("<-- K  L -->", (int)(WINDOW_WIDTH / 3) + 20, 45)

    #button to create more formations (only visuals)
    addFormationButton()




def main():
    #backgroud
    set_clear_color(0, 0, 0)
    clear()
    displayScreen()

    for d in currDancers:
        d.draw()
        d.displayName()

    if len(currDancers) > 0:
        for d in currDancers:
            d.state = formation - 1
            d.transitionTo(d.positions[d.state])


start_graphics(main, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=mousePress,
               key_press=handleKeyPress, mouse_release=handleMouseRelease, mouse_move=handleMouseDrag)
