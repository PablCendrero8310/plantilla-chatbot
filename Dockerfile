# Dockerfile
FROM docker-registry.svc.toolforge.org/toolforge-python313-sssd-web:latest

WORKDIR /opt/tool

# Copia archivos de configuración primero (mejor caché)
COPY pyproject.toml ./
COPY setup.sh .

# Da permisos al script
RUN chmod +x setup.sh

# Crea y configura el entorno virtual
# Esto instala las dependencias dentro del contenedor
RUN setup.sh

# Copia el resto del código
COPY src/ ./src/

# Si tienes tests, cópialos también

# Expone puerto (solo si es web service)

# Comando por defecto (ajusta según tu bot)
CMD ["python -m plantilla-chatbot"]
