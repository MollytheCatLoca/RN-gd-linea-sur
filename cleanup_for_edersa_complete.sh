#!/bin/bash
# Script completo de limpieza y configuración para EDERSA
# Ejecutar desde el directorio gd-edersa-calidad

echo "🧹 Limpiando proyecto para EDERSA..."

# 1. ELIMINAR DATOS ESPECÍFICOS DE LÍNEA SUR
echo "📁 Limpiando datos..."
rm -rf data/processed/*
rm -rf data/viejos/
rm -rf data/external/*
rm -rf data/interim/*
rm -f data/*.pdf data/*.docx data/*.jpeg data/*.md
rm -f data/4\ Unifiliar*
rm -f data/Linea\ Sur*
rm -f data/Costo*
rm -f data/Análisis*

# 2. ELIMINAR DOCUMENTACIÓN ESPECÍFICA
echo "📄 Limpiando documentación..."
rm -rf docs/economic_analysis/
rm -rf docs/technical_analysis/
rm -rf docs/phases/
rm -rf docs/topology/
rm -rf docs/validation/
rm -rf docs/equipment/
rm -rf docs/dashboard/
rm -rf docs/dev/
rm -f docs/dc_*
rm -f docs/fase*
rm -f docs/phase*
rm -f docs/bess_*
rm -f docs/CLAUDE.md
rm -f docs/roadmap_fases_4-9.md

# 3. ELIMINAR REPORTS ESPECÍFICOS
echo "📊 Limpiando reportes..."
rm -rf reports/

# 4. ELIMINAR SCRIPTS ESPECÍFICOS
echo "🔧 Limpiando scripts..."
rm -rf scripts/analysis/
rm -rf scripts/clustering/
rm -rf scripts/debug/
rm -rf scripts/demo/
rm -rf scripts/exploratory/
rm -rf scripts/validation/
rm -f scripts/process_*
rm -f scripts/test_*
rm -f scripts/analyze_*
rm -f scripts/solar_*
rm -f scripts/validate_*
rm -f scripts/optimize_*

# 5. LIMPIAR TESTS ESPECÍFICOS
echo "🧪 Limpiando tests..."
rm -rf tests/results/
rm -rf tests/unit/test_fase*
rm -rf tests/unit/test_phase*
rm -rf tests/unit/test_dc_*
rm -rf tests/unit/test_bess_*
rm -rf tests/unit/test_cap_*
rm -rf tests/unit/test_dashboard_*
rm -f tests/test_*

# 6. LIMPIAR SRC - MANTENER SOLO ESTRUCTURA BASE
echo "💻 Limpiando código fuente..."
rm -rf src/battery/
rm -rf src/power_flow/
rm -rf src/solar/
rm -rf src/validation/
rm -rf src/economics/
rm -rf src/losses/
rm -rf src/ml/
rm -rf src/network/
rm -rf src/node_analysis/
rm -rf src/optimization/
rm -rf src/performance/
rm -rf src/simulation/
rm -rf src/visualization/

# 7. CREAR NUEVA ESTRUCTURA PARA EDERSA
echo "🏗️ Creando estructura EDERSA..."
mkdir -p src/inventory
mkdir -p src/quality  
mkdir -p src/clustering
mkdir -p src/optimization
mkdir -p data/processed/{transformers,quality,geographic}
mkdir -p dashboard/pages
mkdir -p docs/{analysis,methodology}
mkdir -p tests/{unit,integration}
mkdir -p scripts/{processing,analysis}

# 8. ELIMINAR ARCHIVOS DEL ROOT NO NECESARIOS
echo "🗑️ Limpiando archivos raíz..."
rm -f EDERSA_PROJECT_SETUP.md
rm -f cleanup_for_edersa.sh

# 9. CREAR ARCHIVOS PLACEHOLDER
echo "📝 Creando archivos base..."

# __init__.py para los nuevos módulos
touch src/inventory/__init__.py
touch src/quality/__init__.py
touch src/clustering/__init__.py
touch src/optimization/__init__.py

# .gitkeep para mantener estructura
touch data/processed/transformers/.gitkeep
touch data/processed/quality/.gitkeep
touch data/processed/geographic/.gitkeep

echo "✅ Limpieza completada!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Copia los archivos de código del EDERSA_PROJECT_SETUP.md"
echo "2. Crea requirements_edersa.txt con las dependencias"
echo "3. Actualiza el README.md"
echo "4. Commit inicial: git add . && git commit -m 'Setup proyecto EDERSA'"