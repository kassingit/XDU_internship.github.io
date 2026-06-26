      self.avoiding = False  
        self.active_timer = None 
    
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
            self.avoiding = True
            self.turn_right()
            self.active_timer = self.create_timer(2.0, self.stop_avoiding)
        elif( moy2 <= 0.18 ):
            self.avoiding = True
            self.turn_left()
            self.active_timer = self.create_timer(2.0, self.stop_avoiding)
        else:
            msg.linear.x = self.nav_command[0]/2
            msg.angular.z = self.nav_command[1]/2
            self.cmd_vel_pub.publish(msg) 
