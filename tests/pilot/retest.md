# Prairie Bench demo — corrected preview retest

Date: 2026-09-14 | Reviewer: Wilma | Status: Review only

## Readiness verdict

**Ready within the reviewed scope: a usable, fictional local demo visitor journey.**

The corrected `preview.html` gives a mobile visitor a clear path from the garden-care offer to the conversation form, accepts a valid synthetic submission, and accurately states that no message was delivered. The four material findings in `critique.md` are verified closed. This is not permission to publish, add a backend, or represent the form as a real enquiry channel.

## Review scope and method

- **Artifact:** `preview.html`, inspected 2026-09-14 in the supplied local-only Chromium harness.
- **Audience and task:** busy Canmore homeowners seeking garden care and requesting a conversation in a fictional demo.
- **Coverage:** 390 × 900 mobile and 1280 × 900 desktop rendering; visible same-page links; hero action; mobile navigation; required-field validation; valid synthetic form submission; visible focus styling.
- **Test conditions:** `node render.cjs preview.html`; the approved harness loaded the local file and blocked network requests. Additional scoped Chromium checks used the same blocked-network condition.
- **Measured results:** at both widths, navigation was visible, no broken same-page anchors were found, and no horizontal overflow was detected. The rendered mobile screenshot is `preview-390.png`; desktop is `preview-1280.png`.
- **Excluded:** real message delivery, recipient/CRM receipt, live deployment, analytics, performance measurement, screen-reader testing, and a full accessibility audit. These are untested or out of scope, not defects in this local demo.

## Keep

- The clear garden-care offer, Canmore audience, and simple outcome-led headline remain intact.
- The fictional-demo notice and no-customer-claims boundary remain visible.
- The one-H1 / logical-section structure and plain service summary remain easy to scan.
- The form retains explicit labels, browser required-field validation, and a polite status region.

## Retested findings

### WC-01 — Primary call to action misses the conversation form

- **State:** Verified closed | **Priority:** Blocker | **Confidence:** High
- **Direct observation:** at 390 px, activating “Ask about garden care” scrolled the contact section into view and moved focus to the `Name` input. The field was visible in the viewport. The corrected link and handler target `#contact`.
- **Result:** the primary visitor path now reaches a usable conversation form.

### WC-02 — Mobile visitors have no visible navigation path

- **State:** Verified closed | **Priority:** Important | **Confidence:** High
- **Direct observation:** at 390 px, Services, How it works, and Contact each rendered as visible links (about 113 px wide by 41 px high). Each opened its intended same-page section during the local interaction check.
- **Result:** mobile visitors have a direct route to the content and contact area.

### WC-03 — Form field layout is cramped and visually confusing on mobile

- **State:** Verified closed | **Priority:** Important | **Confidence:** High
- **Direct observation:** the 390 px render shows Name and Email as separate vertical fields. Each label is above its matching full-width input, with clear spacing; the button follows both fields. No horizontal overflow was detected.
- **Result:** the conversion step is legible and usable in the reviewed mobile state.

### WC-04 — Confirmation text overstates delivery

- **State:** Verified closed | **Priority:** Important | **Confidence:** High
- **Direct observation:** a valid synthetic submission displayed: “Thanks. Your demo request was recorded on this page; no message was sent.” The visible demo note also says no messages are delivered.
- **Result:** the local completion state does not imply a real enquiry was sent.

## Additional checked behavior

- An empty form submission was stopped by native required-field validation; Chromium focused the Name field and displayed its standard missing-value message.
- Keyboard focus styling is visible on the first mobile navigation link (3 px outline). A complete keyboard-only and screen-reader journey was not tested.
- The form's status proves only the on-page demo interaction. It does not prove delivery, storage, or receipt anywhere else.

## Conclusion and next action

No corrections are recommended for the requested limited demo journey. Jack can review the local `preview.html` and the two generated screenshots. Any future publication, real form connection, or delivery claim requires separate approval and end-to-end testing.

**Rollback:** none required; this review changed no preview or service state. The harness refreshed only its local screenshots.
