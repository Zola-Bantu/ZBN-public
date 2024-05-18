import requests
#import pyqrcode # Not the same as qrcode
import random

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(",")[0]
	else:
		ip = request.META.get('REMOTE_ADDR', None)
	return ip



def get_info(ip):
	"""This function fetches the extra data related to the users IP address from
	http://ip-api.com/json/ and returns it"""

	url = 'http://ip-api.com/json/'
	reply = requests.get(url+str(ip)).json()

	status = reply['status']
	try:
		if status == 'success':
			country = reply['country']
			country_code = reply['countryCode']
			region_code = reply['region']
			region = reply['regionName']
			town = reply['city']
			zip_code = reply['zip']
			lat = reply['lat']
			lon = reply['lon']
			timezone = reply['timezone']
			isp = reply['isp']
			organization = reply['org']
			az = reply['as']
			query = reply['query']
			return status, country, country_code, region_code, region, town, zip_code, lat, lon, timezone, isp, organization, az, query

		else:
			return status, '',  '', '', '', '', '', -26.3811, 27.8376,  '', '', '', '', ''
	except Exception as e:
		print(e)
		return status, '',  '', '', '', '', '', -26.3811, 27.8376,  '', '', '', '', ''




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
		#self.r1 = random.randint(9,17)
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

		#qr = pyqrcode.create(self.data)
		#qr.png("entrance/static/entrance/image/%s.png" % (self.name), scale=10)
		return self.name, self.data



