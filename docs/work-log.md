# Work Log

- 2026-10-07: Created repo and folder structure. Drafted requirements.
- 2026-10-07: Architecture diagram, Flask app, tests passing locally.- <today's date>: Dockerfile built and tested locally (health OK, container healthy).
- 2026-10-08: Dockerfile built and tested locally (port 8010 because 8000 was in use).
- 2026-10-09: CI workflow (lint + tests) green. Failed runs diagnosed (flake8 W292/E303/W293) and fixed. Deliberate red PR captured.
- 2026-10-09: Added Docker build, Trivy scan and GHCR push to the pipeline.
