# Decision Log

## 2026-10-07: Staging environment
- Choice: Render (free tier), deployed via deploy hook from GitHub Actions.
- Why: free, no server to maintain, fast to set up.
- Trade-off: less control than a VPS; free tier sleeps after inactivity.
- Alternatives considered: VPS + SSH, local Docker Compose.
## Docker image
- Base: python:3.12-slim, non-root user, gunicorn as the server.
- Why: small, safer, production-style server instead of Flask's dev server.
- Known limitation: pytest and flake8 are in the image because they share
  requirements.txt. Next improvement: split into requirements-dev.txt.