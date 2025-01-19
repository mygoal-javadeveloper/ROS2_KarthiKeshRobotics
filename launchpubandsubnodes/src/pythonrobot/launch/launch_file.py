from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="pythonrobot",
                executable="firstpubnode",
                name="firstpubnode",
                output="screen",
            ),
            Node(
                package="pythonrobot",
                executable="firstsubnode",
                name="firstsubnode",
                output="screen",
            ),

        ]
    )