import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class LaserFilter(Node):
    def __init__(self):
        super().__init__('laser_filter')
        # Subscriber to the original scan topic
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher for the filtered scan topic
        self.publisher = self.create_publisher(
            LaserScan,
            '/filtered_scan',
            10)

    def listener_callback(self, msg):
        filtered_scan = LaserScan()

        # Copy the header information
        filtered_scan.header = msg.header

        # Set the same time increment
        filtered_scan.time_increment = msg.time_increment

        # Set the same scan time
        filtered_scan.scan_time = msg.scan_time

        # Set the same min and max ranges
        filtered_scan.range_min = msg.range_min
        filtered_scan.range_max = msg.range_max

        # Calculate the index range to filter 0 to 120 degrees
        start_angle = 0  # Starting at 0 degrees
        end_angle = 120  # Ending at 120 degrees

        # Calculate the index of start and end angles
        start_index = int((start_angle - msg.angle_min) / msg.angle_increment)
        end_index = int((end_angle - msg.angle_min) / msg.angle_increment)

        # Filter the ranges and intensities
        filtered_scan.ranges = msg.ranges[start_index:end_index]
        filtered_scan.intensities = msg.intensities[start_index:end_index]

        # Adjust angle parameters
        filtered_scan.angle_min = msg.angle_min + start_index * msg.angle_increment
        filtered_scan.angle_max = msg.angle_min + end_index * msg.angle_increment
        filtered_scan.angle_increment = msg.angle_increment

        # Publish the filtered scan
        self.publisher.publish(filtered_scan)

def main(args=None):
    rclpy.init(args=args)
    laser_filter = LaserFilter()
    rclpy.spin(laser_filter)
    laser_filter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

