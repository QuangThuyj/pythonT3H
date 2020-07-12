from django.db import models

import os
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()
IMG_DIR = os.path.join('static', 'product_images')
IMG_URL_PREFIX = '/static/product_images/'


class Category(models.Model):
    code = models.CharField(max_length=20, verbose_name='Mã nhóm sản phẩm', unique=True)
    name = models.CharField(max_length=50, verbose_name='Tên nhóm sản phẩm')

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=20, verbose_name='Mã sản phẩm', unique=True)
    name = models.CharField(max_length=50, verbose_name='Tên sản phẩm')
    description = models.CharField(blank=True, verbose_name='Mô tả', max_length=200)
    unitPrice = models.FloatField(db_column='unit_price', verbose_name='Đơn giá')
    freeShip = models.BooleanField(db_column='free_ship', verbose_name='Miễn phí vận chuyển', default=False)
    imageURL = models.CharField(db_column='image_url', max_length=1024, default="")

    def saveImage(self, image):
        imgPath = os.path.join(IMG_DIR, image.name)
        savedPath = fs.save(imgPath, image)
        fileName = os.path.basename(savedPath)

        self.imageURL = IMG_URL_PREFIX + fileName
        self.save()

    def delete(self):
        fileName = self.imageURL.split('/')[-1]
        imgPath = os.path.join(IMG_DIR, fileName)

        if os.path.isfile(imgPath):
            os.remove(imgPath)

        super().delete()
