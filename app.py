import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Number Theory Explorer",
    page_icon="🧮",
    layout="wide"
)

# =====================================
# CSS TEMA
# =====================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #e3f2fd,
        #f3e5f5
    );
}

h1{
    text-align:center;
    color:#0d47a1;
}

h2,h3{
    color:#4a148c;
}

.stButton button{
    width:100%;
    height:55px;
    border-radius:15px;
    background:#1976d2;
    color:white;
    font-size:18px;
    font-weight:bold;
}

[data-testid="stMetric"]{
    background:white;
    padding:15px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("📚 Menu")

    st.info("""
    Kalkulator Teori Bilangan

    Materi yang digunakan:

    ✔ FPB

    ✔ KPK

    ✔ Algoritma Euclid

    ✔ Relatif Prima

    ✔ Aritmetika Dasar
    """)

    st.markdown("---")

    st.write("Dibuat untuk Tugas Teori Bilangan")

# =====================================
# JUDUL
# =====================================

st.title("🔢 Number Theory Explorer")

st.markdown("""
### FPB dan KPK Menggunakan Algoritma Euclid

Masukkan dua bilangan bulat positif untuk dianalisis.
""")

# =====================================
# FUNGSI FPB
# =====================================

def hitung_fpb(a, b):

    langkah = []

    while b != 0:

        q = a // b
        r = a % b

        langkah.append({
            "a": a,
            "b": b,
            "q": q,
            "r": r
        })

        a, b = b, r

    return a, langkah

# =====================================
# INPUT
# =====================================

col1, col2 = st.columns(2)

with col1:
    a = st.number_input(
        "Masukkan Bilangan Pertama",
        min_value=1,
        step=1
    )

with col2:
    b = st.number_input(
        "Masukkan Bilangan Kedua",
        min_value=1,
        step=1
    )

# =====================================
# PROSES
# =====================================

if st.button("🚀 Analisis Bilangan"):

    fpb, langkah = hitung_fpb(int(a), int(b))

    kpk = abs(int(a) * int(b)) // fpb

    st.markdown("---")

    st.subheader("📊 Hasil Analisis")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("FPB", fpb)

    with c2:
        st.metric("KPK", kpk)

    st.markdown("---")

    st.subheader("📖 Langkah Algoritma Euclid")

    for i, item in enumerate(langkah, start=1):

        st.markdown(f"### Langkah {i}")

        st.write(
            f"{item['a']} ÷ {item['b']} = "
            f"{item['q']} sisa {item['r']}"
        )

        st.latex(
            f"{item['a']}={item['q']}\\times{item['b']}+{item['r']}"
        )

        if item['r'] != 0:

            st.info(
                f"Karena sisa ≠ 0, lanjut menghitung FPB({item['b']},{item['r']})"
            )

        else:

            st.success(
                "Karena sisa = 0, proses berhenti."
            )

    st.markdown("---")

    st.subheader("🎯 Menentukan FPB")

    st.write("Urutan perhitungan:")

    rantai = []

    x = int(a)
    y = int(b)

    while y != 0:
        rantai.append(f"FPB({x},{y})")
        x, y = y, x % y

    rantai.append(f"FPB({fpb},0)")

    for r in rantai:
        st.write(r)

    st.success(
        f"Maka FPB({int(a)},{int(b)}) = {fpb}"
    )

    st.markdown("---")

    st.subheader("🎯 Menentukan KPK")

    st.write("Menggunakan rumus:")

    st.latex(
        r"KPK(a,b)=\frac{a\times b}{FPB(a,b)}"
    )

    st.write("Substitusi nilai:")

    st.latex(
        rf"KPK({int(a)},{int(b)})=\frac{{{int(a)}\times{int(b)}}}{{{fpb}}}"
    )

    st.latex(
        rf"=\frac{{{int(a)*int(b)}}}{{{fpb}}}"
    )

    st.latex(
        rf"={kpk}"
    )

    st.success(
        f"Jadi KPK({int(a)},{int(b)}) = {kpk}"
    )

    st.markdown("---")

    st.subheader("🧠 Fakta Bilangan")

    if fpb == 1:
        st.success(
            "Kedua bilangan relatif prima karena FPB = 1."
        )
    else:
        st.warning(
            "Kedua bilangan tidak relatif prima karena FPB ≠ 1."
        )

    if int(a) % 2 == 0:
        st.write(f"{int(a)} adalah bilangan genap")
    else:
        st.write(f"{int(a)} adalah bilangan ganjil")

    if int(b) % 2 == 0:
        st.write(f"{int(b)} adalah bilangan genap")
    else:
        st.write(f"{int(b)} adalah bilangan ganjil")

    st.markdown("---")

    st.caption(
        "Number Theory Explorer | Algoritma Euclid | FPB & KPK"
    )
