import time 
import rclpy
from std_msgs.msg import String

def callback(msg):
    print('Received: ' + msg.data)

def main():
    rclpy.init()
    node = rclpy.create_node('subscriber_node')
    sub = node.create_subscription(String, 'topic', callback, 10)
    node.get_logger().info('Subscriber node started, now subscribing to messages')

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('KeyboardInterrupt received, shutting down subscriber node...')
    finally:
        try:
            node.destroy_node()
        except BaseException:
            pass
        try:
            if rclpy.ok():
                rclpy.shutdown()
        except Exception:
            pass

if __name__ == '__main__':
    main()