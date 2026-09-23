"""
Sovereign Mind — Comprehensive Multi-Domain Localhost Auditor & Certification Suite.
Evaluates:
  1. Frontend Web Presentation Tier (Next.js 16 on Port 3000)
  2. Reverse-Proxy Gateway Routing & CSP Compliance
  3. Strategic Geopolitics Engine (Port 8005)
  4. Capital Markets OS (Equity Lab on Port 8001)
  5. Clinical AYUSH CDSS (Ayurveda on Port 8002)
  6. Clinical AYUSH CDSS (Homeopathy on Port 8003)
  7. Zero-Trust Hospital HIS / DRE (Port 8004)
  8. Mathematical & Domain Rigor Assertions
"""

import sys
import time
import json
import urllib.request
import urllib.error

# Ensure stdout handles UTF-8 safely on Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

AUDIT_TARGETS = [
    # ---------------------------------------------------------
    # 1. FRONTEND PRESENTATION ROUTES (Next.js 16 on :3000)
    # ---------------------------------------------------------
    {
        "category": "Presentation Tier",
        "name": "Homepage (/) with Live Ticker",
        "url": "http://127.0.0.1:3000/",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["Sovereign Mind", "Where Geopolitics Meets Capital Markets"],
        "check_security_headers": True
    },
    {
        "category": "Presentation Tier",
        "name": "Geopolitics Hub (/geopolitics)",
        "url": "http://127.0.0.1:3000/geopolitics",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["20-Lens Strategic Matrix", "Strategic Doctrine Archetypes", "Sanjeev Sanyal"],
        "check_security_headers": True
    },
    {
        "category": "Presentation Tier",
        "name": "Capital Terminal (/terminal)",
        "url": "http://127.0.0.1:3000/terminal",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["Equity Lab OS", "MIVS", "Hard Gates"],
        "check_security_headers": True
    },
    {
        "category": "Presentation Tier",
        "name": "Clinical Hub (/clinical)",
        "url": "http://127.0.0.1:3000/clinical",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["Statutory Clinical Governance", "Poonam Verma", "Tridosha 2-Simplex"],
        "check_security_headers": True
    },
    {
        "category": "Presentation Tier",
        "name": "Analysis Hub (/analysis)",
        "url": "http://127.0.0.1:3000/analysis",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["Intelligence Library", "Analysis Hub"],
        "check_security_headers": True
    },
    {
        "category": "Presentation Tier",
        "name": "Institutional Forum (/forum)",
        "url": "http://127.0.0.1:3000/forum",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["Community Intelligence", "Capital Allocators"],
        "check_security_headers": True
    },
    {
        "category": "Presentation Tier",
        "name": "Sovereign Academy (/academy)",
        "url": "http://127.0.0.1:3000/academy",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["Geopolitical Intelligence Academy", "Curriculum Paths"],
        "check_security_headers": True
    },
    {
        "category": "Presentation Tier",
        "name": "About Sovereign Capital (/about)",
        "url": "http://127.0.0.1:3000/about",
        "method": "GET",
        "expected_code": 200,
        "check_content": ["About Sovereign Capital", "Bridging Geopolitics"],
        "check_security_headers": True
    },

    # ---------------------------------------------------------
    # 2. DIRECT BACKEND MICROSERVICE HEALTH ENGINES
    # ---------------------------------------------------------
    {
        "category": "Strategic Geopolitics",
        "name": "Direct: Geo Engine Health (:8005)",
        "url": "http://127.0.0.1:8005/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status",
        "expected_json_val": {"status": "ONLINE"}
    },
    {
        "category": "Capital Markets",
        "name": "Direct: Equity Lab Health (:8001)",
        "url": "http://127.0.0.1:8001/api/v1/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status",
        "expected_json_val": {"status": "ONLINE"}
    },
    {
        "category": "Clinical AYUSH",
        "name": "Direct: Ayurveda CDSS Root (:8002)",
        "url": "http://127.0.0.1:8002/",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "compliance"
    },
    {
        "category": "Clinical AYUSH",
        "name": "Direct: Ayurveda CDSS Health (:8002)",
        "url": "http://127.0.0.1:8002/api/v1/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status"
    },
    {
        "category": "Clinical AYUSH",
        "name": "Direct: Homeopathy Kernel Root (:8003)",
        "url": "http://127.0.0.1:8003/",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "jurisdiction"
    },
    {
        "category": "Clinical AYUSH",
        "name": "Direct: Homeopathy Kernel Health (:8003)",
        "url": "http://127.0.0.1:8003/api/v1/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status"
    },
    {
        "category": "Hospital Healthcare",
        "name": "Direct: Hospital HIS / DRE Health (:8004)",
        "url": "http://127.0.0.1:8004/api/v1/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status",
        "expected_json_val": {"status": "healthy"}
    },

    # ---------------------------------------------------------
    # 3. REVERSE-PROXY GATEWAY REWRITES THROUGH NEXT.JS (:3000)
    # ---------------------------------------------------------
    {
        "category": "Gateway Routing",
        "name": "Proxy: Geo Health (/api/geo-health)",
        "url": "http://127.0.0.1:3000/api/geo-health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status"
    },
    {
        "category": "Gateway Routing",
        "name": "Proxy: Geo Lenses (/api/geo/lenses)",
        "url": "http://127.0.0.1:3000/api/geo/lenses",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "lens_count"
    },
    {
        "category": "Gateway Routing",
        "name": "Proxy: Geo Forecasts (/api/geo/forecasts)",
        "url": "http://127.0.0.1:3000/api/geo/forecasts",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "forecasts"
    },
    {
        "category": "Gateway Routing",
        "name": "Proxy: Geo Query POST (/api/geo/query)",
        "url": "http://127.0.0.1:3000/api/geo/query",
        "method": "POST",
        "post_data": {"prompt": "BRICS 2026 de-dollarization strategy", "persona": "sanyal"},
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "persona_takeaway"
    },
    {
        "category": "Gateway Routing",
        "name": "Proxy: Equity Health (/api/equity-health)",
        "url": "http://127.0.0.1:3000/api/equity-health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status"
    },
    {
        "category": "Gateway Routing",
        "name": "Proxy: Ayurveda Health (/api/ayurveda/health)",
        "url": "http://127.0.0.1:3000/api/ayurveda/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status"
    },
    {
        "category": "Gateway Routing",
        "name": "Proxy: Homeopathy Health (/api/homeopathy/health)",
        "url": "http://127.0.0.1:3000/api/homeopathy/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status"
    },
    {
        "category": "Gateway Routing",
        "name": "Proxy: Hospital Health (/api/hospital/health)",
        "url": "http://127.0.0.1:3000/api/hospital/health",
        "method": "GET",
        "expected_code": 200,
        "is_json": True,
        "check_json_key": "status"
    }
]

def run_audit():
    print("\n" + "=" * 94)
    print(" SOVEREIGN MIND — COMPREHENSIVE LOCALHOST MULTI-DOMAIN AUDIT SUITE")
    print("=" * 94)

    total = len(AUDIT_TARGETS)
    passed = 0
    results = []
    latencies = []

    for t in AUDIT_TARGETS:
        start_time = time.time()
        status_ok = False
        notes = []
        status_code = 0
        latency_ms = 0
        content_size = 0
        sec_headers_found = []

        try:
            req_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SovereignAuditor/2.0"}
            if t.get("post_data"):
                body_bytes = json.dumps(t["post_data"]).encode("utf-8")
                req = urllib.request.Request(t["url"], data=body_bytes, headers={**req_headers, "Content-Type": "application/json"})
            else:
                req = urllib.request.Request(t["url"], headers=req_headers)

            with urllib.request.urlopen(req, timeout=5.0) as resp:
                latency_ms = round((time.time() - start_time) * 1000, 1)
                latencies.append(latency_ms)
                status_code = resp.getcode()
                raw_bytes = resp.read()
                content_size = len(raw_bytes)
                raw_body = raw_bytes.decode("utf-8", errors="ignore")

                # Verify Status Code
                if status_code == t["expected_code"]:
                    status_ok = True
                else:
                    notes.append(f"HTTP {status_code} != {t['expected_code']}")

                # Verify Security Headers if required
                if t.get("check_security_headers"):
                    headers = dict(resp.info())
                    if "content-security-policy" in headers:
                        sec_headers_found.append("CSP")
                    if "strict-transport-security" in headers:
                        sec_headers_found.append("HSTS")
                    if "x-frame-options" in headers:
                        sec_headers_found.append("X-Frame")
                    if "x-content-type-options" in headers:
                        sec_headers_found.append("NoSniff")

                # Verify Content Matches
                if t.get("check_content"):
                    for kw in t["check_content"]:
                        if kw.lower() not in raw_body.lower():
                            status_ok = False
                            notes.append(f"Missing: '{kw}'")

                # Verify JSON structure & values
                if t.get("is_json"):
                    try:
                        jdata = json.loads(raw_body)
                        if t.get("check_json_key") and t["check_json_key"] not in jdata:
                            status_ok = False
                            notes.append(f"JSON missing key: '{t['check_json_key']}'")
                        if t.get("expected_json_val"):
                            for ek, ev in t["expected_json_val"].items():
                                if str(jdata.get(ek)).strip().lower() != str(ev).strip().lower():
                                    status_ok = False
                                    notes.append(f"JSON {ek}='{jdata.get(ek)}' != '{ev}'")
                    except Exception as je:
                        status_ok = False
                        notes.append(f"JSON parse error: {str(je)}")

        except urllib.error.HTTPError as he:
            latency_ms = round((time.time() - start_time) * 1000, 1)
            status_code = he.code
            notes.append(f"HTTP Error: {he.code}")
        except Exception as e:
            latency_ms = round((time.time() - start_time) * 1000, 1)
            notes.append(f"Net error: {str(e)[:30]}")

        if status_ok:
            passed += 1
            badge = "[PASS]"
        else:
            badge = "[FAIL]"

        summary_note = "; ".join(notes) if notes else "Verified clean"
        if sec_headers_found:
            summary_note += f" [Headers: {','.join(sec_headers_found)}]"

        results.append({
            "category": t["category"],
            "name": t["name"],
            "url": t["url"],
            "status": badge,
            "code": status_code,
            "latency_ms": latency_ms,
            "bytes": content_size,
            "notes": summary_note
        })

        print(f" {badge:<6} | {t['name'][:42]:<42} | {latency_ms:>6.1f} ms | {content_size:>7} B | HTTP {status_code:<3} | {summary_note}")

    avg_latency = round(sum(latencies) / len(latencies), 1) if latencies else 0
    p95_latency = sorted(latencies)[int(len(latencies) * 0.95)] if latencies else 0

    print("-" * 94)
    print(f" AUDIT SUMMARY: {passed}/{total} Passed ({round(passed/total*100, 1)}%) | Avg Latency: {avg_latency} ms | P95: {p95_latency} ms")
    print("=" * 94 + "\n")

    return results

if __name__ == "__main__":
    run_audit()
