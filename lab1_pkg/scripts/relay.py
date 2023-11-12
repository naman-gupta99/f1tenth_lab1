#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
    def __init__(self):
        super().__init__('relay')
        self.subscription = self.create_subscription(AckermannDriveStamped, 'drive', self.listener_callback, 0)
        self.publisher = self.create_publisher(AckermannDriveStamped, 'drive_relay', 0)

    def listener_callback(self, msg: AckermannDriveStamped):
        msg.drive.speed = msg.drive.speed * 3
        msg.drive.steering_angle = msg.drive.steering_angle * 3
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
    
def main(args=None):
    rclpy.init(args=args)
    relay = Relay()
    rclpy.spin(relay)
    relay.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()