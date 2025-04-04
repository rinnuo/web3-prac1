from django.db import models
from orders.models import Dish, Waiter, Table

class Order(models.Model):
  table = models.ForeignKey(Table, on_delete=models.CASCADE)
  waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
  dishes = models.ManyToManyField(Dish)
  date_time = models.DateTimeField(auto_now_add=True)
  completed = models.BooleanField(default=False)
  
  def __str__(self):
    status = "Complete" if self.completed else "In Progress"
    return f"Order #{self.id} at Table #{self.table.number} ({status})"
