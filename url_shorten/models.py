from django.db import models

# Create your models here.
class Url(models.Model):
    short_url = models.URLField('Short url', null = True)
    long_url = models.URLField('Long url', null = True)
    long_url_encoded = models.CharField('Long url encoded', max_length = 100, null = True)

    def __str__(self):
        return "{} redirects to {}".format(str(self.long_url_encoded), str(self.long_url))