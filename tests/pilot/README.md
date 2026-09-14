# Wilma Website Suite Pilot

Date: 2026-09-14 (Mountain Time) | Cody | Result: local HTML pilot passed

## What ran

Wilma's real OpenClaw main agent ran five isolated tasks with its existing model settings: analysis, critique, production, tabletop boundaries, and a fresh critique retest. The text files are the input prompts. Markdown reports are Wilma's outputs; absolute paths and screenshot references refer to the retained Wilma workspace. Compact run/session/tool receipts are in receipts.json; private system context and full logs are excluded.

## Evidence

- index.html is the original fictional defective fixture. Its hash was unchanged after all tasks.
- preview.html is Wilma's corrected editable artifact.
- analysis.md shows a useful partial source-based analysis after browser access was blocked.
- critique.md locates the seeded broken hero link, missing mobile navigation and false delivery message, plus the cramped form layout.
- production.md records the actual changed artifact and self-review.
- retest.md verifies WC-01 through WC-04 closed and recommends no further corrections within the demo scope.
- boundaries.md records ten tabletop routing/failure cases; it does not prove real integration behavior.
- render-original.json and verify-preview.json record before/after local Chromium checks. Screenshots were visually reviewed and remain with the preview on Wilma and in Cody's local task artifacts.

## Test harness

render.cjs and verify.cjs are disposable test utilities, excluded from runtime packages. They use the already available /app/node_modules/playwright-core and /usr/bin/chromium, load only the local fixture and block all network requests. The Chromium no-sandbox setting matches the existing container runtime. They do not change browser policy. Copy the fixture and helpers into a disposable directory on an equivalent test host before running; paths are specific to Wilma's pilot environment.

## What this does not prove

No real form delivery, client WordPress/GHL edits, native multi-page template propagation, public launch, formal accessibility/security compliance or business lift was tested. The demo needs no backend, so absence of delivery is an explicit limitation rather than an unresolved demo defect. Full keyboard-only and screen-reader testing remain untested.
