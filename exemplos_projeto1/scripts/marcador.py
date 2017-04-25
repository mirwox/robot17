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
from neato_node.msg import Bump # BUMP
from sensor_msgs.msg import LaserScan#BUMP

x = 0
y = 0
z = 0 
ls = 0
rs = 0
lf = 0
rf = 0
volte = False
right = False
left = False
espera = 0

id = 0

tfl = 0
tf_buffer = tf2_ros.Buffer()
#fbuffer = tf2_ros.Buffer()


x_desejado = 0.12
y_desejado = 0.10
z_desejado = 0.50

#***********BUMP***********
def bateu(dado):
	print('OLAaaa')
	print("{} {} {} {}".format(dado.leftSide, dado.leftFront, dado.rightFront, dado.rightSide))
	global ls, rs, lf, rf, volte, right, left

	ls = dado.leftSide
	rs = dado.rightSide
	lf = dado.leftFront
	rf = dado.rightFront

	if lf == 1 or rf == 1:
		volte = True
		
	elif rs == 1:
		left = True

	elif ls == 1:
	 	right = True


def recebe(msg):
	global x # O global impede a recriacao de uma variavel local, para podermos usar o x global ja'  declarado
	global y
	global z
	global id
<<<<<<< HEAD
	global tfl
	global tf_buffer
	global buffer


	#frame = "head_camera" # Quando for rodar no simulador com webcam
	frame = "camera_frame" # Quando for rodar no robo

	try:
		for marker in msg.markers:
			id = marker.id
			marcador = "ar_marker_" + str(id)

			print(tf_buffer.can_transform(frame, marcador, rospy.Time(0)))
			header = Header(frame_id=marcador)
			# Procura a transformacao em sistema de coordenadas entre a base do robo e o marcador numero 100
			# Note que para seu projeto 1 voce nao vai precisar de nada que tem abaixo, a 
			# Nao ser que queira levar angulos em conta
			trans = tf_buffer.lookup_transform(frame, marcador, rospy.Time(0))
			
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
	except Exception as e:
		print(e.stacktrace())


if __name__=="__main__":
#	global tfl 
#	global buffer
	global velocidade_saida
	rospy.init_node("marcador") # Como nosso programa declara  seu nome para o sistema ROS

	recebedor = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, recebe) # Para recebermos notificacoes de que marcadores foram vistos
	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3) # Para podermos controlar o robo
	recebedor_bump = rospy.Subscriber("/bump", Bump, bateu, queue_size = 3)

	tfl = tf2_ros.TransformListener(tf_buffer) # Para fazer conversao de sistemas de coordenadas - usado para calcular angulo
	
	default_sleep = 0.015

	try:
		# Loop principal - todo programa ROS deve ter um
		while not rospy.is_shutdown():
			print("Oeee")
			velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)



			if volte == False and right == False and left == False:
				print("marcador", espera)
				rospy.sleep(default_sleep)

				if id == 100:
					espera = 0
					print ("z: ",z)
					print ("z desejado: ",z_desejado)
					if z_desejado < z-0.3 and x-0.3 <= x_desejado and x_desejado >= x+0.3:
						print("X CERTO")
					 	print("Vá para frente")
					 	vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
					 	velocidade_saida.publish(vel)
					 	id = 0
					 	x = 0
					 	z = 0
					 	rospy.sleep(default_sleep)
					 	print("										ID VOLTA A 0, id = ")

					elif z-0.3 <= z_desejado and z_desejado <= z+0.3 and x-0.3 <= x_desejado and x_desejado >= x+0.3:
			 	 		print("Z CERTO")
			 	 		print("X CERTO")
			 	 		vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
			 	 		velocidade_saida.publish(vel)
					 	id = 0
					 	x = 0
					 	z = 0
			 	 		rospy.sleep(default_sleep)
			 	 		print("										ID VOLTA A 0, id = ")

			 	 	elif x_desejado < x-0.3:
						print("Vá para direita")
						vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0.2))
						velocidade_saida.publish(vel)
					 	id = 0
					 	x = 0
					 	z = 0
						rospy.sleep(default_sleep)
						print("										ID VOLTA A 0, id = ")


					elif x_desejado > x+0.3:
						print("Vá para esquerda")
						vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, -0.2))
						velocidade_saida.publish(vel)
					 	id = 0
					 	x = 0
					 	z = 0
						rospy.sleep(default_sleep)
						print("										ID VOLTA A 0, id = ")


					elif z_desejado > z + 0.3:
					 	print("Vá para trás")
					 	vel = Twist(Vector3(-0.5, 0, 0), Vector3(0, 0, 0))
				 		velocidade_saida.publish(vel)
					 	id = 0
					 	x = 0
					 	z = 0
			 	 		rospy.sleep(default_sleep)
			 	 		print("										ID VOLTA A 0, id = ")

			 	 	else:
			 	 		print("Nao sei o que fazer mas pra estou vendo o marcador")
			 	 		vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
					 	velocidade_saida.publish(vel)
					 	id = 0
					 	x = 0
					 	z = 0
					 	rospy.sleep(default_sleep)
					 	print("										ID VOLTA A 0, id = ")
			 	 		
				 	

					print("Estou na área A!")
					print ("x: ",x)
					print ("x desejado: ",x_desejado)


				else:
					if espera < 100:
						print("Não encontrei o marcador 100: esperando", espera)
						vel = Twist(Vector3(0,0,0), Vector3(0,0,0))
						velocidade_saida.publish(vel)
						x = 0
						z = 0
						espera += 1
						rospy.sleep(default_sleep)
=======
	for marker in msg.markers:
		x = round(marker.pose.pose.position.x, 2) # para arredondar casas decimais e impressao ficar ok
		y = round(marker.pose.pose.position.y, 2)
		z = round(marker.pose.pose.position.z, 2)
		#print(x)
		id = marker.id
		#print(marker.pose.pose)
		if id == 100:
			print(buffer.can_transform("base_link", "ar_marker_100", rospy.Time(0)))
			header = Header(frame_id= "ar_marker_100")
			# Procura a transformacao em sistema de coordenadas entre a base do robo e o marcador numero 100
			# Note que para seu projeto 1 voce nao vai precisar de nada que tem abaixo, a 
			# Nao ser que queira levar angulos em conta
			trans = buffer.lookup_transform("base_link", "ar_marker_100", rospy.Time(0))
			# Separa as translacoes das rotacoes
			t = transformations.translation_matrix([trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z])
			# Encontra as rotacoes
			r = transformations.quaternion_matrix([trans.transform.rotation.x, trans.transform.rotation.y, trans.transform.rotation.z, trans.transform.rotation.w])
			m = numpy.dot(r,t)
			v2 = numpy.dot(m,[0,0,1,0])
			v2_n = v2[0:-1]
			n2 = v2_n/linalg.norm(v2_n)
			cosa = numpy.dot(n2,[1,0,0])
			angulo_marcador_robo = math.degrees(math.acos(cosa))
			print("Angulo entre marcador e robo", angulo_marcador_robo)


if __name__=="__main__":
	global tfl 
	global buffer

	rospy.init_node("marcador") # Como nosso programa declara  seu nome para o sistema ROS

	recebedor = rospy.Subscriber("/ar_pose_marker", AlvarMarkers, recebe) # Para recebermos notificacoes de que marcadores foram vistos
	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 1) # Para podermos controlar o robo

	tfl = tf2_ros.TransformListener(buffer) # Para fazer conversao de sistemas de coordenadas - usado para calcular angulo


	try:
		# Loop principal - todo programa ROS deve ter um
		while not rospy.is_shutdown():
			if id == 100:
				if
				print ("z: ",z)
				print ("z desejado: ",z_desejado)
				if z_desejado < z-0.5:
				 	print("Vá para frente")
				 	vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
				 	velocidade_saida.publish(vel)
				 	rospy.sleep(0.05)

				elif z-0.5 <= z_desejado or z_desejado >= z+0.5:
		 	 		print("Z CERTO")
		 	 		vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
		 	 		velocidade_saida.publish(vel)
				 	rospy.sleep(0.05)

				 else:
				 	print("Vá para trás")
				 	vel = Twist(Vector3(-0.5, 0, 0), Vector3(0, 0, 0))
			 		velocidade_saida.publish(vel)
				 	rospy.sleep(0.05)

			else:
				print("Não encontrei o marcador 100")
				vel = Twist(Vector3(0,0,0), Vector3(0,0,0))
				velocidade_saida.publish(vel)
			rospy.sleep(0.05)
>>>>>>> f0c2da0c9dd6280985c4b4be6e0471c8a2e169ae

					else:
						print("Não encontrei o marcador 100: PROCURANDO", espera)
						vel = Twist(Vector3(0,0,0), Vector3(0,0,0.2))
						velocidade_saida.publish(vel)
						x = 0
						z = 0
						espera += 1
						rospy.sleep (default_sleep)


			elif volte == True:
				espera = 0
				print("Vá para trás")
	 	 		vel = Twist(Vector3(-1, 0, 0), Vector3(0, 0, 0))
 		 		velocidade_saida.publish(vel)


 		 		volte = False
 		 		rospy.sleep(0.4)
 		 		vel = Twist(Vector3(0,0,0),Vector3(0,0,0))
	 	 		velocidade_saida.publish(vel)
	 	 		rospy.sleep(default_sleep)

	 	 	elif left == True:
	 	 		espera = 0
	 	 		print("Vá para direita")
				vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0.5))
				velocidade_saida.publish(vel)
				rospy.sleep(0.4)
				vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
	 			velocidade_saida.publish(vel)
	 			rospy.sleep(0.4)
				left = False
				vel = Twist(Vector3(0,0,0),Vector3(0,0,0))
	 	 		velocidade_saida.publish(vel)
	 	 		rospy.sleep(default_sleep)

			elif right == True:
				espera = 0
				print("Vá para esquerda")
				vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, -0.5))
				velocidade_saida.publish(vel)
				rospy.sleep(0.4)
				vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
	 			velocidade_saida.publish(vel)
	 			rospy.sleep(0.4)
				right = False
				vel = Twist(Vector3(0,0,0),Vector3(0,0,0))
	 	 		velocidade_saida.publish(vel)
	 	 		rospy.sleep(default_sleep)

	
			rospy.sleep(default_sleep)

	except rospy.ROSInterruptException:
		print("Ocorreu uma exceção com o rospy")