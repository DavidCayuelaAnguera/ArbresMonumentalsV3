# Autor: David Cayuela Anguera
# Any: 2025
# Descripció: Genera pàgines HTML per arbres, comarques i províncies a partir del fitxer arbres_complert.json

import os
import json
import unicodedata

# 🔧 Utilitat per normalitzar noms per a fitxers i URLs
def slugify(text):
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return text.lower().replace(" ", "-").replace("'", "").replace("’", "").replace("à", "a").replace("é", "e").replace("è", "e").replace("í", "i").replace("ó", "o").replace("ò", "o").replace("ú", "u").replace("ü", "u").replace("ç", "c")

# 📥 Carrega el fitxer JSON
with open("data/arbres_complert.json", encoding="utf-8") as f:
    dades = json.load(f)

# 📁 Directori de sortida per arbres
os.makedirs("arbre", exist_ok=True)

# 🗂️ Estructura per guardar comarques per província
provincies = {"Barcelona": [], "Girona": []}

# 🔁 Genera fitxes d’arbres i prepara dades per comarques
for provincia in dades:
    for comarca in dades[provincia]:
        slug_comarca = slugify(comarca)
        ruta_comarca = f"comarques/{slugify(provincia)}/{slug_comarca}.html"
        os.makedirs(os.path.dirname(ruta_comarca), exist_ok=True)

        arbres = dades[provincia][comarca]
        provincies[provincia].append((comarca, ruta_comarca, arbres))

        for arbre in arbres:
            matricula = arbre["matricula"]
            nom = arbre["nom"]
            fitxer_arbre = f"arbre/{matricula}.html"

            html = f"""<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>{nom}</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header><h1>{nom}</h1></header>
    <main>
        <ul>
            <li><strong>Matrícula:</strong> {matricula}</li>
            <li><strong>Tàxon:</strong> {arbre["taxon"]}</li>
            <li><strong>Tipologia:</strong> {arbre["tipologia"]}</li>
            <li><strong>Terme municipal:</strong> {arbre["terme_municipal"]}</li>
            <li><strong>Comarca:</strong> {arbre["comarca"]}</li>
            <li><strong>Propietat:</strong> {arbre["propietat"]}</li>
            <li><strong>Classificació Etnoecològica:</strong> {arbre["classificacio_etnoecologica"]}</li>
        </ul>

        <h2>Informació Etnoecològica</h2>
        <p class="ample">{arbre["informacio_etnoecologica"]}</p>

        <h2>Observacions</h2>
        <form onsubmit="afegirObservacio(event)">
            <textarea id="observacions" rows="5" placeholder="Escriu aquí la teva observació..."></textarea><br>
            <button type="submit">Afegir observació</button>
        </form>
        <div id="llista-observacions"></div>

        <h2>Bibliografia</h2>
        <p class="ample">{arbre["bibliografia"]}</p>

        <div class="center">
            <a href="../{ruta_comarca}">Torna a la comarca</a>
            <a href="../index.html">Torna a l'inici</a>
        </div>
    </main>
    <script>
        function afegirObservacio(e) {{
            e.preventDefault();
            const text = document.getElementById("observacions").value;
            if (text.trim() === "") return;
            const div = document.createElement("div");
            div.textContent = text;
            document.getElementById("llista-observacions").appendChild(div);
            document.getElementById("observacions").value = "";
        }}
    </script>
</body>
</html>"""

            with open(fitxer_arbre, "w", encoding="utf-8") as out:
                out.write(html)

# 🗂️ Genera pàgines per comarques
for provincia, comarques in provincies.items():
    for comarca, path, arbres in comarques:
        html = f"""<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>{comarca}</title>
    <link rel="stylesheet" href="../../css/style.css">
</head>
<body>
    <header><h1>Arbres monumentals de {comarca}</h1></header>
    <main>
        <ul>
"""

        for arbre in arbres:
            html += f'<li><a href="../../arbre/{arbre["matricula"]}.html">{arbre["nom"]}</a></li>\n'

        html += f"""</ul>
        <div class="center">
            <a href="../../{slugify(provincia)}.html">Torna a {provincia}</a>
            <a href="../../index.html">Torna a l'inici</a>
        </div>
    </main>
</body>
</html>"""

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

# 📄 Genera pàgines de províncies
for provincia, comarques in provincies.items():
    html = f"""<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>{provincia}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header><h1>Comarques de {provincia}</h1></header>
    <main>
        <div class="grid-cards">
"""

    for comarca, path, _ in comarques:
        html += f'<a class="card" href="{path}">{comarca}</a>\n'

    html += f"""</div>
        <div class="center">
            <a href="index.html" class="back-button">Torna a l'inici</a>
        </div>
    </main>
</body>
</html>"""

    with open(f"{slugify(provincia)}.html", "w", encoding="utf-8") as f:
        f.write(html)

print("✅ Totes les pàgines s'han generat correctament!")

