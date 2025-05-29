import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import math
import time
from std_msgs.msg import Int32


class drawsquare(Node):

    def __init__(self):
        super().__init__('drawsquare')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.count = self.create_publisher(Int32, 'pose', 10)
        go=Twist()
        go.linear.x=3.0
        go.angular.z=0.0
        turn=Twist()
        turn.linear.x=0.0
        turn.angular.z=math.pi/2
        self.i=0
        
        while True :
            self.publisher_.publish(go)
            time.sleep(2)
            self.publisher_.publish(turn)
            time.sleep(1)
            self.publisher_.publish(go)
            time.sleep(2)
            self.publisher_.publish(turn)
            time.sleep(1)
            self.publisher_.publish(go)
            time.sleep(2)
            self.publisher_.publish(turn)
            time.sleep(1)
            self.publisher_.publish(go)
            time.sleep(2)
            self.publisher_.publish(turn)
            time.sleep(1)
            self.i=self.i+1
            msg=Int32()
            msg.data=self.i
            self.count.publish(msg)


def main(args=None):

    rclpy.init(args=args)
    node = drawsquare()
    drawsquare
    drawsquare.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
