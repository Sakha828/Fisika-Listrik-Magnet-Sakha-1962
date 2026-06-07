import streamlit as st
import numpy as np

# --- KONFIGURASI HALAMAN UTAMA ---
st.set_page_config(
    page_title="Aplikasi Komputasi Fisika Listrik & Magnet - Sakha Ardiansyah",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🔥 FUNGSI ANTI-BOCOR DESIMAL (.00 -> Bersih Total!)
def format_angka(nilai):
    if nilai == 0:
        return "0"
    if abs(nilai) < 0.01 or abs(nilai) > 100000:
        text = f"{nilai:.2e}"
        return text.replace("+0", "").replace("-0", "-")
    if nilai % 1 == 0:
        return f"{int(nilai)}"
    return f"{nilai:.4f}".rstrip('0').rstrip('.')

# 📂 INJECTOR TEMA CSS & HTML UTAMA (ALL-IN-ONE MOBILE OPTIMIZED ENGINE)
def pasang_visual_tema(bg, card, border, glow, mode_animasi="listrik_biru"):
    # Suntikan Gaya CSS Murni ke dalam Aplikasi
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {bg} !important;
            font-family: 'Segoe UI', Roboto, sans-serif;
            font-size: 15px !important;
            transition: all 0.5s ease-in-out;
        }}
        
        #MainMenu, footer, header {{
            visibility: hidden !important;
        }}
        
        /* --- CORE ANIMATIONS --- */
        @keyframes popIn {{
            0% {{ opacity: 0; transform: scale(0.97) translateY(10px); }}
            100% {{ opacity: 1; transform: scale(1) translateY(0); }}
        }}
        @keyframes naikVertikal {{
            0% {{ transform: translateY(0) rotate(0deg); opacity: 0; }}
            10% {{ opacity: 0.6; }}
            90% {{ opacity: 0.6; }}
            100% {{ transform: translateY(-1100px) rotate(360deg); opacity: 0; }}
        }}
        @keyframes gerakHorizontal {{
            0% {{ transform: translateX(-100px); opacity: 0; }}
            10% {{ opacity: 0.7; }}
            90% {{ opacity: 0.7; }}
            100% {{ transform: translateX(100vw); opacity: 0; }}
        }}
        @keyframes berputarLoop {{
            0% {{ transform: rotate(0deg) translateX(20px) rotate(0deg); opacity: 0.1; }}
            50% {{ opacity: 0.8; }}
            100% {{ transform: rotate(360deg) translateX(20px) rotate(-360deg); opacity: 0.1; }}
        }}
        @keyframes denyutPlasma {{
            0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 5px {glow}); opacity: 0.3; }}
            50% {{ transform: scale(1.3); filter: drop-shadow(0 0 25px {glow}); opacity: 0.8; }}
        }}
        @keyframes sambaranPetir {{
            0%, 92%, 96%, 100% {{ background-color: rgba(0, 0, 0, 0); }}
            94%, 98% {{ background-color: rgba(255, 255, 255, 0.05); }}
        }}

        /* --- STYLING CARD COMPONENT --- */
        .custom-box {{
            background: {card};
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 12px;
            border: 1px solid {border};
            margin-bottom: 20px;
            animation: popIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            transition: all 0.3s ease;
        }}
        .custom-box:hover {{
            border-color: {glow};
            box-shadow: 0 0 15px {glow};
            transform: translateY(-2px);
        }}
        .result-box {{
            background: rgba(9, 12, 22, 0.96);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 12px;
            border: 2px solid {glow};
            animation: popIn 0.5s ease-out;
            box-shadow: 0 0 15px rgba(0,0,0,0.7);
        }}
        h1, h2, h3, h4 {{ color: #FFFFFF !important; font-weight: 600 !important; }}
        h1 {{ font-size: 23px !important; margin-bottom: 15px !important; }}
        h4 {{ font-size: 15px !important; margin-bottom: 5px !important; }}
        
        .nilai-gila {{
            color: {glow} !important;
            font-size: 28px !important;
            font-weight: 700 !important;
            font-family: 'Courier New', Courier, monospace;
            margin: 10px 0;
            word-wrap: break-word;
        }}

        /* --- BACKGROUND CANVAS BASE --- */
        .bg-canvas {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            overflow: hidden; z-index: 0; pointer-events: none;
        }}
        .partikel-umum {{
            position: absolute; display: block;
            background: {glow};
            border-radius: 50%;
        }}

        /* STYLING BALOK MAGNET KELAS KHUSUS M-SERIES */
        .balok-magnet {{
            position: absolute; display: flex;
            flex-direction: column; width: 22px; height: 46px;
            border-radius: 4px; overflow: hidden;
            box-shadow: 0 0 10px rgba(255,255,255,0.15);
        }}
        .balok-magnet::before {{
            content: 'N'; font-weight: bold; color: white; text-align: center; font-size: 10px; line-height: 23px;
            background: #EF4444; height: 50%; width: 100%;
        }}
        .balok-magnet::after {{
            content: 'S'; font-weight: bold; color: white; text-align: center; font-size: 10px; line-height: 23px;
            background: #3B82F6; height: 50%; width: 100%;
        }}

        /* Posisi Kolom Grid Penempatan Partikel */
        .col-1 {{ left: 8%; }} .col-2 {{ left: 28%; }} .col-3 {{ left: 48%; }} .col-4 {{ left: 68%; }} .col-5 {{ left: 88%; }}
        
        /* Sidebar styling hardsync */
        div[data-testid="stSidebar"] {{ background-color: #0B0F19 !important; border-right: 1px solid #1E293B; }}
        label {{ color: #E2E8F0 !important; font-size: 14px !important; font-weight: 500 !important; }}

        /* 📱 TWEAK OPTIMALISASI TAMPILAN MOBILE (HP) */
        @media (max-width: 768px) {{
            h1 {{ font-size: 19px !important; }}
            .custom-box, .result-box {{ padding: 15px !important; margin-bottom: 15px !important; }}
            .nilai-gila {{ font-size: 22px !important; }}
            
            /* Sembunyikan sebagian partikel di HP agar tidak mengganggu bacaan */
            .col-1, .col-5 {{ display: none !important; }}
            .bg-canvas [style*="top: 75%"], .bg-canvas [style*="top: 80%"] {{ display: none !important; }}
        }}
        </style>
    """, unsafe_allow_html=True)
    
    # 🌟 VARIATION FILTER ROUTING HTML GENERATOR
    if mode_animasi == "listrik_biru":
        st.markdown(f"""
            <div class="bg-canvas" style="animation: sambaranPetir 5s infinite;">
                <div class="partikel-umum col-1" style="width:25px; height:25px; bottom:-50px; animation: naikVertikal 13s infinite linear, denyutPlasma 3s infinite ease-in-out;"></div>
                <div class="partikel-umum col-3" style="width:35px; height:35px; bottom:-50px; animation: naikVertikal 16s infinite linear 1s, denyutPlasma 4s infinite ease-in-out 0.5s;"></div>
                <div class="partikel-umum col-5" style="width:20px; height:20px; bottom:-50px; animation: naikVertikal 11s infinite linear 2s, denyutPlasma 2.5s infinite ease-in-out 1.5s;"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "listrik_hijau":
        st.markdown(f"""
            <div class="bg-canvas">
                <div class="partikel-umum col-2" style="width:18px; height:18px; bottom:-50px; border-radius: 4px; animation: naikVertikal 14s infinite linear; box-shadow: 0 0 10px {glow};"></div>
                <div class="partikel-umum col-4" style="width:28px; height:28px; bottom:-50px; border-radius: 4px; animation: naikVertikal 18s infinite linear 2s; box-shadow: 0 0 15px {glow};"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "listrik_emas":
        st.markdown(f"""
            <div class="bg-canvas" style="background: radial-gradient(circle at 50% 50%, rgba(255,215,0,0.03) 0%, transparent 70%);">
                <div class="partikel-umum col-1" style="width:12px; height:12px; bottom:-50px; animation: naikVertikal 20s infinite linear; opacity: 0.8;"></div>
                <div class="partikel-umum col-2" style="width:16px; height:16px; bottom:-50px; animation: naikVertikal 15s infinite linear 3s; opacity: 0.9;"></div>
                <div class="partikel-umum col-4" style="width:14px; height:14px; bottom:-50px; animation: naikVertikal 17s infinite linear 1s; opacity: 0.7;"></div>
                <div class="partikel-umum col-5" style="width:22px; height:22px; bottom:-50px; animation: naikVertikal 22s infinite linear 4s; opacity: 0.6;"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "listrik_ungu":
        st.markdown(f"""
            <div class="bg-canvas">
                <div class="partikel-umum col-3" style="width:150px; height:150px; bottom:-200px; background:radial-gradient(circle, rgba(168,85,247,0.15) 0%, transparent 70%); animation: naikVertikal 25s infinite linear;"></div>
                <div class="partikel-umum col-1" style="width:8px; height:8px; bottom:-50px; animation: naikVertikal 12s infinite linear;"></div>
                <div class="partikel-umum col-5" style="width:10px; height:10px; bottom:-50px; animation: naikVertikal 14s infinite linear 2s;"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "kapasitor_cyan":
        # DIKUNCI ANTI-BOCOR: Tanda kutip dibersihkan total dari inline style agar aman di mobile & desktop
        st.markdown(f"""
            <div class="bg-canvas">
                <div class="partikel-umum col-2" style="width:30px; height:6px; border-radius:2px; bottom:-50px; animation: naikVertikal 16s infinite linear;"></div>
                <div class="partikel-umum col-2" style="width:30px; height:6px; border-radius:2px; bottom:-70px; animation: naikVertikal 16s infinite linear;"></div>
                <div class="partikel-umum col-4" style="width:30px; height:6px; border-radius:2px; bottom:-50px; animation: naikVertikal 20s infinite linear;"></div>
                <div class="partikel-umum col-4" style="width:30px; height:6px; border-radius:2px; bottom:-70px; animation: naikVertikal 20s infinite linear;"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "arus_oranye":
        st.markdown(f"""
            <div class="bg-canvas">
                <div class="partikel-umum" style="width:12px; height:12px; top:25%; animation: gerakHorizontal 7s infinite linear; box-shadow: 0 0 8px {glow};"></div>
                <div class="partikel-umum" style="width:16px; height:16px; top:45%; animation: gerakHorizontal 5s infinite linear; box-shadow: 0 0 10px {glow};"></div>
                <div class="partikel-umum" style="width:10px; height:10px; top:75%; animation: gerakHorizontal 9s infinite linear; box-shadow: 0 0 6px {glow};"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "kirchoff_loop":
        st.markdown(f"""
            <div class="bg-canvas">
                <div class="partikel-umum col-2" style="width:15px; height:15px; top:30%; border-radius:3px; animation: berputarLoop 4s infinite linear;"></div>
                <div class="partikel-umum col-4" style="width:15px; height:15px; top:60%; border-radius:3px; animation: berputarLoop 5s infinite linear;"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "magnet_slow":
        st.markdown(f"""
            <div class="bg-canvas">
                <div class="balok-magnet col-1" style="bottom:-100px; animation: naikVertikal 18s infinite linear;"></div>
                <div class="balok-magnet col-3" style="bottom:-100px; animation: naikVertikal 24s infinite linear;"></div>
                <div class="balok-magnet col-5" style="bottom:-100px; animation: naikVertikal 20s infinite linear;"></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif mode_animasi == "gaya_lorentz":
        st.markdown(f"""
            <div class="bg-canvas">
                <div class="balok-magnet" style="top:20%; left:-50px; animation: gerakHorizontal 12s infinite linear; transform: rotate(90deg);"></div>
                <div class="balok-magnet" style="top:55%; left:-50px; animation: gerakHorizontal 16s infinite linear; transform: rotate(90deg);"></div>
                <div class="balok-magnet" style="top:80%; left:-50px; animation: gerakHorizontal 10s infinite linear; transform: rotate(90deg);"></div>
            </div>
        """, unsafe_allow_html=True)

# --- SIDEBAR BRANDING LOGO LAB KOMPUTASI FLM ---
st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #1E1B4B 0%, #0F172A 100%); 
                padding: 15px; border-radius: 10px; border: 1px solid #312E81; 
                text-align: center; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
        <div style="font-size: 32px; margin-bottom: 5px; filter: drop-shadow(0 0 8px #6366F1);">⚡🌐</div>
        <div style="color: #FFFFFF; font-weight: 700; font-size: 14px; letter-spacing: 1px;">LAB KOMPUTASI FLM</div>
        <div style="color: #6366F1; font-weight: 600; font-size: 11px; margin-top: 2px; letter-spacing: 0.5px;">TEKNIK INFORMATIKA</div>
    </div>
""", unsafe_allow_html=True)

st.sidebar.title("Navigasi Materi")
menu = st.sidebar.radio(
    "Pilih Modul Pertemuan:",
    [
        "Pertemuan 1: Gaya Coulomb (Segaris)",
        "Pertemuan 2: Gaya Coulomb (Tidak Segaris)",
        "Pertemuan 3: Kuat Medan Listrik",
        "Pertemuan 4: Energi Potensial & Potensial Listrik",
        "Pertemuan 5: Kapasitor",
        "Pertemuan 6: Arus Listrik & Hambatan Kawat",
        "Pertemuan 7: Hukum Kirchoff (2 Loop)",
        "Pertemuan 9: Induksi Magnetik (Kawat & Toroida)",
        "Pertemuan 10: Gaya Lorentz (3 Kawat Sejajar)"
    ]
)

st.sidebar.write("---")
st.sidebar.markdown("""
**Penyusun:** Sakha Ardiansyah  
NPM: 202443501962  
*Universitas Indraprasta PGRI*
""")


# ==============================================================================
# ROUTING LOGIKAL OPERASI HITUNGAN DAN TEMA HARDSYNC UTAMA
# ==============================================================================

if menu == "Pertemuan 1: Gaya Coulomb (Segaris)":
    pasang_visual_tema("#040A12", "rgba(10, 25, 47, 0.7)", "#172A45", "#00F0FF", mode_animasi="listrik_biru")
    st.title("Pertemuan 1: Gaya Coulomb (Muatan Segaris)")
    st.markdown("""
    <div class="custom-box">
        <h4>Persamaan Utama (Hukum Coulomb)</h4>
        <code>F = k · (|q₁ · q₂|) / r²</code><br><br>
        Keterangan: Konstanta <b>k = 9 × 10⁹ N·m²/C²</b>. Interaksi muatan sejenis menghasilkan gaya tolak-menolak.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        q1 = st.number_input("Besar Muatan 1 (q₁) - μC", value=4.0, format="%g") * 10**-6
        q2 = st.number_input("Besar Muatan 2 (q₂) - μC", value=-2.0, format="%g") * 10**-6
        r = st.number_input("Jarak Antar Muatan (r) - cm", value=4.0, format="%g") / 100.0
    
    F = (9 * 10**9) * abs(q1 * q2) / (r**2)
    with col2:
        st.markdown(f'<div class="result-box"><h4>Hasil Analisis Perhitungan</h4><div class="nilai-gila">{format_angka(F)} N</div></div>', unsafe_allow_html=True)

elif menu == "Pertemuan 2: Gaya Coulomb (Tidak Segaris)":
    pasang_visual_tema("#04120B", "rgba(16, 44, 31, 0.7)", "#1F4E37", "#39FF14", mode_animasi="listrik_hijau")
    st.title("Pertemuan 2: Gaya Coulomb (Muatan Tidak Segaris / Membentuk Sudut)")
    st.markdown('<div class="custom-box"><h4>Persamaan Kosinus Resultan Gaya Vektor</h4><code>F_total = √(F_ac² + F_bc² + 2 · F_ac · F_bc · cos(α))</code></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        fac = st.number_input("Besar Gaya F_ac - N", value=10.0, format="%g")
        fbc = st.number_input("Besar Gaya F_bc - N", value=15.0, format="%g")
        sudut = st.number_input("Sudut Elevasi α - Derajat", value=60.0, format="%g")
        
    f_total = np.sqrt(fac**2 + fbc**2 + 2 * fac * fbc * np.cos(np.radians(sudut)))
    with col2:
        st.markdown(f'<div class="result-box"><h4>Hasil Analisis Perhitungan</h4><div class="nilai-gila">{format_angka(f_total)} N</div></div>', unsafe_allow_html=True)

elif menu == "Pertemuan 3: Kuat Medan Listrik":
    pasang_visual_tema("#120F04", "rgba(43, 36, 12, 0.7)", "#544315", "#FFD700", mode_animasi="listrik_emas")
    st.title("Pertemuan 3: Kuat Medan Listrik")
    st.markdown('<div class="custom-box"><h4>Persamaan Kuat Medan Listrik</h4><code>E = k · Q / r²</code></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        Q = st.number_input("Besar Muatan Sumber (Q) - μC", value=2.0, format="%g") * 10**-6
        r = st.number_input("Jarak Titik ke Muatan (r) - cm", value=10.0, format="%g") / 100.0
        
    E = (9 * 10**9) * Q / (r**2)
    with col2:
        st.markdown(f'<div class="result-box"><h4>Hasil Analisis Perhitungan</h4><div class="nilai-gila">{format_angka(E)} N/C</div></div>', unsafe_allow_html=True)

elif menu == "Pertemuan 4: Energi Potensial & Potensial Listrik":
    pasang_visual_tema("#0B0412", "rgba(31, 14, 46, 0.7)", "#452066", "#C084FC", mode_animasi="listrik_ungu")
    st.title("Pertemuan 4: Energi Potensial & Potensial Listrik")
    st.markdown('<div class="custom-box"><h4>Persamaan Utama Voltase & Energi</h4>Energi Potensial: <code>Ep = k · q₁ · q₂ / r</code> | Potensial Listrik: <code>V = k · Q / r</code></div>', unsafe_allow_html=True)
    
    tipe = st.selectbox("Pilih Komponen yang Akan Dihitung:", ["Potensial Listrik (V)", "Energi Potensial (Ep)"])
    col1, col2 = st.columns(2)
    k = 9 * 10**9
    
    with col1:
        if tipe == "Potensial Listrik (V)":
            q_source = st.number_input("Besar Muatan Sumber (Q) - μC", value=5.0, format="%g") * 10**-6
            r_dist = st.number_input("Jarak r - cm", value=10.0, format="%g") / 100.0
            hasil = k * q_source / r_dist
            satuan = "Volt"
        else:
            q1 = st.number_input("Besar Muatan 1 (q₁) - μC", value=5.0, format="%g") * 10**-6
            q2 = st.number_input("Besar Muatan 2 (q₂) - μC", value=-4.0, format="%g") * 10**-6
            r_dist = st.number_input("Jarak r - cm", value=10.0, format="%g") / 100.0
            hasil = k * q1 * q2 / r_dist
            satuan = "Joule"
            
    with col2:
        st.markdown(f'<div class="result-box"><h4>Hasil Analisis {tipe}</h4><div class="nilai-gila">{format_angka(hasil)} {satuan}</div></div>', unsafe_allow_html=True)

elif menu == "Pertemuan 5: Kapasitor":
    pasang_visual_tema("#020F12", "rgba(10, 38, 38, 0.7)", "#184D4D", "#2DD4BF", mode_animasi="kapasitor_cyan")
    st.title("Pertemuan 5: Kapasitor Sederhana")
    st.markdown('<div class="custom-box"><h4>Persamaan Kapasitas & Muatan Kapasitor</h4><code>Q = C · V</code></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        C = st.number_input("Kapasitansi Efektif (C) - μF", value=10.0, format="%g") * 10**-6
        V = st.number_input("Beda Potensial / Tegangan (V) - Volt", value=12.0, format="%g")
        
    Q_cap = C * V
    with col2:
        st.markdown(f'<div class="result-box"><h4>Hasil Analisis Perhitungan</h4><div class="nilai-gila">{format_angka(Q_cap)} C</div></div>', unsafe_allow_html=True)

elif menu == "Pertemuan 6: Arus Listrik & Hambatan Kawat":
    pasang_visual_tema("#120702", "rgba(44, 23, 12, 0.7)", "#593119", "#F97316", mode_animasi="arus_oranye")
    st.title("Pertemuan 6: Hambatan Jenis Kawat Penghantar")
    st.markdown('<div class="custom-box"><h4>Persamaan Resistansi Konduktor (Hukum Ohm Kontinu)</h4><code>R = ρ · L / A</code></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hambatan Jenis Bahan (ρ) - Ω·m", value=3.14e-6, format="%.2e")
        length = st.number_input("Panjang Total Kawat (L) - m", value=10.0, format="%g")
        diameter = st.number_input("Diameter Kawat (d) - mm", value=2.0, format="%g")
        
    A = np.pi * (((diameter / 1000.0) / 2.0)**2)
    R_kawat = rho * length / A
    with col2:
        st.markdown(f'<div class="result-box"><h4>Hasil Analisis Perhitungan</h4><div class="nilai-gila">{format_angka(R_kawat)} Ω</div></div>', unsafe_allow_html=True)

elif menu == "Pertemuan 7: Hukum Kirchoff (2 Loop)":
    pasang_visual_tema("#021207", "rgba(11, 38, 20, 0.7)", "#184D2B", "#10B981", mode_animasi="kirchoff_loop")
    st.title("Pertemuan 7: Analisis Hukum Kirchoff II (Rangkaian Multiloop)")
    st.markdown('<div class="custom-box"><h4>Penyelesaian Sistem Persamaan Linear Arus Cabang</h4><code>∑E + ∑I·R = 0</code></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        e1 = st.number_input("Gaya Gerak Listrik 1 (E₁) - V", value=12.0, format="%g")
        e2 = st.number_input("Gaya Gerak Listrik 2 (E₂) - V", value=6.0, format="%g")
        r1 = st.number_input("Nilai Resistor 1 (R₁) - Ω", value=2.0, format="%g")
        r2 = st.number_input("Nilai Resistor 2 (R₂) - Ω", value=3.0, format="%g")
        r3 = st.number_input("Nilai Resistor Cabang Tengah (R₃) - Ω", value=4.0, format="%g")

    try:
        arus = np.linalg.solve(np.array([[r1 + r3, r3], [r3, r2 + r3]]), np.array([e1, e2]))
        i1, i2 = arus[0], arus[1]
        i3 = i1 + i2
    except:
        i1, i2, i3 = 0, 0, 0

    with col2:
        st.markdown(f"""
        <div class="result-box">
            <h4>Hasil Analisis Kuat Arus Loop</h4>
            <div style='color:#A7F3D0; font-size:14px; margin-top:5px;'>Arus Cabang I₁: <b style='color:#10B981; font-size:18px;'>{format_angka(i1)} A</b></div>
            <div style='color:#A7F3D0; font-size:14px; margin-top:5px;'>Arus Cabang I₂: <b style='color:#10B981; font-size:18px;'>{format_angka(i2)} A</b></div>
            <div style='color:#A7F3D0; font-size:14px; margin-top:5px;'>Arus Distribusi Tengah I₃: <b style='color:#10B981; font-size:22px;'>{format_angka(i3)} A</b></div>
        </div>
        """, unsafe_allow_html=True)

elif menu == "Pertemuan 9: Induksi Magnetik (Kawat & Toroida)":
    pasang_visual_tema("#090412", "rgba(22, 13, 41, 0.7)", "#3C236E", "#A855F7", mode_animasi="magnet_slow")
    st.title("Pertemuan 9: Induksi Magnetik pada Sumbu Toroida")
    st.markdown('<div class="custom-box"><h4>Persamaan Kuat Induksi Magnetik GGL</h4><code>B = (μ₀ · N · I) / (2 · π · R)</code></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        turns = st.number_input("Kerapatan Jumlah Lilitan (N)", value=50, format="%d")
        current = st.number_input("Kuat Arus Listrik (I) - A", value=0.8, format="%g")
        r_toroid = st.number_input("Jari-jari Efektif Toroida (R) - cm", value=20.0, format="%g") / 100.0
        
    B_toroid = ((4 * np.pi * 10**-7) * current * turns) / (2 * np.pi * r_toroid)
    with col2:
        st.markdown(f'<div class="result-box"><h4>Hasil Analisis Perhitungan</h4><div class="nilai-gila">{format_angka(B_toroid)} T</div></div>', unsafe_allow_html=True)

elif menu == "Pertemuan 10: Gaya Lorentz (3 Kawat Sejajar)":
    pasang_visual_tema("#12040E", "rgba(41, 13, 32, 0.7)", "#6E2353", "#EC4899", mode_animasi="gaya_lorentz")
    st.title("Pertemuan 10: Gaya Lorentz pada Sistem 3 Kawat Sejajar")
    st.markdown('<div class="custom-box"><h4>Persamaan Interaksi Gaya Vektor Lintasan Kawat Penghantar</h4><code>F/l = (μ₀ · I₁ · I₂) / (2 · π · a)</code></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        cur1 = st.number_input("Kuat Arus Kawat 1 (I₁) - A", value=3.0, format="%g")
        cur2 = st.number_input("Kuat Arus Kawat 2 (I₂) - A", value=4.0, format="%g")
        cur3 = st.number_input("Kuat Arus Kawat 3 (I₃) - A", value=5.0, format="%g")
        dist12 = st.number_input("Jarak Kawat 1 ke Kawat 2 (a₁₂) - cm", value=2.0, format="%g") / 100.0
        dist23 = st.number_input("Jarak Kawat 2 ke Kawat 3 (a₂₃) - cm", value=3.0, format="%g") / 100.0

    miu0 = 4 * np.pi * 10**-7
    f12 = (miu0 * cur1 * cur2) / (2 * np.pi * dist12)
    f13 = (miu0 * cur1 * cur3) / (2 * np.pi * (dist12 + dist23))
    
    f_netto = abs(f12 - f13)
    direction = "Kiri" if f12 > f13 else "Kanan"
        
    with col2:
        st.markdown(f"""
        <div class="result-box">
            <h4>Resultan Gaya Akhir Kawat 1</h4>
            <div class="nilai-gila">{format_angka(f_netto)} N/m</div>
            <div style='color:#FCE7F3; font-size:15px; margin-top:5px;'>Arah Pergerakan Vektor: <b style='color:#EC4899; font-size:18px;'>{direction}</b></div>
        </div>
        """, unsafe_allow_html=True)