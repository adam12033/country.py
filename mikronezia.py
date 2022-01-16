#Délczeg ÁDÁM
#2022-01-10
#Ifra I N


from country import Country     #1.

class Mikronezia:
	def __init__(self):
		self.countries = []
		self.sep = ':'  #24
	def read_content(self):
		file_name = 'countries.txt'  #3.
		fp = open(file_name, 'r', encoding='utf-8')
		self.lines = fp.readlines()
		fp.close()

	def convert_content(self):
		for line in self.lines[1::]:            
			(id, name, area, population) = line.split('#')
			country = Country(id, name, int(area), int(population))
			self.countries.append(country)

	# Legnépesebb ország #15.
	def most_populated(self):
		max_country = self.countries[0]
		for country in self.countries:
			if country.population > max_country.population:
				max_country = country
		print("Legnépesebb ország", max_country.name, max_country.population) 


	# Legkisebb területű ország #16.
	def smallest_area(self):
		min_country = self.countries[0]
		for country in self.countries:
			if country.area < min_country.area:
				min_country = country
		print("Legkisebb területű ország:", min_country.id, min_country.name, min_country.area, min_country.population)
		

	# 99 ezernél kisebb népesség #17.
	def less_than_ninety_nine_thousand(self):
		for country in self.countries:
			if country.population < 99000:
				print("99 ezernél kisebb népesség: ", country.name, country.population)
		

	# Hány 500 négyeztkilométernél nagyobb területi ország van? #18.
	def more_than_five_hunderd_area(self):
		count = 0
		for country in self.countries:
			if country.area > 500:
				count += 1
		print("500 négyeztkilométernél nagyobb területi ország: ", count )

	# Hány ország nevében szerepel a "sziget" szó? #19.
	def island_word_in_name(self):
		count = 0
		for country in self.countries:
			if country.name.find("sziget") != -1:
				count += 1
		print("A sziget szó ennyi ország nevében van: ", count)
		
		
		
	# Az országok területe összesen #20.
	def sum_areas(self):
		osszeg = 0
		for country in self.countries:
			osszeg += country.area
		print('Az országok területe összesen: ', osszeg)
		
	# Az országok népességének átlaga #21.
	def population_average(self):
		osszeg = 0
		darab = 0
		for country in self.countries:
			darab += 1
			osszeg += country.population
		atlag = osszeg / darab
		print("A népesség átlaga: %.2f" % atlag) #2-tizedes jegyre kiiras		
		

	# Állapítsuk meg, hogy egyszavas, vagy nem, a név #22.
	def is_one_word(self, country):
		res = country.name.find('-')
		if res == -1:
			return True
		else:
			return False
			

	def write_a_country(self, fp, country):
		fp.write(country.id)
		fp.write(self.sep)
		fp.write(country.name)
		fp.write(self.sep)
		fp.write(str(country.area))
		fp.write(self.sep)
		fp.write(str(country.population))
		fp.write('\n')


	def write_one_word(self):
		fp = open('oneword.txt', 'w', encoding='utf-8') #23.
		for country in self.countries:
			if self.is_one_word(country):
				self.write_a_country(fp, country)
		fp.close()


mikro = Mikronezia() 
mikro.read_content() 
mikro.convert_content()
mikro.most_populated()
mikro.smallest_area()
mikro.less_than_ninety_nine_thousand()   #4-14
mikro.more_than_five_hunderd_area() 
mikro.island_word_in_name()
mikro.sum_areas()
mikro.population_average()
mikro.write_one_word()


