#!/usr/bin/env python3  
""" This line indicates to the system to use Python3 """
import rclpy # rclpy is the Python client library for ROS 2
from rclpy.node import Node 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, ReliabilityPolicy
import statistics
sample_nb =10


class MyNode(Node): # Class MyNode that inherits from Node
    
    def __init__(self):
        super().__init__("obstacle_avoidance") # Named the node "obstacle_avoidance"
        

        # 1.Publisher  for controlling the wheels 
        self.cmd_vel_pub =  self.create_publisher(Twist,"/cmd_vel",10)
        if()
        self.create_timer( 0.09,self.corrected_command) 

         # 2.Subscriber  to listen to /scan 
        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = ReliabilityPolicy.BEST_EFFORT
        self.scan_pub =  self.create_subscription(LaserScan,"/scan",self.scan_callback,qos_profile)
        self.scan_data = [ 0.0 for i in range(2*sample_nb)] 

        # 3.Subscriber to listen to /cmd_vel
        self.nav_sub = self.create_subscription(Twist, "/cmd_vel_nav",self.nav_callback,10)
        self.nav_command = [0.0,0.0] # linear speed , angular speed
        self.value_mesured = [0.0]*247 
        self.mean_of_value_mesured = [0.0]*25

        self.test_timer = self.create_timer(0.1, self.control_correction_command)
        self.test_phase = 0

    def control_correction_command(self):
        msg = Twist()
        
        if self.test_phase < 100:  # 5 secondes à 10Hz = 50 cycles
            msg.linear.x = 0.0
            msg.angular.z = -0.3  # Rotation à gauche plus marquée
        else:
            msg.linear.x = 0.3
            msg.angular.z = 0.0
            self.test_timer.cancel()  # Maintenant ça fonctionne
        
        self.cmd_vel_pub.publish(msg)
        self.test_phase += 1


    def nav_callback(self,msg:Twist):
        self.nav_command[0] = msg.linear.x 
        self.nav_command[1] = msg.angular.z
    
    def scan_callback(self,msg: LaserScan):
        for i in range(247):
            val = msg.ranges[i]
            if val == float('inf') or val !=val:
                val = 10.0
            self.value_mesured[i] = val
        self.compute_mean_of_value_mesured() # compute of the means
        
        self.get_logger().info('======================= Means ==========================')
        for i in range(25):
            self.get_logger().info(f'Moyenne groupe {i}: {self.mean_of_value_mesured[i]:.2f}m')

    def compute_mean_of_value_mesured(self):
        for i in range(24):
            start = i*10
            end = (1+i)*10
            somme = 0.0
            for j in range(start,end):
                somme+= self.value_mesured[j]
            self.mean_of_value_mesured[i] = somme/10

        somme = 0.0
        for i in range(240,247):
            somme+= self.value_mesured[i]
        self.mean_of_value_mesured[24] = somme/7
    

    def corrected_command(self):
        msg = Twist()
        for i in range(25):
            if ( self.mean_of_value_mesured[i] <= 0.13):
                self.control_correction_command()
                return
        msg.linear.x  = 0.7*self.nav_command[0]
        msg.angular.z = 0.7*self.nav_command[1]
        self.cmd_vel_pub.publish(msg) 

def main(args=None):
    rclpy.init(args=args) # Initialization of ROS 2 communication

    # Start node creation
    node = MyNode() # creation of the node 
    rclpy.spin(node) # This keeps the node alive indefinitely, until ctrl+c is pressed
    rclpy.shutdown() # Shutdown ROS 2 communication when stopped


if __name__ == "__main__":
    main()
