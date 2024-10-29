import numpy as np
from config import N, p, C, state_space_dict, PARK_STATUS_NS, ACTION_SPACE_NS, PARKED_STATE


class BaseEnv():
    def __init__(self):
        self.states = state_space_dict
        self.init_state = self.reset()
        # self.done = False

    def reset(self):
        park_status = self.get_next_parking_spot_status()
        self.state = state_space_dict[f"{(N, park_status)}"]
        self.done = False
        self.rewards = []
        return self.state
    

    # @staticmethod
    def get_next_parking_spot_status(self):
        if np.random.random() < p:
            park_status = PARK_STATUS_NS.CAN_PARK
        else:
            park_status = PARK_STATUS_NS.CANNOT_PARK
        return park_status

    
    def step(self, action):
        if self.done:
            print('Episode has ended.')
            return None, None, None
        
        # Define state-action-state transitions
        if self.state[0] in range(1, N + 1):
            if action == ACTION_SPACE_NS.PARK:
                if self.state[1] == PARK_STATUS_NS.CANNOT_PARK:
                    self.raise_invalid_action_error(self.state, action)
                
                elif self.state[1] == PARK_STATUS_NS.CAN_PARK:
                    new_state = PARKED_STATE
                    reward = -self.state[0]
                    self.state = new_state
                    self.rewards.append(reward)
                    self.done = True
                
                else:
                    raise ValueError

            elif action == ACTION_SPACE_NS.KEEP_LOOKING:
                if self.state[0] == 1:
                    park_status = PARK_STATUS_NS.CAN_PARK # move to private-parking lot
                else:
                    park_status = self.get_next_parking_spot_status()

                new_state = (self.state[0] - 1, park_status)
                reward = 0
                self.state = new_state
                self.rewards.append(reward)
            else:
                raise ValueError
            
        elif self.state[0] == 0:
            if action == ACTION_SPACE_NS.KEEP_LOOKING:
                self.raise_invalid_action_error(self.state, action) # we have to park once we end up in the private parking lot

            elif action == ACTION_SPACE_NS.PARK:
                new_state = PARKED_STATE
                reward = -C
                self.state = new_state
                self.rewards.append(reward)
                self.done = True
            else:
                raise ValueError            

        return self.state, reward, self.done
    

    def raise_invalid_action_error(self, state, action):
        print(f"Invalid action {action} at state {state}")
        raise ValueError



