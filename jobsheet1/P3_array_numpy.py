import numpy as np
import matplotlib.pyplot as plt
from skimage import data

# Menjelaskan bagaimana citra disimpan dalam array NumPy

# Memuat gambar dari scikit-image
gambar_coins = data.coins()
gambar_camera = data.camera()
gambar_astronaut = data.astronaut()

# Fungsi untuk menampilkan informasi array NumPy dari gambar
def info_array_numpy(image, nama):
    print(f"\n=== {nama} ===")
    print(f"Tipe Data: {type(image)}")          # Harusnya <class 'numpy.ndarray'>
    print(f"Dimensi: {image.shape}")             # Menampilkan dimensi gambar (height, width, channels jika RGB)
    print(f"Tipe Nilai Piksel: {image.dtype}")   # Menampilkan tipe data dalam array (uint8)

    # Menampilkan sebagian kecil dari array (5x5 piksel pertama)
    print("Contoh nilai piksel (5x5 pertama):")
    print(image[:5, :5] if len(image.shape) == 2 else image[:5, :5, :])

# Menampilkan informasi setiap gambar
info_array_numpy(gambar_coins, "Coins")
info_array_numpy(gambar_camera, "Camera")
info_array_numpy(gambar_astronaut, "Astronaut")

# Visualisasi bagaimana array NumPy mewakili citra
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

gambar_list = [gambar_coins, gambar_camera, gambar_astronaut]
nama_list = ["Coins", "Camera", "Astronaut"]

for ax, img, nama in zip(axes, gambar_list, nama_list):
    ax.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
    ax.set_title(f"{nama}\nArray Shape: {img.shape}")
    ax.axis('off')

plt.tight_layout()
plt.show()
