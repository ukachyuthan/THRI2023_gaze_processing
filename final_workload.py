import rosbag
from geometry_msgs.msg import Point
import pandas as pd
from argparse import ArgumentParser
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix, quaternion_from_matrix, euler_from_matrix
import glob, os
import numpy as np

total_list = ["mp2", "mp3", "ap2", "ap3", "sp2", "sp3", "shp2", "shp3"]

for name in total_list:

    try:

        sum = 0

        for file in glob.glob("*.csv"):

            column_names = ["workload"]
            df = pd.DataFrame(columns=column_names)

            # print(file)

            if name in file:

                name_of_file = file.replace(".csv", "")
                df_1 = pd.read_csv('./' + name_of_file + '.csv')
                data1 = df_1.values

                # print(data1)

                sum += 0.5 * (data1[0][1])
            
        df = df.append({'workload' : sum}, ignore_index = True)
        df.to_csv(name_of_file + 'cognitive_wl.csv')
    
    except:
        print(name)