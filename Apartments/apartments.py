import json
all = []
class apartments:
	def __init__(self, name, rating, address, phone, price, sqrft):
		self.name = name
		self.rate = rating 
		self.address = address 
		self.phone = phone 
		self.price = price
		self.sqrft = sqrft
		all.append(self)

	def all_info(self):
		print("{}\n{}\n{}\n{}\n{}\n{}\n".format(self.name, self.address, self.phone, self.price, self.sqrft, self.rate))

	def save(self):
		file = open("./saved/" + self.name, "w")
		file.write(json.dumps(self, default=jdefault, indent=4))
		file.close()

	@classmethod
	def from_json(cls, file):
		with open(file) as json_file:
			data = json.load(json_file)
			return cls(data['name'], data['rate'], data['address'], data['phone'], data['price'], data['sqrft'])

def	jdefault(o):
	return o.__dict__

