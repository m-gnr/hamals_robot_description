from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    package_share = FindPackageShare("hamals_robot_description")

    robot_description_file = PathJoinSubstitution([
        package_share,
        "urdf",
        "hamals_robot.urdf.xacro"
    ])

    robot_description = {
        "robot_description": Command([
            "xacro ",
            robot_description_file
        ])
    }

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
        output="screen"
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen"
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen"
    )

    return LaunchDescription([
        joint_state_publisher_gui,
        robot_state_publisher,
        rviz
    ])