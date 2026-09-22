# Sovereignmind

> **Autonomous Multi-Domain Ecosystem for Institutional Geopolitical Intelligence, Quantitative Capital Markets, and Zero-Trust Clinical Healthcare.**

[![Next.js 16](https://img.shields.io/badge/Next.js-16.2.5-black.svg)](https://nextjs.org/)
[![React 19](https://img.shields.io/badge/React-19.2.4-blue.svg)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141+-009688.svg)](https://fastapi.tiangolo.com/)
[![Python 3.14](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Ecosystem-Certified%20Production-brightgreen.svg)]()

---

## 🏛️ Ecosystem Architecture

Sovereignmind unifies five autonomous, specialized intelligence backends through a unified **Next.js 16 Reverse-Proxy Gateway (BFF)**:

```
                               SOVEREIGN MIND PLATFORM (svgin1)
                                      [Port: 3000]
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         │                                 │                                 │
   /geopolitics                        /terminal                         /clinical
         │                                 │                                 │
         ▼                                 ▼                                 ▼
Geo_Economy_politics               Equity_Lab_v_0.0            Sovereign Health Hub
  [Port: 8005]                       [Port: 8001]             ┌─────────────────────┐
  • 20-Lens Strategic Matrix         • 94 Production Endpoints │ • AYURVEDA (8002)   │
  • 6 Persona Projections            • 27-Engine Screener      │ • HOMEOPATHY (8003) │
  • 5-Tier Truth Hierarchy           • MIVS 100-Point Gates    │ • HOSPITAL (8004)   │
  • 89 Calibrated Forecasts          • GenAI Red-Team Audit    └─────────────────────┘
```

---

## 🌐 Capability Suites & Modules

### 1. Presentation Tier (`svgin1`)
- **Port:** `3000`
- **Stack:** Next.js 16.2.5 (App Router, Turbopack), React 19.2.4, Tailwind CSS v4, Lucide icons, Framer Motion, GSAP, Prisma 7.
- **Routes:**
  - `/` — Homepage with dynamic telemetry ticker sync.
  - `/geopolitics` — 20-Lens Strategic Matrix, 6 persona doctrine projections (Sanyal, Doval, Jaishankar, Ranganathan, Ankit Shah, Neutral), and negative-space communiqué deconstruction.
  - `/terminal` — Capital Markets OS, 27-engine multibagger screener, market regime detection, and GenAI concall red-team audits.
  - `/clinical` — Statutory clinical decision support (AYUSH & Hospital HIS) with NCISM/NCH/NMC Poonam Verma doctrine defense and ARN verification.
  - `/analysis`, `/forum`, `/academy`, `/about`, `/admin` — Preserved core editorial and community modules.

### 2. Strategic Geopolitics (`Geo_Economy_politics`)
- **Port:** `8005` (`geo_engine/api_server.py`)
- **Capabilities:**
  - 20-Lens Strategic Matrix (DeepTech, Petro-Logistics, Subsea Cables, Astro-Politics, Caloric Sovereignty, etc.).
  - 5-Tier Epistemic Truth Hierarchy (Kinetic Ground > Financial CapEx > Treaties > Kinesics > PR Communiqués).
  - 89 Calibrated Forecast records stored in SQLite `events.db`.

### 3. Capital Markets OS (`Equity_Lab_v_0.0`)
- **Port:** `8001` (`app/main.py`)
- **Capabilities:**
  - 94 institutional REST endpoints.
  - 27-Engine Multibagger Framework (§51-§58).
  - MIVS 100-Point Score & 7 Hard Negative Gates.
  - Options A2 Payoff calculator and valuation-responsive SIP policy (§40).

### 4. Ayurvedic Clinical Decision Support (`AYURVEDA_AGENT`)
- **Port:** `8002` (`main.py`)
- **Capabilities:**
  - 52 FastAPI routers under `/api/v1`.
  - Tridosha 2-Simplex ($\Delta^2$) conserved biophysical calculus ($V + P + K \equiv 100\%$).
  - 28-point botanical drug interaction matrix and Schedule E(1) statutory poison firewall.

### 5. Homeopathic CSR Repertory Kernel (`HOMEOPATHY_AGENT`)
- **Port:** `8003` (`app/main.py`)
- **Capabilities:**
  - Compressed Sparse Row (CSR) bipartite graph repertorization kernel across Kent's 37 chapters.
  - Information-Theoretic Shannon Entropy rubric weighting.
  - Dynamic Posology Calculus ($\sigma = \frac{S \times V}{\Delta T + 1.0}$).

### 6. Zero-Trust Hospital Infrastructure (`HOSPITAL_AGENT`)
- **Port:** `8004` (`services/core-api/main.py`)
- **Capabilities:**
  - Rust Deterministic Rule Engine (@48.4µs).
  - ESI 5-Tier Emergency Triage with decoupled zero-payment resuscitation priority.
  - Trilingual discharge dossiers in Bengali (বাংলা), Hindi (हिंदी), and English with 2D QR bridges.

---

## 🚀 Quick Start & Process Supervision

### 1. Audit Ecosystem Ports & Telemetry
```bash
python start_ecosystem.py --check
```

### 2. Run the Next.js Frontend
```bash
cd svgin1
npm run dev
# Open http://localhost:3000
```

### 3. Build & Prerender for Production
```bash
cd svgin1
npm run build
```

---

## 📜 Full Upgradation Journey
For the complete, line-by-line machine-verifiable history and mathematical proofs of this ecosystem, see [`History_upgradation.md`](History_upgradation.md).
