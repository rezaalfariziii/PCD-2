import imageio.v3 as image
import numpy as np

path = "d:\\sg.jpeg"
my_image = image.imread(path)

if len(my_image.shape) < 3 or my_image.shape[2] < 3:
    print("Image does not have the required RGB channels.")
    exit()

r = my_image[:, :, 0]
g = my_image[:, :, 1]
b = my_image[:, :, 2]

gs = (0.2989 * r + 0.5870 * g + 0.1140 * b).astype(np.uint8)

threshold_value = 128
binary_image = np.where(gs > threshold_value, 255, 0).astype(np.uint8)

image_r = np.zeros_like(my_image)
image_g = np.zeros_like(my_image)
image_b = np.zeros_like(my_image)
image_gs = np.zeros_like(my_image)
binary_rgb_image = np.zeros_like(my_image)

image_r[:, :, 0] = r
image_g[:, :, 1] = g
image_b[:, :, 2] = b

image_gs[:, :, 0] = gs
image_gs[:, :, 1] = gs
image_gs[:, :, 2] = gs

binary_rgb_image[:, :, 0] = binary_image
binary_rgb_image[:, :, 1] = binary_image
binary_rgb_image[:, :, 2] = binary_image

image.imwrite("d:\\sg1.jpeg", image_r)
image.imwrite("d:\\sg2.jpeg", image_g)
image.imwrite("d:\\sg3.jpeg", image_b)
image.imwrite("d:\\sg4.jpeg", image_gs)
image.imwrite("d:\\sg5.jpeg", binary_rgb_image)

print(f"Dimensi gambar adalah {my_image.shape}")
print("Proses selesai")