# Mapeamento no ROS / RViz




Inicie o robô real com roslaunch

Abra o rviz


Para fazer um mapa, rode:

	$ roslaunch neato_2dnav gmapping_demo.launch

Isso vai iniciar o código de SLAM. Recomendo que abra o RViz para ver os dados do sensor e também o teleop_twist_keyboard para pilotar o robô. Para que o mapa seja criado o robô precisa se mover.


Pilote o robô por alguns instantes. Quando quiser salvar seu mapa, dê o comando:

	$ rosrun map_server map_saver -f ~/mymap

Isso vai salvar o mapa como dois arquivos (mymap.pgm and mymap.yaml).

Agora pode fechar o  gmapping_demo.launch.

Como um teste, você pode rodar o particle filter nativo do ros usando o mapa que acabou de salvar:

	roslaunch neato_2dnav amcl_builtin.launch map_file:=/home/SEU_LOGIN/mymap.yaml scan_topic:=stable_scan



## Testando / visualizando o filtro de partículas:


### Usando o mapa que você fez

Veja como o particle filter embutido do ROS faz:

	roslaunch neato_2dnav amcl_builtin.launch map_file:=/home/SEU_LOGIN/mymap.yaml scan_topic:=stable_scan

Para fazer o teste, defina o Fixed Frame como "map"  no RViz

Adicione visualizações para /particle_cloud e também para /map

**Você deve executar o rosbag play ou então dirigir o robô usando *teleop* **

Você pode usar o **2D Pose Estimate Widget** no RViz para definir um palpite de posição inicial do robô




### Usando o simulador

	roslaunch neato_simulator neato_playground.launch
	roslaunch neato_2dnav amcl_builtin.launch map_file:=`rospack find neato_2dnav`/maps/playground_smaller.yaml
	roslaunch turtlebot_rviz_launchers view_navigation.launch



## Rosbag

Para gerar um arquivo de testes e debugar use o ROSBAG:

	rosbag record /scan /stable_scan /odom /tf /tf_static /cmd_vel

Quando quiser gravar digite Ctrl + C. Um arquivo bag com nome baseado na data atual (por exemplo *2016-03-23-17-52-46.bag*) será criado em seu diretório de usuário (por exemplo /home/borg se você usa o Linux fornecido pelo professor)

###Para fazer playback depois:

1.Feche todos os roslaunch  e programas ROS

2.Abra o roscore para resetar o horário da simulação


	roscore
	rosparam set use_sim_time true

3.Feche o roscore depois disso


4.Configure o ROS para usar o tempo simulado vindo do arquivo BAG

	roslaunch neato_node set_urdf.launch
	rosbag play --clock your-bag-file-name-here
