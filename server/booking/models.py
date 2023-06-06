from django.db import models

# Create your models here.
class Booking(models.Model):
    status = models.CharField(max_length=100)
    paid_deposit = models.BooleanField(default=False)
    paid_in_full = models.BooleanField(default=False)
    enquiry_method = models.CharField(max_length=100)
    enquiry_date = models.DateField()
    enquiry_name = models.CharField(max_length=100)
    enquiry_email = models.CharField(max_length=100)
    set_option = models.CharField(max_length=100, blank=True)
    travel_cost = models.BigIntegerField()
    quote = models.BigIntegerField()
    event_type = models.CharField(max_length=100, blank=True)
    event_date = models.DateField(blank=True)
    venue = models.CharField(max_length=100, blank=True)
    contact_full_names = models.CharField(max_length=100, blank=True)
    contact_address = models.CharField(max_length=100, blank=True)
    contact_telephone = models.CharField(max_length=100, blank=True)
    song_request = models.CharField(max_length=100, blank=True)
    setup_info = models.CharField(max_length=100, blank=True)
    music_between_sets = models.CharField(max_length=100, blank=True)
    wedding_theme = models.CharField(max_length=100, blank=True)
    introduced_as = models.CharField(max_length=100, blank=True)
    timings = models.CharField(max_length=100, blank=True)
    any_other_info = models.CharField(max_length=100, blank=True)

    def add_fields(self, dict):
        for key, value in dict.items():
            setattr(self, key, value)

