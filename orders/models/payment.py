from django.db import models
from orders.models import Order, Client

class Payment(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  date_time = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"Order #{self.order.id} paid for by Client: {self.client.name}"