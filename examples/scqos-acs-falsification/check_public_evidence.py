"""Verify the shape of the public SCQOS ACS evidence summary.

This checks published evidence only. It does not certify AGT or SCQOS.
"""
from __future__ import annotations

import json
import urllib.request

SUMMARY = "https://raw.githubusercontent.com/KnowledgeeKZA3224/scqos-acs-falsification-lab/main/evidence/SUMMARY.json"


def main() -> int:
    with urllib.request.urlopen(SUMMARY, timeout=15) as response:
        data = json.load(response)

    artifacts = data.get("artifacts", [])
    ok = (
        bool(data.get("all_pass"))
        and bool(artifacts)
        and all(item.get("all_pass") is True for item in artifacts)
    )

    print(f"external evidence summary: {'PASS' if ok else 'FAIL'}")
    for item in artifacts:
        print(f"- {item.get('mode')}: {item.get('sha256')}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
