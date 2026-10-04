# External ACS falsification with SCQOS

This example shows a simple idea:

**An agent asks to do something → ACS carries the request → an independent Guardian decides → the action happens only if allowed → the test checks what actually changed.**

The external Guardian here is SCQOS. The important part is not the product name. The important part is that the test does not trust either implementation to grade itself.

## Why this example exists

AGT already has extensive first-party tests. External interoperability asks a different question: can a separate Guardian receive the same class of governed request, fail closed on bad input, and leave evidence another engineer can reproduce?

The public SCQOS ACS falsification lab exercises valid requests, wrong-authority requests, missing or tampered signatures, stale timestamps, replayed request IDs, chain mismatches, all five ACS-style dispositions, a controlled real filesystem consequence, and deliberately broken Guardians so an easy-to-game harness cannot report a trustworthy green result.

## Reproduce

```bash
git clone https://github.com/KnowledgeeKZA3224/scqos-acs-falsification-lab.git
cd scqos-acs-falsification-lab
./scripts/bootstrap.sh
./scripts/verify-everything.sh
```

The run writes machine-readable evidence under `run-evidence/` and exits non-zero when a required assertion or harness-integrity control fails.

## Initial published evidence

The external project's pinned initial run records **20/20** SCQOS Guardian lab probes passing against its live ProofGate path, **6/6** deliberate harness mutants detected, and a controlled cloud-to-terminal consequence proof in which the authorized write happened, the wrong-authority write did not, replay was blocked, and the target digest stayed unchanged after the rejected replay.

Those numbers describe that pinned run. They are **not** an OWASP certification, a Microsoft certification, or a claim that either implementation is defect-free.

## Differential use with AGT

The same harness can point at an AGT-backed Guardian and preserve the observations beside the SCQOS run. Differences are not decided by majority vote. The applicable ACS requirement is the oracle; each implementation is reported independently.

A green run means only that the pinned implementation produced the recorded behavior for the pinned inputs in that run. It does not mean certified, unbreakable, or automatically conformant in future versions.

## Prior art and related projects

- Microsoft Agent Governance Toolkit: https://github.com/microsoft/agent-governance-toolkit
- OWASP Agent Control Standard project: https://github.com/GenAI-Security-Project/agent-control-standard
- SCQOS reference implementation: https://github.com/KnowledgeeKZA3224/scqos-reference-implementation
- SCQOS ACS falsification lab: https://github.com/KnowledgeeKZA3224/scqos-acs-falsification-lab

SCQOS is an independent external project. This example does not make it a Microsoft-supported component and does not add it as an AGT dependency.
