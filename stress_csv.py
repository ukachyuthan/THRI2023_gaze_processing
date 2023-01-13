import rosbag
from geometry_msgs.msg import Point
import pandas as pd
from argparse import ArgumentParser
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix, quaternion_from_matrix, euler_from_matrix
import glob, os
import numpy as np

# parser = ArgumentParser()
# parser.add_argument('filename', metavar='N', type=str, nargs='+',
#                     help='an integer for the accumulator')
# args = parser.parse_args()
# name_of_file = args.filename[-1]

# bag = rosbag.Bag(name_of_file + '.bag')
# valid = 0
for file in glob.glob("*.bag"):
    # try:
    valid = 0
    x_val = []
    y_val = []
    pupil_data = []
    name_of_file = file.replace(".bag", "")
    bag = rosbag.Bag(name_of_file + '.bag')
    if "calib" in name_of_file:
        topic = '/Pupil'
        # column_names = ['ee_gaze']
        # df = pd.DataFrame(columns=column_names)
        # i = 0
        # sum = 0
        # print(name_of_file)
        for topic, data, t in bag.read_messages(topics=topic):
            # print(data.data[0], data.data[1])
            if np.isnan(data.data[0]):
                if np.isnan(data.data[1]) == False:
                    pupil_data.append(data.data[1])
                    valid += 1
            elif np.isnan(data.data[1]):
                if np.isnan(data.data[0]) == False:
                    pupil_data.append(data.data[0])
                    valid += 1
            else:
                avg = (data.data[0] + data.data[1])/ 2
                pupil_data.append(avg)
                valid += 1

        eye_calib_value = sum(pupil_data)/valid

print(eye_calib_value)

max_pupil_average = -100000000000000000

for file in glob.glob("*.bag"):
    
    valid = 0
    x_val = []
    y_val = []
    pupil_data = []
    name_of_file = file.replace(".bag", "")
    bag = rosbag.Bag(name_of_file + '.bag')
    try:
        if ("calib" in name_of_file) == False:
            topic = '/Pupil'
            # column_names = ['ee_gaze']
            # df = pd.DataFrame(columns=column_names)
            # i = 0
            # sum = 0
            # print(name_of_file)
            for topic, data, t in bag.read_messages(topics=topic):
                if np.isnan(data.data[0]):
                    if np.isnan(data.data[1]) == False:
                        pupil_data.append(data.data[1])
                        valid += 1
                elif np.isnan(data.data[1]):
                    if np.isnan(data.data[0]) == False:
                        pupil_data.append(data.data[0])
                        valid += 1
                else:
                    avg = (data.data[0] + data.data[1])/ 2
                    pupil_data.append(avg)
                    valid += 1

        pupil_average = sum(pupil_data)/valid

        if pupil_average > max_pupil_average:
            max_pupil_average = pupil_average
    except:
        print(name_of_file)

max_pupil_diff = max_pupil_average - eye_calib_value

for file in glob.glob("*.bag"):
    
    valid = 0
    x_val = []
    y_val = []
    pupil_data = []
    name_of_file = file.replace(".bag", "")
    bag = rosbag.Bag(name_of_file + '.bag')
    try:
        if ("calib" in name_of_file) == False:
            topic = '/Pupil'
            # column_names = ['ee_gaze']
            # df = pd.DataFrame(columns=column_names)
            # i = 0
            # sum = 0
            # print(name_of_file)
            for topic, data, t in bag.read_messages(topics=topic):
                if np.isnan(data.data[0]):
                    if np.isnan(data.data[1]) == False:
                        pupil_data.append(data.data[1])
                        valid += 1
                elif np.isnan(data.data[1]):
                    if np.isnan(data.data[0]) == False:
                        pupil_data.append(data.data[0])
                        valid += 1
                else:
                    avg = (data.data[0] + data.data[1])/ 2
                    pupil_data.append(avg)
                    valid += 1

        pupil_average = sum(pupil_data)/valid
        column_names = ['pupil_average']
        df = pd.DataFrame(columns=column_names)
        i = 0
        # sum = 0
        # print(name_of_file)
        df = df.append({'pupil_average':(pupil_average - eye_calib_value)/max_pupil_diff}, ignore_index = True)
        df.to_csv(name_of_file + 'pupil.csv')
    except:
        print(name_of_file)
