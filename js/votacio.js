/**
 * Autor: David Cayuela Anguera
 * Any: 2025
 * Descripció: Sistema de votació per l'Arbre Monumental Català de l'Any
 */

// Ruta al JSON complet
const JSON_URL = "data/arbres_complert.json";

// Normalitza cadenes per ID únic
function slugify(text) {
  return text.toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/ /g, "-")
    .replace(/[^\w-]/g, "");
}

// Carrega dades i mostra arbres
fetch(JSON_URL)
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("llista-votacio");

    Object.values(data).forEach(provincia => {
      Object.values(provincia).forEach(arbres => {
        arbres.forEach(arbre => {
          const id = slugify(arbre["Matrícula"]);
          const nom = arbre["Nom de l'arbre"];
          const vots = localStorage.getItem(`vots-${id}`) || 0;

          const card = document.createElement("div");
          card.className = "card";
          card.innerHTML = `
            <h3>${nom}</h3>
            <p><strong>Matrícula:</strong> ${arbre["Matrícula"]}</p>
            <p><strong>Vots:</strong> <span id="comptador-${id}">${vots}</span></p>
            <button onclick="votar('${id}')">Vota!</button>
          `;
          container.appendChild(card);
        });
      });
    });
  });

// Funció per votar
function votar(id) {
  let vots = parseInt(localStorage.getItem(`vots-${id}`) || "0");
  vots += 1;
  localStorage.setItem(`vots-${id}`, vots);
  document.getElementById(`comptador-${id}`).textContent = vots;
}
