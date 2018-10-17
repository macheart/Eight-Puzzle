
class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ A constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your cod  e for the rest of __init__ below.
        # Do *NOT* remove our code above.

        for r in range(3):
            for c in range(3):
                if digitstr[3*r + c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                    self.tiles[r][c] = int(digitstr[3*r + c])
                else:
                    self.tiles[r][c] = int(digitstr[3*r + c])


    ### Add your other method definitions below. ###

    def __repr__(self):
        """Returns a string representation of a Board"""
        
        s = ''

        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == 0:
                    s += '_' + ' '
                else: 
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'

        return s

    def move_blank(self, direction):
        """Takes a string direction (that the blank should move)
           and attempts to modify the contents of the Board
           returns True or False to indicate whether the move
           if possible"""

        if direction != 'up' and direction != 'down' and direction != 'left' and direction != 'right':
            print('unknown direction:', direction)
            return False 

        if direction == 'up':
            new_r = self.blank_r - 1
            new_c = self.blank_c

        if direction == 'down':
            new_r = self.blank_r + 1
            new_c = self.blank_c

        if direction == 'left':
            new_r = self.blank_r
            new_c = self.blank_c - 1

        if direction == 'right':
            new_r = self.blank_r
            new_c = self.blank_c + 1

        if new_r > 2 or new_r < 0 or new_c > 2 or new_c < 0:
            return False

        else:

            original_tile = self.tiles[new_r][new_c]
            self.tiles[new_r][new_c] = 0
            self.tiles[self.blank_r][self.blank_c] = original_tile

            self.blank_r = new_r
            self.blank_c = new_c

            return True

    def digit_string(self):
        """Returns a string of digits that corresponds to the current contents of Board"""
        current_digitstr = ''

        for r in range(3):
            for c in range(3):
                current_digitstr += str(self.tiles[r][c])

        return current_digitstr

    def copy(self):
        """Returns a Board object that is a deep copy of the called object"""
        copy_string = self.digit_string()
        copy_board = Board(copy_string)
        return copy_board

    def num_misplaced(self):
        """Counts and returns the number of tiles not in goal state"""
        goal = 0
        num = 0 

        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == 0:
                    goal += 1 
                else:
                    if self.tiles[r][c] == goal:
                        goal += 1
                    else:
                        goal += 1
                        num += 1            
        return num

    def where_misplaced(self):
        """Returns a list of location of misplaced tiles"""
        goal = 0
        misplaced_locations = []
        goal_list = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1],
                     [1, 2], [2, 0], [2, 1], [2, 2]]
        misplaced_sum = 0 

        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == goal:
                    goal += 1
                else:
                    location = [r, c]
                    misplaced_locations += [location]
                    goal += 1
                    
        #found misplaced_locations in a list

        for x in misplaced_locations:
            current = self.tiles[x[0]][x[1]]
            goal_index = current 
            
            y = goal_list[goal_index]

            misplaced_sum += abs(x[0] - y[0])
            misplaced_sum += abs(x[1] - y[1])

        return misplaced_sum 

            
    def __eq__(self, other):
        """Overloads the == operator
           Return True if the called object and the argument have same values
           for the tiles
           False otherwise"""

        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != other.tiles[r][c]:
                    return False

        return True

        
           
