import datetime;
from django.db import models;
from django.db.models.signals import post_save, pre_save;
from django.dispatch import receiver;
from django.core.mail import send_mail;
from django.conf import settings;

# Create your models here.

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
    pkn = models.TextField(blank=True, null=True);	# Public key n.
    pke = models.CharField(max_length=50, default='0');
    address = models.CharField(max_length=100, default='0');		 # Public key e.

    def __str__(self):
        return "%s" % (self.username);

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	"""
	This is a signal sent by email to signal the successful creation of a new user.
	"""
	mosebedisi = instance;
	if created:
		prof = Profile.objects.create(
		mosebedisi=mosebedi0si
		);

		email = "jhamauhuru@gmail.com";
		subject = "User created!";
		message = "Please note that a new user has been created!";

		send_mail(subject, message, email, [settings.EMAIL_HOST_USER], fail_silently=False);

	else:
		pass;

post_save.connect(post_save_user_receiver, sender=Mosebedisi);

#Profile table (one-to-one)

class Profile(models.Model): 
    mosebedisi = models.OneToOneField(
        Mosebedisi,
        on_delete=models.CASCADE,
        primary_key=True,
        );
    picture = models.FileField(blank=True, null=True);
    gender = models.CharField(max_length=50, blank=True, null=True);
    Status = models.CharField(max_length=50, blank=True, null=True);
    bio = models.CharField(max_length=600, blank=True, null=True);

    def __str__(self):
        return "%s" % (self.female);

class FriendRequest(models.Model): # Redundant for now 
	"""
		Immutable.
		Actually many-to-many
	"""
	sender = models.ManyToManyField(Profile);
	receiver = models.ManyToManyField(Profile, related_name="request_receiver");
	signature = models.CharField(max_length=100, blank=True, null=True);
	accepted = models.CharField(max_length=100, default="False");

	def __str__(self):
		return "%s" % (self.signature);

class Contact(models.Model): # replaced by pipe - may be useful later
	time_created = models.DateTimeField(auto_now_add=True)
	user = models.ManyToManyField(Mosebedisi);
	connected = models.BooleanField(default=False);
	#secret = models.CharField(max_length=50, blank=True, null=True);

	def __str__(self):
		return "%s" % (self.connected);


class Pipe(models.Model): # Good for now, will eventually become contact request
	time_created = models.DateTimeField(auto_now_add=True)
	user0_addr = models.CharField(max_length=50, blank=True, null=True);
	user1_addr = models.CharField(max_length=50, blank=True, null=True);
	connected = models.BooleanField(default=False);
	secret = models.TextField(blank=True, null=True);
	nonce = models.TextField(blank=True, null=True);

	def __str__(self):
		return "%s" % (self.connected);

# Message table (one-to-many).
class Message(models.Model):
	time_created = models.DateTimeField(auto_now_add=True)
	timestamp = models.CharField(max_length=500, blank=True, null=True);
	sender_addr = models.CharField(max_length=100, blank=True, null=True);
	reciever_addr = models.CharField(max_length=100, blank=True, null=True);
	message = models.TextField(blank=True, null=True);
	secret = models.TextField(blank=True, null=True);
	nonce = models.CharField(max_length=50, blank=True, null=True);
	signature = models.CharField(max_length=50, blank=True, null=True);
	pkn = models.TextField(blank=True, null=True);	    # Public key n.
	pke = models.CharField(max_length=100, default='0');	    # Public key e.

	def __str__(self):
		return "%s | %s" % (self.time_created, self.sender_addr);

# Group Table (not a relational table).
class Group(models.Model):
	NUCLEARFAM = "NF";
	EXTENDEDFAM = "EF";
	CLAN = "Cl";
	TRIBE = "Tr";
	NATION = "Na";
	FRIENDS = "Fr"
	COMPANY = "Co";
	MESSAGES = "Msg";
	REGION = "Reg";
	COUNTRY = "C";
	GROUP_TYPES = (
	    (NUCLEARFAM, "Nuclear family"),
	    (EXTENDEDFAM, "Extended family"),
	    (CLAN, "Clan"),
	    (TRIBE, "Tribe"),
	    (NATION, "Nation"),
	    (FRIENDS, "Friends"),
	    (COMPANY, "Company"),
	    (MESSAGES, "Messages"),
	    (REGION, "Region"),
	    (COUNTRY, "Country"),
	);
	name = models.CharField(max_length=50, blank=True, null=True);
	image= models.FileField(blank=True, null=True);
	story= models.CharField(max_length=1000, blank=True, null=True);
	group_type= models.CharField( max_length=3
	                            , choices=GROUP_TYPES
	                            , default=NUCLEARFAM
	                            );
	closed = models.BooleanField(default=True);
	members = models.ManyToManyField(
		Mosebedisi,
		through='Membership',
		through_fields=('group', 'person'),
	)

	def __str__(self):
		return "%s" % (self.name);

class Membership(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE);
	person = models.ForeignKey(Mosebedisi, on_delete=models.CASCADE);
	inviter = models.ForeignKey(
		Mosebedisi,
		on_delete=models.CASCADE,
		related_name="membership_invites"
		);
	invite_reason = models.CharField(max_length=64)

	def __str__(self):
		return "%s" % (self.invite_reason);

# Group member table (many-to-many).
class Member(models.Model):
	"""
	A table relating users to the groups they are a part of and groups to their members.
	"""
	group = models.ForeignKey(Group, on_delete=models.CASCADE);
	person = models.ForeignKey(Mosebedisi, on_delete=models.CASCADE);
	admin = models.BooleanField(default=False);

	def __str__(self):
		return "%s" % (self.admin);

class Need(models.Model):
	"""
	(relation : many to one)
	A table of all possible needs of a group.
	"""
	SELFKNOWLEDGE = "SK";
	SOCIOLOGICAL = "SO";
	PHYSICAL = "PH";
	NEED_TYPES = (
	    (SELFKNOWLEDGE, "Self-knowledge"),
	    (SOCIOLOGICAL, "Sociological"),
	    (PHYSICAL, "Physical"),
	);
	need = models.CharField(max_length=100, blank=True, null=True);
	need_type = models.CharField(max_length=2, choices=NEED_TYPES, default=PHYSICAL);
	group = models.ForeignKey(to=Group, on_delete=models.CASCADE);
	due_date = models.DateField(default = datetime.date(2023,7,8));

	def __str__(self):
		return "%s" % (self.need);

class MileStone(models.Model):
	"""
	(relational: many to one)
	A table relating the many milestones that need to be hit to achieve the goal of satisfying a need.
	"""
	milestone = models.CharField(max_length=100, blank=True, null=True);
	need = models.ForeignKey(to=Need, on_delete=models.CASCADE);
	description = models.CharField(max_length=1000, blank=True, null=True);
	dependant = models.BooleanField(default=False);
	due_date = models.DateField(default=datetime.date(2023,7,8));

	def __str__(self):
		return "%s" % (self.milestone);
"""
class Dependency(models.Model):

	#(relation : one to one)
	#A table relating all the dependent milestones to the milestone they are dependent on.

	dependant_milestone = models.ManyToManyField(to=MileStone);
	milestone = models.ManyToManyField(to=MileStone);
	completable = models.BooleanField(default=False);

	def __str__(self):
		return "%s" % (self.completable);
"""
class Responsibility(models.Model):
	"""
	(relational: many to many)
	A table relating the milestones of the needs of a group to those (members)
	who have qualified and are responsible for coordinating the provision for
	these needs.
	NOTE: The responsibility table will be populated by comparing the
	QUALIFICATION REQUIREMENT table and ACHIEVER table. Accepting those who
	qualify for the position.
	"""
	member = models.ManyToManyField(to=Member);
	milestone = models.ManyToManyField(to=MileStone);
	complete = models.BooleanField(default=False);

	def __str__(self):
		return "%s" % (self.complete);

class Candidates(models.Model):
	"""
	(relational: many to many)
	A table relating the candidates chosen and the qualification requirements for
	an individual to be given the responsibility of coordinating the provision for
	a milestone of a need.
	"""
	member = models.ManyToManyField(to=Member);
	milestone = models.ManyToManyField(to=MileStone);
	qualified = models.BooleanField(default=False);

	def __str__(self):
		return "%s" % (self.qualified);

class Achievement(models.Model):
	"""
	(non-relational)
	A table of all possible achievements.
	"""
	achievement = models.CharField(max_length=100, blank=True, null=True);
	description = models.CharField(max_length=1000, blank=True, null=True);

	def __str__(self):
		return "%s" % (self.achievement);

class Achiever(models.Model):
	"""
	(relational: many to many)
	A table relating achievements to the user/users who achieved them.
	"""
	profile = models.ManyToManyField(to=Profile);
	achievement = models.ManyToManyField(to=Achievement);
	date_achieved = models.DateField(auto_now_add=True);
	location_latitude = models.CharField(max_length=30, blank=True, null=True);
	location_longitude = models.CharField(max_length=30, blank=True, null=True);
	verifier_pkn = models.CharField(max_length=50, default='0');
	verifier_pke = models.CharField(max_length=50, default='0');
	verified = models.BooleanField(default=False);

	def __str__(self):
		return "%s" % (self.date_achieved);

class QualificationRequirements(models.Model):
	"""
	(relational: many to many)
	A table relating achievements required for an individual to be given the
	responsibility to coordinate the provision of a need (or needs) that the
	group has.
	NOTE: An achievement is a track record that indicates competency.  The
	needs of a group are vital and cannot be entrusted to an incompetent
	individual or incompetent individuals, lest disaster ensue.
	"""
	name = models.CharField(max_length=20, blank=True, null=True);
	milestone = models.ManyToManyField(to=MileStone);
	achievement = models.ManyToManyField(to=Achievement);

	def __str__(self):
		return "%s" % (self.name);

class LTime(models.Model):
	"""
		Many-to-many
	"""
	CLOCK_IN = "CI";
	CLOCK_OUT = "CO";
	LUNCH_START = "LS";
	LUNCH_END = "LE";
	STATUS_OPTIONS = (
		(CLOCK_IN, "Clock In"),
		(CLOCK_OUT, "Clock Out"),
		(LUNCH_START, "Lunch Start"),
		(LUNCH_END, "Lunch End"),
	);

	time_stamp = models.CharField(max_length=15, blank=True, null=True);
	status = models.CharField(max_length=2, choices=STATUS_OPTIONS, default=CLOCK_OUT);
	hashKey = models.CharField(max_length=100, blank=True, null=True);
	signature = models.CharField(max_length=50, blank=True, null=True);
	mosebedisi = models.ManyToManyField(to=Mosebedisi);

	def __str__(self):
		 return "%s"  % (self.time_stamp);

class Header(models.Model):
	"""
		Immutable
	"""
	nounce = models.CharField(max_length=100, blank=True, null=True);
	prev_hash = models.CharField(max_length=100, blank=True, null=True);
	hashKey = models.CharField(max_length=100, blank=True, null=True);
	signature = models.CharField(max_length=50, blank=True, null=True);
	pkn = models.CharField(max_length=150, default='0');
	pke = models.CharField(max_length=50, default='0');

	def __str__(self):
		return "%s" % (self.nounce);

