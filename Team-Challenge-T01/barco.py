class Barco:
	def __init__(self, descripcion, eslora):
		self.descripcion = descripcion
		self.eslora = eslora

		# Lista de aciertos recibidos
		self.aciertos = {}

		# Ubicación
		self.coordenadas = []

		self.cant_aciertos = 0
		self.esta_hundido = False
		self.esta_tocado = False


	def establecer_ubicacion(self, coordenadas, orientacion):
		if len(coordenadas) != self.eslora:
			raise ValueError("Las coordenadas no coinciden con la eslora del barco.")

		self.coordenadas = coordenadas
		self.orientacion = orientacion


	def posicionar(self, punto_inicial, orientacion):
		"""
		Función para posicionar el barco en el tablero dando un punto inicial
		y una orientación.

		Args:
			- punto_inicial (xi, yi)
			- orientación (N, S, E, O)
		esta_posicionado = True
		"""
		pass

	def esta_posicionado(self):
		"""
		Está posicionado el barco? Si nuestro listado de ubicaciónes no tiene
		datos entonces el barco no está posicionado
		"""
		return len(self.coordenadas) != 0

	def danar(self, posicion):
		"""
		Funcion para dañar el barco
		"""

		self.cant_aciertos += 1

	def esta_tocado(self):
		"""
		Función para saber si el barco esta tocado
		"""
		return self.cant_aciertos > 0

	def esta_hundido(self):
		"""
		Función para saber si el barco esta hundido
		"""
		return self.cant_aciertos == self.eslora

	def mostrar(self):
		print(f"{self.descripcion.upper()} ({self.eslora})") 
		esta_posicionado = self.esta_posicionado()
		print(f"¿Barco posicionado? {esta_posicionado}")
		if esta_posicionado:
			print(f"\tORIENTACIÓN: {self.orientacion}") 
			print(f"\tCOORDENADAS: {self.coordenadas}")