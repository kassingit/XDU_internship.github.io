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
        #self.create_timer(0.3,self.timer_callback) # to display "Obstacle detected at x distance" every one seconde

        # 1.---- Publisher  for controlling the wheels 
        self.cmd_vel_pub =  self.create_publisher(Twist,"/cmd_vel",10)
        self.create_timer( 0.09,self.corrected_command) # send the corrrected commands

         # 2.------ Subscriber  to listen to /scan 
        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = ReliabilityPolicy.BEST_EFFORT
        self.scan_pub =  self.create_subscription(LaserScan,"/scan",self.scan_callback,qos_profile)
        self.scan_data = [ 0.0 for i in range(2*sample_nb)] # right, right diagonal, forward,left diagonal ,left

        # 3.------ Subscriber to listen to /cmd_vel
        self.nav_sub = self.create_subscription(Twist, "/cmd_vel_nav",self.nav_callback,10)
        self.nav_command = [0.0,0.0] # linear speed , angular speed

        self.avoiding = False  # ? MANQUANT dans __init__
        self.active_timer = None  # ? MANQUANT dans __init__
    
    def scan_callback(self,msg: LaserScan):
        self.get_logger().info('=================================================')            
        for i in range(2*sample_nb):
            self.scan_data[i]=msg.ranges[113+i]
            self.get_logger().info(f'Distance a indice {i} = {self.scan_data[i]}')            

    def nav_callback(self,msg:Twist):
        self.nav_command[0] = msg.linear.x 
        self.nav_command[1] = msg.angular.z
        
    # /scan and /controller_server data treatement
    def turn_left(self):
        msg = Twist()
        msg.linear.x = 0.3
        msg.angular.z = 0.3
        self.cmd_vel_pub.publish(msg) # allows to publish the message

    def turn_right(self):
        msg = Twist()
        msg.linear.x = 0.3
        msg.angular.z = -0.3
        self.cmd_vel_pub.publish(msg) # allows to publish the message

    def back_up(self):
        msg = Twist()
        msg.linear.x = -0.3
        msg.angular.z = 0.0
        self.cmd_vel_pub.publish(msg) # allows to publish the message

    def stop_avoiding(self):
        """Arrête le timer d'évitement"""
        if self.active_timer is not None:
            self.active_timer.cancel()
            self.active_timer = None
        self.avoiding = False
        self.get_logger().info("Fin de l'évitement")
        
    def corrected_command(self):

        msg = Twist()
        moy1 = statistics.mean(self.scan_data[0:10])
        moy2 = statistics.mean(self.scan_data[10:20])
        if ( moy1 <= 0.18):
            # Obstacle à gauche ? tourner à droite
            self.avoiding = True
            self.turn_right()
            # Timer pour arrêter l'évitement après 2 secondes
            self.active_timer = self.create_timer(2.0, self.stop_avoiding)
        elif( moy2 <= 0.18 ):
            # Obstacle à droite ? tourner à gauche
            self.avoiding = True
            self.turn_left()
            # Timer pour arrêter l'évitement après 2 secondes
            self.active_timer = self.create_timer(2.0, self.stop_avoiding)
        else:
            msg.linear.x = self.nav_command[0]/2
            msg.angular.z = self.nav_command[1]/2
            self.cmd_vel_pub.publish(msg) # allows to publish the message
        
    

    #-------------------- Alert message
    def timer_callback(self):
        self.get_logger().info(f"Obstacle detected at {self.distance_forward :.2f} meters")

def main(args=None):
    rclpy.init(args=args) # Initialization of ROS 2 communication

    # Start node creation
    node = MyNode() # creation of the node 
    rclpy.spin(node) # This keeps the node alive indefinitely, until ctrl+c is pressed
    rclpy.shutdown() # Shutdown ROS 2 communication when stopped


if __name__ == "__main__":
    main()
