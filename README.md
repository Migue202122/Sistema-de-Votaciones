# API RESTful de Sistema de Votaciones (FastAPI)

Prueba técnica de desarrollo construida con **FastAPI**, **SQLAlchemy/Pydantic** y procesamiento de datos con **Pandas**.

# Características

- **Gestión de Votantes y Candidatos:** Registro de usuarios con validación estricta para evitar que un votante sea candidato y viceversa.
- **Sistema de Voto Único:** Control de integridad para garantizar que cada votante emita un único sufragio (`has_voted`).
- **Análisis y Visualización:** Módulo de utilidades con Pandas para generar representaciones gráficas del estado de las votaciones.

# Tecnologías Utilizadas

- FastAPI
- Pydantic
- Pandas
- Uvicorn

# Instalación y Ejecución Local

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/Migue202122/Sistema-de-Votaciones.git](https://github.com/Migue202122/Sistema-de-Votaciones.git)
   cd Sistema-de-Votaciones