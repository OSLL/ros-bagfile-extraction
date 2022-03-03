# Сбор датасета ground truth

1. Необходимо для каждого watchtower выполнить команду на хосте:
<br>``dts stack up -H [HOSTNAME] core -d``
2. Необходимо для каждого watchtower и duckiebot (для которого необходимо собрать информацию):
<br>``dts stack up -H [HOSTNAME] autolab -d``
3. Необходимо включить передачу одометрии 
<br>``dts stack up -H [HOSTNAME] encoder -d``
4. В репозитории  [dt-autolab-localization](https://github.com/OSLL/dt-autolab-localization/tree/ETU_autolab) в ветке ETU_autolab необходимо выполнить следующую команду:
<br>``dts devel build -f``
<br>``dts devel run -f -X -L single-experiment -- --hostname ETUautolabtrack``
5. Помимо этого одновременно с запуском ``single-experiment`` необходимо записать bagfile:
<br>
5.1) Необходимо подключиться к боту:
<br> ```ssh duckie@autobot<bot_number>.local```
<br>
5.2) Зайти в ```dt-ros-commons``` контейнер
<br> ```docker exec -it duckietown/dt-ros-commons:<some_version>```
<br>
5.3) Записать bagfile:
<br>```rosbag record  /autobot<number>/deadreckoning_node/odom /autobot<number>/camera_node/camera_info /autobot<number>/camera_node/image/compressed```
6. С помощью [ros-bagfile-extraction](https://github.com/OSLL/ros-bagfile-extraction) можно конвертировать compressed topic из bagfile:
``catkin_ws/converter.launch veh:=<bot_name> bag_name:=<bagfile_name>``
