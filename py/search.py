# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import heappush, heappop
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
      """
      Returns the start state for the search problem
      """
      util.raiseNotDefined()

    def isGoalState(self, state):
      """
      state: Search state

      Returns True if and only if the state is a valid goal state
      """
      util.raiseNotDefined()

    def getSuccessors(self, state):
      """
      state: Search state

      For a given state, this should return a list of triples,
      (successor, action, stepCost), where 'successor' is a
      successor to the current state, 'action' is the action
      required to get there, and 'stepCost' is the incremental
      cost of expanding to that successor
      """
      util.raiseNotDefined()

    def getCostOfActions(self, actions):
      """
      actions: A list of actions to take

      This method returns the total cost of a particular sequence of actions.  The sequence must
      be composed of legal moves
      """
      util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure that you implement the graph search version of DFS,
    which avoids expanding any already visited states. 
    Otherwise your implementation may run infinitely!
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    """
    YOUR CODE HERE
    """

    closedSet = []
    expandedSet = [problem.getStartState()]
    path = {}

    while len(expandedSet) > 0:
        state = expandedSet.pop()
        closedSet.append(state)

        if problem.isGoalState(state):
            print("Goal!")

            action = []
            while state != problem.getStartState():
                action.insert(0, path[state][1])
                state = path[state][0]

            print(action)
            return action
        else:
            adjList = []
            for (successor, action, stepCost) in problem.getSuccessors(state):
                if successor not in closedSet:
                    adjList.insert(0, successor)
                    path[successor] = (state, action)
            expandedSet += adjList

def breadthFirstSearch(problem):
    """
    YOUR CODE HERE
    """

    closedSet = []
    expandedSet = [problem.getStartState()]
    path = {}

    while len(expandedSet) > 0:
        state = expandedSet.pop()
        closedSet.append(state)

        if problem.isGoalState(state):
            print("Goal!")

            action = []
            while state != problem.getStartState():
                action.insert(0, path[state][1])
                state = path[state][0]

            print(action)
            return action
        else:
            for (successor, action, stepCost) in problem.getSuccessors(state):
                if successor not in closedSet:
                    expandedSet.insert(0, successor)
                    closedSet.append(successor)
                    path[successor] = (state, action)


def uniformCostSearch(problem):
    """
    YOUR CODE HERE
    """
    closedSet = []
    expandedSet = []
    heappush(expandedSet, (0, problem.getStartState()))
    path = {}

    while len(expandedSet):
        stateInfo = heappop(expandedSet)
        state = stateInfo[1]
        cost = stateInfo[0]
        closedSet.append(state)

        if problem.isGoalState(state):
            print("Goal!")

            action = []
            while state != problem.getStartState():
                action.insert(0, path[state][1])
                state = path[state][0]

            print(action)
            return action
        else:
            for (successor, action, stepCost) in problem.getSuccessors(state):
                if successor not in closedSet:
                    if successor not in path:
                        path[successor] = (state, action, stepCost + cost)
                        heappush(expandedSet, (stepCost + cost, successor))
                    elif path[successor][2] > stepCost+cost:
                        path[successor] = (state, action, stepCost + cost)
                        heappush(expandedSet, (stepCost + cost, successor))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    YOUR CODE HERE
    """
    closedSet = []
    expandedSet = []
    heappush(expandedSet, (heuristic(problem.getStartState(), problem), problem.getStartState()))
    path = {}

    while len(expandedSet):
        stateInfo = heappop(expandedSet)
        state = stateInfo[1]
        cost = 0
        if state in path:
            cost += path[state][2]
        closedSet.append(state)

        if problem.isGoalState(state):
            print("Goal!")
            print(path)

            action = []
            while state != problem.getStartState():
                action.insert(0, path[state][1])
                state = path[state][0]

            print(action)
            return action
        else:
            for (successor, action, stepCost) in problem.getSuccessors(state):
                print(heuristic(successor, problem))
                if successor not in closedSet:
                    heur = heuristic(successor, problem) + stepCost + cost
                    if successor not in path:
                        path[successor] = (state, action, stepCost + cost)
                        heappush(expandedSet, (heur, successor))
                    elif path[successor][2] > stepCost + cost:
                        path[successor] = (state, action, stepCost + cost)
                        heappush(expandedSet, (heur, successor))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
