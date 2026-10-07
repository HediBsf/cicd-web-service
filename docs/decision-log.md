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
  ## Trivy scan method
- Choice: run Trivy from a pinned container image (0.69.2) instead of trivy-action.
- Why: the action's version tags were compromised in March 2026; the original
  tag I used no longer resolves. A pinned image avoids relying on mutable tags.
- Trade-off: slightly more verbose workflow step.