default seduction = 200 # Your charm and persuasion.
default p_favor = -100 # How you are seen by the masses ( Workers, Peasants, Villagers)
default n_favor = -200 # The people in the higher circle see you ( Royals, Aristocrats )
default intellect = -100 # How smart you are, how smart you seem to others.
default constitution = -100 # How you are seen (Healthy or Sick.) (Some actions might require a higher constitution (body strength)
default magic = 50 # Having High Magic increases Your action bar. Every 100 points of magic = +5 Action points.

default action_points = 150
default max_action = 150
default karma = 0

default day = 0
default prince = 0

define e = Character("Eileen")

default place = "bedroom"
# The game starts here.

screen stats:
        hbox:
            vbox:
                text "energy"
                text "seduction"
                text "p favor"
                text "n favor"
                text "intellect"
                text "constitution"
                text "magic"
            vbox:
                text "[action_points]"
                text "[seduction]"
                text "[p_favor]"
                text "[n_favor]"
                text "[intellect]"
                text "[constitution]"
                text "[magic]"

label start:
    show screen stats
    while day < 60:
        $action_points = max_action
        $day += 1
        "day [day]"
        call bedroom
        while action_points-35>0:
            call expression place
        "end of the day"
        
        $p_favor
        $n_favor
        $prince -= 10
        "qqq"

    return

label bedroom:
    menu:
        "Mirror(minigame)":
            $action_points -= 35
            $start_game()
            call screen minigame
        "relax":
            $action_points -= 35
            "relaxing"
        "talk to the knight":
            $action_points -= 35
            "taklking"
        "go outside":
            $place = map_place
    return

label map_place:
    menu:
        "go to courtyard":
            $place = courtyard
        "go to bedroom":
            $place = bedroom
    return

label courtyard:
    menu:
        "stake stroll":
            $action_points -= 35
            if renpy.random.randint(0,1):
                $seduction += 100
                $n_favor += 50
                "Smell the flowers"
            else:
                $constitution += 100
                $n_favor += 100
                "picnic"
        "talk to the prince":
            $action_points -= 35
            $seduction -= 100
            $n_favor -= 100
            $prince += 20
            "You fell while taking a stroll and made an embarrassing Display of yourself"
        "go outside":
            $place = map
    return
