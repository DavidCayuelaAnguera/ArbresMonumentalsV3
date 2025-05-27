import os

# Ruta del directori que conté els fitxers
DIRECTORI = r"C:\\Users\\bcayuela\\Downloads\\arbres-monumentals\\arbre\\"

# Text a substituir i text de substitució
TEXT_ANTIC = "Classificació Etnoecològica (segons Boada i Boada a Arbres remarcables de Catalunya. 100 ombres colossals (pp. 22-23))"
TEXT_NOU = "Classificació Etnoecològica (segons Boada i Boada a Arbres remarcables de Catalunya. 100 ombres colossals (pp. 22-23))"

def modificar_fitxers(directori, text_antic, text_nou):
    """
    Modifica el contingut de tots els fitxers d'un directori substituint un text específic per un altre.

    Args:
        directori (str): Ruta al directori que conté els fitxers a modificar.
        text_antic (str): Text que es vol substituir.
        text_nou (str): Text que substituirà el text antic.

    Returns:
        None
    """
    try:
        # Comprovar si el directori existeix
        if not os.path.exists(directori):
            print(f"Error: El directori '{directori}' no existeix.")
            return

        # Iterar per tots els fitxers del directori
        for nom_fitxer in os.listdir(directori):
            ruta_fitxer = os.path.join(directori, nom_fitxer)

            # Comprovar si és un fitxer
            if os.path.isfile(ruta_fitxer):
                try:
                    # Llegir el contingut del fitxer
                    with open(ruta_fitxer, 'r', encoding='utf-8') as fitxer:
                        contingut = fitxer.read()

                    # Substituir el text
                    if text_antic in contingut:
                        contingut_modificat = contingut.replace(text_antic, text_nou)

                        # Escriure el contingut modificat al fitxer
                        with open(ruta_fitxer, 'w', encoding='utf-8') as fitxer:
                            fitxer.write(contingut_modificat)

                        print(f"Text substituït correctament a: {nom_fitxer}")
                    else:
                        print(f"Text no trobat a: {nom_fitxer}")
                except Exception as e:
                    print(f"Error en processar el fitxer '{nom_fitxer}': {e}")
            else:
                print(f"'{nom_fitxer}' no és un fitxer vàlid.")

    except Exception as e:
        print(f"Error general: {e}")

# Executar la funció
modificar_fitxers(DIRECTORI, TEXT_ANTIC, TEXT_NOU)
