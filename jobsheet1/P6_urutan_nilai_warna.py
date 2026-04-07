import matplotlib.pyplot as plt
from skimage import data

# Menjelaskan urutan tiga nilai warna dalam citra scikit-image dengan titik penanda koordinat piksel

# Memuat gambar RGB dari scikit-image
gambar_rgb = data.astronaut()  # Gambar astronaut dalam format RGB

# Ekstrak tiga kanal warna (R, G, B)
red_channel   = gambar_rgb[:, :, 0]  # Kanal merah
green_channel = gambar_rgb[:, :, 1]  # Kanal hijau
blue_channel  = gambar_rgb[:, :, 2]  # Kanal biru

# Koordinat tiga titik sampel untuk menampilkan nilai piksel RGB
titik_koordinat = [(100, 100), (200, 150), (300, 250)]

# Menampilkan gambar asli dan masing-masing kanal warna
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

# Tampilkan gambar asli dengan titik penanda
axes[0].imshow(gambar_rgb)
axes[0].set_title("Gambar Asli (RGB)")
for x, y in titik_koordinat:
    axes[0].scatter(x, y, color='yellow', s=50, edgecolors='black', linewidth=1.2)

# Tampilkan kanal merah dengan titik
axes[1].imshow(red_channel, cmap="Reds")
axes[1].set_title("Kanal Merah (Red)")
for x, y in titik_koordinat:
    axes[1].scatter(x, y, color='black', s=50, edgecolors='white', linewidth=1.2)

# Tampilkan kanal hijau dengan titik
axes[2].imshow(green_channel, cmap="Greens")
axes[2].set_title("Kanal Hijau (Green)")
for x, y in titik_koordinat:
    axes[2].scatter(x, y, color='black', s=50, edgecolors='white', linewidth=1.2)

# Tampilkan kanal biru dengan titik
axes[3].imshow(blue_channel, cmap="Blues")
axes[3].set_title("Kanal Biru (Blue)")
for x, y in titik_koordinat:
    axes[3].scatter(x, y, color='black', s=50, edgecolors='white', linewidth=1.2)

# Hilangkan sumbu koordinat
for ax in axes:
    ax.axis("off")

plt.suptitle("Urutan Tiga Nilai Warna dalam Citra scikit-image dengan Titik Sampel",
             fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

# Menampilkan contoh nilai piksel untuk titik-titik yang dipilih
print("Nilai RGB pada titik koordinat yang dipilih:")
for i, (x, y) in enumerate(titik_koordinat):
    r_val, g_val, b_val = gambar_rgb[y, x, 0], gambar_rgb[y, x, 1], gambar_rgb[y, x, 2]
    print(f"Titik {i+1} - Koordinat ({x}, {y}):")
    print(f"  Red   (Merah) : {r_val}")
    print(f"  Green (Hijau) : {g_val}")
    print(f"  Blue  (Biru)  : {b_val}")
    print(f"  RGB Triplet   : ({r_val}, {g_val}, {b_val})\n")
