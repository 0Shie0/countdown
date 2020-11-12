default all = []
default open = []

default t_seduction = 0
default t_p_favor = 0
default t_n_favor = 0
default t_intellect = 0
default t_constitution = 0
default t_magic = 0

default t_stats  = [t_seduction,t_p_favor,t_n_favor,t_intellect,t_constitution,t_magic]
default energy = 10

init python:
    def start_game():
        for i in range(10):
            store.all.append([])
            store.open.append([])
            for j in range(10):
                q = renpy.random.randint(1,6)
                store.all[i].append(q)
                store.open[i].append(1)
        q = renpy.random.randint(0,9)
        w = renpy.random.randint(0,9)
        store.open[q][w] = 0

    def change_open(q,w):
        if store.all[q][w] == 1:
            store.t_seduction += 10
        if store.all[q][w] == 2:
            store.t_p_favor += 10
        if store.all[q][w] == 3:
            store.t_n_favor += 10
        if store.all[q][w] == 4:
            store.t_intellect += 10
        if store.all[q][w] == 5:
            store.t_constitution += 10
        if store.all[q][w] == 6:
            store.t_magic += 10
        store.all[q][w] = ""
        a = len(open)-1
        b = len(open[q])-1
        if q > 0:
            store.open[q-1][w] = 0
            if w > 0:
                store.open[q-1][w-1] = 0
            if w < b:
                store.open[q-1][w+1] = 0
        if q < a:
            store.open[q+1][w] = 0
            if w > 0:
                store.open[q+1][w-1] = 0
            if w < b:
                store.open[q+1][w+1] = 0
        if w > 0:
            store.open[q][w-1] = 0
        if w < b:
            store.open[q][w+1] = 0
label finish_minigame:
    $all = []
    $open = []
    $seduction += t_seduction
    $p_favor += t_p_favor
    $n_favor += t_n_favor
    $intellect += t_intellect
    $constitution += t_constitution
    $magic += t_magic
    $t_seduction = 0
    $t_p_favor = 0
    $t_n_favor = 0
    $t_intellect = 0
    $t_constitution = 0
    $t_magic = 0
    $energy=10
    return


screen minigame:
    hbox:
        if energy:
            grid 10 10:
                spacing 20
                for i in range(10):
                    for j in range(10):
                        if open[i][j]:
                            textbutton "":
                                xsize 100
                                ysize 40
                                xalign 0.5
                        else:
                            textbutton "{}".format(all[i][j]):
                                action Function(change_open,i,j),SetVariable("energy", energy - 1)
                                xsize 100
                                ysize 20
                                xalign 0.5
        else:
            textbutton "no energy left":
                action Call("finish_minigame")
                xsize 700
                xalign 0.5
                yalign 0.5
        hbox:
            vbox:
                text "energy"
                text "seduction"
                text "p favir"
                text "n favor"
                text "intellect"
                text "constitution"
                text "magic"
            vbox:
                text "[energy]"
                text "[seduction] (+[t_seduction])"
                text "[p_favor] (+[t_p_favor])"
                text "[n_favor] (+[t_n_favor])"
                text "[intellect] (+[t_intellect])"
                text "[constitution] (+[t_constitution])"
                text "[magic] (+[t_magic])"
