# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Para rodar:
    roslaunch projeto2 server_with_map_and_gui_plus_robot.launch
    roslaunch stdr_launchers rviz.launch
	rosrun projeto2 projeto2.py
"""


# Métodos úteis 
from helper_functions import (convert_pose_inverse_transform,
                              convert_translation_rotation_to_pose,
                              convert_pose_to_xy_and_theta,
                              angle_diff)





if __name__ == '__main__':
    r = rospy.Rate(10)

    while not(rospy.is_shutdown()):
        # in the main loop all we do is continuously broadcast the latest map to odom transform
        n.broadcast_last_transform()
        r.sleep()
