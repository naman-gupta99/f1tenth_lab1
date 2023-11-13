# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/foxy/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: `source /opt/ros/foxy/setup.bash`  sets the environment for ros2 commands whereas `source install/local_setup.bash` sets the environment for the specific packages allowing us to use its modules and nodes

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: If more than `queue_size` messages are pushed to a certain topic before they are consumed, the new coming messages start get dropped

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: If you call `ros2 launch` in the directory where the launch file is then there is no need to run colcon build as the file refered will be in the current working directory. Although, when calling `ros2 launch` when it si installed with the package, the file inside the install directory will not be updated until we run `colcon build`.
