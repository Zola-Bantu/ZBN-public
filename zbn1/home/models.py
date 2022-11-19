from django.db import models;

RELATIONSHIP_STATUS_CHOICES = (
    ('SI', 'single'),
    ('IR', 'in committed relationship'),
    ('MA', 'married'),
    ('SP', 'separated'),
    ('DV', 'divorced'),
    ('WI', 'widowed')
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


#Profile table

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


