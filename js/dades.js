/**
 * Autor: David Cayuela Anguera
 * Any: 2025
 * Descripció: Funcions per carregar arbres monumentals segons la comarca
 */

function carregarArbresPerComarca(comarca, provincia) {
    
    const contenedor = document.getElementById('llista-arbres');
    const fitxer = provincia === 'barcelona' ? '../data/arbres_barcelona.json' : '../data/arbres_girona.json';
    console.log("Carregant JSON des de:", fitxer);

    fetch(fitxer)
        .then(resposta => resposta.json())
        .then(dades => {
            const arbres = dades.filter(arbre => arbre.Comarca === comarca);

            if (arbres.length === 0) {
                contenedor.innerHTML = '<p>No s\'han trobat arbres per aquesta comarca.</p>';
                return;
            }

            let html = '<ul>';
            arbres.forEach(arbre => {
                html += `<li><a href="../arbres/${arbre.Matricula}.html">${arbre["Nom de l'arbre"]}</a></li>`;
            });
            html += '</ul>';
            contenedor.innerHTML = html;
        })
        .catch(error => {
            console.error('Error carregant els arbres:', error);
            contenedor.innerHTML = '<p>Error carregant dades.</p>';
        });
        console.log("Arbres trobats:", arbres);

}
