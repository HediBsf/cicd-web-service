# Decision Log

## 2026-10-07: Staging environment
- Choice: Render (free tier), deployed via deploy hook from GitHub Actions.
- Why: free, no server to maintain, fast to set up.
- Trade-off: less control than a VPS; free tier sleeps after inactivity.
- Alternatives considered: VPS + SSH, local Docker Compose.