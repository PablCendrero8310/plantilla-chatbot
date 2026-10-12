#!/bin/bash
set -euo pipefail

FILTERS_DIR="src/plantilla_chatbot/filters"

if [ -d "$FILTERS_DIR" ] && [ "$(ls -A "$FILTERS_DIR")" ]; then
  echo "Filtros ya presentes, saltando clonado"
  exit 0
fi

if [ -z "${GIT_USERNAME:-}" ] || [ -z "${GIT_TOKEN:-}" ]; then
  echo "ERROR: GIT_USERNAME y GIT_TOKEN no están definidos"
  exit 1
fi

git clone "https://${GIT_USERNAME}:${GIT_TOKEN}@gitlab.wikimedia.org/pcendrer/plantilla-chatbot-filtros.git" \
  "$FILTERS_DIR"

rm -rf "$FILTERS_DIR/.git"
echo "Filtros clonados correctamente"
