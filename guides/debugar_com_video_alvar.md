# Como testar seu projeto sem um robô físico

## Da primeira vez

Mude para o diretório catkin_ws/src

	cd ~catkin_ws/src


Baixe o projeto pi_vision, que contém o ros2opencv, de que precisamos

    git clone https://github.com/hansonrobotics/pi_vision

Baixe os pacotes de que o pi_vision precisa:

    sudo apt-get install ros-indigo-cv-bridge ros-indigo-image-transport ros-indigo-mjpeg-server ros-indigo-openni-camera  ros-indigo-usb-cam ros-indigo-ar-track-alvar

Mude para o diretório catkin:

    cd ~/catkin

Compile tudo (deve levar 1 ou 2 minutos):

    catkin_make


## Para fazer o teste com um arquivo de vídeo:

### Com um arquivo de vídeo:

    roslaunch ros2opencv avi2ros.launch input:=ARQUIVO_DE_VIDEO.avi 

Atenção: **não necessariamente o vídeo precisa ser na extensão avi**. Internamente o *avi2ros* usa o método [cv.cvCaptureFromFile da OpenCV](http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html)


### Inicie o tag tracking como se fosse do Neato!

	roslaunch tag_tracking ar_track_neato.launch


### Monitore a deteção num terminal

	rostopic echo /ar_pose_marker


### Rode o robô Virtual

    roslaunch neato_simulator neato_playground.launch





#Como desenvolver sem robô - Alvar

Siga os passos a seguir para testar seus programas sem ter um robô, se você está usando marcadores Alvar

## 1. Instalar ros-indigo-ar-track-alvar
    sudo apt-get install ros-indigo-ar-track-alvar


## 2. Abrir a webcam

    roslaunch tag_tracking usb_cam

(a webcam deve acender)

## 3. Abrir rastreamento da webcam
    roslaunch tag_tracking ar_track_usb_cam

 Para que esta etapa funcione, você precisa ter um **arquivo de calibração de câmera**.

Veja [aqui mais detalhes](calibrar_camera.md) sobre como calibrar


## 4. Para ver se detectou
    rostopic echo ar_pose_marker

## 5. Para usar o robô virtual
    roslaunch neato_simulator neato_playground.launch


## Para imprimir marcadores
Lembre-se de que para gerar o arquivo de marcador para imprimir, use o comando

    rosrun ar_track_alvar createMarker
