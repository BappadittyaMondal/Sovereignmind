"""
Sovereign Mind — Ecosystem Master Orchestrator & Telemetry Health Supervisor.
Provides machine-verifiable diagnostics, port audits, and service coordination
across all five sovereign intelligence engines and the svgin1 web presentation tier.
"""

import sys
import os
import socket
import argparse
import json
import urllib.request
import urllib.error
from typing import Dict, Any

SERVICES = {
    "frontend": {
        "name": "svgin1 (Next.js 16 Web Portal)",
        "port": 3000,
        "health_url": "http://127.0.0.1:3000",
        "domain": "Presentation Tier"
    },
    "geo_engine": {
        "name": "Geo_Economy_politics (20 Lenses & 5 Personas)",
        "port": 8005,
        "health_url": "http://127.0.0.1:8005/health",
        "command": "python -m uvicorn geo_engine.api_server:app --port 8005",
        "cwd": "Geo_Economy_politics",
        "domain": "Strategic Geopolitics"
    },
    "equity_lab": {
        "name": "Equity_Lab_v_0.0 (94-Endpoint Capital Markets OS)",
        "port": 8001,
        "health_url": "http://127.0.0.1:8001/api/v1/health",
        "command": "python -m uvicorn app.main:app --port 8001",
        "cwd": "Equity_Lab_v_0.0",
        "domain": "Capital Markets"
    },
    "ayurveda": {
        "name": "AYURVEDA_AGENT (A-CDSS 52 Routers)",
        "port": 8002,
        "health_url": "http://127.0.0.1:8002/health",
        "command": "python -m uvicorn main:app --port 8002",
        "cwd": "AYURVEDA_AGENT",
        "domain": "Clinical AYUSH"
    },
    "homeopathy": {
        "name": "HOMEOPATHY_AGENT (CSR Repertory Kernel)",
        "port": 8003,
        "health_url": "http://127.0.0.1:8003/health",
        "command": "python -m uvicorn app.main:app --port 8003",
        "cwd": "HOMEOPATHY_AGENT",
        "domain": "Clinical AYUSH"
    },
    "hospital": {
        "name": "HOSPITAL_AGENT (Zero-Trust HIS / DRE)",
        "port": 8004,
        "health_url": "http://127.0.0.1:8004/health",
        "command": "python -m uvicorn services.core-api.main:app --port 8004",
        "cwd": "HOSPITAL_AGENT",
        "domain": "Hospital Healthcare"
    }
}


def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    """Check if TCP port is actively bound."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0


def probe_http(url: str, timeout: float = 1.5) -> Dict[str, Any]:
    """Perform HTTP probe against service health endpoint."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SovereignMindSupervisor/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.getcode()
            body = resp.read().decode("utf-8", errors="ignore")
            try:
                data = json.loads(body)
            except Exception:
                data = body[:100]
            return {"status": "ONLINE", "http_code": code, "data": data}
    except urllib.error.HTTPError as he:
        return {"status": "ONLINE_WARN", "http_code": he.code, "error": str(he)}
    except Exception as e:
        return {"status": "OFFLINE", "error": str(e)}


def audit_ecosystem() -> Dict[str, Any]:
    """Execute complete deterministic audit across the ecosystem."""
    report = {
        "timestamp": os.environ.get("CURRENT_TIME", "2026-09-23"),
        "total_services": len(SERVICES),
        "results": {}
    }

    for key, meta in SERVICES.items():
        port_active = is_port_in_use(meta["port"])
        probe = probe_http(meta["health_url"]) if port_active else {"status": "PORT_CLOSED"}

        report["results"][key] = {
            "name": meta["name"],
            "port": meta["port"],
            "domain": meta["domain"],
            "port_bound": port_active,
            "probe": probe
        }

    return report


def main():
    parser = argparse.ArgumentParser(description="Sovereign Mind Ecosystem Supervisor")
    parser.add_argument("--check", action="store_true", help="Audit all ecosystem services and ports")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    audit = audit_ecosystem()

    if args.json:
        print(json.dumps(audit, indent=2))
        return

    print("\n" + "=" * 78)
    print(" SOVEREIGN MIND — MULTI-DOMAIN ECOSYSTEM STATUS REPORT")
    print("=" * 78)
    print(f" {'SERVICE':<38} | {'PORT':<5} | {'PORT STATUS':<12} | {'HEALTH PROBE'}")
    print("-" * 78)

    for key, data in audit["results"].items():
        port_str = "BOUND [ACTIVE]" if data["port_bound"] else "FREE [OFFLINE]"
        probe_stat = data["probe"].get("status", "N/A")
        print(f" {data['name'][:38]:<38} | {data['port']:<5} | {port_str:<12} | {probe_stat}")

    print("=" * 78 + "\n")


if __name__ == "__main__":
    main()
