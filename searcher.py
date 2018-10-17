
import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        """Constructs a new Searcher object"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def add_state(self, new_state):
        """Adds a single State object and
           adds it to the Searcher's list of untested states"""
        self.states += [new_state]

    def should_add(self, state):
        """Takes a State object,
           returns True if the called Searcher should add state
           to its list of untested states
           and False otherwise"""
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif State.creates_cycle(state) == True:
            return False
        else:
            return True

    def add_states(self, new_states):
        """Takes a list of State objects called new_states,
           Procsses the elements of new_states one at a time"""
        for state in new_states:
            if self.should_add(state) == True:
                self.add_state(state)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        """Full state-space search begins at specified initial state,
           Ends when the goal state is found
           Or when Searcher runs out of untested states"""
        self.add_state(init_state)

        while self.states != []:
            s = self.next_state()
            if State.is_goal(s) == True:
                self.num_tested += 1 
                return s
            else:
                self.num_tested += 1
                successors = State.generate_successors(s)
                self.add_states(successors)

        return None 
            
           
            
    def __repr__(self):
        """ Returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """Performs breadth first search (BFS) instead of random search"""
    
    def next_state(self):
        """Follow first-in-first-out (FIFO) ordering in choosing which state to test"""
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """Performs depth first search (DFS) instead of random search"""

    def next_state(self):
        """Follow last-in-first-out (LIFO) ordering in choosing which state to test"""
        s = self.states[-1]
        self.states.remove(s)
        return s


   
def h0(state):
    """ A heuristic function that always returns 0 """
    return 0

def h1(state):
    """A heuristic function that computes
       and returns an estimate of how many additional moves
       are needed to get from state to goal state"""
    moves_needed = state.board.num_misplaced()
    return moves_needed

### Add your other heuristic functions here. ###

def h2(state):
    """A heuristic function that computes
       and returns an estimate of the number of moves needed
       to get from state to goal state"""
    moves_needed = state.board.where_misplaced()
    return moves_needed 

    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __init__(self, heuristic):
        """Constructs a new GreedySearcher object"""
        super().__init__(-1)
        self.heuristic = heuristic

    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def add_state(self, state):
        """Add a sublist [priority, state] pair
           priority of state is determined by calling priority method"""
        to_add = [self.priority(state)] + [state]
        self.states += [to_add]

    def next_state(self):
        """Choose one sub-list of the highest priority"""
        s = max(self.states)
        self.states.remove(s)
        return s[-1]

    def __repr__(self):
        """ Returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """Creates searcher object that perform A* search"""

    def priority(self, state):
        """computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        priority = -1 * (self.heuristic(state) + state.num_moves)
        return priority 

        
