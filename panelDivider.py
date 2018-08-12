import time

class Board:
    """
    Board class
    This class is useful to define your boards and scantlings. You can give each board a name to ease recognition. By default, the number of boards is 1 and its name is a counter starting at 1.
    """
    counter = 1
    def __init__(self, width=0, length=0, thickness=0, number=1, name=""):
        if (name):
            self.name = name
        else:
            self.name = str(Board.counter)
            Board.counter += 1

        self.width = width
        self.length = length
        self.thickness = thickness
        self.number = number

class Rect:
    """
    Rect class
    Define a rectangle and provide the helper function needed by the sorting algorithm
    """
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.a = w*h

    def fit_in(self, rect):
        if ((self.w <= rect.w) and (self.h <= rect.h)):
            return 1
        elif ((self.w <= rect.h) and (self.h <= rect.w)):
            return -1
        else:
            return 0

    def removeRect(self, rect):
        out = []
        out.append(Rect(self.x, self.y + rect.h, rect.w, self.h - rect.h))
        out.append(Rect(self.x + rect.w, self.y + rect.h, self.w - rect.w, self.h - self.h))
        out.append(Rect(self.x + rect.w, self.y, self.w - rect.w, rect.h))
        ret = []
        for t in out:
            print("aire is " + str(t.a))
            if (t.a != 0):
                ret.append(t)
        return ret



class Divider:
    """
    Divider class
    Will try to place all boards given in the panels given. The algorithm will try to place the boards first on smaller panels and then going to bigger panels if needed. A cut margin is considered.
    """
    def __init__(self, boards = [], panels = [], margin = 0.5):
        self.boards = boards
        self.panels = panels
        self.margin = margin


    def print(self):
        for board in self.boards:
            print("Board \"" + board.name + "\" x" + str(board.number) + ": w = " + str(board.width) + ", l = " + str(board.length) + ", t = " + str(board.thickness))
        for board in self.panels:
            print("Panel \"" + board.name + "\" x" + str(board.number) + ": w = " + str(board.width) + ", l = " + str(board.length) + ", t = " + str(board.thickness))

    def divide(self):
        start = time.time()
        #list of panels
        listPanel = []
        for board in self.panels:
            for i in range(board.number):
                listPanel.append([Rect(0, 0, board.width, board.length), board.name, i])

        #list boards
        toSort = []
        for board in self.boards:
            for i in range(board.number):
                toSort.append([Rect(w=board.width + self.margin, h=board.length + self.margin), board.name, i])

        toSort.sort(key=lambda x: x[0].a, reverse=True)
        listPanel.sort(key=lambda x: x[0].a, reverse=False)

        output = []

        for elem in toSort:
            for spot in listPanel[:]:
                isFit = elem[0].fit_in(spot[0])
                pos = []
                if (isFit is 1):
                    pos = Rect(spot[0].x, spot[0].y, elem[0].w, elem[0].h)
                if (isFit is -1):
                    pos = Rect(spot[0].x, spot[0].y, elem[0].h, elem[0].w)
                if (isFit):
                    output.append([pos, elem[1], elem[2], spot[1], spot[2]])
                    toAdd = spot[0].removeRect(pos)
                    listPanel.remove(spot)
                    for ta in toAdd:
                        listPanel.append([ta, spot[1], spot[2]])
                    break
            listPanel.sort(key=lambda x: x[0].a, reverse=False)

            #TODO: Add storing unsorted element in seperate list


        if (len(output) != len(toSort)):
            print("Failed to sort all elements")

        print("exec time is " + str(time.time() - start))
        return output
