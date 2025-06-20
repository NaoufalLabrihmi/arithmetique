import streamlit as st
import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

st.set_page_config(page_title="Microlearning Maths Lycée : Arithmétique Interactive", layout="wide")
st.title("🔢 Microlearning Maths Lycée : Arithmétique Interactive")
st.subheader("Résumé, Calculatrice et Résolution d'Équations")
col1, col2 = st.columns([1.2, 1])

with col1:
    st.header("📖 Propriétés et Théorèmes Fondamentaux")
    properties = [
        ("Division euclidienne et divisibilité",
         [r"a = bq + r \quad \text{avec} \quad 0 \leq r < |b|",
          r"a \mid b \iff \exists k \in \mathbb{Z},\ b = ka"],
         r"23 = 7 \times 3 + 2\quad 7 \mid 21,\ 7 \nmid 23"),
        ("PGCD (Plus Grand Commun Diviseur)",
         [r"\mathrm{PGCD}(a, b) = \max\{d \in \mathbb{N}^* : d \mid a \text{ et } d \mid b\}"],
         r"\mathrm{PGCD}(18, 30) = 6"),
        ("PPCM (Plus Petit Commun Multiple)",
         [r"\mathrm{PPCM}(a, b) = \min\{m \in \mathbb{N}^* : a \mid m \text{ et } b \mid m\}",
          r"|ab| = \mathrm{PGCD}(a, b) \times \mathrm{PPCM}(a, b)"],
         r"\mathrm{PPCM}(8, 12) = 24\quad |8 \times 12| = 96 = 4 \times 24"),
        ("Algorithme d'Euclide",
         [r"\mathrm{PGCD}(a, b) = \mathrm{PGCD}(b, r)\ \text{où}\ r = a \bmod b"],
         r"119 = 34 \times 3 + 17 \Rightarrow \mathrm{PGCD}(119,34) = \mathrm{PGCD}(34,17)"),
        ("Relation de Bézout",
         [r"\exists\ (u, v) \in \mathbb{Z}^2,\ au + bv = \mathrm{PGCD}(a, b)"],
         r"26 \times (-1) + 7 \times 4 = 1"),
        ("Entiers premiers entre eux",
         [r"a\ \text{et}\ b\ \text{sont premiers entre eux} \iff \mathrm{PGCD}(a, b) = 1"],
         r"\mathrm{PGCD}(15,28)=1"),
        ("Nombres premiers",
         [r"n \geq 2\ \text{est premier} \iff n\ \text{a seulement 2 diviseurs : 1 et lui-même}"],
         r"17\ \text{est premier},\ 21\ \text{ne l'est pas}"),
        ("Théorème de Gauss",
         [r"a \mid bc\ \text{et}\ \mathrm{PGCD}(a, b) = 1 \implies a \mid c"],
         r"3 \mid 2 \times 15\ \text{et}\ \mathrm{PGCD}(3,2)=1 \implies 3 \mid 15"),
        ("Congruence",
         [r"a \equiv b\ [n] \iff n \mid (a-b)"],
         r"17 \equiv 5\ [12] \quad (12 \mid 17-5 = 12)"),
        ("Petit théorème de Fermat",
         [r"p\ \text{premier},\ a \in \mathbb{Z} \implies a^p \equiv a\ [p]\ \text{et si}\ p \nmid a,\ a^{p-1} \equiv 1\ [p]"],
         r"2^7 = 128 \equiv 2\ [7]\quad 3^6 = 729 \equiv 1\ [7]"),
        ("Équations diophantiennes linéaires",
         [r"ax + by = c\ \text{a une solution entière} \iff \mathrm{PGCD}(a, b) \mid c"],
         r"15x + 25y = 5\ \text{a une solution car}\ \mathrm{PGCD}(15,25)=5\mid 5"),
    ]
    for title, formulas, example in properties:
        with st.expander(title):
            for formula in formulas:
                st.latex(formula)
            st.markdown("**Exemple :**")
            st.latex(example)

with col2:
    st.header("🧮 Calculatrice Arithmétique")
    st.markdown("""
Entrez deux entiers \(a\) et \(b\) pour :
- Calculer leur **PGCD**
- Calculer leur **PPCM**
- Vérifier si chacun est un **nombre premier**
""")
    a = st.number_input("Entrez le premier entier (a)", value=12, step=1)
    b = st.number_input("Entrez le deuxième entier (b)", value=18, step=1)
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
    if st.button("Calculer"):
        pgcd = math.gcd(int(a), int(b))
        ppcm = abs(int(a)*int(b)) // pgcd if pgcd != 0 else 0
        st.success(f"PGCD({int(a)}, {int(b)}) = {pgcd}")
        st.success(f"PPCM({int(a)}, {int(b)}) = {ppcm}")
        st.info(f"{int(a)} est {'premier' if is_prime(int(a)) else 'non premier'}.")
        st.info(f"{int(b)} est {'premier' if is_prime(int(b)) else 'non premier'}.")
    st.markdown("""
    ---
    """)
    st.header("🧩 Équation diophantienne linéaire")
    st.markdown("""
    Entrez trois entiers \(a\), \(b\), \(c\) pour l'équation :
     ax + by = c 
    """)
    
    a_dio = st.number_input("a (≠ 0 ou b ≠ 0)", value=15, step=1, key="a_dio")
    b_dio = st.number_input("b (≠ 0 ou a ≠ 0)", value=25, step=1, key="b_dio")
    c_dio = st.number_input("c", value=5, step=1, key="c_dio")
    if st.button("Résoudre l'équation diophantienne"):
        a_int, b_int, c_int = int(a_dio), int(b_dio), int(c_dio)
        g, u, v = extended_gcd(a_int, b_int)
        if g == 0:
            st.error("a et b ne peuvent pas être tous deux nuls.")
        elif c_int % g != 0:
            st.warning(f"Pas de solution entière car {g} ne divise pas {c_int}.")
        else:
            x0 = u * (c_int // g)
            y0 = v * (c_int // g)
            st.success(f"Solution particulière : x = {x0}, y = {y0}")
            # Simplification des coefficients de la solution générale
            def reduce_frac(num, den):
                if den == 0:
                    return 0, 1
                g = math.gcd(num, den)
                num, den = num // g, den // g
                # On veut le dénominateur toujours positif
                if den < 0:
                    num, den = -num, -den
                return num, den
            b_num, b_den = reduce_frac(b_int, g)
            a_num, a_den = reduce_frac(a_int, g)
            g_abs = abs(g)
            st.latex(
                rf"""
                a = {a_int},\quad b = {b_int},\quad c = {c_int},\\
                \mathrm{{PGCD}}(a, b) = {g_abs},\\
                x_0 = {x0},\quad y_0 = {y0}
                """
            )
            # Affichage de la solution générale avec signe explicite
            def format_k_term(val):
                if val >= 0:
                    return f"+ {val}k"
                else:
                    return f"- {abs(val)}k"
            def format_k_frac(num, den):
                if num == 0:
                    return ""
                sign = "+" if num > 0 else "-"
                return f" {sign} \\frac{{{abs(num)}}}{{{den}}}k"

            if b_den == 1 and a_den == 1:
                xk = format_k_term(b_num)
                yk = format_k_term(-a_num)
                st.latex(
                    rf"""
                    \text{{Solution générale :}} \\
                    x = {x0} {xk}, \quad y = {y0} {yk}, \quad k \in \mathbb{{Z}}
                    """
                )
            else:
                xk = format_k_frac(b_num, b_den)
                yk = format_k_frac(-a_num, a_den)
                st.latex(
                    rf"""
                    \text{{Solution générale :}} \\
                    x = {x0}{xk}, \quad y = {y0}{yk}, \quad k \in \mathbb{{Z}}
                    """
                )


