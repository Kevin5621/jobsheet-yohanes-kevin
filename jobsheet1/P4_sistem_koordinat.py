import matplotlib.pyplot as plt
from skimage import data

# Menjelaskan sistem koordinat kiri atas dalam citra digital dengan warna anotasi yang lebih kontras

# Pilih salah satu gambar untuk contoh koordinat
gambar_sample = data.coins()

# Ukuran gambar
height, width = gambar_sample.shape

# Buat plot
fig, ax = plt.subplots(figsize=(6, 6))

# Tampilkan gambar
ax.imshow(gambar_sample, cmap='gray')

# Tambahkan anotasi sumbu koordinat
ax.set_title("Sistem Koordinat Kiri Atas dalam Citra Digital", fontsize=12, fontweight="bold")
ax.set_xlabel("Sumbu X (Lebar) →", fontsize=10, color="blue")
ax.set_ylabel("↓ Sumbu Y (Tinggi)", fontsize=10, color="red")

# Tambahkan garis koordinat utama
ax.axhline(y=0, color='red', linestyle='--', linewidth=1, label="Y = 0 (Atas)")
ax.axvline(x=0, color='blue', linestyle='--', linewidth=1, label="X = 0 (Kiri)")

# Tambahkan beberapa titik koordinat penting dengan warna kontras (cyan)
koordinat_titik = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1), (width//2, height//2)]
for x, y in koordinat_titik:
    ax.scatter(x, y, color='cyan', s=50, edgecolors='black', linewidth=1.2)  # Titik dengan outline hitam
    ax.text(x + 10, y + 10, f"({x}, {y})", color="cyan", fontsize=10,
            fontweight="bold", ha="left", va="bottom")

# Tambahkan legenda
ax.legend(loc="upper right")

plt.show()
