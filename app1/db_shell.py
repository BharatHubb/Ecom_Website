from app1.models.category import Category
from app1.models.product import Product


# exec(open(r"D:\python_program\python_code\Django_projects\Django Projects\Ecom_Main\app1\db_shell.py").read())

# from openpyxl import load_workbook
# FILE_PATH = r"C:\Users\HP\Desktop\data.xlsx"

# wb = load_workbook(filename = FILE_PATH)
# sheet = wb.active
# l = []
# # c = 1
# for x in range(1, sheet.max_row +1):
#     id = sheet.cell(row = x, column = 1).value
#     name = sheet.cell(row = x, column = 2).value
#     obj = Category(id  =id, name = name)
#     l.append(obj)
# Category.objects.bulk_create(l)
# wb.save(FILE_PATH)

# from openpyxl import load_workbook
# FILE_PATH = r"C:\Users\HP\Desktop\data.xlsx"

# wb = load_workbook(filename = FILE_PATH)
# sheet = wb.active
# c = 1
# lst = []
# for x in range(1, sheet.max_row +1 ):
#     id = sheet.cell(row = x, column = 1).value
#     name = sheet.cell(row = x, column = 2).value
#     price = sheet.cell(row = x, column = 3).value
#     catgory = sheet.cell(row = x, column = 4).value
#     description = sheet.cell(row = x, column = 5).value
#     image = sheet.cell(row = x, column = 6).value
#     obj = Product(id = id, name = name, price = price, catogory_id = catgory, description = description, image = image)
#     lst.append(obj)
# Product.objects.bulk_create(lst[1:])

# for x in lst:
#     sheet.append(x)
# wb.save(FILE_PATH)

    # name = models.CharField(max_length = 100)
    # price = models.IntegerField()
    # catogory = models.ForeignKey(Category, on_delete= models.CASCADE, default = 1)
    # description = models.CharField(max_length = 500, null = True, default = "", blank = True)
    # image = models.ImageField(upload_to = 'media/')
# [57, 'knee-length Frock', 699, 22, None, 'uploads/products/7_uhXCNAG.jpg']
# {'_state': <django.db.models.base.ModelState object at 0x0000027C63B82B80>, 'id': 57, 'name': 'knee-length Frock', 'price': 699, 'category_id': 22, 'description': None, 'image': 'uploads/products/7_uhXCNAG.jpg'}



# n = 5
# for x in range(1, n+1):
    # print("-"*(2*n-2*x), end="")
    # for y in range(1, x+1):
        # print(chr(96+n-y+1)+"-", end="")
    # for z in range(x-1):
        # if x == n and z == x-2:
            # print(chr(96+n+z-x+2), end="")
        # else:
            # print(chr(96+n+z-x+2)+"-", end="")
    # for w in range(1, 2*n-2*x):
        # print("-", end="")
    # print()
# 
# for x in range(1, n):
    # print("-"*(2*x), end="")
    # for y in range(1, n-x+1):
        # print(chr(97+n-y)+"-", end="")
    # for z in range(1, n-x):
        # print(chr(96+n+z-y+1)+"-", end="")
    # for w in range(1, 2*x):
        # print("-", end="")
    # print()