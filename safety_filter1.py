#!/usr/bin/env python3  
""" This line indicates to the system to use Python3 """
import rclpy # rclpy is the Python client library for ROS 2
from rclpy.node import Node 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, ReliabilityPolicy
import statistics
sample_nb =10


class MovingAverge():
    def __init__(self,window_size=10):
        self.window_size = window_size
        self.distance = []
    
    def update(self,value):
        # Filtering infinite and Nan value
        if value == float('inf') or value != value:
            value = 10.0 # we replace the unvalid value by 10.0 meters
        self.distance.append(value)

        if len(self.distance) > len(self.window_size):
            self.distance.pop(0)

        return sum(self.distance)/len(self.distance)
    
    def reset(self):
        self.distance = []

class MyNode(Node): # Class MyNode that inherits from Node
    
    def __init__(self):
        super().__init__("obstacle_avoidance") # Named the node "obstacle_avoidance"
        

        # 1.---- Publisher  for controlling the wheels 
        self.cmd_vel_pub =  self.create_publisher(Twist,"/cmd_vel",10)
        self.create_timer( 0.09,self.corrected_command) 

         # 2.------ Subscriber  to listen to /scan 
        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = ReliabilityPolicy.BEST_EFFORT
        self.scan_pub =  self.create_subscription(LaserScan,"/scan",self.scan_callback,qos_profile)
        self.scan_data = [ 0.0 for i in range(2*sample_nb)] 

        # 3.------ Subscriber to listen to /cmd_vel
        self.nav_sub = self.create_subscription(Twist, "/cmd_vel_nav",self.nav_callback,10)
        self.nav_command = [0.0,0.0] # linear speed , angular speed
# ==========================================================================================================
    # prepare 25 list of values of set of 10 values
    self.all_values = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] for i in range(25)]
    def get_zone_indice(self, angle_deg):
        angle_rad = angle_deg*(3.14/180)
        return int(angle_rad_- angle_min)/angle_increment
    


#===========================================================================================================
  
        
    


def main(args=None):
    rclpy.init(args=args) # Initialization of ROS 2 communication

    # Start node creation
    node = MyNode() # creation of the node 
    rclpy.spin(node) # This keeps the node alive indefinitely, until ctrl+c is pressed
    rclpy.shutdown() # Shutdown ROS 2 communication when stopped


if __name__ == "__main__":
    main()