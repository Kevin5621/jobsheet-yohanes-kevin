import os
import matplotlib.pyplot as plt
from skimage import data, io

gambar = data.astronaut()

# Menjelaskan perbedaan kompresi lossy dan lossless dalam citra digital

# Simpan gambar dalam format lossy (JPEG) dan lossless (PNG)
jpeg_quality_50 = "astronaut_lossy_50.jpg"
jpeg_quality_90 = "astronaut_lossy_90.jpg"
png_lossless    = "astronaut_lossless.png"

io.imsave(jpeg_quality_50, gambar, quality=50)  # JPEG lossy dengan kualitas rendah
io.imsave(jpeg_quality_90, gambar, quality=90)  # JPEG lossy dengan kualitas tinggi
io.imsave(png_lossless,    gambar)              # PNG lossless

# Fungsi untuk menghitung ukuran file
def ukuran_file(nama_file):
    size_bytes = os.path.getsize(nama_file)
    size_kb    = size_bytes / 1024
    size_mb    = size_kb / 1024
    return f"{size_bytes} Bytes ({size_kb:.2f} KB, {size_mb:.4f} MB)"

# Menampilkan ukuran file dari masing-masing format
nama_file_kompresi = [jpeg_quality_50, jpeg_quality_90, png_lossless]
ukuran_kompresi    = [ukuran_file(file) for file in nama_file_kompresi]

# Menampilkan gambar hasil kompresi
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

kompresi_label = ["JPEG (Lossy, Q=50)", "JPEG (Lossy, Q=90)", "PNG (Lossless)"]

for ax, file, label in zip(axes, nama_file_kompresi, kompresi_label):
    img = io.imread(file)
    ax.imshow(img)
    ax.set_title(f"{label}\nUkuran:\n{ukuran_file(file)}", fontsize=12,
                 fontweight="bold", color="black", pad=10)
    ax.axis("off")

plt.suptitle("Perbedaan Kompresi Lossy dan Lossless dalam Citra Digital",
             fontsize=16, fontweight="bold", color="darkblue", y=1.05)
plt.tight_layout()
plt.show()

# Menampilkan informasi perbedaan kompresi dalam teks
print("Perbedaan Kompresi Lossy dan Lossless:")

print("\n1. JPEG (Lossy, Quality=50):")
print("- Menggunakan kompresi lossy dengan kualitas rendah (Q=50).")
print("- Detail gambar berkurang, muncul artefak kompresi.")
print("- Ukuran file lebih kecil.")
print(f"- Ukuran file: {ukuran_kompresi[0]}")

print("\n2. JPEG (Lossy, Quality=90):")
print("- Menggunakan kompresi lossy dengan kualitas lebih tinggi (Q=90).")
print("- Detail gambar masih cukup baik, artefak lebih sedikit.")
print("- Ukuran file lebih besar dibanding Q=50, tetapi lebih kecil dibanding lossless.")
print(f"- Ukuran file: {ukuran_kompresi[1]}")

print("\n3. PNG (Lossless):")
print("- Menggunakan kompresi lossless, tidak ada kehilangan data.")
print("- Detail gambar tetap sempurna seperti aslinya.")
print("- Ukuran file lebih besar dibanding JPEG lossy.")
print(f"- Ukuran file: {ukuran_kompresi[2]}")
