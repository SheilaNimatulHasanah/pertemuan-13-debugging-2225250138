# Pertemuan 13 - Debugging dan Testing

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Kasus
Program yang diuji adalah program pengolah data nilai mahasiswa yang bertugas menghitung rata-rata nilai, menentukan status kelulusan (dengan batas nilai minimal 60), serta mencari nilai tertinggi. Pada program awal, terdapat beberapa kesalahan logika (*logical error*) yang menyebabkan hasil perhitungan dan pengkondisian menjadi salah.

## Test Case
| ID | Target | Input | Expected | Actual Awal | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T1 | rata-rata | `[80, 60, 90, 70]` | 75.0 | 60.0 | FAIL |
| T2 | rata-rata | `[100, 80]` | 90.0 | 36.0 | FAIL |
| T3 | status | `60` | Lulus | Tidak lulus | FAIL |
| T4 | status | `59` | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | `[80, 60, 90, 70]` | 90 | 0 | FAIL |

## Bug Report
* **Bug B01 (Fungsi `hitung_rata_rata`)**:
  * **Gejala**: Output rata-rata bernilai salah (T1 menghasilkan `60.0` alih-alih `75.0`, T2 menghasilkan `36.0` alih-alih `90.0`).
  * **Test Case**: T1, T2.
  * **Lokasi**: Fungsi `hitung_rata_rata()` pada bagian baris pembagian.
  * **Akar Penyebab**: Pembagi nilai di-hardcode dengan angka konstan `5` (`sum(nilai) / 5`), sehingga tidak fleksibel terhadap jumlah elemen list yang sebenarnya (`len(nilai)`).
  * **Perbaikan**: Mengubah pembagi menjadi `len(nilai)` serta menambahkan penanganan kondisi jika list kosong (`if len(nilai) == 0: return 0`).

* **Bug B02 (Fungsi `status`)**:
  * **Gejala**: Nilai tepat `60` menghasilkan status `"Tidak lulus"`.
  * **Test Case**: T3.
  * **Lokasi**: Fungsi `status()` pada bagian perbandingan `if nilai > 60:`.
  * **Akar Penyebab**: Menggunakan operator lebih dari (`>`), sehingga nilai batas `60` tidak termasuk dalam kategori lulus.
  * **Perbaikan**: Mengubah operator perbandingan menjadi lebih dari atau sama dengan (`>=`), yaitu `if nilai >= 60:`.

* **Bug B03 (Fungsi `nilai_tertinggi`)**:
  * **Gejala**: Output nilai tertinggi selalu menghasilkan `0`.
  * **Test Case**: T5.
  * **Lokasi**: Fungsi `nilai_tertinggi()` pada inisialisasi variabel dan pembandingan `if x < tertinggi:`.
  * **Akar Penyebab**: Variabel `tertinggi` diinisialisasi dengan angka `0` dan menggunakan operator pembanding yang salah (`<` alih-alih `>`).
  * **Perbaikan**: Menginisialisasi `tertinggi = nilai[0]` dan memperbarui perbandingan menjadi `if x > tertinggi:`.

## Retest
| ID | Target | Input | Expected | Actual Akhir | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| T1 | rata-rata | `[80, 60, 90, 70]` | 75.0 | 75.0 | PASS |
| T2 | rata-rata | `[100, 80]` | 90.0 | 90.0 | PASS |
| T3 | status | `60` | Lulus | Lulus | PASS |
| T4 | status | `59` | Tidak lulus | Tidak lulus | PASS |
| T5 | tertinggi | `[80, 60, 90, 70]` | 90 | 90 | PASS |

## Cara Menjalankan
Buka terminal VS Code di root folder proyek, lalu jalankan perintah:
```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi
Teknik debugging yang paling membantu adalah memanfaatkan fitur **Debugger VS Code** (menggunakan *Breakpoint*, *Step Over*, dan *Step Into*) serta menyusun **Tabel Test Case**. Fitur breakpoint dan pengamatan variabel membantu kita menelusuri alur eksekusi baris demi baris, sehingga dapat menemukan akar penyebab *logical error* secara pasti tanpa harus menebak-nebak kode yang salah.