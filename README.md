# 😄 Smile Detection

Proyek deteksi senyum secara real-time menggunakan webcam dengan **OpenCV** dan algoritma **Haar Cascade Classifier**.

## 📋 Deskripsi

Program ini menggunakan kamera secara langsung untuk:
- Mendeteksi **wajah** manusia di dalam frame
- Mendeteksi **senyum** di dalam area wajah yang terdeteksi
- Menampilkan kotak pembatas (bounding box) di sekitar wajah dan senyum secara real-time

## 🛠️ Teknologi

| Library | Kegunaan |
|---------|----------|
| `opencv-python` | Computer vision & pemrosesan gambar |
| `haarcascade_frontalface_default.xml` | Model deteksi wajah (built-in OpenCV) |
| `smile_ref.xml` | Model deteksi senyum (custom) |

## 📁 Struktur Proyek

```
smile detect/
├── main.py           # Program utama
├── smile_ref.xml     # Haar cascade classifier untuk senyum
├── .gitignore
└── README.md
```

## ⚙️ Instalasi

1. **Clone repository ini** atau download file-nya.

2. **Buat virtual environment** (opsional tapi disarankan):
   ```bash
   python -m venv virtual
   virtual\Scripts\activate   # Windows
   ```

3. **Install dependensi:**
   ```bash
   pip install opencv-python
   ```

## 🚀 Cara Menjalankan

```bash
python main.py
```

Pastikan webcam kamu sudah terhubung sebelum menjalankan program.

## 🎮 Kontrol

| Tombol | Aksi |
|--------|------|
| `Q` | Keluar dari program |

## 🔍 Cara Kerja

1. Program membuka webcam dan membaca frame secara terus-menerus.
2. Setiap frame dikonversi ke **grayscale** untuk efisiensi deteksi.
3. **Detect wajah** menggunakan `haarcascade_frontalface_default.xml`:
   - `scaleFactor`: 1.1
   - `minNeighbors`: 5
   - `minSize`: 80×80 px
4. Untuk setiap wajah yang terdeteksi, **detect senyum** di dalam ROI (Region of Interest) wajah menggunakan `smile_ref.xml`:
   - `scaleFactor`: 1.7
   - `minNeighbors`: 20
   - `minSize`: 25×25 px
5. Visualisasi:
   - 🔴 Kotak **merah** → area wajah
   - 🟢 Kotak **hijau** + teks "Smile :)" → senyum terdeteksi

## 📌 Catatan

- Pastikan pencahayaan ruangan cukup untuk hasil deteksi yang optimal.
- File `smile_ref.xml` harus berada di direktori yang sama dengan `main.py`.
- Program menggunakan kamera dengan index `0` (kamera default). Ganti angkanya jika kamu menggunakan kamera eksternal.

## 👤 Author

**Rafie** — Semester 6 · Belajar Python & Computer Vision
