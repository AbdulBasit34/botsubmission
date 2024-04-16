from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Node to run your script
        Node(
            package='bot_control',
            executable='your_script',
            name='bot_controller',
            output='screen',
        ),
        
        # Launch RViz2 with a pre-configured view
        ExecuteProcess(
            cmd=['rviz2', '-d', 'install/bot_control/share/bot_control/config/filtered_scan.rviz'],
            output='screen'
        ),
    ])

