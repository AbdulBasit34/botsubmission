clone the files to your workspace, the bot_description files have been uploaded seperately due to file limit exceeding, apologies for that bot_control has been uploaded but due to the gazebo software not working properly the code's running is ver random.

execute the following commands:-
   colcon build
   ros2 launch my_first_pkg gazebo.launch.py for launching the bot
   open a new terminal and run:- 
           ros2 run teleop_twist_keyboard teleop_twist_keyboard for teleoperation

In 6 hours I could do only the bot control urdf file and launch file I have added differential drive plugin
the laser plugin wasnt working for me so couldnt fix that 
