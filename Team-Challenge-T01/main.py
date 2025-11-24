import constants as const
import funciones as utils
import os

from barco import Barco
from tablero import Tablero


utils.clear_console()
print(const.LOGO)

is_valid = False
while not is_valid:
	user = input("Ingrese su nombre de usuario: ")
	if user.strip() != "":
		is_valid = True

barcos = const.BARCOS

print("\n")
player = Tablero(user, const.TABLERO_DIMENSION, barcos)
print("\n")
player.posicionar_barcos()
print("\n")
print("\n")
opponent = Tablero("IA", const.TABLERO_DIMENSION, barcos)
print("\n")
opponent.posicionar_barcos()
print("\n")

# player.mostrar_tablero_barcos()
# opponent.mostrar_tablero_barcos()

print("\n")
print("PARTIDA INICIADA")
print("="*80)

juego_finalizado = False
while not juego_finalizado:
	juego_finalizado = utils.establecer_turno(player, opponent, False)
	if juego_finalizado:
		print("\nESCUADRA DE BATALLA")
		player.mostrar_tablero_barcos()
		print("\nHISTORIAL DE DISPAROS")
		player.mostrar_tablero_referencia()
		break

	juego_finalizado = utils.establecer_turno(opponent, player, True)
	if juego_finalizado:
		print("\nESCUADRA DE BATALLA")
		opponent.mostrar_tablero_barcos()
		print("\nHISTORIAL DE DISPAROS")
		opponent.mostrar_tablero_referencia()
		break
