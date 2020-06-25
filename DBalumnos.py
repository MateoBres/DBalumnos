
import sqlite3

migrar = True

while migrar:
	#alumnos.txt es el file que contiene los alumnos
	nombre_archivo = input('Ingrese el nombre del archivo txt para migrar: ')
	try:
		texto = open(nombre_archivo, 'r')
	except FileNotFoundError:
		print('El archivo no existe!')
	else:
		nombre_db = input('Ingrese el nombre de la base de datos .db: ')
		conn = sqlite3.connect(nombre_db)
		cursor = conn.cursor()
		try:
			cursor.execute("CREATE TABLE alumnos(nombre TXT, cursos INT, curso_actual TXT);")
		except sqlite3.OperationalError:
			pass
		finally:
			alumnos = texto.readlines()
			alumnos_db = []
			for i in range(0, len(alumnos)-1):
				alumnos[i] = alumnos[i][0:-1]
			for alumno in alumnos:
				alumno = alumno.split(',')
				alumno = [alumno[0] , int(alumno[1]), alumno[2]]
				alumnos_db.append(alumno)
			for i in range(0, len(alumnos_db)):
				cursor.execute("INSERT INTO alumnos VALUES (?, ?, ?);", alumnos_db[i])
				#cursor.execute('INSERT INTO alumnos VALUES (' + "'" + str(alumnos_db[i][0]) + "', " + str(alumnos_db[i][1]) + ", '" + str(alumnos_db[i][2]) + "'" + ');')
			conn.commit()		
				
			migrar = False



conn.close()
texto.close()
