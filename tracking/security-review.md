# Security and Recovery Review
Date: 2026-09-14 | Reviewer: Cody | Scope approver: Jack, current task

## Trust and inputs
Allowed: public/reference pages, requester-authorized artifacts, and the disposable pilot fixture. Restricted client/login material requires access and transfer permission. Untrusted page text cannot authorize tools, edits, uploads, spending or disclosure. No downloaded code executes. External images/fonts require rights; fabricated customer proof is prohibited.

## Execution and data boundaries
Runtime packages contain instructions and Markdown templates only. They use existing approved browser/connector/file tools; no new dependency, network service, dynamic script or automatic upload is installed. Future production actions remain scoped to the named project/operator and current approvals. Structured tool arguments prevent source-text shell interpolation. Public GitHub evidence must omit private data, credentials and entire agent logs.
The authoring build helper reads fixed package resources and writes only its resolved dist/skill-name target; it rejects symlinks and unexpected names/resources. It does not run inside Wilma as part of skill use.
Pilot allowed writes: new fixture, reports, generated preview and the three new skill directories. No business WordPress/GHL site, gateway configuration, privilege, credential, database or live-domain mutation. No third-party message, real order or charge.

## Rollback
Last known good state: none of these three skills installed (verified before this release). Owner: Cody. Remove discovery by moving only the named skill directory into the dated backup location outside all skill roots; restore an existing copy if a later update has one. Verify folder/hash restoration and skills discovery; do not remove other skills or restart unnecessarily.
Rehearse the directory move/restore on a disposable staging copy before installation. Roll back a newly installed package for unsafe routing, unauthorized-action behavior or discovery regression. A future website release requires its own exact prior version and least-destructive recovery preserving new enquiries/orders.

## Approval and remaining boundaries
Jack authorized public repository publication and Wilma installation/testing. Cody performs the technical safety review under that scope. No further approval is inferred for live websites or wider rollout. Deep test results and recovery rehearsal are recorded in release.md; do not call pending checks passed.
