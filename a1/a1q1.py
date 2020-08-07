#Alexa Armitage
#NSID: ama043
#Student ID: 11158883
#CMPT 317 Assignment 1 Question 1

class MathProblemState:
    def __init__(self, equation, goal, numbers, path_cost=1):
        """Represents the equation state for a simple math problem

        Keyword Arguments:
        equation -- The equation for the current state. Can be a single number
        goal -- The number the equation is trying to create
        numbers -- Possible numbers to add to the equation, a list of strings
        """
        self.g = int(goal)
        self.n = numbers
        self.eqn = str(equation) #Cast to str for when int is ocassionaly passed
        self.pc = path_cost

    def __str__(self):
        """An override method for nicely printing the state. """
        prstr = "Goal: " + str(self.g) + "   \tUnused Numbers: " + str(self.n)
        prstr +="\nEvaluation: "+str(eval(self.eqn))+"\tEquation: " + self.eqn
        return prstr


class MathProblem:
    def __init__(self, state):
        self.init_state = state  #Used to create initial frontier

    def is_goal(self, state):
        """Returns true if the equation evaluates to the goal, false otherwise
        Keyword Arguments:
        state -- A MathProblemState with an equation and goal
        """
        return eval(state.eqn) == state.g

    def actions(self, state):
        """Returns a list of actions usable on a state
        Returns: a list of strings composed of one operator and one number
        """
        actions = []
        for num in state.n:
            actions.append(" + " + num)
            actions.append(" - " + num)
            if eval(state.eqn) != 0:          #0*num is 0, so pointless
                actions.append(" * " + num)
            if int(num) != 0 and eval(state.eqn) != 0:     #Cannot divide by 0
                actions.append(" // " + num)
        return actions

    def result(self, state, action):
        """Return a new MathProblemState with the action applied
        Return: The new state with the action added to the equation
        """
        action_num = action.split()[1]
        new_num_list = []
        if isinstance(state.n, (list,)):
            new_num_list = state.n.copy()
            new_num_list.remove(action_num)
        new_eqn = "(" + state.eqn + action + ")"
        new_state = MathProblemState(new_eqn, state.g, new_num_list)
        return new_state

def testing():
    """A quick testing method. Uses manual verification."""
    test_state = MathProblemState("0", "5", ["2","3",])
    test_problem = MathProblem(test_state)
    acts = test_problem.actions(test_state)
    print(acts)
    new_test_state = test_problem.result(test_state, acts[0])
    print(new_test_state)
    print("Goal reached" if test_problem.is_goal(new_test_state) else "Not goal.")
    acts = test_problem.actions(new_test_state)
    print(acts)
    final_test_state = test_problem.result(new_test_state, acts[0])
    print(final_test_state)
    print("Goal reached" if test_problem.is_goal(final_test_state) else "Not goal.")

#Uncomment out the next line to see testing
#testing()
