# Prairie Bench demo — mobile conversation journey critique

Date: 2026-09-14 | Reviewer: Wilma | Status: Review only

## Readiness verdict

**Fix before calling this demo ready for its stated mobile visitor journey.** The page explains a garden-care offer clearly, but its main “Ask about garden care” action points to a missing `#quote` anchor instead of the conversation form. A visitor who uses the prominent first action is not taken to a way to start a conversation.

This is a **Focused** review of the single supplied demo version at `http://127.0.0.1:8765/` (source: `index.html`), for a mobile visitor seeking garden care and requesting a conversation. It is not publication permission.

## Coverage and evidence

- **Inspected:** 2026-09-14, local disposable HTTP demo, unauthenticated.
- **Mobile rendering:** Chromium headless, 390 px wide. The rendered mobile page hid the full navigation and showed the contact form below the initial viewport.
- **Desktop rendering:** Chromium headless, 1440 × 900 (basic layout check only).
- **HTTP:** `GET /` returned `200 OK`; returned body matched the supplied `index.html`.
- **Synthetic form test (authorized):** submitted `Demo Visitor` / `demo@example.test` in the disposable demo. Browser validation passed and the status changed to “Thanks! Request sent.” The page did not navigate. The form has no configured delivery method beyond the default same-page GET action, and its inline handler calls `event.preventDefault()`.
- **Not fully tested:** keyboard-only sequence, screen-reader announcement, browser-native invalid-field wording, network delivery (explicitly out of scope and not implemented), performance, and a full accessibility audit.

## Keep

- **Clear audience and value:** the H1 names garden care and the Canmore homeowner audience; supporting copy gives a practical outcome.
- **Scannable service summary:** the three service types are easy to find.
- **Reasonable structure:** one H1 followed by H2 sections; the contact result uses `role="status"`.
- **Trust boundaries:** the page plainly identifies itself as fictional and makes no customer claims.

## Findings

### WC-01 — Primary call to action misses the conversation form

- **Priority:** Blocker | **State:** Open | **Confidence:** High
- **Component:** hero link, “Ask about garden care”
- **Evidence:** the rendered/source link is `href="#quote"`; the page contains sections with IDs `services`, `process`, and `contact`, but no `quote`. The form is in `#contact`.
- **Impact:** the most visible action does not move a mobile visitor toward the requested conversation. It leaves them at a nonexistent fragment instead of the form.
- **Exact correction:** point the hero action to `#contact` (or provide a real quote section containing the same conversation form). Preserve the garden-care wording and the fictional-demo disclosure.
- **Done when:** tapping the hero action on a 390 px viewport moves focus/scroll to the “Request a conversation” form, with its Name field visible and usable.
- **Retest:** actual mobile tap plus viewport screenshot.

### WC-02 — Mobile visitors have no visible navigation path

- **Priority:** Important | **State:** Open | **Confidence:** High
- **Component:** header navigation at ≤600 px
- **Evidence:** the stylesheet applies `@media(max-width:600px){nav{display:none}}`. At 390 px, the rendered header shows the Prairie Bench label but no Services, How it works, or Contact links; no menu replacement is present.
- **Impact:** visitors who do not use the hero link must scroll to discover services or the form. Once WC-01 is fixed, this is less harmful, but the normal mobile route remains absent.
- **Exact correction:** retain a clear mobile way to reach Services, How it works, and Contact—such as visible stacked links or an accessible menu. Do not add navigation complexity that obscures the main conversation action.
- **Done when:** at 390 px, a visitor can find and open/close the menu (if used) and reach all three destinations, including Contact, by touch and keyboard.
- **Retest:** mobile touch and keyboard navigation test.

### WC-03 — Form field layout is cramped and visually confusing on mobile

- **Priority:** Important | **State:** Open | **Confidence:** High
- **Component:** Request a conversation form at 390 px
- **Evidence:** in the mobile render, the Name input sits inline after its label, the Email label begins immediately after that input, and the Email input wraps onto the next line. The Send request button sits beside the wrapped input rather than following a clean field stack.
- **Impact:** a visitor can still complete the form, but the rushed layout weakens trust at the point of conversion and makes the required fields harder to scan.
- **Exact correction:** make each label/input pair a separate vertical field, with a clear gap between fields and the button below them. Keep explicit Name and Email labels and the existing `required` validation.
- **Done when:** at 390 px, both labels and full-width inputs are legible on separate lines, no label begins beside another input, and the button follows the completed fields without overlap or an ambiguous association.
- **Retest:** 390 px screenshot plus a synthetic valid submission.

### WC-04 — Confirmation text overstates delivery

- **Priority:** Important | **State:** Open | **Confidence:** High
- **Component:** post-submit status
- **Evidence:** the tested form displays “Thanks! Request sent.” Its own page copy says “Demo form: no messages are delivered,” and the inline submit code prevents the form from sending anywhere.
- **Impact:** “sent” implies a real conversation request reached someone. The disclosure appears below the form, so it does not reliably correct that impression at the completion moment.
- **Exact correction:** for this disposable demo, change the result to unambiguous wording such as: “Thanks. Your demo request was recorded on this page; no message was sent.” For a future real form, use delivery language only after the receiving route is verified.
- **Done when:** a synthetic valid submission shows a status message that accurately states the demo’s no-delivery behavior.
- **Retest:** submit authorized synthetic data and read the live status text.

## Handoff and acceptance checks

**Owner:** demo builder. **Deliverable:** corrected local demo and a mobile retest at the existing project folder.

Call the demo ready within this reviewed scope only when all of these are observed:

1. Hero action reaches the actual conversation form at 390 px.
2. Mobile navigation has a usable Services / How it works / Contact route.
3. The mobile form fields stack cleanly and a valid synthetic submission works.
4. The completion message accurately says no message was delivered (unless a separately authorized and verified delivery route is added).
5. The existing clear offer, fictional-demo notice, and no-customer-claims boundary remain intact.

**Rollback:** not applicable; this review changed no website files or live service state.
