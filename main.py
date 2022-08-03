#exercise 1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

list(filter(lambda city: city[2:] , places))

#exercise 2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

(list(map(lambda name: name.split()[-1], author)))

#exercise 3
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
list(map(lambda place: place[1]*1.8 + 32, places))