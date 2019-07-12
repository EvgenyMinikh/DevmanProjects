from PIL import Image


def crop_image(image, direction=1):
    cut_pixels = 50
    coords_2sides = (cut_pixels, 0, image.width - cut_pixels, image.height)

    if (direction == 1):  # Cut from left
        coords = (2 * cut_pixels, 0, image.width, image.height)
    elif (direction == -1):  # Cut from right
        coords = (0, 0, image.width - 2 * cut_pixels, image.height)

    cropped_both_sides = image.crop(coords_2sides)
    cropped_one_side = image.crop(coords)

    return cropped_both_sides, cropped_one_side


def print_image_info(image):
    st = """Ширина - {width}
Высота - {height}
Цветовая модель - {color}
================"""

    print(st.format(width=image.width, height=image.height, color=image.mode))


image_path = "monro.jpg"
final_image_path = "final.jpg"

image = Image.open(image_path)
if (image.mode == "CMYK"):
    image = image.convert("RGB")

red, green, blue = image.split()

red_cropped_both, red_cropped_left = crop_image(red, 1)
red_merged = Image.blend(red_cropped_both, red_cropped_left, 0.5)

blue_cropped_both, blue_cropped_left = crop_image(blue, -1)
blue_merged = Image.blend(blue_cropped_both, blue_cropped_left, 0.5)

green_cropped_both = crop_image(green)[0]

final_image = Image.merge("RGB", (red_merged, blue_merged, green_cropped_both))

# print_image_info(final_image)

final_image.thumbnail((80, 80))
final_image.save(final_image_path)