#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class StraightMover(Node):
    def __init__(self):
        super().__init__('straight_mover')

        self.cmd_vel_pub = self.create_publisher(
            Twist, 
            '/turtle1/cmd_vel', 
            10
        )

        self.timer = self.create_timer(0.1, self.timer_callback)

        self.get_logger().info('🚀 直行控制节点已启动！')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.0

        self.cmd_vel_pub.publish(msg)
        self.get_logger().info('Published: linear.x=1.0')


def main(args=None):
    rclpy.init(args=args)
    node = StraightMover()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
