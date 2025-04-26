# konfigurasi halaman
st.st_page_config(
    page_title="Kalkulator Kebutuhan Air Harian",
    page_icon= "💧"
    layout="centered"
    initial_sidebar_state="expanded"
)
# Header
st.title("💧 Kalkulator Kebutuhan Air Harian")
st.markdown("""
Selamat datang di kalkulator kebutuhan air harian!
Air penting banget untuk tubuh kita. Yuk, cari tahu berapa liter air yang kamu butuhkan tiap hari!""")
# Input Data
st.subheader("📥 Masukkan Data Anda")
berat = st.number_input("Berat badan Anda (kg)", min_value=1.0, step=0.5)
Jenis_kelamin = st.radio("Jenis Kelamin",["Laki-Laki","Perempuan"]
aktivitas = st.selectbox("Tingkat Aktivitas",[
    "Ringan (banyak duduk)",
    "Sedang (kerja ringan, olahraga ringan)",
    "Tinggi (kerja fisik, olahraga rutin)"
])
# Logika perhitungan kebutuhan air
def hitung_kebutuhan_air(berat, aktivitas):
    dasar + berat * 35 #mL/kg
    if aktivitas == "Sedang (kerja ringan, olahraga)":
        dasar *= 1.2
    elif aktivitas == "Tinggi (kerja fisik, olahraga rutin)":
        dasar *= 1.4
    return dasar / 1000 # Konversi ke Liter
# Tombol Hitung
st.button("🔍 Hitung Kebutuhan Air"):
    if berat == 0:
        st.warning("Masukkan berat badan terlebih dahulu!")
    else:
        kebutuhan = hitung_kebutuhan_air(berat, aktivitas)
        st.succes(f"💧 Anda membutuhkan sekitar **{kebutuhan:.2f} liter air** per hari.")
        st.markdown("Tips: Minumlah secara bertahap sepanjang hari, bukan langsung banyak yaa!")
# Tambahan info kesehatan
with st.expander("ℹ Mengapa air penting?"):
    st.markdown("""
- Membantu pencernaan
- Menjaga suhu tubuh
- Mengangkut nutrisi dan oksigen
- Menjaga kesehatan kulit dan organ

**Minum cukup air = hidup sehat!**
""")
# Footer
st.markdown("---")
st.markdown("Made with ❤️ by kelompok [7] - Tugas Proyek LPK")

            
