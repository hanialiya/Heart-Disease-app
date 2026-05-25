import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model():
    with open('heart_disease_model.pkl', 'rb') as f:
        model_data = pickle.load(f)

    model = model_data['model']
    scaler = model_data['scaler']
    columns = model_data.get('features') or model_data.get('columns')
    return model, scaler, columns

model, scaler, columns = load_model()

# Custom CSS for beautiful styling
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    .main {
        padding-top: 2rem;
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 16px;
        font-weight: 600;
        padding: 12px 24px;
    }
    
    .header-style {
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    
    .header-style h1 {
        font-size: 48px;
        margin-bottom: 10px;
        font-weight: 700;
    }
    
    .header-style p {
        font-size: 18px;
        opacity: 0.95;
    }
    
    .param-section {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 2px solid #e0e7ff;
    }
    
    .param-section h3 {
        color: #2d3748;
        margin-bottom: 15px;
        font-size: 16px;
        font-weight: 600;
    }
    
    .result-positive {
        background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #d63031;
        color: #2d3748;
        box-shadow: 0 4px 12px rgba(214, 48, 49, 0.2);
    }
    
    .result-negative {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #00b894;
        color: #2d3748;
        box-shadow: 0 4px 12px rgba(0, 184, 148, 0.2);
    }
    
    .result-positive h2,
    .result-negative h2 {
        color: #2d3748;
        margin-bottom: 10px;
        font-size: 24px;
    }
    
    .result-positive p,
    .result-negative p {
        color: #2d3748;
        font-size: 15px;
        line-height: 1.6;
    }
    
    .alert-box {
        padding: 16px;
        border-radius: 10px;
        margin-top: 15px;
        font-weight: 600;
        color: #2d3748;
    }
    
    .alert-warning {
        background-color: #fff3cd;
        border-left: 5px solid #ffca2c;
    }
    
    .alert-success {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
    }
    
    .metric-box {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .metric-box h4 {
        color: #667eea;
        font-size: 14px;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-box p {
        color: #2d3748;
        font-size: 18px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-style">
    <h1>❤️ Heart Disease Prediction System</h1>
    <p>AI-Powered Medical Risk Assessment</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/808/808657.png", width=200)
    st.markdown("---")
    st.markdown("""
    ### 📋 Panduan Penggunaan
    
    **Langkah-langkah**:
    1. Masukkan data kesehatan Anda
    2. Klik tombol "Predict"
    3. Lihat hasil prediksi risiko
    
    **⚠️ Disclaimer**: 
    Aplikasi ini hanya untuk edukasi. 
    Bukan pengganti diagnosis dokter profesional.
    """)
    st.markdown("---")
    st.info("💡 Hubungi dokter untuk pemeriksaan lebih lanjut.")

# =========================
# ENCODING FUNCTIONS
# =========================
def encode_binary(val):
    return 1 if val == "Yes" else 0

def encode_gender(val):
    return 1 if val == "Male" else 0

def encode_level(val):
    return {
        "None": 0,
        "Low": 1,
        "Medium": 2,
        "High": 3
    }[val]

# Create tabs
tab1, tab2, tab3 = st.tabs(["🔮 Prediksi", "📊 Analisis", "ℹ️ Informasi"])

with tab1:
    st.subheader("📝 Masukkan Data Kesehatan Anda")
    
    # Row 1: Basic Info & Cardiovascular
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown('<div class="param-section"><h3>👤 Informasi Dasar</h3>', unsafe_allow_html=True)
        Age = st.number_input("Umur (Tahun)", 0, 100, 40, step=1)
        Gender = st.selectbox("Jenis Kelamin", ["Male", "Female"],
                             format_func=lambda x: "Laki-laki" if x == "Male" else "Perempuan")
        BMI = st.number_input("BMI", 15.0, 40.0, 25.0, step=0.1)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        st.markdown('<div class="param-section"><h3>💓 Kesehatan Kardiovaskular</h3>', unsafe_allow_html=True)
        Blood_Pressure = st.number_input("Tekanan Darah (mmHg)", 80, 200, 120)
        Cholesterol = st.number_input("Kolesterol (mg/dl)", 100, 400, 200)
        High_BP = st.selectbox("Hipertensi", ["No", "Yes"],
                              format_func=lambda x: "Ya" if x == "Yes" else "Tidak")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 2: Lifestyle & Risk Factors
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown('<div class="param-section"><h3>🏃 Gaya Hidup</h3>', unsafe_allow_html=True)
        Exercise = st.selectbox("Aktivitas Fisik", ["None","Low","Medium","High"],
                               format_func=lambda x: {"None": "Tidak Ada", "Low": "Rendah", "Medium": "Sedang", "High": "Tinggi"}[x])
        Smoking = st.selectbox("Merokok", ["No", "Yes"],
                              format_func=lambda x: "Ya" if x == "Yes" else "Tidak")
        Sleep = st.number_input("Jam Tidur", 3.0, 12.0, 7.0, step=0.5)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        st.markdown('<div class="param-section"><h3>⚠️ Faktor Risiko</h3>', unsafe_allow_html=True)
        Family = st.selectbox("Riwayat Keluarga", ["No", "Yes"],
                             format_func=lambda x: "Ada" if x == "Yes" else "Tidak")
        Diabetes = st.selectbox("Diabetes", ["No", "Yes"],
                               format_func=lambda x: "Ya" if x == "Yes" else "Tidak")
        Low_HDL = st.selectbox("HDL Rendah", ["No", "Yes"],
                              format_func=lambda x: "Ya" if x == "Yes" else "Tidak")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 3: Advanced Parameters (full width)
    st.markdown('<div class="param-section"><h3>🧪 Parameter Laboratorium</h3>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        High_LDL = st.selectbox("LDL Tinggi", ["No", "Yes"],
                               format_func=lambda x: "Ya" if x == "Yes" else "Tidak")
    with col2:
        Triglyceride = st.number_input("Triglyceride (mg/dl)", 50.0, 500.0, 200.0, step=1.0)
    with col3:
        FBS = st.number_input("Gula Darah Puasa (mg/dl)", 70.0, 200.0, 100.0, step=1.0)
    with col4:
        CRP = st.number_input("CRP (mg/L)", 0.0, 20.0, 5.0, step=0.1)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Homo = st.number_input("Homocysteine (µmol/L)", 0.0, 30.0, 10.0, step=0.1)
    with col2:
        Alcohol = st.selectbox("Konsumsi Alkohol", ["None","Low","Medium","High"],
                              format_func=lambda x: {"None": "Tidak Ada", "Low": "Rendah", "Medium": "Sedang", "High": "Tinggi"}[x])
    with col3:
        Stress = st.selectbox("Tingkat Stress", ["None","Low","Medium","High"],
                             format_func=lambda x: {"None": "Tidak Ada", "Low": "Rendah", "Medium": "Sedang", "High": "Tinggi"}[x])
    
    Sugar = st.selectbox("Konsumsi Gula", ["None","Low","Medium","High"],
                        format_func=lambda x: {"None": "Tidak Ada", "Low": "Rendah", "Medium": "Sedang", "High": "Tinggi"}[x])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Prediction Button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_btn = st.button("🔍 Lakukan Prediksi", use_container_width=True)
    
    if predict_btn:
        input_dict = {
            'age': Age,
            'gender': encode_gender(Gender),
            'blood_pressure': Blood_Pressure,
            'cholesterol_level': Cholesterol,
            'exercise_habits': encode_level(Exercise),
            'smoking': encode_binary(Smoking),
            'family_heart_disease': encode_binary(Family),
            'diabetes': encode_binary(Diabetes),
            'bmi': BMI,
            'high_blood_pressure': encode_binary(High_BP),
            'low_hdl_cholesterol': encode_binary(Low_HDL),
            'high_ldl_cholesterol': encode_binary(High_LDL),
            'alcohol_consumption': encode_level(Alcohol),
            'stress_level': encode_level(Stress),
            'sleep_hours': Sleep,
            'sugar_consumption': encode_level(Sugar),
            'triglyceride_level': Triglyceride,
            'fasting_blood_sugar': FBS,
            'crp_level': CRP,
            'homocysteine_level': Homo
        }

        input_df = pd.DataFrame([input_dict])
        input_df = input_df[columns]
        input_scaled = scaler.transform(input_df)
        
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]

        st.markdown("---")
        
        if prediction == 1:
            st.markdown(f"""
            <div class="result-positive">
                <h2>⚠️ HASIL: MEMILIKI PENYAKIT JANTUNG</h2>
                <p><b>Tingkat Kepercayaan Prediksi:</b> <span style="font-size:20px;color:#d63031">{probability[1]*100:.1f}%</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(
                '<div class="alert-box alert-warning">⚠️ Sangat disarankan untuk segera berkonsultasi dengan dokter spesialis jantung untuk pemeriksaan lebih mendalam.</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(f"""
            <div class="result-negative">
                <h2>✅ HASIL: TIDAK MEMILIKI PENYAKIT JANTUNG</h2>
                <p><b>Tingkat Kepercayaan Prediksi:</b> <span style="font-size:20px;color:#00b894">{probability[0]*100:.1f}%</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(
                '<div class="alert-box alert-success">✅ Tetap jaga kesehatan dengan pola hidup sehat dan pemeriksaan berkala.</div>',
                unsafe_allow_html=True
            )
        
        # Visualizations - Only Risk Factors
        st.markdown("<h3>📊 Profil Faktor Risiko</h3>", unsafe_allow_html=True)
        risk_factors = {
            'Umur': Age / 100 * 100,
            'BMI': BMI / 40 * 100,
            'T. Darah': Blood_Pressure / 200 * 100,
            'Kolesterol': Cholesterol / 400 * 100,
        }
        
        fig2 = go.Figure(go.Bar(
            y=list(risk_factors.keys()),
            x=list(risk_factors.values()),
            orientation='h',
            marker=dict(
                color=['#FF6B6B', '#FFA500', '#FFD700', '#90EE90'],
                line=dict(color='#2d3748', width=1.5)
            ),
            text=[f"{v:.0f}%" for v in risk_factors.values()],
            textposition='outside'
        ))
        
        fig2.update_layout(
            title="Perbandingan Faktor Risiko",
            xaxis_title="Tingkat (%)",
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("📊 Interpretasi Hasil Prediksi")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-box">
            <h4>Risiko Rendah</h4>
            <p>0 - 30%</p>
            <p style="font-size:12px;color:#999">Profil kesehatan baik</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box">
            <h4>Risiko Sedang</h4>
            <p>30 - 70%</p>
            <p style="font-size:12px;color:#999">Perlu perhatian lebih</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box">
            <h4>Risiko Tinggi</h4>
            <p>70 - 100%</p>
            <p style="font-size:12px;color:#999">Konsultasi dokter</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🩺 Parameter yang Digunakan
    
    **Demografi:**
    - Umur dan Jenis Kelamin
    
    **Kardiovaskular:**
    - Tekanan Darah
    - Kadar Kolesterol
    - Hipertensi
    
    **Gaya Hidup:**
    - Aktivitas Fisik
    - Status Merokok
    - Jam Tidur
    - Konsumsi Alkohol dan Gula
    - Tingkat Stress
    
    **Faktor Genetik:**
    - Riwayat Keluarga
    - Diabetes
    
    **Laboratorium:**
    - Kolesterol HDL/LDL
    - Triglyceride
    - Gula Darah Puasa
    - CRP (Inflamasi)
    - Homocysteine
    - BMI
    """)

with tab3:
    st.subheader("ℹ️ Tentang Aplikasi Ini")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🤖 Model AI
        
        - **Algoritma**: Random Forest Classifier
        - **Akurasi**: Model terlatih dengan data medis komprehensif
        - **Input**: 20 parameter kesehatan
        - **Output**: Probabilitas risiko penyakit jantung
        
        ### 📈 Metodologi
        
        - Data preprocessing dan normalisasi
        - Feature scaling dengan StandardScaler
        - Random Forest ensemble learning
        - Cross-validation untuk akurasi optimal
        """)
    
    with col2:
        st.markdown("""
        ### ⚠️ Disclaimer Penting
        
        ⚠️ **Aplikasi ini hanya untuk keperluan edukasi dan informasi**
        
        - Bukan pengganti diagnosis profesional
        - Hasil prediksi bersifat estimatif
        - Selalu konsultasikan dengan dokter bersertifikat
        - Data tidak disimpan atau dibagikan
        
        ### 🎯 Rekomendasi
        
        1. Lakukan pemeriksaan kesehatan berkala
        2. Jaga pola hidup sehat
        3. Hindari faktor risiko (merokok, alkohol)
        4. Olahraga minimal 150 menit/minggu
        5. Konsultasi dokter jika ada gejala
        """)
    
    st.markdown("---")
    st.info("📧 Untuk pertanyaan atau feedback, silakan hubungi tim pengembang.")