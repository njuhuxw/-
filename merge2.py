from PIL import Image

big_image =Image.open('hot0.png')
small_image=Image.open('hot1.png')
# small_image.thumbnail((400,400))  可以实现压缩
cropped = small_image.crop((223, 80, 388, 180))  # (left, upper, right, lower)

cropped.save("./cut/pil_cut_thor.png")
big_image.paste(cropped,(223, 80))
big_image.show()