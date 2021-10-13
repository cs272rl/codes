# simple SARSA example
# model-free control slides - The corresponding MDP is on a slide

import numpy as np
import random

class MyModel:
    def __init__(self):
        # Model
        self.rs = ((0,0), (1,0), (15,0), (0,0), (0,10), (0,0), (0,-15), (0,0))
        self.num_states = len(self.rs)
        self.succs = ((1,4), (2,5), (3,5), (3,3), (5,6), (5,5), (5,7), (7,7))

        self.num_actions = 2 # West or North
        # West: 0
        # North: 1

    def terminate_tran(self):
        return None, 0, True

    def step(self, current_s, act):
        if current_s == 3:
            next_s, imR, is_terminal = self.terminate_tran()
        elif current_s == 5:
            next_s, imR, is_terminal = self.terminate_tran()
        elif current_s == 7:
            next_s, imR, is_terminal = self.terminate_tran()
        else:
            imR = self.rs[current_s][act]
            next_s = self.succs[current_s][act]
            is_terminal = False

        return imR, next_s, is_terminal


class Agent:
    initial_s = 0
    def __init__(self, num_states):
        self.Qs = []

        # init to 0s
        for _ in range(num_states):
            self.Qs.append([0,0])

        # episode count
        self.k = 0

        self.current_s = Agent.initial_s # initial state 0
        self.is_terminal = False

        self.step_size = 0.02
        self.gamma = 0.8

    def refresh(self):
        self.current_s = Agent.initial_s # initial state 0
        self.is_terminal = False

        self.k += 1
        print()

    def learn_ep(self, env):
        # SARSA
        # beginning of the episode, current state is 0
        print(f'-- New episode {self.k} --')
        print(f'Initial state: {self.current_s}')
        act = self.egreedy(self.current_s, self.k)

        # for an episode
        while not self.is_terminal:
            # take a step by choosing an action (act)
            imR, next_s, self.is_terminal = env.step(self.current_s, act)
            print(f's:{self.current_s}, a:{act}, R:{imR}, s\':{next_s}')

            if self.is_terminal:
                print('End of an episode')
                print()
            else:
                # epsilon greedy
                next_a = self.egreedy(next_s, self.k)
                print(f'next action a\': {next_a}')

                # Q val of the next state
                qspa = self.Qs[next_s][next_a]

                print(f'{self.Qs[self.current_s][act]} + {self.step_size} * ({imR} + {self.gamma} * {qspa} - {self.Qs[self.current_s][act]})')
                # SARSA UPDATE
                self.Qs[self.current_s][act] = self.Qs[self.current_s][act] + self.step_size * (imR + self.gamma * qspa - self.Qs[self.current_s][act])
                print(f'new Q[s{self.current_s}][a{act}] = {self.Qs[self.current_s][act]}')

                self.current_s = next_s
                act = next_a

                self.show_Qs()
            print()
        # initialize
        self.refresh()

    def egreedy(self, next_s, k):
        epsilon = 0.5 - 0.00005 * k
        r = random.random()
        if r < epsilon:  # take a random action
            n_a = random.choice(range(len(self.Qs[next_s])))
        else:  # choose a greedy action based on Q
            n_a = np.argmax(self.Qs[next_s])
        return n_a

    def show_Qs(self):
        print(f'Q: {self.Qs}')




if __name__ ==  '__main__':
    env = MyModel()
    agent = Agent(env.num_states)

    # num of episodes
    limit = 50000

    while agent.k < limit:
        agent.learn_ep(env)
