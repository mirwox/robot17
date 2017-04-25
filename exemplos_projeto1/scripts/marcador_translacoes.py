#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = ["Rachel P. B. Moraes", "Fabio Miranda"]

import rospy
import numpy
from numpy import linalg
import transformations
from tf import TransformerROS
import tf2_ros
import math
from geometry_msgs.msg import Twist, Vector3, Pose, Vector3Stamped
from ar_track_alvar_msgs.msg import AlvarMarker, AlvarMarkers
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Image
from std_msgs.msg import Header

x = 0
y = 0
z = 0 
id = 0

<<<<<<< HEAD
=======
frame = "camera_frame"
# frame = "head_camera"  # DESCOMENTE para usar com webcam USB via roslaunch tag_tracking usbcam
>>>>>>> f0c2da0c9dd6280985c4b4be6e0471c8a2e169ae

tfl = 0

tf_buffer = tf2_ros.Buffer()

def recebe(msg):
	global x # O global impede a recriacao de uma variavel local, para podermos usar o x global ja'  declarado
	global y
	global z
	global id
	for marker in msg.markers:
		id = marker.id
		marcador = "ar_marker_" + str(id)

<<<<<<< HEAD
		print(tf_buffer.can_transform("head_camera", marcador, rospy.Time(0)))
=======
		print(tf_buffer.can_transform(frame, marcador, rospy.Time(0)))
>>>>>>> f0c2da0c9dd6280985c4b4be6e0471c8a2e169ae
		header = Header(frame_id=marcador)
		# Procura a transformacao em sistema de coordenadas entre a base do robo e o marcador numero 100
		# Note que para seu projeto 1 voce nao vai precisar de nada que tem abaixo, a 
		# Nao ser que queira levar angulos em conta
<<<<<<< HEAD
		trans = tf_buffer.lookup_transform("head_camera", marcador, rospy.Time(0))
=======
		trans = tf_buffer.lookup_transform(frame, marcador, rospy.Time(0))
>>>>>>> f0c2da0c9dd6280985c4b4be6e0471c8a2e169ae
		
		# Separa as translacoes das rotacoes
		x = trans.transform.translation.x
		y = trans.transform.translation.y
		z = trans.transform.translation.z
		# ATENCAO: tudo o que vem a seguir e'  so para calcular um angulo
		# Para medirmos o angulo entre marcador e robo vamos projetar o eixo Z do marcador (perpendicular) 
		# no eixo X do robo (que e'  a direcao para a frente)
		t = transformations.translation_matrix([x, y, z])
		# Encontra as rotacoes e cria uma matriz de rotacao a partir dos quaternions
		r = transformations.quaternion_matrix([trans.transform.rotation.x, trans.transform.rotation.y, trans.transform.rotation.z, trans.transform.rotation.w])
		m = numpy.dot(r,t) # Criamos a matriz composta por translacoes e rotacoes
		z_marker = [0,0,1,0] # Sao 4 coordenadas porque e'  um vetor em coordenadas homogeneas
		v2 = numpy.dot(m, z_marker)
		v2_n = v2[0:-1] # Descartamos a ultima posicao
		n2 = v2_n/linalg.norm(v2_n) # Normalizamos o vetor
		x_robo = [1,0,0]
		cosa = numpy.dot(n2, x_robo) # Projecao do vetor normal ao marcador no x do robo
		angulo_marcador_robo = math.degrees(math.acos(cosa))

		# Terminamos
		print("id: {} x {} y {} z {} angulo {} ".format(id, x,y,z, angulo_marcador_robo))


if __name__=="__main__":

<<<<<<< HEAD
=======
	print("Coordenadas configuradas para usar Neato, para usar webcam USB altere no código fonte a variável frame")
>>>>>>> f0c2da0c9dd6280985c4b4be6e0471c8a2e169ae

	rospy.init_node("marcador") # Como nosso programa declara  seu nome para o sistema ROS

	recebedor = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, recebe) # Para recebermos notificacoes de que marcadores foram vistos
	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 1) # Para podermos controlar o robo

	tfl = tf2_ros.TransformListener(tf_buffer) # Para fazer conversao de sistemas de coordenadas - usado para calcular angulo


	try:
		# Loop principal - todo programa ROS deve ter um
		while not rospy.is_shutdown():
				# Coloque aqui o que quiser
			rospy.sleep(0.05)

	except rospy.ROSInterruptException:
	    print("Ocorreu uma exceção com o rospy")


