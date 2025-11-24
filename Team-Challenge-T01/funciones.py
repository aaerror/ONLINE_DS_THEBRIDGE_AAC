import constants as const

import numpy as np
import os


def clear_console(): # {{{
	os.system("cls" if os.name == "nt" else "clear")
# }}}

def mostrar_menu(): # {{{
	opcion = 0
	while (opcion < 1) or (opcion > 3):
		print("Seleccionar una opción del menú")
		print("1) Realizar disparo")
		print("2) Ver posicionamiento de barcos propios")
		print("3) Ver disparos realizados")
		print("-"*80)
		opcion = int(input("OPCIÓN:"))
		if (opcion < 1) or (opcion > 3):
			print("-"*80)
			print("Opción incorrecta. Intente nuevamente\n")

	return opcion
# }}}

def crear_coordenadas_automaticas(): # {{{
	"""
	Función para generar coordenadas x e y de forma automática

	Return:
		(x,y): tupla de coordenadas x e y
	"""
	# print("Generando coordenadas automáticas...")

	return (
		np.random.randint(0, const.TABLERO_DIMENSION),
		np.random.randint(0, const.TABLERO_DIMENSION)
	)
# }}}

def posicionar_disparo(disparo_automatico=False): # {{{
	"""
	Función que permite posicionar el disparo (elegir coordenadas de disparo)
	o realizar disparo automático.

	Args:
		disparo_automatico: opcion para configurar disparo automático o manual

	Return:
		(x, y): coordenadas de disparo
	"""
	print("\nPreparando disparo")
	print("-"*80)

	if disparo_automatico:
		return crear_coordenadas_automaticas()
	else:
		x = int(input("Ingresar la coordenada x a la que desea disparar: "))
		y = int(input("Ingresar la coordenada y a la que desea disparar: "))

		return (x, y)
# }}}

def juego_finalizado(player, cantidad_aciertos): # {{{
	if cantidad_aciertos == const.ACIERTOS:
		msg = f"""
╔════════════════════════════════════════════════════════╗
║                                                        ║
║  ██╗  ██╗ █████╗ ███████╗                              ║
║  ██║  ██║██╔══██╗██╔════╝                              ║
║  ███████║███████║███████╗                              ║
║  ██╔══██║██╔══██║╚════██║                              ║
║  ██║  ██║██║  ██║███████║                              ║
║  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                              ║
║                                                        ║
║   ██████╗  █████╗ ███╗   ██╗ █████╗ ██████╗  ██████╗   ║
║  ██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗  ║
║  ██║  ███╗███████║██╔██╗ ██║███████║██║  ██║██║   ██║  ║
║  ██║   ██║██╔══██║██║╚██╗██║██╔══██║██║  ██║██║   ██║  ║
║  ╚██████╔╝██║  ██║██║ ╚████║██║  ██║██████╔╝╚██████╔╝  ║
║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝  ╚═════╝   ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
			"""
		print(f"¡Juego finalizado!\nFelicitaciones {player.upper()}", msg)
		return True

	return False
# }}}

def mecanica_turno(player, contrincante, disparo_automatico=False): # {{{
	es_disparo_valido = False
	while not es_disparo_valido:
		coordenadas = posicionar_disparo(disparo_automatico)

		es_disparo_valido = player.disparar(coordenadas)
		if es_disparo_valido:
			print("Esperando reporte enemigo...\n")
			es_acierto = contrincante.dibujar_disparo_enemigo(coordenadas)
			player.dibujar_disparo_propio(coordenadas, es_acierto)
		else:
			print("\nIntente realizar nuevamente un disparo 🙃")

	return es_acierto
# }}}

def establecer_turno(player, contrincante, disparo_automatico=False): # {{{
	"""
	Función para crear turno de usuario

	Args:
		- player: tablero del jugador al que le corresponde el turno
		- disparo_automatico: permite la generación automática de coordenadas
	"""

	clear_console()
	print("="*80)
	print(f"Turno de {player.descripcion}".upper())
	print("="*80)

	hay_ganador = False
	turno_finalizado = False
	while not turno_finalizado:
		seleccion = mostrar_menu()
		# seleccion = 1
		if seleccion == 1:
			es_acierto = mecanica_turno(player,
										contrincante,
										disparo_automatico)

			if not es_acierto:
				turno_finalizado = True
			else:
				hay_ganador = juego_finalizado(player.descripcion,
											   player.aciertos)
				turno_finalizado = hay_ganador

		if seleccion == 2:
			print("\nESCUADRA DE BATALLA")
			print("="*80)
			player.mostrar_tablero_barcos()

		if seleccion == 3:
			print("\nHISTORIAL DE DISPAROS")
			print("="*80)
			player.mostrar_tablero_referencia()

	print("\nTURNO FINALIZADO")
	print("-"*80)
	print(f"Reporte del turno:\n\tAciertos: {player.aciertos}\n")

	return hay_ganador
# }}}
