# test_repository
1) roslaunch  bicycle_robot_gazebo test_world.launch
2)in another terminal paste the following: rosrun gazebo_ros spawn_model -file `rospack find car_model_description`/urdf/car_model.urdf -urdf -x 0 -y 0 -z 1 -model car_model
3) roslaunch robot_control bicycle_control.launch
