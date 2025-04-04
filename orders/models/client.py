from django.db import models

class Client(models.Model):
  name = models.CharField(max_length=50)
  nit = models.CharField(max_length=20, blank=True)
  
  def __str__(self):
    if self.nit:
      return f"{self.name} - 🪪{self.nit}"
    return self.name