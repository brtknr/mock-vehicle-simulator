import gym
import numpy as np
# import tensorflow as tf

state = 1
goal = 5

class VehicleEnv(gym.Env):
	'''This is a description of the environment of the simulation vehicle to be updated at every timestep.
	'''
	action_space = 4 # 0 = do nothing, 1 = left lane, 2 = right lane, 3 = accelerate, 4 = brake
	def __init__(self):
		pass
	def _step(self,action):
		# Update the environment observation and reward for the agent based on the last action
		global state
		observation = state = state * action
		reward = 1./np.exp(abs(goal - state))
		done = False
		info = dict()
		return observation, reward, done, info

class NeuralAgent(object):
	''' This is a description of how the agent is implemented.
	'''
	def __init__(self, env):
		self.env = env
	def action(self):
		# Link to environment
		env = self.env
		# Initial action
		action = 1
		while True:
			observation,reward,done,_ = env.step(action)
			# Based on the current observation, this should be the next action
			correction = 0.2 * (1 - reward)

			if observation > goal:
				action = 1 - correction
			else:
				action = 1 + correction
			print 'observation={}, reward={}, action={}'.format(observation, reward, action)				
			yield action


env = VehicleEnv()
agent = NeuralAgent(env = env)
action = agent.action()

def AAPIManage():
	# What should the next action be based on the current observations?
	action.next()

	# Apply action in Aimsun


# Invoke AAPIManage
for tstep in range(15):
	AAPIManage()

