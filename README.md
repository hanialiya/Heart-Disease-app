# ❤️ Heart Disease Prediction System - Enhanced Edition

Aplikasi **Streamlit** yang elegan dan komprehensif untuk memprediksi risiko penyakit jantung menggunakan Machine Learning model Random Forest dengan **20 parameter kesehatan lengkap**.

## 🎯 Fitur Utama

- **🔮 Prediksi Real-time**: Input 20 parameter kesehatan dengan interface yang intuitif
- **📊 Visualisasi Interaktif**: Gauge chart risiko dan bar chart kontribusi faktor
- **💡 Interface Modern**: UI yang clean dengan design responsif dan profesional
- **📋 Multiple Tabs**:
  - **Prediksi**: Input data kesehatan dengan layout 3 kolom terorganisir
  - **Analisis Risiko**: Detail parameter berdasarkan kategori kesehatan
  - **Informasi**: Dokumentasi lengkap sistem dan rekomendasi pencegahan

## 📋 Parameter Input Lengkap (20 Parameter)

### 👤 **Demografi**

- **Age**: Usia pasien (20-80 tahun)
- **Gender**: Jenis kelamin (Male/Female)

### 🏃‍♂️ **Gaya Hidup**

- **Exercise Habits**: Aktivitas fisik (Low/Medium/High)
- **Smoking**: Kebiasaan merokok (No/Yes)
- **Alcohol Consumption**: Konsumsi alkohol (Low/Medium/High)
- **Sleep Hours**: Jam tidur per malam (3-12 jam)
- **Sugar Consumption**: Konsumsi gula (Low/Medium/High)
- **Stress Level**: Tingkat stress (Low/Medium/High)

### 🧬 **Riwayat Kesehatan**

- **Family Heart Disease**: Riwayat keluarga (No/Yes)
- **Diabetes**: Riwayat diabetes (No/Yes)

### 💓 **Kardiovaskular**

- **Blood Pressure**: Tekanan darah (80-200 mmHg)
- **High Blood Pressure**: Hipertensi (No/Yes)

### 🩸 **Profil Lipid**

- **Cholesterol Level**: Kolesterol total (100-400 mg/dl)
- **Low HDL Cholesterol**: HDL rendah (No/Yes)
- **High LDL Cholesterol**: LDL tinggi (No/Yes)
- **Triglyceride Level**: Triglyceride (50-500 mg/dl)

### 🩺 **Biomarker**

- **BMI**: Body Mass Index (15-40)
- **Fasting Blood Sugar**: Gula darah puasa (70-200 mg/dl)
- **CRP Level**: C-Reactive Protein (0-20 mg/L)
- **Homocysteine Level**: Homocysteine (0-30 µmol/L)

## 🚀 Cara Menggunakan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Pastikan File Model Lengkap

Folder harus berisi:

- `rf_model.pkl` - Model Random Forest terlatih
- `scaler.pkl` - StandardScaler untuk normalisasi data
- `columns.pkl` - Urutan kolom untuk input data
- `app.py` - File aplikasi Streamlit
- `requirements.txt` - Dependencies

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## 📊 Cara Kerja Sistem

1. **Input Data**: Masukkan 20 parameter kesehatan di tab Prediksi
2. **Preprocessing**: Data di-encode dan dinormalisasi sesuai training
3. **Prediction**: Model Random Forest menghasilkan prediksi probabilitas
4. **Output**:
   - Status risiko (Tinggi/Rendah) dengan styling visual
   - Probabilitas persen dengan gauge chart interaktif
   - Analisis kontribusi faktor risiko

## 🎨 Interface Features

### Styling & Design

- ✅ Header gradient yang elegan (ungu-biru)
- ✅ Layout responsif dengan 3 kolom input terorganisir
- ✅ Parameter grouping dengan card design
- ✅ Color coding intuitif (hijau=aman, kuning=warning, merah=risiko)
- ✅ Sidebar dengan guidance dan disclaimer
- ✅ Custom CSS untuk pengalaman pengguna yang lebih baik

### Visualisations

- **Gauge Chart**: Menampilkan persentase risiko dengan color coding
- **Bar Chart**: Analisis kontribusi 7 faktor risiko utama
- **Expandable Sections**: Kategori parameter kesehatan yang dapat dilipat
- **Data Tables**: Ringkasan parameter dengan kategori

### Navigation

- **3 Main Tabs**: Prediksi, Analisis, Informasi
- **Expandable Categories**: 9 kategori parameter kesehatan
- **Responsive Design**: Mobile-friendly interface

## ⚠️ Disclaimer Penting

- ⚠️ Aplikasi ini **HANYA untuk tujuan edukasi dan demonstrasi**
- Hasil prediksi **BUKAN pengganti diagnosis medis profesional**
- Selalu konsultasikan dengan dokter spesialis untuk evaluasi kesehatan yang akurat
- Data pasien tidak disimpan atau dibagikan

## 📊 Model Information

- **Algorithm**: Random Forest Classifier
- **Training Data**: Comprehensive Heart Disease Dataset
- **Features**: 20 parameter kesehatan lengkap
- **Target**: Binary classification (High Risk/Low Risk)
- **Preprocessing**: Label encoding + StandardScaler normalization

## 📝 Parameter Categories

| Kategori       | Jumlah Parameter | Contoh                                           |
| -------------- | ---------------- | ------------------------------------------------ |
| Demografi      | 2                | Age, Gender                                      |
| Gaya Hidup     | 6                | Exercise, Smoking, Alcohol, Sleep, Sugar, Stress |
| Riwayat        | 2                | Family History, Diabetes                         |
| Kardiovaskular | 2                | Blood Pressure, Hypertension                     |
| Lipid          | 4                | Cholesterol, HDL, LDL, Triglyceride              |
| Biomarker      | 4                | BMI, FBS, CRP, Homocysteine                      |

## 🎯 Rekomendasi Pencegahan

1. **Diet Sehat**: Kurangi garam (<5g/hari), lemak jenuh, dan gula
2. **Olahraga Teratur**: 150 menit per minggu aktivitas sedang
3. **Berhenti Merokok**: Konsultasi program stop merokok
4. **Kontrol Berat Badan**: BMI 18.5-24.9
5. **Pantau Kesehatan**: Pemeriksaan rutin tekanan darah, kolesterol
6. **Kelola Stress**: Teknik relaksasi, meditasi, istirahat cukup
7. **Kontrol Diabetes**: Pantau gula darah secara teratur

## 💬 Support & Feedback

Untuk perbaikan atau saran, silakan hubungi developer.

---

**Dibuat dengan ❤️ menggunakan Streamlit & Machine Learning**
**Enhanced Design - Professional Medical AI Assistant**

```bash
streamlit run app.py
```

Aplikasi akan membuka di browser pada `http://localhost:8501`

## 📊 Cara Kerja

1. **Input Data**: Masukkan data kesehatan pasien di tab Prediksi
2. **Preprocessing**: Data akan dinormalisasi menggunakan StandardScaler
3. **Prediction**: Model Random Forest membuat prediksi
4. **Output**:
   - Status risiko (Tinggi/Rendah)
   - Probabilitas dalam persen
   - Visualisasi gauge chart

## ⚠️ Disclaimer Penting

- ⚠️ Aplikasi ini **HANYA untuk tujuan edukasi dan demonstrasi**
- Hasil prediksi **BUKAN pengganti diagnosis medis profesional**
- Selalu konsultasikan dengan dokter spesialis untuk evaluasi kesehatan yang akurat
- Data pasien tidak disimpan atau dibagikan

## 📊 Model Information

- **Algorithm**: Random Forest Classifier
- **Training Data**: Heart Disease UCI Dataset (303 sampel)
- **Features**: 13 parameter kesehatan
- **Target**: Binary classification (Berisiko/Tidak Berisiko)
- **Preprocessing**: StandardScaler normalization

## 🎨 Interface Features

### Styling

- Gradient header dengan tema ungu
- Warna-warna yang intuitif (hijau=aman, kuning=warning, merah=berisiko)
- Responsive design yang mobile-friendly
- Custom CSS untuk pengalaman pengguna yang lebih baik

### Visualisations

- **Gauge Chart**: Menampilkan persentase risiko dengan color coding
- **Bar Chart**: Analisis faktor-faktor risiko
- **Data Table**: Tabel ringkasan parameter

## 📝 Notes

- Semua input memiliki validasi range untuk keamanan data
- Model menggunakan algoritma Random Forest yang robust
- Scaler diload sekali saja untuk efisiensi (caching)
- Hasil prediksi ditampilkan dengan confidence probabilitas

## 💬 Feedback & Suggestions

Untuk perbaikan atau saran, silakan hubungi developer.

---

**Dibuat dengan ❤️ menggunakan Streamlit & Machine Learning**
