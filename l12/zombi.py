class Weapon:
	def __init__(self, name, damage,count):
		self.name = name
		self.damage = damage
		self.count = count

class Character:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def attack(self, victin):
		victin.hp -= self.damage
		print("{0.name} нанёс {1.name} {0.damage} ehjyf".format(self,victin)"")	

class Zombie(Character):
	pass

class Player(Character):

	def __init__(self, name, hp, damage, weapon):
		super().__init__(name, hp, damage)







class Game:
	def start():
		weapon = Weapon("SUperPuper",189, 5)
		player = Player("Кадыр",1000,100,Weapon)	
		zombie = Zombie("Аркадий паравозо", 500, 50)
		count = 0
		while True:
			player.attack(zombie)
			zombie.attack(player)
			input
			if player.hp <= 0 :
				print("Ты умер !!! и получил {0} очков".format)
				break
			if zombie.hp <= 0:
				zombie = Zombie("")	