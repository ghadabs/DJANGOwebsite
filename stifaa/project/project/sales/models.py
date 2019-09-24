from django.db import models
from django.db.models import CASCADE
from multiselectfield import MultiSelectField
from django.utils.translation import ugettext_lazy as _

#put all your subcategories of all the categories in this list 

Subs = ((_('sub1'), _('sub1')),
        (_('sub2'), _('sub2')),
        (_('sub3'), _('sub3')),
        (_('sub4'), _('sub4')),
        (_('sub5'), _('sub5')))



class Category(models.Model):
    name = models.CharField(max_length=200 ,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.ImageField(upload_to='images/', blank=True)
    subcategories = MultiSelectField(choices=Subs,
                                 max_choices=10,
                                 max_length=1000)
     
    class Meta:
        ordering = ('name',)
        verbose_name='category'
        verbose_name_plural = 'categories'
        index_together=(('id','slug'))
    def __str__(self):
        return self.name

# class Subcategory(models.Model):
#     name = models.CharField(max_length=200 ,db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name='subcatgory'
#         verbose_name_plural = 'subcategories'
#         #index_together=(('id','slug'))
#     def __str__(self):
#         return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Product', on_delete=CASCADE, default=None) 
    # one category contiens multple products 1 to many relation
    subcategory = models.CharField(choices=Subs,
                                   max_length=1000)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=True)
    img1 = models.ImageField(upload_to='images/', blank=True)
    img2 = models.ImageField(upload_to='images/', blank=True)
    img3 = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    oldprice = models.DecimalField(max_digits=1000, decimal_places=3)
    newprice = models.DecimalField(max_digits=1000, decimal_places=3)
    brand_photo = models.ImageField(upload_to='images/', blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',) 
        index_together=(('id','slug'))
    def __str__(self):
        return self.name
    def pourcentage(self):
        return ((self.oldprice - self.newprice)*100)/self.oldprice
   

