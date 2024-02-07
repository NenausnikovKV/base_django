from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [("can_eat_pizzas", "Can eat pizzas")]