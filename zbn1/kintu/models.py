from django.db import models

# Create your models here.
class Account(models.Model):
	"""
		Account is a One-to-one relation with Transaction.
	"""
	pkn = models.CharField(max_length=150, default='0');	    # Public key n.
	pke = models.CharField(max_length=50, default='0');	    # Public key e.
	last_transaction = models.OneToOneField(Transaction
		, on_delete=models.CASCADE
		, primary_key=True,
       	 );
	def __str__(self):
		return "%s" % (self.last_transaction);

class Transaction(models.Model):
	"""
		Immutable.
		Actually many-to-many, may need to come back for relook at
		'sender' and 'receiver'		
	"""
	sender = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True);
	receiver = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True);
	amount = models.CharField(max_length=100, blank=True, null=True);
	utxo = models.CharField(max_length=100, blank=True, null=True);
	hashKey = models.CharField(max_length=150, blank=True, null=True);
	signature = models.CharField(max_length=100, blank=True, null=True);
	
	def __str__(self):
		return "%s" % (self.utxo);

class Header(models.Model):
	"""
		Immutable
	"""
	nounce = models.CharField(max_length=100, blank=True, null=True);
	prev_hash = models.CharField(max_length=100, blank=True, null=True);
	hashKey = models.CharField(max_length=100, blank=True, null=True);
	signature = models.CharField(max_length=100, blank=True, null=True);
	pkn = models.CharField(max_length=150, default='0');	    # Public key n.
	pke = models.CharField(max_length=50, default='0');	    # Public key e.
	
	def __str__(self):
		return "%s" % (self.nounce);
