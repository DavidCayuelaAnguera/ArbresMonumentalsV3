#!/usr/bin/env python3
"""
Script per reduir la resolució d'una imatge a 1920x1080 píxels.

Aquest script utilitza la llibreria Pillow (PIL) per redimensionar una imatge
anomenada 'fons.jpg' a la resolució Full HD (1920x1080) mantenint la
qualitat òptima.

Autor: Script automatitzat
Data: 2025
"""

import os
import sys
from PIL import Image, ImageOps
from pathlib import Path


def resize_image(input_path: str, output_path: str, target_size: tuple = (1920, 1080)) -> bool:
    """
    Redimensiona una imatge a la mida especificada.
    
    Args:
        input_path (str): Ruta del fitxer d'imatge original
        output_path (str): Ruta on guardar la imatge redimensionada
        target_size (tuple): Tupla amb la mida objectiu (amplada, alçada)
    
    Returns:
        bool: True si l'operació ha estat exitosa, False en cas contrari
    
    Raises:
        FileNotFoundError: Si el fitxer d'entrada no existeix
        PermissionError: Si no hi ha permisos per escriure el fitxer de sortida
        PIL.UnidentifiedImageError: Si el fitxer no és una imatge vàlida
    """
    try:
        # Verificar que el fitxer d'entrada existeix
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"El fitxer '{input_path}' no existeix")
        
        # Obrir la imatge
        print(f"Carregant imatge: {input_path}")
        with Image.open(input_path) as img:
            # Mostrar informació de la imatge original
            print(f"Mida original: {img.size} píxels")
            print(f"Format: {img.format}")
            print(f"Mode: {img.mode}")
            
            # Verificar si la imatge ja té la mida objectiu
            if img.size == target_size:
                print("La imatge ja té la mida objectiu!")
                return True
            
            # Redimensionar la imatge mantenint la qualitat
            # Utilitzem LANCZOS per obtenir la millor qualitat en el redimensionament
            resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
            
            # Guardar la imatge redimensionada
            print(f"Guardant imatge redimensionada: {output_path}")
            resized_img.save(output_path, quality=95, optimize=True)
            
            print(f"✅ Imatge redimensionada correctament a {target_size} píxels")
            return True
            
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return False
    
    except PermissionError as e:
        print(f"❌ Error de permisos: {e}")
        print("Verifica que tens permisos d'escriptura al directori de destí")
        return False
    
    except Image.UnidentifiedImageError:
        print(f"❌ Error: '{input_path}' no és un fitxer d'imatge vàlid")
        return False
    
    except Exception as e:
        print(f"❌ Error inesperat: {e}")
        return False


def main():
    """
    Funció principal del script.
    
    Redimensiona la imatge 'fons.jpg' a 1920x1080 píxels i la guarda
    com 'fons_1920x1080.jpg' al mateix directori.
    """
    # Configuració de fitxers
    input_file = "fons.jpg"
    output_file = "fons_1920x1080.jpg"
    target_resolution = (1920, 1080)
    
    print("🖼️  Script de redimensionament d'imatges")
    print("=" * 50)
    
    # Verificar que Pillow està instal·lat
    try:
        from PIL import Image
    except ImportError:
        print("❌ Error: La llibreria Pillow no està instal·lada")
        print("Instal·la-la amb: pip install Pillow")
        sys.exit(1)
    
    # Executar el redimensionament
    success = resize_image(input_file, output_file, target_resolution)
    
    if success:
        # Mostrar informació dels fitxers
        input_size = os.path.getsize(input_file) / (1024 * 1024)  # MB
        output_size = os.path.getsize(output_file) / (1024 * 1024)  # MB
        
        print("\n📊 Resum de l'operació:")
        print(f"   Fitxer original: {input_file} ({input_size:.2f} MB)")
        print(f"   Fitxer resultant: {output_file} ({output_size:.2f} MB)")
        print(f"   Resolució final: {target_resolution[0]}x{target_resolution[1]} píxels")
        
        if output_size < input_size:
            reduction = ((input_size - output_size) / input_size) * 100
            print(f"   Reducció de mida: {reduction:.1f}%")
    else:
        print("\n❌ L'operació ha fallat. Revisa els errors anteriors.")
        sys.exit(1)


if __name__ == "__main__":
    main()
