from PIL import Image

foo = Image.open("image.jpg")
foo.size
foo  = foo.resize((160,300),Image.ANTIALIAS)
foo.save("mod.jpg",quality=95)
# gives out more optimized image compression
foo.save("mod_opt.jpg",optimize=True,quality=95)
