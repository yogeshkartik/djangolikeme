from django.db import models

# Create your models here.


# class users(models.Model):
# 	name = models.CharField(max_length=200)
# 	username = models.CharField(max_length=200)
# 	userpswd = models.CharField(max_length=200)
# 	userlocation = models.IntegerField()

# 	def __str__(self):
# 		return self.name


# class Item(models.Model):
# 	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
# 	text = models.CharField(max_length=300)
# 	complete = models.BooleanField()

# 	def __str__(self):
# 		return self.text