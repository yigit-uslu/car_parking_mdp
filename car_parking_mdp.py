import numpy as np
from collections import defaultdict
from env import BaseEnv
from car_parking_mdp.policy import OptimalPolicy, GreedyPolicy, ConservativePolicy
from config import  PARK_STATUS_NS

def main():
    n_episodes = 10000
    env = BaseEnv()
    policies = [OptimalPolicy(), GreedyPolicy(), ConservativePolicy()]

    all_rewards = defaultdict(list)
    for policy in policies:

        for _ in range(n_episodes):
            env.reset()

            done = False
            timestep = 0
            while not done:

                action = policy.select_action(state = env.state)

                old_state = env.state
                new_state, reward, done = env.step(action=action)
                print(f'Timestep = {timestep}\tWAS PARKING AVAILABLE = {old_state[1] == PARK_STATUS_NS.CAN_PARK}\tOld state = {old_state}\tNew state = {new_state}\treward = {reward}')

                timestep += 1

            total_reward = np.sum(env.rewards)
            print(f'Episode = {_}\tTotal reward = {total_reward}')
            all_rewards[policy.__class__.__name__].append(total_reward.item())


    print('\n****************************** SUMMARY **************************************')
    best_policy_idx = 0
    best_reward = -float('Inf')
    for i, policy in enumerate(policies):
        print(f'Policy = {policy.__class__.__name__}\tAverage reward = {np.mean(all_rewards[policy.__class__.__name__]).item()}')

        if i == 0:
            best_reward = np.mean(all_rewards[policy.__class__.__name__]).item()
        else:
            if np.mean(all_rewards[policy.__class__.__name__]).item() > best_reward:
                best_reward = np.mean(all_rewards[policy.__class__.__name__]).item()
                best_policy_idx = i

    print(f'Best policy = {policies[best_policy_idx].__class__.__name__}, best average reward = {best_reward}')
    print('*****************************************************************************')


if __name__ == "__main__":
    main()