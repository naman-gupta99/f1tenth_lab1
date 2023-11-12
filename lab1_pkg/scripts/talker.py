#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 0)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.declare_parameter('v', 0.5)
        self.declare_parameter('d', 0.0)

    def timer_callback(self):
        drive_msg = AckermannDriveStamped()
        drive_msg.drive.speed = self.get_parameter('v').value
        drive_msg.drive.steering_angle = self.get_parameter('d').value
        self.publisher_.publish(drive_msg)
        self.get_logger().info('Publishing: "%s"' % drive_msg)

def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
