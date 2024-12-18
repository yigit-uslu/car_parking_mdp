import abc
from config import PARK_STATUS_NS, ACTION_SPACE_NS, PARKED_STATE

class Policy(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def select_action(self, state):
        pass
        

class OptimalPolicy(Policy):
    def __init__(self):
        super().__init__()

    def select_action(self, state):

        if state == PARKED_STATE:
            action = None
        elif state[0] == 0:
            action = ACTION_SPACE_NS.PARK # we have to park once we are at the private lot

        # implement this part based on the solution of Bellman's equation
        else:
            ################## TO DO #######################
            if state[1] == PARK_STATUS_NS.CANNOT_PARK:
                action = ACTION_SPACE_NS.KEEP_LOOKING
            else:
                if state[0] <= 2: # this threshold depends on the values of p and C
                    action = ACTION_SPACE_NS.PARK
                else:
                    action = ACTION_SPACE_NS.KEEP_LOOKING

            ################## TO DO #######################

        return action
    

class GreedyPolicy(Policy):
    def __init__(self):
        super().__init__()

    def select_action(self, state):
        if state == PARKED_STATE:
            action = None
        elif state[0] == 0:
            action = ACTION_SPACE_NS.PARK
        else:
            if state[0] == 1 and state[1] == PARK_STATUS_NS.CAN_PARK: # wait until last public parking spot
                action = ACTION_SPACE_NS.PARK 
            else:
                action = ACTION_SPACE_NS.KEEP_LOOKING

        return action
    


class ConservativePolicy(Policy):
    def __init__(self):
        super().__init__()

    def select_action(self, state):
        if state == PARKED_STATE:
            action = None
        elif state[0] == 0:
            action = ACTION_SPACE_NS.PARK
        else:
            if state[1] == PARK_STATUS_NS.CAN_PARK: # park at the first available public parking spot
                action = ACTION_SPACE_NS.PARK 
            else:
                action = ACTION_SPACE_NS.KEEP_LOOKING

        return action

