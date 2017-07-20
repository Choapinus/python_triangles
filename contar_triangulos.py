
#inicializo mis listas
#arrayVertices=[0, 0, 0, 0, 1, 1, 1, 2, 2, 469, 469, 469, 6, 6, 385, 385, 385, 3, 3, 3, 3, 4, 4, 4, 4, 419, 419, 419, 422, 422, 422, 422, 5, 5, 98, 98, 98, 420, 420, 7, 7, 7, 7, 8, 8, 9, 9, 9, 79, 79, 79, 33, 33, 33, 10, 10, 10, 10, 84, 84, 84, 11, 11, 11, 110, 110, 110, 12, 12, 12, 12, 13, 13, 13, 13, 108, 108, 108, 108, 95, 95, 14, 14, 14, 14, 94, 94, 94, 15, 16, 16, 77, 77, 17, 17]
arrayLados=[(0, 1), (0, 2), (0, 469), (1, 0), (1, 6), (1, 385), (2, 0), (2, 3), (469, 0), (469, 380), (469, 37415), (6, 1), (6, 5), (385, 1), (385, 384), (385, 386), (3, 2), (3, 4), (3, 419), (3, 422), (4, 3), (4, 5), (4, 98), (4, 420), (419, 3), (419, 420), (419, 35698), (422, 3), (422, 183), (422, 423), (422, 37415), (5, 4), (5, 6), (5, 98), (98, 4), (98, 5), (98, 470), (98, 35729), (420, 4), (420, 419), (420, 35709), (7, 8), (7, 9), (7, 79), (8, 7), (8, 33), (9, 7), (9, 10), (9, 84), (79, 7), (79, 78), (79, 119), (33, 8), (33, 32), (33, 34), (10, 9), (10, 11), (10, 84), (10, 110), (84, 9), (84, 10), (84, 83), (84, 85), (11, 10), (11, 12), (11, 110), (110, 10), (110, 11), (110, 111), (110, 112), (12, 11), (12, 13), (12, 95), (12, 108), (13, 12), (13, 14), (13, 94), (13, 95), (108, 12), (108, 109), (108, 113), (108, 123), (95, 12), (95, 13), (95, 96), (14, 13), (14, 15), (14, 16), (14, 77), (94, 13), (94, 77), (94, 93), (15, 14), (16, 14), (16, 17), (77, 14), (77, 17), (77, 94), (17, 16), (17, 18)]
#arrayVertices = [0,1,2,3]
#arrayLados = [(0,1), (0,2), (2,1)]

arrayTriangulo=[]
arrayTrianguloCompleto =[]
posibles_lados = []
pos_lados = []
arr_lados = []
arr_ver = []
vertices = []
global_triangulos = []
cont = 0

#print "lados: ", arrayLados
#print
#print "vertices: ", arrayVertices

##parseamos los lados y los vertices para que no se repitan
"""
arr_lados = []
for i in arrayLados:
	if i not in arr_lados:
		arr_lados.append(i)
arrayLados = arr_lados
arr_lados = []
#print arrayLados

arr_ver = []
for a in arrayVertices:
	if a not in arr_ver:
		arr_ver.append(a)
arrayVertices = arr_ver
arr_ver = []
#print arrayVertices
"""


#generar todos los posibles triangulos
for i in range(len(arrayLados)):
	for j in range(len(arrayLados)):
		for k in range(len(arrayLados)):
			if(len(arrayTriangulo) < 3 and arrayLados[i] not in arrayTriangulo):
				arrayTriangulo.append(arrayLados[i])
				if(len(arrayTriangulo) < 3 and arrayLados[j] not in arrayTriangulo):
					arrayTriangulo.append(arrayLados[j])
					if(len(arrayTriangulo) < 3 and arrayLados[k] not in arrayTriangulo):
						arrayTriangulo.append(arrayLados[k])
			
			#solo si el array tiene longitud 3, trabajarlo
			if(len(arrayTriangulo) == 3):
				#print arrayTriangulo
				for lado in arrayTriangulo:
					if(lado[0] not in vertices):
						vertices.append(lado[0])
					if(lado[1] not in vertices):
						vertices.append(lado[1])
					#print "lado: ", lado

				#solo si la cantidad de vertices es 3, trabajarlo
				if(len(vertices) == 3):
					##print "triangulo: ", arrayTriangulo
					##print "vertices: ", vertices
					#generar los posibles lados
					for ver1 in vertices:
						for ver2 in vertices:
							posibles_lados.append((ver1, ver2))

					if({arrayTriangulo[0]}.issubset(arrayLados) and {arrayTriangulo[1]}.issubset(arrayLados) and {arrayTriangulo[2]}.issubset(arrayLados)):
						if(not arrayTriangulo[0][::-1] in arrayTriangulo and not arrayTriangulo[1][::-1] in arrayTriangulo and not arrayTriangulo[2][::-1] in arrayTriangulo):
							cont += 1
							global_triangulos.append(arrayTriangulo)

					#resetear los posibles lados
					posibles_lados = []
					pos_lados = []
				#se deben limpiar los vertices despues de que sean 3
				vertices = []
			arrayTriangulo = []

print "triangulos contados: ", cont
if(raw_input('Desea imprimir los {} triangulos? [y/n]: '.format(cont)) == "y"):
	print "triangulos: ", global_triangulos
else:
	print "bye!"


"""
importante tener en cuenta que se tuvo en consideracion que, 

- el triangulo [(0,1),(0,2),(2,1)] no es el mismo que [(0,1),(2,1),(0,2)]

- los triangulos son unidireccionales.

- para verificar que el vertice no estuviera repetido, 
  aplicamos la funcion de invertir el lado para compararlo con sus vecinos (linea 72)

- los lados se consideran una lista de tuplas -> [(0,1), (1,2), (2,0)]

- los triangulos se consideran como una lista de listas de tuplas
"""