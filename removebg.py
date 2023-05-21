from rembg import remove
from PIL import Image
input_path = 'Cow_female_black_white.jpg'
output_path = 'Cow.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
