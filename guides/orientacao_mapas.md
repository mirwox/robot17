# Como rodar o Turtlebot STDR

## Onde estão os mapas

/opt/ros/kinetic/share/turtlebot_stdr/maps/hospital_section.yaml
/opt/ros/kinetic/share/turtlebot_stdr/maps/hospital_section.png

## Como exportar a variável de mapa
export TURTLEBOT_MAP_FILE=/opt/ros/kinetic/share/turtlebot_stdr/maps/hospital_section.yaml


# Conserto do TurtleBot in STDR

Mude para o diretório do TurtleBot in STDR

    roscd turtlebot_stdr

    cd launch

Edite o arquivo turtlebot_in_stdr.launch

    sudo subl turtlebot_in_stdr

Mude a linha:

    <include file="$(find turtlebot_navigation)/launch/includes/amcl.launch.xml">


Para

    <include file="$(find turtlebot_navigation)/launch/includes/amcl/amcl.launch.xml">
