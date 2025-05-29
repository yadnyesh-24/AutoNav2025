import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class count(Node):

    def __init__(self):
        super().__init__('count')
        self.subscription = self.create_subscription(
            Int32,
            'pose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Number of turns moved: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = count()

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
