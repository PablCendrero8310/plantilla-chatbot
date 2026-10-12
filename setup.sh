#!/bin/bash
set -euo pipefail

echo "🔧 Configurando entorno Python 3.13 para Toolforge..."

# Eliminar venv existente
rm -rf pyvenv

# Crear nuevo venv con Python 3.13 explícito
python3.13 -m venv pyvenv

# Activar
source pyvenv/bin/activate

# Actualizar pip, wheel y setuptools
pip install -U pip wheel setuptools

# Instala las dependencias del proyecto
echo "📦 Instalando dependencias..."
pip install .

echo "✅ Entorno Python 3.13 listo"
echo "🐍 Versión: $(python --version)"
echo "📂 Venv: $(which python)"
