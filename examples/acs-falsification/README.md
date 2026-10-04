# External ACS Guardian falsification example

This example shows a simple way to test an external **Agent Control Standard (ACS) Guardian** beside Microsoft Agent Governance Toolkit (AGT) without asking anyone to trust either implementation just because it says it is correct.

## The idea in plain English

An AI agent asks to do something.

A Guardian decides whether that exact action should be allowed, denied, deferred, modified, or sent for approval.

A serious test should not stop at **"the Guardian returned the right word."** It should also check whether the real bounded action actually happened, whether a blocked action stayed blocked, whether replay was rejected, and whether the evidence can be independently reproduced.

The testing circuit is:

```text
same ACS request
      |
      +--> AGT / reference Guardian
      |
      +--> external Guardian
                |
                v
       compare against the
       pinned ACS requirement
                |
                v
       inspect the real effect
                |
                v
       preserve reproducible evidence
```

The **ACS requirement is the oracle**. One Guardian is not considered correct merely because it disagrees with another.

## Why falsification matters

A test is weak if an implementation can cheat by always allowing, always denying, ignoring signatures, ignoring replay, skipping tests, or merely printing "success."

A stronger harness deliberately injects those broken behaviors and proves that the harness turns red.

That changes the question from:

> "Can this implementation produce a green demo?"

to:

> "Can another engineer reproduce the same inputs, attack the same assumptions, inspect the same side effects, and still get the same result?"

## Public worked example: SCQOS

The public **SCQOS ACS Falsification Lab** is an independently implemented example of this testing pattern:

https://github.com/KnowledgeeKZA3224/scqos-acs-falsification-lab

The repository publishes the Guardian adapter, falsification harness, negative controls, evidence records, claim boundaries, and one-command reproduction path.

Its initial published run records:

- **20/20 SCQOS laboratory probes passed** against the live SCQOS decision substrate.
- **All 6 deliberately broken harness conditions were detected**: allow-everything, deny-everything, signature-blind, replay-blind, fake-success, and skipped-test execution.
- The controlled cloud-to-terminal consequence proof verified that:
  - an authorized write occurred;
  - a wrong-authority write did not occur;
  - the first valid replay-target execution occurred once;
  - the duplicate request was rejected;
  - the target SHA-256 remained unchanged after the rejected replay.

Those statements describe the **published pinned run only**. They are not a claim of Microsoft, OWASP, or third-party certification.

## Reproduce it

```bash
git clone https://github.com/KnowledgeeKZA3224/scqos-acs-falsification-lab.git
cd scqos-acs-falsification-lab
./scripts/bootstrap.sh
./scripts/verify-everything.sh
```

A successful run produces machine-readable evidence under `run-evidence/`.

## How to interpret a result

A green result means:

- the exact pinned implementation,
- the exact pinned ACS revision,
- the exact probes,
- and the exact recorded environment

behaved as documented for that run.

A green result does **not** mean:

- the implementation is universally secure;
- every future ACS revision will behave the same way;
- Microsoft or OWASP certified the external project;
- disagreement with AGT automatically proves AGT or the external Guardian is wrong.

The useful output is the evidence itself: inputs, decisions, side effects, failures, hashes, and enough information for another engineer to challenge the result.

## Scope

This contribution is documentation/example material only. It does not change AGT runtime behavior, security defaults, public APIs, or package dependencies.

## Prior art and related projects

- Microsoft Agent Governance Toolkit: https://github.com/microsoft/agent-governance-toolkit
- OWASP / GenAI Security Project Agent Control Standard: https://github.com/GenAI-Security-Project/agent-control-standard
- SCQOS ACS Falsification Lab: https://github.com/KnowledgeeKZA3224/scqos-acs-falsification-lab
