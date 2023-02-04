import pyqrcode # Not the same as qrcode
import random

class Challenge:

	def __init__(self):
		"""This funtion runs the generate function as soon as the Challenge object
		 is initialized"""
		
	
	def generate(self):
		"""This function generates a challenge QRcode for the Ntu secure login
		system"""
		self.s0 = "abcdefghijkllmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[];',./`\~!@#$%^&*()_+{}:<>?"
		self.s1 = "abcdefghijkllmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
		
		self.data = ""
		self.name = ""
		
		self.r0 = random.randint(8,16)
		self.r1 = random.randint(4,8)
		#print(self.r0, self.r1) #For Debugging
		
		self.counter0 = 0
		self.counter1 = 0
		
		while self.counter0 < self.r0:
			x = random.randint(0,len(self.s0)-1)
			self.data = self.data + self.s0[x]
			self.counter0+=1
		
		#print(self.data) #For Debugging
		
		while self.counter1 < self.r1:
			y = random.randint(0,len(self.s1)-1)
			self.name = self.name + self.s1[y]
			self.counter1+=1
		
		#print(self.name) #For Debugging
		
		qr = pyqrcode.create(self.data)
		qr.png("muntu/static/muntu/image/%s.png" % (self.name), scale=10)
		return self.name

