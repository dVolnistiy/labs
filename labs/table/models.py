# from typing import Required
from django.db import models
from django.urls import reverse
from datetime import date
from django import forms
import uuid

class Building(models.Model):
  """
  Model representing a building where all this are going on
  """
  name = models.CharField(max_length=40, help_text="Enter street and number of university building")

  def __str__(self):
      """
      String for representing the Model object (in Admin site etc.)
      """
      return self.name
    
class Floor(models.Model):
  """
  Model representing a floor of building
  """
  number_of_floor = models.IntegerField(default=1, help_text="Enter the university floor (from 1 to 9)")
  building = models.ForeignKey(Building, help_text="select in which building this floor", on_delete=models.SET_NULL, null=True)
  def __str__(self):
      """
      String for representing the university floor object (in Admin site etc.)
      """
      return self.number_of_floor

class Room(models.Model):
  number_of_room = models.IntegerField(
  help_text="Enter the number of room in which you want check PC")
  floor = models.ForeignKey(Floor, on_delete=models.SET_NULL, null=True)
  def __str__(self):
      """String for the object (in Admin site etc.)"""
      return self.number_of_room

class Workplace(models.Model):
  place = models.IntegerField(
  help_text="Enter the number of student place(?)")
  room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
  def __str__(self):
      return self.place

# PROC_CHOICES = (
#   ("1", "AMD Ryzen 5000"),
#   ("2", "Intel i5 12600"),
#   ("3", "AMD Ryzen 9 5900X"),
#   ("4", "Intel i3 9100")
# )

class Proc(models.Model):
  class TypeClass(models.TextChoices):
    RYZEN_5000 = "AMD_Ryzen_5000"
    # Intel_i5_12600 = "2"
    # AMD_Ryzen_9_5900X = "3"
    # Inte_i3_9100 = "4"


  processor = models.CharField(
   # required=True,
    null=True,
    max_length=70,
    choices=TypeClass.choices,
  )

  id_proc = models.UUIDField(default=uuid.uuid4)

  def __str__(self):
    return '({0}) {1}'.format(self.processor, self.id_proc)

# CARD_CHOICES = (
#   # ASUS GeForce GTX 1050 Ti 
#   # HP Radeon HD 7670 
#   # AMD Radeon HD8490
#   # ASUS GeForce GT 710
# )
# class Proc(models.Model):
#   #processor = models.CharField(max_length=25, default=None)
#   id_proc = models.UUIDField(default=uuid.uuid4)
#   processor=models.TextField(max_length = 1, choices = PROC_CHOICES, default = "2")

#   def __str__(self):
#       return '({0}) {1}'.format(self.processor, self.id_proc)

class Graphic_card(models.Model):
  pass

class RAM(models.Model):
  pass

class HDD(models.Model):
  pass

class PC(models.Model):
  pc = models.UUIDField(primary_key=True,
  default=uuid.uuid4,
  help_text="Inventory ID for PC")
  class TypeClass(models.TextChoices):
    RYZEN_5000 = "AMD_Ryzen_5000"
  processor = models.CharField(
   # required=True,
    null=True,
    max_length=70,
    choices=TypeClass.choices,
  )
  # graphic=models.
  # ram=models.
  # hdd=models. 
  def __str__(self):
      return self.pc
  time_of_setup = models.DateField(null=True)

  class Meta:
        verbose_name = "PC"
        verbose_name_plural = "PCs"

# PROC_CHOICES = (
#   ("1", "AMD Ryzen 5000"),
#   ("2", "Intel i5 12600"),
#   ("3", " AMD Ryzen 9 5900X"),
#   ("4", " Intel i3 9100")
# )

# class Proc(models.Model):
#   processor = models.CharField(max_length=25, default=None)
#   id_proc = models.UUIDField(default=uuid.uuid4)
#   proc_field=forms.MultipleChoiceField(choices = PROC_CHOICES)

#   def __str__(self):
#       return self.processor



# # Create your models here.
