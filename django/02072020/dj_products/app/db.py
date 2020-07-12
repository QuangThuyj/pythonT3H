from .models import Product, Category


def getCategories():
    return Category.objects.all()


def getProducts(keyword, categoryId, freeShip):
    phrase = '%' + keyword + '%'
    if categoryId != '':
        return Product.objects.raw(
            'SELECT * FROM app_product WHERE category_id=%s AND (name LIKE %s OR code LIKE %s) AND free_ship=%s',
            [categoryId, phrase, phrase, "1" if freeShip else "0"])
    else:
        return Product.objects.raw('SELECT * FROM app_product WHERE (name LIKE %s OR code LIKE %s) AND free_ship=%s',
                                   [phrase, phrase, "1" if freeShip else "0"])


def findProductById(id):
    return Product.objects.get(pk=id)


def deleteProduct(id):
    product = findProductById(id)
    if product:
        product.delete()
