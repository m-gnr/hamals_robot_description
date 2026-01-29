from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hamals_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # ROS package index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # package.xml
        ('share/' + package_name, ['package.xml']),

        # launch dosyaları
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),

        # urdf / xacro dosyaları
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*')),

        # ileride eklemek için hazır:
        # rviz configleri
        # (os.path.join('share', package_name, 'rviz'),
        #     glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='m_gnr',
    maintainer_email='m_gnr@icloud.com',
    description='Hamals robot description package (URDF/Xacro)',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
