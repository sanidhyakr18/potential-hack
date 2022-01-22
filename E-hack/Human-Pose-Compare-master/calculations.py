import tensorflow.compat.v1 as tf
import pickle
import cv2
import numpy as np
import posenet
from pose import Pose
from score import Score
from dtaidistance import dtw


class get_Score(object):
	def __init__(self, lookup='lookup.pickle'):
		self.a = Pose()
		self.s = Score()
		self.b = pickle.load(open(lookup, 'rb'))
		self.input_test = []

	def get_action_coords_from_dict(self,action):
			for (k,v) in self.b.items():
				if k==action:
					(model_array,no_of_frames) = (v,v.shape[0])
			return model_array,no_of_frames

	def calculate_Score(self,video,action,path):
		with tf.Session() as sess:

			model_cfg, model_outputs = posenet.load_model(101, sess)
			model_array,j = self.get_action_coords_from_dict(action)

			cap = cv2.VideoCapture(video)

			frame_width = int(cap.get(3))
			frame_height = int(cap.get(4))
			size = (frame_width, frame_height)

			result = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

			i = 0

			if cap.isOpened() is False:

				print("error in opening video")

			while cap.isOpened():

				ret_val, image = cap.read()

				if ret_val:

					input_points= self.a.getpoints(cv2.resize(image,(372,495)),sess,model_cfg,model_outputs)

					if len(input_points) == 0:
						continue

					input_new_coords = np.asarray(self.a.roi(input_points)[0:34]).reshape(17,2)
					self.input_test.append(input_new_coords)

					img = image * 0
					input_new_c = input_new_coords

					input_new_coords = (input_new_coords * list(size)) / 256
					cv2.polylines(img, np.int32([np.asarray(input_new_coords)]), True, color=(0,255,0))
					result.write(img)

					model_array[i%100] = (model_array[i%100] * list(size)) / 256
					cv2.polylines(img, np.int32([np.asarray(model_array[i%100])]), True, color=(0,0,255))
					result.write(img)

					final_score,score_list = self.s.compare(np.asarray(input_new_c),np.asarray(model_array[i%100]),1,1)
					img = cv2.putText(img, 'Score: ' + str(final_score) + '%', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
					result.write(img)

					i = i + 1
				else:
					break

			cap.release()
			result.release()

			final_score,score_list = self.s.compare(np.asarray(self.input_test),np.asarray(model_array),j,i)
			print(i,j)

		# return final_score,score_list
