import random
import os

class Board:

    def __init__(self, player, size = 6):
        self._size = size
        self._walls = []
        self._player = player

################################ Getter/Setter Size
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size):
        self._size = new_size
################################ Getter/Setter Walls
    @property
    def walls(self):
        return self._walls

    @walls.setter
    def walls(self, new_walls):
        self._walls = new_walls

################################ Getter/Setter Player
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        self._player = new_player
    
################################# Methods

    #Show the board
    def draw(self):

        i = 0
        ii = 0
        is_wall = False
        is_player = False
        while i < self._size:
            while ii < self._size:

                for wall in self._walls:
                    if i == wall[0] and ii == wall[1]:
                        if ii == (self._size - 1) :
                            print("X")
                        else:
                            print("X", end="")
                        is_wall = True

                if self._player.position[0] == i and self._player.position[1] == ii and not is_wall:
                    if ii == (self._size - 1):
                        print("O")
                    else:
                        print("O", end="")
                    is_player = True

                if ii == (self._size - 1) and is_wall:
                    ii = 0
                    is_wall = False
                    break

                if ii == (self._size - 1) and is_player:
                    ii = 0
                    is_player = False
                    break

                if ii == (self._size - 1) and not is_wall and not is_player:
                    print(".")
                    ii = 0
                    break

                elif not is_wall and not is_player:
                    print(".", end="")

                ii += 1
                is_wall = False
                is_player = False

            i += 1

    def pop_wall(self):
        new_wall = (random.randrange(-1,self._size),random.randrange(-1,self._size))
        if new_wall not in self._walls:
            self._walls.append(new_wall)

    def check_win(self):
        return self._player.position == (self._size -1, self._size -1)
    
    def check_death(self):
        for wall in self._walls:
            if self._player.position == wall:
                return True

    def play_game(self):
        while not self.check_death() and not self.check_win():
            self.draw()
            self._player.move()
            self.pop_wall()

        if self.check_win():
            print("YOU WON")
            input()

        if self.check_death():
            print("YOU LOOSE")
            input()




















class Player:

    
    def __init__(self, name, board = None):
        self._name = name
        self._position = (0,0)
        self.keyboard_key = {"z":(-1,0), "q":(0,-1), "d":(0,1), "s":(1,0)}
        self.board = board


################################ Getter/Setter name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
    
################################ Getter/Setter position
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position
    
################################# Methods

    def move(self):
        selection = input()
        while selection != "q" and selection != "z" and selection != "s" and selection != "d":
            selection = input()
        for letter in self.keyboard_key:
            if letter == selection:
                if self.board._size > (self._position[0] + self.keyboard_key[letter][0]) and 0 <= (self._position[0] + self.keyboard_key[letter][0]) and self.board._size > (self._position[1] + self.keyboard_key[letter][1]) and 0 <= (self._position[1] + self.keyboard_key[letter][1]):
                    self._position = (self._position[0] + self.keyboard_key[letter][0], self._position[1] + self.keyboard_key[letter][1])
        os.system("cls")