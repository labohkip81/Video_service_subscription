from django.db import models

MEMBBERSHIP_CHOICES = (
    ('Enterprise', 'ent'),
    ('Professional', 'pro'),
    ('Free', 'free')
)
# Create your models here.
class Membership(models.Model):
    slug = models.SlugField(),
    membership_type = models.CharField(choices=MEMBBERSHIP_CHOICES, default='Free', max_length=30)
    price = models.IntegerField(max_length=15, blank=True),
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type