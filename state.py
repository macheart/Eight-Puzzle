
from board import *

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###

    def __init__(self, board, predecessor, move):
        """Constructs a new State object"""
        self.board = board
        self.predecessor = predecessor
        self.move = move
        self.num_moves = 0

        if predecessor != None:
            self.num_moves = predecessor.num_moves + 1
             
    def print_moves_to(self):
        """Prints the sequence of moves
           from the initial state to the called State object"""
        if self.predecessor == None:
            print('initial state:')
            print(self.board)

        else:
            self.predecessor.print_moves_to()
            move_info = str(self.move) + ':'
            print('move the blank', move_info)
            print(self.board)
            

    def is_goal(self):
        """Returns True if State object is a goal state
           False otherwise"""

        for r in range(3):
            for c in range(3):
                if self.board.tiles[r][c] != GOAL_TILES[r][c]:
                    return False
        return True

    def generate_successors(self):
        """Creates and returns a list of State objects
           for all successor states of the called State object"""
        successors = [] 

        direction = MOVES[0]
        copy_board1 = Board.copy(self.board)
        decision = Board.move_blank(copy_board1, direction)
        if decision == True:
            state1 = State(copy_board1, self, MOVES[0])
            successors += [state1]

        direction = MOVES[1]
        copy_board2 = Board.copy(self.board)
        decision = Board.move_blank(copy_board2, direction)
        if decision == True:
            state2 = State(copy_board2, self, MOVES[1])
            successors += [state2]

        direction = MOVES[2]
        copy_board3 = Board.copy(self.board)
        decision = Board.move_blank(copy_board3, direction)
        if decision == True:
            state3 = State(copy_board3, self, MOVES[2])
            successors += [state3]

        direction = MOVES[3]
        copy_board4 = Board.copy(self.board)
        decision = Board.move_blank(copy_board4, direction)
        if decision == True:
            state4 = State(copy_board4, self, MOVES[3])
            successors += [state4]

        return successors
        

        
    def __repr__(self):
        """ Returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ Returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ Implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
