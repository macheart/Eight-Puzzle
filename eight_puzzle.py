
from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):
    """Open the file with the specified filename for reading
       and use a loop to process the file one line at a time"""
    f = open(filename)
    puzzles_solved = 0
    moves = 0
    states_tested = 0
    
    for line in f:
        line = line[:-1]
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        
        searcher = create_searcher(algorithm, param)
        soln = None
        try:
            soln = searcher.find_solution(init_state)
            if soln == None:
                line_colon = str(line) +':'
                print(line_colon, 'no solution')
                
            else:
                line_colon = str(line) +':'
                moves += soln.num_moves
                states_tested += searcher.num_tested
                print (line_colon, soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
                puzzles_solved += 1
                
        except KeyboardInterrupt:
            print('search terminated, ', end='')
            print('no solution')
            
    print()
    if puzzles_solved == 0:
        print('solved', puzzles_solved, 'puzzles')
    else:
        print('solved', puzzles_solved, 'puzzles')
        average_moves = moves/puzzles_solved
        average_states_tested = states_tested/puzzles_solved
        print('averages:', average_moves, 'moves,', average_states_tested, 'states tested')

    
            
        
