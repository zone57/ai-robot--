



















#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class SquareMover(Node):

    def __init__(self):
        super().__init__('square_mover')

        # 创建发布者
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # 参数
        self.speed = 1.0
        self.turn_speed = 1.0
        self.side_time = 2.0      # 每条边走2秒
        self.turn_time = 1.57     # 90度

    def move(self):
        for i in range(4):
            self.get_logger().info(f'第{i+1}条边')

            # ===== 直行 =====
            msg = Twist()
            msg.linear.x = self.speed
            msg.angular.z = 0.0

            start = time.time()
            while time.time() - start < self.side_time:
                self.pub.publish(msg)
                time.sleep(0.05)

            # 停一下
            self.stop()

            # ===== 转弯 =====
            self.get_logger().info('转弯')

            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = self.turn_speed

            start = time.time()
            while time.time() - start < self.turn_time:
                self.pub.publish(msg)
                time.sleep(0.05)

            self.stop()

        self.get_logger().info('完成正方形！')

    def stop(self):
        msg = Twist()
        self.pub.publish(msg)
        time.sleep(0.2)


def main():
    rclpy.init()
    node = SquareMover()

    time.sleep(1)  # 等系统准备好

    node.move()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
