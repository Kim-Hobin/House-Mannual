from django.db import models
from phone_field import PhoneField
from tinymce.models import HTMLField


class Accommodation(models.Model):

    """ Accommodation Model Definition """

    name = models.CharField(max_length=20)
    avatar = models.ImageField(blank=True, upload_to="avatars")
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="backgrounds", blank=True)
    address = models.CharField(max_length=30)
    phone_number = PhoneField(blank=True, help_text="Contact phone number")
    check_in = models.TimeField()
    check_out = models.TimeField()
    wifi = models.CharField(max_length=20)
    facility = models.TextField(blank=True)
    recycle = models.TextField(blank=True)
    house_rule = models.TextField(blank=True)
    content = HTMLField(default="")
    slug = models.SlugField(default="", unique=True)
    host = models.ForeignKey(
        "users.user", related_name="Accommodation", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/" + self.slug

    def get_attractions(self):
        return list(self.Attraction.all())

  
class TouristAttraction(models.Model):

    """ TouristAttraction Mdoel Definition """

    accommodation = models.ForeignKey(
        Accommodation, related_name="Attraction", on_delete=models.CASCADE
    )
    file = models.ImageField(upload_to="TouristAttractions")
    caption = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    attraction_phone_number = PhoneField(blank=True, help_text="Contact phone number")

    def __str__(self):
        return self.caption
