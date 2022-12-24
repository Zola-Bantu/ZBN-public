from django.db import models;

RELATIONSHIP_STATUS_CHOICES = (
    ('SI', 'single'),
    ('IR', 'in committed relationship'),
    ('MA', 'married'),
    ('SP', 'separated'),
    ('DV', 'divorced'),
    ('WI', 'widowed')
    );
    
MESSAGE_CHOICES = (
    ('TE', 'text'),
    ('VN', 'voice note'),
    ('IM', 'image'),
    ('VI', 'video'),
    );
    
# Users table

class Mosebedisi(models.Model):
    username = models.CharField(max_length=50	# Maximum number of characters allowed for username.
    				,blank=True, null=True      # Allows username to be left blank.
    				);
    pkn = models.CharField(max_length=150, default='0');	    # Public key n.
    pke = models.CharField(max_length=50, default='0');	    # Public key e.
	
    def __str__(self):
        return "%s" % (self.username);


#Profile table (one-to-one)

class Profile(models.Model):
    mosebedisi = models.OneToOneField(
        Mosebedisi,
        on_delete=models.CASCADE,
        primary_key=True,
        );
    picture = models.FileField();
    female = models.BooleanField(default=True);
    Status = models.CharField(
        max_length=2,
        choices=RELATIONSHIP_STATUS_CHOICES, 
        default='SI'
        );
    bio =  models.CharField(max_length=300, blank=True, null=True);
	
    def __str__(self):
        return "%s" % (self.female);

# Message table (one-to-many).
class Message(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE);
	message = models.FileField();
	msg_type= models.CharField(
        max_length=2,
        choices=MESSAGE_CHOICES, 
        default='TE'
        );
	signature = models.FileField();
	pkn = models.CharField(max_length=150, default='0');	    # Public key n.
	pke = models.CharField(max_length=50, default='0');	    # Public key e.
	
	def __str__(self):
		return "%s" % (self.msg_type);

# Group Table (not a relational table).
class Group(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True);
	image= models.FileField(blank=True, null=True);
	story= models.CharField(max_length=1000, blank=True, null=True);
	
	def __str__(self):
		return "%s" % (self.name);

# Group member table (many-to-many).
class Member(models.Model):
	group = models.ManyToManyField(Group);
	mosebedisi = models.ManyToManyField(Mosebedisi);
	admin = models.BooleanField(default=True);
	
	def __str__(self):
		return "%s" % (self.admin);
