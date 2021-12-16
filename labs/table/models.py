# from typing import Required
import builtins
from django.db import models
from django.db.models.enums import TextChoices
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

  class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"    

class Floor(models.Model):
  """
  Model representing a floor of building
  """
  floor = models.IntegerField(help_text="Enter the university floor")
  building = models.ForeignKey(Building, help_text="select in which building this floor", on_delete=models.CASCADE, null=True)
  def __str__(self):
      """
      String for representing the university floor object (in Admin site etc.)
      """
      return f"Floor {self.floor}"

  class Meta:
        verbose_name = "Floor"
        verbose_name_plural = "Floors"

class Room(models.Model):
  room_number = models.IntegerField(
  help_text="Enter the number of room in which you want check PC")
  floor = models.ForeignKey(Floor, on_delete=models.SET_NULL, null=True)
  building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
  def __str__(self):
      """String for the object (in Admin site etc.)"""
      return f"Room {self.room_number}"
  
  class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

class Workplace(models.Model):
  place = models.IntegerField(
  help_text="Enter the number of student place(?)")
  room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
  def __str__(self):
      return f"Workplace {self.place}"

  class Meta:
        verbose_name = "Workplace"
        verbose_name_plural = "Workplaces"

class PC(models.Model):
  pc = models.UUIDField(primary_key=True,
  default = uuid.uuid4,
  help_text = "Inventory ID for PC")
  place = models.OneToOneField(Workplace, on_delete = models.CASCADE, null = True)
  
  date_of_setup = models.DateField(
  help_text = "When computer delivered to the room",
  null = True)
  
  class TypeClassProc(models.TextChoices):
    AMD_RYZEN_5000 = "AMD_Ryzen_5000"
    INTEL_I5_12600 = "Intel_i5_12600"
    AMD_RYZEN_9_5900X = "AMD_Ryzen_9_5900"
    INTEL_I3_9100 = "Intel_i3_9100"
  processor = models.CharField(
    help_text = "Choose processor for PC",
    null = True,
    max_length = 50,
    choices = TypeClassProc.choices,
  )
  processor_id = models.UUIDField(
  default = uuid.uuid4,
  help_text = "Inventory ID of this proc")
  # date_of_setup_proccessor = models.DateField(
  #   help_text = "When processor changed in PC",
  #   default = date_of_setup,
  #   null = True)

  class TypeClassVideo(models.TextChoices):
    ASUS_GEFORCE_GTX_1050_TI = "ASUS_Geforce_GTX_1050_Ti" 
    HP_RADEON_HD_7670 = "HP_Radeon_HD_7670"
    AMD_RADEON_HD8490 = "AMD_Radeon_HD8490"
    ASUS_GEFORCE_GT_710 = "ASUS_GeForce_GT_710"
  videocard = models.CharField(
    help_text = "Choose graphic card for PC",
    null = True,
    max_length = 50,
    choices = TypeClassVideo.choices,
  )
  videocard_id = models.UUIDField(
  default = uuid.uuid4,
  help_text = "Inventory ID of this videocard")
  # date_of_setup_videocard = models.DateField(
  #   help_text = "When videocard changed in PC",
  #   default = date_of_setup,
  #   null = True)

  class TypeClassMemmory(models.TextChoices):
    RAM_16GB_DDR4_2666 = "16GB_DDR4_2666"
    RAM_8GB_DDR4_2666 = "8GB_DDR4_2666"
    RAM_4GB_DDR3L_1866 = "4GB_DDR3L_1866"
    RAM_2GB_DDR3L_1600 = "2GB_DDR3L_1600"
  memmory = models.CharField(
    help_text = "Choose memmory for PC",
    null = True,
    max_length = 50,
    choices = TypeClassMemmory.choices,
  )
  memmory_id = models.UUIDField(
  default = uuid.uuid4,
  help_text = "Inventory ID of this memmory")
  # date_of_setup_memmory = models.DateField(
  #   help_text = "When memmory changed in PC",
  #   default = date_of_setup,
  #   null = True)

  class TypeClassHardMemmory(models.TextChoices):
    SSD_EXEGATE_NEXT_60GB = "SSD_ExeGate_Next_60GB"
    SEAGATE_VIDEO_3_320GB = "Seagate_Video_3_320GB"
    SSD_AMD_RADEON_R5_128GB = "SSD_AMD_Radeon_R5_128GB"
    WESTERN_DIGITAL_AV_GP_500GB = "WESTERN_DIGITAL_AV_GP_500GB"
  hdd = models.CharField(
    help_text = "Choose hdd for PC",
    null = True,
    max_length = 50,
    choices = TypeClassHardMemmory.choices,
  )
  hdd_id = models.UUIDField(
  default = uuid.uuid4,
  help_text = "Inventory ID of this hdd")
  # date_of_setup_videocard = models.DateField(
  #   help_text = "When hdd changed in PC",
  #   default = date.date_of_setup,
  #   null = True)

  def __str__(self):
      return f'PC {self.pc}'
  
  class Meta:
        verbose_name = "PC"
        verbose_name_plural = "PCs"

# # Create your models here.
