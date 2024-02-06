from django.db import models
from datetime import date


SHOE_CATEGORIES = (
    ('S', 'Sneakers'),
    ('B', 'Boots'),
    ('F', 'Flats'),
    ('H', 'Heels'),
    ('S', 'Sandals'),
)

CLEANING = (
   ('M', 'Morning'),
   ('A', 'Afternoon'),
   ('E', 'Evening'),
)

# Create your models here
class ShoeAccessory(models.Model):
   name = models.CharField(max_length=50)
   color = models.CharField(max_length=20)

   def __str__(self):
      return self.name    
   
class Shoe(models.Model):
    brand = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    size = models.CharField(max_length=10, default='')
    color = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchase_date = models.DateField(default='')
    category = models.CharField(
        max_length=1,
        choices=SHOE_CATEGORIES,
        default=SHOE_CATEGORIES[0][0]
    )
    shoeAccessory = models.ManyToManyField(ShoeAccessory) 

    def __str__(self):
        return f"{self.brand} {self.model} - Size: {self.size}, Color: {self.color}, Purchased on: {self.purchase_date}"

    def clean_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count() >= len(CLEANING)



class Cleaning(models.Model):
  date = models.DateField()
  cleaned = models.CharField(
    max_length=1,
	 choices=CLEANING,
	 default=CLEANING[0][0]
  )
  # Create a cat_id FK
  shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_shoe_display()} on {self.date}"
  
class Meta:
    ordering = ['-date']