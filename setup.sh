#!/bin/bash
set -euo pipefail

echo "🔧 Configurando entorno Python 3.13 con uv para Toolforge..."

# Instalar uv en el home si no está disponible
if ! command -v uv &>/dev/null && [ ! -x "$HOME/.local/bin/uv" ]; then
  echo "📥 Instalando uv en \$HOME/.local/bin..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Asegurar que $HOME/.local/bin esté en el PATH
export PATH="$HOME/.local/bin:$PATH"

# Verificar instalación
echo "🐍 uv versión: $(uv --version)"

# Eliminar venv existente

# Asegurar que uv gestione Python 3.13
echo "⬇️  Instalando Python 3.13 con uv (si no está ya)..."
# Activar (uv venv crea el activate igual que venv)

# Instalar dependencias del proyecto con uv pip
echo "📦 Instalando dependencias..."
uv sync

echo "✅ Entorno Python 3.13 listo"
echo "🐍 Versión: $(python --version)"
echo "📂 Venv: $(which python)"
echo "🛠️  uv: $(which uv)"
