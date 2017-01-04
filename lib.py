import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matrix

def get_data():
	cols = ["fs_id","user_id","story_id","story_user_id","emoticon","datetime","favorite","username","aliasname"]
	fav_story = pd.read_csv('fav_story.csv',names=cols)
	fav_story.head()

	userid = np.array(fav_story["user_id"])
	storyid = np.array(fav_story["story_id"])

	unique_uid = np.array(np.unique(userid))
	unique_stid = np.array(np.unique(storyid))

	num_users = len(unique_uid)
	num_stories = len(unique_stid)

	fav_mat = np.zeros((num_users,num_stories))

	for i in range(num_users):
		current_uid = unique_uid[i]
		current_fav = storyid[userid == current_uid]

		for j in range(len(current_fav)):
			fav_mat[i,unique_stid==current_fav[j]] = 1

	return np.array(fav_mat)

def gen_graph(alpha):
	R = get_data()
	N = len(R)
	M = len(R[0])
	K = 2

	P = np.random.rand(N, K)
	Q = np.random.rand(M, K)

	xData = []
	yData = []

	for step in range(1000, 50000000, 100):
		err = matrix.squared_error(R, P, Q, K, step, alpha)

	xData.append(step)
	yData.append(err)

    plt.figure()
	plt.plot(xData, yData)
	plt.savefig('graph-alpha-' + str(alpha) + '.png')
