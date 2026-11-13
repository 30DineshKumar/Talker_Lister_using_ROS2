import time
import rclpy
from std_msgs.msg import String

def main():
    rclpy.init()
    node = rclpy.create_node('publisher_node')
    pub = node.create_publisher(String, 'topic', 10)
    node.get_logger().info('Publisher node started, now publishing messages')

    count = 0
    try:
        while rclpy.ok():
            msg = String()
            msg.data = 'Hello Dinesh ' + str(count)
            pub.publish(msg)
            node.get_logger().info('Publishing: ' + msg.data)
            count += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print('KeyboardInterrupt received, shutting down publisher node...')
    finally:
        try:
            node.destroy_node()
        except BaseException:
            pass
        try:
            if rclpy.ok():
                rclpy.shutdown()
        except BaseException:
            pass



if __name__ == '__main__':
    main()