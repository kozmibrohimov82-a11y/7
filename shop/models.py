from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=255,unique=True,verbose_name='Nomi')
    slug=models.SlugField(max_length=255,unique=True)
    icon = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Kategoriya'
        verbose_name_plural='Kategoriyalar'


class Product(models.Model):
    name=models.CharField(max_length=255,unique=True,verbose_name='Nomi')
    slug = models.SlugField(max_length=255, unique=True)
    description=models.TextField(verbose_name='Tavsifi')
    price=models.IntegerField(verbose_name='Narxi')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Kategoriyasi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Mahsulot'
        verbose_name_plural='Mahsulotlar'



class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Mahsuloti')
    image=models.ImageField(upload_to='media/',verbose_name='Rasmi')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name='Rasmi'
        verbose_name_plural='Rasimlar'

    def get_image(self):
        product_images=self.images.all()
        if product_images:
            return product_images[0].image.url
        else:
            return "https://www.youtube.com/watch?v=_wuyv7N6CdE"
