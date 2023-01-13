import rosbag
from geometry_msgs.msg import Point
import pandas as pd
from argparse import ArgumentParser
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix, quaternion_from_matrix, euler_from_matrix
import glob, os

# parser = ArgumentParser()
# parser.add_argument('filename', metavar='N', type=str, nargs='+',
#                     help='an integer for the accumulator')
# args = parser.parse_args()
# name_of_file = args.filename[-1]

# bag = rosbag.Bag(name_of_file + '.bag')
for file in glob.glob("*.bag"):
    try:
        x_val = []
        y_val = []
        name_of_file = file.replace(".bag", "")
        bag = rosbag.Bag(name_of_file + '.bag')
        topic = '/ee_gaze'
        column_names = ['ee_gaze']
        df = pd.DataFrame(columns=column_names)
        i = 0
        sum = 0
        print(name_of_file)
        for topic, data, t in bag.read_messages(topics=topic):
            # print(t)
            x_val.append(data.data)
            if data.data == 1:
                sum+=1
        value = sum/len(x_val)

        # for i in range(len(x_val)):

        df = df.append({'ee_gaze':value}, ignore_index = True)

            

        df.to_csv(name_of_file + 'gaze.csv')
    except:
        print("calib", name_of_file)