#!/usr/bin/env python3
"""
Knowledge Base Setup Script - Smart Version
Descarga e instala la Knowledge Base de Generación Distribuida en tu proyecto
Detecta y usa MCP si está disponible, o usa git tradicional como fallback

Uso:
    python kb_setup.py
    
    o directamente desde URL:
    curl -o kb_setup.py https://raw.githubusercontent.com/MollytheCatLoca/RN-gd-linea-sur/main/kb_setup.py && python kb_setup.py
"""

import os
import subprocess
import shutil
import sys
import json
from pathlib import Path

# Configuración del repositorio
REPO_OWNER = "MollytheCatLoca"
REPO_NAME = "RN-gd-linea-sur"
REPO_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}.git"
KB_PATH = "version_final/knowledge_base"

def check_mcp_available():
    """Verifica si MCP está disponible en el sistema"""
    try:
        # Intenta detectar si hay herramientas MCP disponibles
        # Esta es una verificación simplificada
        import importlib.util
        return importlib.util.find_spec("mcp") is not None
    except:
        return False

def setup_kb_with_mcp():
    """Usa MCP GitHub para descargar la KB (más eficiente)"""
    print("🔌 MCP detectado! Usando método directo...")
    print("⚠️  Para usar MCP, ejecuta desde Claude Code con el siguiente comando:")
    print("\n" + "="*60)
    print("# Instrucciones para Claude Code con MCP:")
    print(f"# 1. Obtener estructura: mcp__github__get_file_contents('{REPO_OWNER}', '{REPO_NAME}', '{KB_PATH}/')")
    print("# 2. Para cada carpeta, descargar recursivamente los archivos")
    print("# 3. Guardar localmente con Write tool")
    print("="*60 + "\n")
    return False

def setup_kb_traditional():
    """Descarga y configura la Knowledge Base usando git tradicional"""
    
    print("📥 Usando método tradicional (git clone)...")
    print("=" * 60)
    
    # Verificar si ya existe
    if os.path.exists("knowledge_base"):
        response = input("⚠️  Ya existe una carpeta 'knowledge_base'. ¿Deseas reemplazarla? (s/n): ")
        if response.lower() != 's':
            print("❌ Instalación cancelada.")
            return
        shutil.rmtree("knowledge_base")
    
    # Directorio temporal
    temp_dir = "/tmp/kb_temp_gd"
    
    try:
        # Clonar repositorio (solo la carpeta necesaria con depth=1)
        print(f"📥 Descargando Knowledge Base desde {REPO_URL}...")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        
        result = subprocess.run([
            "git", "clone", "--depth=1",
            REPO_URL,
            temp_dir
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Error al descargar: {result.stderr}")
            return
        
        # Copiar Knowledge Base
        kb_source = os.path.join(temp_dir, KB_PATH)
        kb_dest = "./knowledge_base"
        
        if not os.path.exists(kb_source):
            print("❌ No se encontró la Knowledge Base en el repositorio")
            print(f"   Buscando en: {kb_source}")
            return
            
        shutil.copytree(kb_source, kb_dest)
        
        # Limpiar
        shutil.rmtree(temp_dir)
        
        # Verificar instalación
        expected_dirs = [
            "1_fundamentos",
            "2_metodologia", 
            "3_analisis_tecnico",
            "4_innovacion",
            "5_beneficios",
            "6_analisis_economico",
            "7_casos_estudio",
            "8_guia_implementacion",
            "9_guias_operativas",
            "herramientas",
            "ejemplos"
        ]
        
        missing = [d for d in expected_dirs if not os.path.exists(f"knowledge_base/{d}")]
        
        if missing:
            print(f"⚠️  Advertencia: Faltan directorios: {', '.join(missing)}")
        
        print("\n✅ Knowledge Base instalada exitosamente!")
        print(f"📁 Ubicación: {os.path.abspath('knowledge_base')}")
        print("\n📚 Contenido instalado:")
        print("   • KB.1-9: Documentación completa")
        print("   • /herramientas: Plantillas Excel y scripts Python")
        print("   • /ejemplos: Casos de estudio reales")
        print("\n🎯 Próximos pasos:")
        print("   1. Lee knowledge_base/README.md para una visión general")
        print("   2. Para evaluar un proyecto: KB.8 (Guía de Implementación)")
        print("   3. Para análisis económico: KB.6 + herramientas/")
        print("\n💡 Tip: Busca 'KB_Quick_Start' en MCP Memory para más guías de uso")
        
    except Exception as e:
        print(f"❌ Error durante la instalación: {str(e)}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        sys.exit(1)

def setup_kb_smart():
    """Detecta el mejor método e instala la KB"""
    print("🚀 Instalando Knowledge Base de Generación Distribuida...")
    print("🔍 Detectando mejor método de instalación...")
    
    if "--mcp" in sys.argv:
        print("📌 Forzando instrucciones MCP...")
        setup_kb_with_mcp()
    elif check_mcp_available():
        setup_kb_with_mcp()
    else:
        setup_kb_traditional()

def show_info():
    """Muestra información sobre la Knowledge Base"""
    print("\n📋 INFORMACIÓN DE LA KNOWLEDGE BASE")
    print("=" * 60)
    print("Framework universal para análisis de generación distribuida")
    print("Basado en proyectos exitosos con TIR > 20%")
    print("\nEstructura:")
    print("  • Fundamentos teóricos y metodología")
    print("  • Análisis técnico y económico")
    print("  • Casos de estudio y benchmarks")
    print("  • Guías de implementación")
    print("  • Herramientas y plantillas")
    print(f"\nRepositorio: {REPO_URL}")
    print("\nPara más información, busca 'KB_Generacion_Distribuida' en MCP Memory")

def show_mcp_instructions():
    """Muestra instrucciones detalladas para usar con MCP"""
    print("\n🔌 INSTRUCCIONES PARA USAR CON MCP")
    print("=" * 60)
    print("Si tienes Claude Code con MCP activo, puedes usar estos comandos:")
    print("\n# Opción 1: Delegar a Task Agent")
    print("Task: 'Descargar Knowledge Base desde GitHub'")
    print(f"  - Owner: {REPO_OWNER}")
    print(f"  - Repo: {REPO_NAME}")
    print(f"  - Path: {KB_PATH}")
    print("  - Descargar recursivamente todas las carpetas y archivos")
    print("\n# Opción 2: Comandos MCP directos")
    print(f"mcp__github__get_file_contents('{REPO_OWNER}', '{REPO_NAME}', '{KB_PATH}/')")
    print("# Luego para cada carpeta, obtener archivos y guardar con Write")
    print("\n# Opción 3: Buscar en MCP Memory")
    print("search_nodes('KB generacion distribuida')")
    print("# Seguir instrucciones detalladas que aparecen")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Setup de Knowledge Base para Generación Distribuida")
    parser.add_argument("--info", action="store_true", help="Muestra información sobre la KB")
    parser.add_argument("--mcp", action="store_true", help="Muestra instrucciones para MCP")
    
    args = parser.parse_args()
    
    if args.info:
        show_info()
    elif args.mcp:
        show_mcp_instructions()
    else:
        setup_kb_smart()