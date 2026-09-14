# Prairie Bench local preview — completion report

Date: 2026-09-14 | Agent: Wilma | Status: Completed local preview

## Assignment and scope

- **Goal:** Give Canmore homeowners a clear path to request a garden-care conversation in the supplied fictional one-page demo.
- **Authorized work:** Create a corrected local `preview.html` from the supplied `index.html`, then test it. No publication, real service, backend, or change to `index.html` was authorized.
- **Protected content retained:** Prairie Bench fictional business name, garden-care service descriptions, Canmore location, simple green identity, fictional-demo notice, and no-customer-claims boundary.

## Deliverable

- **Artifact:** `preview.html` in this folder.
- **State:** Local preview only. No form backend or message-delivery route exists.
- **Operator and capability:** Plain local HTML/CSS/inline JavaScript. The provided Chromium harness loaded only the named local HTML and blocked all network requests.

## Changes made

- Corrected the hero action from the missing `#quote` fragment to the real `#contact` conversation form.
- Added the approved local focus behavior: activating the hero action scrolls to the conversation area and focuses the Name field.
- Kept Services, How it works, and Contact visible at 390 px as touch-sized links.
- Rebuilt the form as separate label/input field stacks with full-width inputs and a button below them.
- Changed the result to: “Thanks. Your demo request was recorded on this page; no message was sent.”
- Preserved the visible note: “Demo form: no messages are delivered.”

## Tests and results

| Check | Conditions | Result |
|---|---|---|
| Desktop render | Chromium, 1280 px wide, network blocked | Passed: navigation visible, no broken same-page links, no horizontal overflow. Screenshot: `preview-1280.png`. |
| Mobile render | Chromium, 390 px wide, network blocked | Passed: navigation visible, fields stack cleanly, no horizontal overflow. Screenshot: `preview-390.png`. |
| Hero conversation path | Chromium, 390 px wide, mouse activation | Passed: Name field became the active element after the hero action; Contact section was scrolled into view. |
| Form interaction | Chromium, 1280 px and 390 px wide; synthetic name/email only | Passed: required fields accepted valid synthetic data and showed the accurate no-delivery status. |
| Keyboard check | Chromium, 390 px wide | Passed: focus moved from the Name field back to the hero action with Shift+Tab; visible focus styling is defined for links, inputs, and buttons. |

## Self-review

**Method: self-review.** Checked against findings WC-01 through WC-04 in `critique.md`.

- **WC-01:** Closed — hero action reaches and focuses the actual form.
- **WC-02:** Closed — mobile has visible Services, How it works, and Contact links.
- **WC-03:** Closed — labels and inputs are separate vertical fields at 390 px.
- **WC-04:** Closed — submission status accurately says no message was sent.

## Limits, recovery, and next action

- **Known limit:** This is a fictional local demonstration. The form records a status on the page only; it does not deliver an enquiry.
- **Business outcome:** Unmeasured. No tracking or live traffic exists for this fixture.
- **Recovery:** Delete `preview.html` and its generated preview screenshots to return the directory to its supplied fixture state; `index.html` was not changed.
- **Next action:** Jack can review `preview.html` locally. Publication or connecting a real form requires separate approval and verification.
