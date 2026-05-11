# E. Hasil Praktik — Jobsheet 5: Similarity, Matching, dan CBIR

## Praktikum 1 — Menghitung Jarak Berbasis Piksel (Euclidean & Manhattan)

### Tujuan
Memahami perbedaan jarak Euclidean (L2) dan Manhattan (L1) pada dua patch citra sederhana, serta membandingkan jarak untuk patch yang berbeda lokasi dengan patch yang lebih mirip.

### Hasil dan Analisis
Pada pengujian menggunakan patch dari citra `camera`, diperoleh nilai jarak sebagai berikut:

- Jarak Euclidean antara Patch 1 dan Patch 2: **24.7650**
- Jarak Euclidean antara Patch 1 dan Patch 3: **5.0000**
- Jarak Manhattan antara Patch 1 dan Patch 2: **936.4392**
- Jarak Manhattan antara Patch 1 dan Patch 3: **250.0000**

Patch 2 diambil dari lokasi berbeda sehingga perbedaannya terhadap Patch 1 jauh lebih besar. Patch 3 dibuat dari Patch 1 dengan sedikit perubahan intensitas, sehingga jaraknya jauh lebih kecil. Hasil ini sesuai dengan ekspektasi visual: patch yang lebih mirip memiliki jarak yang lebih kecil.

Jika dibandingkan, jarak Manhattan menghasilkan angka yang lebih besar karena menjumlahkan selisih absolut semua elemen, sedangkan Euclidean memberikan penalti berbasis kuadrat dan akar kuadrat. Secara tren, keduanya konsisten: Patch 1 dan Patch 3 selalu lebih dekat daripada Patch 1 dan Patch 2.

### Kesimpulan
Jarak Euclidean dan Manhattan sama-sama dapat membedakan patch yang mirip dan tidak mirip. Pada data ini, Patch 1 dan Patch 3 terbukti lebih dekat dibanding Patch 1 dan Patch 2.

---

## Praktikum 2 — Menghitung Cosine Similarity antara Histogram Warna

### Tujuan
Memahami kemiripan dua citra berwarna berdasarkan histogram warna menggunakan Cosine Similarity.

### Hasil dan Analisis
Hasil cosine similarity yang diperoleh adalah:

- Image 1 (`astronaut`) vs Image 2 (`coffee`): **0.7599**
- Image 1 (`astronaut`) vs Image 3 (`astronaut`): **1.0000**
- Image 1 (`astronaut`) vs Image 4 (`astronaut` downsampled): **1.0000**

Nilai untuk citra identik mendekati 1, sesuai dengan ekspektasi. Citra `astronaut` dan `coffee` memiliki distribusi warna yang berbeda, sehingga tingkat kemiripannya lebih rendah. Menariknya, citra asli dan versi downsampled memiliki similarity 1 karena histogram warna globalnya tetap sangat mirip meskipun ukuran citra berubah.

### Kesimpulan
Cosine Similarity pada histogram warna efektif untuk mengukur kemiripan distribusi warna global. Citra yang identik atau sangat mirip menghasilkan nilai mendekati 1.

---

## Praktikum 3 — Menghitung Structural Similarity Index (SSIM)

### Tujuan
Memahami pengukuran kemiripan struktural antar citra menggunakan SSIM dan membandingkan pengaruh noise, perubahan kontras, serta blur.

### Hasil dan Analisis
Nilai SSIM yang diperoleh adalah:

- Ref vs Same: **1.0000**
- Ref vs Noisy: **0.2948**
- Ref vs Contrast: **0.9651**
- Ref vs Blurred: **0.8027**

Citra yang sama menghasilkan SSIM 1.0, sesuai harapan. Citra dengan noise Gaussian turun drastis karena struktur lokal menjadi lebih acak. Perubahan kontras masih mempertahankan struktur utama sehingga SSIM tetap tinggi. Citra blur menurunkan ketajaman tepi dan detail, sehingga SSIM berada di antara citra noisy dan citra kontras.

Hasil ini sesuai dengan persepsi visual: citra yang tampak masih mirip secara struktur menghasilkan SSIM lebih tinggi.

### Kesimpulan
SSIM sangat baik untuk menilai kemiripan struktural. Nilainya sensitif terhadap noise dan blur, namun lebih tahan terhadap perubahan kontras global.

---

## Praktikum 4 — Penerapan Template Matching

### Tujuan
Memahami pencocokan template untuk menemukan lokasi objek kecil dalam citra yang lebih besar.

### Hasil dan Analisis
Template yang diambil dari citra `coins` berhasil ditemukan pada koordinat **(x, y) = (190, 15)** dengan skor puncak heatmap **1.0000**. Area paling terang pada heatmap sesuai dengan lokasi template pada citra asli, sehingga metode `match_template` berhasil menemukan koin yang dijadikan template.

Metode ini sangat efektif jika objek memiliki orientasi dan ukuran yang sama seperti template. Namun, template matching standar tidak tahan terhadap rotasi dan perubahan skala. Jika template dirotasi atau ukurannya diubah, skor kecocokan biasanya turun drastis.

### Kesimpulan
Template matching berhasil menemukan objek target pada citra `coins`, tetapi metode ini terbatas terhadap rotasi dan skala.

---

## Praktikum 5 — Simulasi Content-Based Image Retrieval (CBIR) Sederhana

### Tujuan
Memahami CBIR sederhana dengan fitur histogram warna dan menilai urutan retrieval berdasarkan kemiripan warna.

### Hasil dan Analisis
Dengan query citra `chelsea`, urutan retrieval berbasis histogram warna adalah:

1. `chelsea` — distance **0.0000**
2. `coins` — distance **0.2873**
3. `coffee` — distance **0.3638**
4. `astronaut` — distance **0.4619**
5. `camera` — distance **0.6032**

Citra yang paling mirip dengan query muncul di peringkat atas, terutama citra query itu sendiri. Namun, histogram warna masih memiliki keterbatasan karena hanya menangkap distribusi warna global, bukan bentuk atau tekstur objek.

### Kesimpulan
Histogram warna cukup efektif untuk database kecil, tetapi belum mampu membedakan citra secara semantik. Untuk CBIR yang lebih baik biasanya diperlukan fitur tambahan seperti tekstur, bentuk, atau embedding yang lebih kaya.

---

## E. Tabel Hasil Praktik

| No. | Nama Praktikum | Hasil Praktikum |
|---:|---|---|
| 1 | Menghitung Jarak Berbasis Piksel (L1 & L2) | Patch yang lebih mirip menghasilkan jarak yang lebih kecil. Patch 1 dan Patch 3 memiliki jarak lebih kecil dibanding Patch 1 dan Patch 2, baik untuk Euclidean maupun Manhattan. |
| 2 | Menghitung Cosine Similarity (Histogram Warna) | Citra identik menghasilkan similarity 1.0. Histogram warna cukup baik untuk mengukur kemiripan distribusi warna global. |
| 3 | Menghitung Structural Similarity Index (SSIM) | SSIM sama dengan 1.0 untuk citra identik, turun untuk noise dan blur, dan tetap tinggi untuk perubahan kontras. |
| 4 | Penerapan Template Matching | Template berhasil ditemukan pada citra `coins`. Metode ini tidak invariant terhadap rotasi dan skala. |
| 5 | Simulasi Content-Based Image Retrieval (CBIR) Sederhana | Citra dengan warna paling mirip muncul di peringkat atas. Histogram warna efektif untuk database kecil, tetapi masih terbatas secara semantik. |

## F. Penugasan

### 3. Fitur Berbeda untuk CBIR
Jika fitur histogram warna dibandingkan dengan fitur rata-rata warna (mean R, mean G, mean B), histogram warna lebih baik untuk database kecil ini. Alasan utamanya, histogram menyimpan distribusi warna yang lebih kaya, sedangkan mean RGB hanya menyimpan satu nilai rata-rata per kanal sehingga banyak informasi warna hilang.

Pada eksperimen ini, retrieval berbasis histogram menghasilkan urutan:

- `chelsea`
- `coins`
- `coffee`
- `astronaut`
- `camera`

Sedangkan retrieval berbasis mean RGB menghasilkan urutan:

- `chelsea`
- `astronaut`
- `coffee`
- `camera`
- `coins`

Hasil mean RGB terlalu kasar karena hanya melihat warna rata-rata global. Histogram lebih baik membedakan variasi warna dalam citra.

### 4. Template Matching Invariant
Metode `skimage.feature.match_template` standar **tidak invariant terhadap rotasi maupun perubahan skala**. Metode ini menghitung kecocokan berdasarkan korelasi template pada bentuk piksel asli, sehingga perubahan orientasi atau ukuran template akan menurunkan skor kecocokan.

Metode ini lebih cocok untuk objek yang posisinya berubah, tetapi ukuran dan orientasinya relatif sama. Jika ingin menangani rotasi atau skala, biasanya diperlukan preprocessing, multi-scale search, atau pendekatan fitur lain yang lebih robust.

## G. Kesimpulan
Jobsheet 5 membahas ukuran kemiripan dan pencarian citra melalui jarak piksel, histogram warna, SSIM, template matching, dan CBIR sederhana. Hasil eksperimen menunjukkan bahwa tidak semua fitur cocok untuk semua kasus: jarak piksel cocok untuk patch sederhana, histogram warna cocok untuk distribusi warna global, SSIM cocok untuk menilai struktur visual, sedangkan template matching dan CBIR memerlukan fitur yang lebih spesifik sesuai tujuan pencarian.
