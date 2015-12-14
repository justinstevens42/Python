class Band:
	def __init__(self, name, year, albums, album):
		self.name=name
		self.year=year
		self.albums=albums
		self.album=album
	def print_albums(self):
		print("The name of the band is ", self.name) 
		print("The year the band originated is ", self.year)
		print("The number of albums the band has is ", self.albums)
		print("The list of albums the band has is ", self.album)
p=["Vintalogy", "Versus", "Ten", "Blah", "Blah", "Greatest Hits: Tim Mcgraw"]
f=["Torches", "ugh"]
pearl=Band("Pearl Jam", 1991, 6, p)
foster=Band("Foster the People", 2010, 2, f)

pearl.print_albums()
foster.print_albums()
