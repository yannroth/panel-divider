import panelDivider as pd

boards = []
boards.append(pd.Board(1,2,3,4,"side"))
boards.append(pd.Board(5,6,7,2,"top"))

panels = []
panels.append(pd.Board(70,70,3,1,"panel"))
panels.append(pd.Board(5,5,3,1,"dechet"))

div = pd.Divider(boards, panels, 0.5)

output = div.divide()

for o in output:
    print("Board \"" + o[1] + "\" #" + str(o[2]) + " on panel \"" + o[3] + "\" #" + str(o[4]) + " at (" + str(o[0].x) + ", " + str(o[0].y) + ", " + str(o[0].w) +", " + str(o[0].h) +")")
