jours = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a = -1
while a<24:
	a = a + 1
	b = a % 7
	print(jours[b], a + 1, 'décembre')