# import streamlit as st
# import pickle
# import pandas as pd
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

# # =========================================================================
# # 1. KONFIGURASI HALAMAN
# # =========================================================================
# st.set_page_config(
#     page_title="KosIn - Cari dan Prediksi Harga Kos",
#     page_icon="🏠",
#     layout="wide"
# )

# # PAKSA STREAMLIT MENGGUNAKAN LIGHT THEME (Biar Dropdown Otomatis Putih & Teks Hitam)
# st.config.set_option("theme.base", "light")
# st.config.set_option("theme.primaryColor", "#14213d")
# st.config.set_option("theme.backgroundColor", "#ffffff")
# st.config.set_option("theme.secondaryBackgroundColor", "#e5e5e5")
# st.config.set_option("theme.textColor", "#000000")


# # =========================================================================
# # 2. LOAD FILE PKL & DATA
# # =========================================================================
# @st.cache_resource
# def load_ml_components():
#     with open('../models/model_kos.pkl', 'rb') as f:
#         model = pickle.load(f)
#     with open('../models/model_columns.pkl', 'rb') as f:
#         cols = pickle.load(f)
#     return model, cols

# @st.cache_data
# def load_database():
#     return pd.read_csv('../data/Data_Indekos_Jabodetabek_Mamikos_Cleaned.csv')

# rf_model, model_columns = load_ml_components()
# df_cleaned = load_database()


# # =========================================================================
# # 3. CUSTOM CSS UTUH & TERBARU (FIGMA ALIGNMENT)
# # =========================================================================
# st.markdown("""
#     <style>
#     /* ===== 1. BACKGROUND & LAYOUT ===== */
#     .stApp {
#         background-color: #ffffff !important;
#     }
#     .block-container { 
#         padding: 3rem 6rem !important; 
#     }
            
#         /* =========================================================================
#     LOGO KOSIN
#     ========================================================================= */
#     .kosin-logo {
#     font-weight: bold !important;
#     font-size: 40px !important;
#     color: #14213d !important;
#     margin-top: 0 !important;
#     margin-bottom: 0 !important;
#     padding-bottom: 0 !important;
#     line-height: 1 !important;
#     }
    
#         /* =========================================================================
#     DIVIDER
#     ========================================================================= */
#     div[data-testid="stDivider"] {
#         margin-top: 0rem !important;
#         margin-bottom: 0rem !important;
#     }
#     div[data-testid="stDivider"] hr {
#         margin-top: 0rem !important;
#         margin-bottom: 0rem !important;
#     }

#     /* ===== 2. TIPOGRAFI ===== */
#     # h1, h3, h4, h5, p, span, label, caption, div[data-testid="stWidgetLabel"] p {
#     #     color: #000000 !important;
#     #     font-family: 'Inter', 'Segoe UI', sans-serif !important;
#     # }
#     .sub-deskripsi {
#         color: #64748B !important;
#         font-size: 16px !important;
#         line-height: 1.6 !important;
#         margin-top: 8px !important;
#         margin-bottom: 24px !important;
#     }

#     /* ===== 3. KOTAK FORM UTAMA =====
#        FIX #1: Selector lebih spesifik — hanya menarget container LANGSUNG
#        di dalam col_kiri, bukan semua VerticalBlockBorderWrapper */
#     /* Ganti yang lama dengan ini */
#     div[data-testid="stColumn"]:first-child 
#     div[data-testid="stHorizontalBlock"] 
#     div[data-testid="stVerticalBlockBorderWrapper"] {
#         background-color: transparent !important;
#         padding: 0px !important;
#         box-shadow: none !important;
#         border-radius: 0px !important;
#         border: none !important;
#     }
#     /* ===== 4. DROPDOWN / SELECTBOX =====
#        FIX #2: Pisahkan styling kotak utama vs list melayang dengan lebih tegas */
    
#     /* Kotak input utama */
#     div[data-baseweb="select"] {
#         border: 1px solid #CBD5E1 !important;
#         border-radius: 8px !important;
#     }
#     div[data-baseweb="select"] > div:first-child {
#         background-color: #ffffff !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Teks dan ikon di kotak input */
#     div[data-baseweb="select"] span,
#     div[data-baseweb="select"] div[class*="singleValue"],
#     div[data-baseweb="select"] div[class*="placeholder"] {
#         color: #000000 !important;
#     }
#     div[data-baseweb="select"] svg {
#         fill: #000000 !important;
#     }

#     /* List melayang — FIX UTAMA: paksa background putih dan teks hitam */
#     div[data-baseweb="popover"] {
#         background-color: #ffffff !important;
#     }
#     ul[role="listbox"] {
#         background-color: #ffffff !important;
#         border: 1px solid #E5E5E5 !important;
#         border-radius: 8px !important;
#         padding: 4px !important;
#     }
#     /* Setiap item list: background putih, teks hitam — ini yang paling penting */
#     ul[role="listbox"] li {
#         background-color: #ffffff !important;
#         color: #000000 !important;
#     }
#     ul[role="listbox"] li * {
#         color: #000000 !important;
#         background-color: transparent !important;
#     }
#     /* Hover & selected item */
#     ul[role="listbox"] li:hover,
#     ul[role="listbox"] li[aria-selected="true"] {
#         background-color: #14213d !important;
#     }
#     ul[role="listbox"] li:hover *,
#     ul[role="listbox"] li[aria-selected="true"] * {
#         color: #ffffff !important;
#         background-color: transparent !important;
#     }

#     /* ===== 5. CHECKBOX ===== */
#     div[data-testid="stCheckbox"] div[role="checkbox"] {
#         background-color: #e5e5e5 !important;
#         border: 1px solid #CBD5E1 !important;
#         border-radius: 4px !important;
#     }
#     div[data-testid="stCheckbox"] label {
#         gap: 10px !important;
#     }

#         /* ===== RADIO BUTTON ===== */

#     /* Hilangkan highlight background di area label */
#     div[data-testid="stRadio"] label,
#     div[data-testitem="stRadio"] label * {
#         background-color: transparent !important;
#         background: none !important;
#         box-shadow: none !important;
#         border: none !important;
#     }

#     /* Lingkaran radio — DIAM: abu-abu */
#     div[data-testid="stRadio"] div[role="radio"] {
#         background-color: #e5e5e5 !important;
#         border: 2px solid #CBD5E1 !important;
#         border-radius: 50% !important;
#     }

#     /* Lingkaran radio — DIPILIH: biru */
#     div[data-testid="stRadio"] div[data-checked="true"] {
#         background-color: #1a73e8 !important;
#         border-color: #1a73e8 !important;
#         border-radius: 50% !important;
#     }

#     /* Titik putih di dalam saat dipilih */
#     div[data-testid="stRadio"] div[data-checked="true"] > div {
#         background-color: #ffffff !important;
#     }

#     /* ===== 7. SLIDER ===== */
#     div[data-testid="stSlider"] div {
#         color: #000000 !important;
#     }

#         /* ===== BUTTON LIHAT PREDIKSI ===== */

#         /* Kondisi NORMAL: biru, teks putih */
#     div.stButton > button {
#         background-color: #14213d !important;
#         color: #ffffff !important;
#         border-radius: 10px !important;
#         padding: 0.8rem !important;
#         font-weight: bold !important;
#         border: none !important;
#         font-size: 16px !important;
#         width: 100% !important;
#     }

#     /* Paksa span di dalam button ikut putih */
#     div.stButton > button span {
#         color: #ffffff !important;
#     }

#     /* Kondisi HOVER: oranye, teks hitam */
#     div.stButton > button:hover {
#         background-color: #fca311 !important;
#         color: #000000 !important;
#     }

#     /* Paksa span di dalam button saat hover ikut hitam */
#     div.stButton > button:hover span {
#         color: #000000 !important;
#     }
#     /* Tombol Kembali */
#     div.stButton > button[key="back_btn"] {
#         background-color: transparent !important;
#         color: #14213d !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     div.stButton > button[key="back_btn"]:hover {
#         background-color: transparent !important;
#         color: #fca311 !important;
#         box-shadow: none !important;
#     }

#     /* ===== 9. BANNER KANAN ===== */
#     .right-image-banner img { 
#         border-radius: 20px !important; 
#         object-fit: cover !important; 
#         height: 1080px !important;
#         width: 100% !important;
#         box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.05) !important;
#     }

#     /* ===== 10. HALAMAN HASIL ===== */
#     .prediction-banner {
#         background-color: #14213d; 
#         color: #ffffff !important; 
#         padding: 50px;
#         border-radius: 20px; 
#         text-align: center; 
#         margin-bottom: 2.5rem;
#     }
#     .prediction-banner p, .prediction-banner div, .prediction-banner span {
#         color: #ffffff !important;
#     }
#     .price-text { 
#         color: #fca311 !important; 
#         font-size: 56px; 
#         font-weight: bold; 
#         margin: 15px 0; 
#     }
#     .badge-container { 
#         display: flex; 
#         justify-content: center; 
#         gap: 15px; 
#         margin-top: 20px; 
#     }
#     .badge-custom { 
#         background-color: rgba(255, 255, 255, 0.12); 
#         padding: 8px 20px; 
#         border-radius: 24px; 
#         font-size: 14px; 
#         border: 1px solid rgba(255, 255, 255, 0.2); 
#     }
#     .accent-link { 
#         text-align: right; 
#         color: #fca311 !important; 
#         font-weight: bold; 
#         font-size: 15px;
#     }
#     </style>
# """, unsafe_allow_html=True)


# # =========================================================================
# # 4. ENGINE SISTEM REKOMENDASI (Cosine Similarity)
# # =========================================================================
# def get_top_5_recommendations(user_input_processed, df_cleaned):
#     fasilitas_user = [col for col in user_input_processed.columns if col != 'room_area' and user_input_processed[col].iloc[0] == 1.0]
    
#     if len(fasilitas_user) == 0:
#         fasilitas_user = [col for col in user_input_processed.columns if col != 'room_area']
        
#     features_database = df_cleaned[fasilitas_user]
#     user_features = user_input_processed[fasilitas_user]
#     sim_fasilitas = cosine_similarity(user_features, features_database)[0]
    
#     luas_user = user_input_processed['room_area'].iloc[0]
#     luas_db = df_cleaned['room_area'].values
#     sim_luas = 1 / (1 + np.abs(luas_db - luas_user))
    
#     df_cleaned['similarity'] = (sim_fasilitas * 0.7) + (sim_luas * 0.3)
    
#     wilayah_user = st.session_state.get('selected_region', 'Pilih Wilayah di Jakarta')
#     df_filtered = df_cleaned.copy()
#     if wilayah_user != 'Pilih Wilayah di Jakarta':
#         df_filtered = df_filtered[df_filtered['region'] == wilayah_user]
    
#     return df_filtered.sort_values(by='similarity', ascending=False).head(5)


# if 'halaman' not in st.session_state:
#     st.session_state.halaman = 'input'


# # =========================================================================
# # 5. HALAMAN 1: INPUT FORM
# # =========================================================================
# def tampilkan_halaman_input():
#     st.markdown("<p class='kosin-logo'>KosIn</p>", unsafe_allow_html=True)
#     st.markdown("""
#     <style>
#     /* Hapus border di grid fasilitas halaman input */
#     div[data-testid="stHorizontalBlock"] div[data-testid="stVerticalBlockBorderWrapper"] {
#         background-color: transparent !important;
#         padding: 0px !important;
#         box-shadow: none !important;
#         border-radius: 0px !important;
#         border: none !important;
#     }
#     </style>
# """, unsafe_allow_html=True)
#     # Ganti st.divider() dengan ini
#     st.markdown("<hr style='border-top: 1px solid #E5E5E5; margin: 8px 0 16px 0;'>", unsafe_allow_html=True)
    
#     col_kiri, col_kanan = st.columns([1.2, 1])
    
#     with col_kiri:
#         st.markdown("<h1 style='font-weight: 800; margin-bottom: 0;'>Cari Prediksi Harga Kos</h1>", unsafe_allow_html=True)
#         st.markdown("<p class='sub-deskripsi'>Masukkan detail untuk mengetahui estimasi harga pasar. Dapatkan analisis harga berbasis data untuk hunian ideal Anda.</p>", unsafe_allow_html=True)
#         st.markdown("<p style='font-size: 14px; margin-bottom: 20px;'><span style='color: #fca311;'>🟠</span> <b>1</b> Pilih Lokasi &nbsp;&nbsp;&nbsp; <span style='color: #CBD5E1;'>⚪</span> <b>2</b> Fasilitas &nbsp;&nbsp;&nbsp; <span style='color: #CBD5E1;'>⚪</span> <b>3</b> Hasil</p>", unsafe_allow_html=True)
        
#         with st.container(border=True):
#             lokasi = st.selectbox(
#                 "Lokasi / Area",
#                 ["Pilih Wilayah di Jakarta", "Jakarta Barat", "Jakarta Pusat","Jakarta Selatan", "Jakarta Timur", "Jakarta Utara"]
#             )
#             luas_kamar = st.slider("Luas Kamar (m2)", min_value=4, max_value=40, value=10, step=1)
#             tipe_kos = st.radio("Tipe Kos", ["Kos Campur", "Kos Putra", "Kos Putri"], horizontal=True)
            
#             st.write("---")
#             st.markdown("<h5 style='font-weight: bold; margin-bottom: 15px;'>Fasilitas Utama <span style='font-size:12px; color:gray; font-weight: normal;'>(Pilih minimal 1)</span></h5>", unsafe_allow_html=True)
            
#             st.caption("Fasilitas Kamar")
#             f_kamar_col1, f_kamar_col2, f_kamar_col3 = st.columns(3)
#             with f_kamar_col1:
#                 ac = st.checkbox("AC")
#                 listrik = st.checkbox("Termasuk Listrik")
#                 kipas = st.checkbox("Kipas Angin")
#             with f_kamar_col2:
#                 wifi = st.checkbox("WiFi")
#                 furnished = st.checkbox("Full Furnished")
#                 udara = st.checkbox("Sirkulasi Udara")
#             with f_kamar_col3:
#                 laundry = st.checkbox("Laundry")
#                 tv = st.checkbox("TV")
                
#             st.caption("Furnitur Kamar")
#             furnitur_col1, furnitur_col2, furnitur_col3 = st.columns(3)
#             with furnitur_col1:
#                 bantal = st.checkbox("Bantal")
#                 kursi = st.checkbox("Kursi")
#             with furnitur_col2:
#                 guling = st.checkbox("Guling")
#             with furnitur_col3:
#                 cermin = st.checkbox("Cermin")

#             st.caption("Kamar Mandi")
#             km_col1, km_col2, km_col3 = st.columns(3)
#             with km_col1:
#                 km_dalam = st.checkbox("Kamar Mandi Dalam")
#                 air_panas = st.checkbox("Air Panas")
#                 bak_mandi = st.checkbox("Bak Mandi")
#             with km_col2:
#                 kloset_duduk = st.checkbox("Kloset Duduk")
#                 wastafel = st.checkbox("Wastafel")
#             with km_col3:
#                 shower = st.checkbox("Shower")
#                 ember = st.checkbox("Ember Mandi")

#             st.caption("Fasilitas Umum & Bersama")
#             fu_col1, fu_col2, fu_col3 = st.columns(3)
#             with fu_col1:
#                 p_motor = st.checkbox("Parkir Motor")
#                 r_bersama = st.checkbox("Ruang Bersama")
#                 d_bersama = st.checkbox("Dapur Bersama")
#             with fu_col2:
#                 p_mobil = st.checkbox("Parkir Mobil")
#                 l_kebersihan = st.checkbox("Layanan Kebersihan")
#                 k_bersama = st.checkbox("Kulkas Bersama")
#             with fu_col3:
#                 cctv = st.checkbox("Keamanan / CCTV")
#                 jemur = st.checkbox("Area Jemur")
#                 dispenser = st.checkbox("Dispenser Bersama")
#                 mesin_cuci = st.checkbox("Mesin Cuci")
                
#             st.write("")
            
#             if st.button("Lihat Prediksi", use_container_width=True):
#                 user_input_df = pd.DataFrame(0.0, index=[0], columns=model_columns)
#                 user_input_df['room_area'] = float(luas_kamar)
                
#                 user_input_df['fac_ac'] = 1.0 if ac else 0.0
#                 user_input_df['is_electricity'] = 1.0 if listrik else 0.0
#                 user_input_df['fac_kipas_angin'] = 1.0 if kipas else 0.0
#                 user_input_df['fac_wifi'] = 1.0 if wifi else 0.0
#                 user_input_df['is_full_furnished'] = 1.0 if furnished else 0.0
#                 user_input_df['fac_sirkulasi_udara'] = 1.0 if udara else 0.0
#                 user_input_df['fac_tv'] = 1.0 if tv else 0.0
#                 user_input_df['fac_bantal'] = 1.0 if bantal else 0.0
#                 user_input_df['fac_kursi'] = 1.0 if kursi else 0.0
#                 user_input_df['fac_guling'] = 1.0 if guling else 0.0
#                 user_input_df['fac_cermin'] = 1.0 if cermin else 0.0
#                 user_input_df['is_kamar_mandi_dalam'] = 1.0 if km_dalam else 0.0
#                 user_input_df['fac_air_panas'] = 1.0 if air_panas else 0.0
#                 user_input_df['fac_bak_mandi'] = 1.0 if bak_mandi else 0.0
#                 user_input_df['is_kloset_duduk'] = 1.0 if kloset_duduk else 0.0
#                 user_input_df['fac_wastafel'] = 1.0 if wastafel else 0.0
#                 user_input_df['fac_shower'] = 1.0 if shower else 0.0
#                 user_input_df['fac_ember_mandi'] = 1.0 if ember else 0.0
#                 user_input_df['fac_parkir_motor'] = 1.0 if p_motor else 0.0
#                 user_input_df['fac_ruang_bersama'] = 1.0 if r_bersama else 0.0
#                 user_input_df['fac_dapur'] = 1.0 if d_bersama else 0.0
#                 user_input_df['fac_parkir_mobil'] = 1.0 if p_mobil else 0.0
#                 user_input_df['fac_layanan_kebersihan'] = 1.0 if l_kebersihan else 0.0
#                 user_input_df['fac_kulkas'] = 1.0 if k_bersama else 0.0
#                 user_input_df['fac_keamanan'] = 1.0 if cctv else 0.0
#                 user_input_df['fac_area_jemur'] = 1.0 if jemur else 0.0
#                 user_input_df['fac_dispenser'] = 1.0 if dispenser else 0.0
#                 user_input_df['fac_mesin_cuci'] = 1.0 if mesin_cuci else 0.0
                
#                 log_prediction = rf_model.predict(user_input_df)[0]
#                 st.session_state.predicted_price = np.expm1(log_prediction)
#                 st.session_state.user_input_features = user_input_df
#                 st.session_state.selected_region = lokasi
                
#                 st.session_state.halaman = 'hasil'
#                 st.rerun()

#     with col_kanan:
#         st.markdown('<div style="margin-top: 5.6rem;"></div>', unsafe_allow_html=True)
#         st.markdown('<div class="right-image-banner">', unsafe_allow_html=True)
#         st.image("Kost-mahasiswa-jpg.webp", use_column_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)


# # =========================================================================
# # 6. HALAMAN 2: HASIL PREDIKSI & TOP REKOMENDASI
# # =========================================================================
# def tampilkan_halaman_hasil():
#     col_back, _ = st.columns([1, 10])
#     with col_back:
#         if st.button("← Hasil Prediksi", key="back_btn"):
#             st.session_state.halaman = 'input'
#             st.rerun()
            
#     st.write("")
    
#     harga_tampil = st.session_state.get('predicted_price', 0.0)
#     wilayah_tampil = st.session_state.get('selected_region', 'Jakarta')
#     harga_format = f"Rp {harga_tampil:,.0f}".replace(",", ".")
    
#     st.markdown(f"""
#         <div class="prediction-banner">
#             <p style="letter-spacing: 2px; font-size: 13px; font-weight: 500;">ESTIMASI HARGA IDEAL</p>
#             <div class="price-text">{harga_format} <span style="font-size: 20px; font-weight: normal;">/ bulan</span></div>
#             <p style="max-width: 650px; margin: 0 auto; font-size: 15px; line-height: 1.6;">
#                 Berdasarkan analisis fitur yang Anda pilih serta data historis di area {wilayah_tampil}.
#             </p>
#             <hr style="border-color: rgba(255,255,255,0.15); margin: 20px 0;">
#         </div>
#     """, unsafe_allow_html=True)
    
#     col_title, col_link = st.columns([5, 1])
#     with col_title:
#         st.markdown("<h4 style='font-weight: bold; margin: 0;'>Top 5 Rekomendasi Untukmu</h4>", unsafe_allow_html=True)
        
#     st.write("")
    
#     user_input_df = st.session_state.get('user_input_features')
#     df_rekomendasi = get_top_5_recommendations(user_input_df, df_cleaned)
#     list_cards = list(df_rekomendasi.iterrows())
    
#     # --- BARIS KE-1 ---
#     row1_cols = st.columns(3)
#     for idx in range(min(3, len(list_cards))):
#         _, row = list_cards[idx]
#         with row1_cols[idx]:
#             with st.container(border=True):
#                 nama_kos_fix = row.get('room_name', row.get('name', 'Kos Eksklusif'))
#                 st.markdown(f"<h5 style='font-weight: bold; margin-bottom: 2px;'>{nama_kos_fix[:35]}...</h5>", unsafe_allow_html=True)
#                 st.markdown(f"<span style='color: #64748B; font-size: 13px;'>{row.get('location', 'Jakarta')}, {row.get('region', '')}</span>", unsafe_allow_html=True)
                
#                 harga_aktual = f"Rp {row['price']:,.0f}".replace(",", ".")
#                 st.write("---")
#                 st.markdown(f"""
#                     <div style='display:flex; justify-content:space-between; align-items: center;'>
#                         <span style='color: #64748B; font-size: 14px;'>Harga Aktual</span>
#                         <b style='font-size: 16px;'>{harga_aktual}</b>
#                     </div>
#                 """, unsafe_allow_html=True)
                
#     # --- BARIS KE-2 ---
#     st.write("")
#     row2_cols = st.columns(3)
#     for idx in range(3, min(5, len(list_cards))):
#         _, row = list_cards[idx]
#         with row2_cols[idx - 3]:
#             with st.container(border=True):
#                 nama_kos_fix = row.get('room_name', row.get('name', 'Kos Eksklusif'))
#                 st.markdown(f"<h5 style='font-weight: bold; margin-bottom: 2px;'>{nama_kos_fix[:35]}...</h5>", unsafe_allow_html=True)
#                 st.markdown(f"<span style='color: #64748B; font-size: 13px;'>{row.get('location', 'Jakarta')}, {row.get('region', '')}</span>", unsafe_allow_html=True)
                
#                 harga_aktual = f"Rp {row['price']:,.0f}".replace(",", ".")
#                 st.write("---")
#                 st.markdown(f"""
#                     <div style='display:flex; justify-content:space-between; align-items: center;'>
#                         <span style='color: #64748B; font-size: 14px;'>Harga Aktual</span>
#                         <b style='font-size: 16px;'>{harga_aktual}</b>
#                     </div>
#                 """, unsafe_allow_html=True)


# # =========================================================================
# # 7. LOGIKA JALUR NAVIGASI UTAMA
# # =========================================================================
# if st.session_state.halaman == 'input':
#     tampilkan_halaman_input()
# elif st.session_state.halaman == 'hasil':
#     tampilkan_halaman_hasil()