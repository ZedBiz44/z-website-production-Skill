# Prairie Bench fixture: website analysis

## Answer

This is a fictional, single-page garden-care service site. It takes a visitor from a clear local-service promise to a brief list of services, then explains the first step and presents a name/email request form. On a desktop-width view, the header menu jumps to those three sections. The form intentionally stops normal submission, shows “Thanks! Request sent.” locally, and states that no messages are delivered.

## Coverage and evidence

- **Source inspected:** `index.html`, supplied fixture at `http://127.0.0.1:8765/index.html`.
- **Inspection time:** 2026-09-14, 5:07 PM America/Edmonton.
- **Method:** static source and responsive CSS inspection. No login, data submission, publication, or site change was performed.
- **Rendered-browser limit:** the managed browser rejected both the supplied `file:` URL and loopback navigation under policy. Desktop and mobile rendering, click targets, keyboard use, and the form’s live status update were therefore **not rendered-tested**.

## How the page works

1. **Header/navigation:** The desktop header identifies the demo and provides `Services`, `How it works`, and `Contact` links. Each points to a matching section on the same page.
2. **Opening message:** The H1 targets busy Canmore homeowners; the paragraph frames the benefit as enjoying the yard without weekend maintenance.
3. **Service explanation:** The Services section names three offer types: seasonal cleanup, recurring care, and planting support.
4. **Process explanation:** The next section sets the expected first step: a short conversation followed by a written work scope.
5. **Contact path:** The Contact section asks for a required name and an email-formatted email address. Its inline handler prevents a real form submit and places a confirmation message in a `role="status"` area. The visible note says this demo does not deliver messages.

### Responsive behavior found in source

- At viewports **above 600px**, the `nav` is a flex row with 25px gaps.
- At **600px or below**, the CSS sets `nav{display:none}`. The header brand remains, but the source contains no menu button or other replacement navigation. This is an observation of the CSS rule, not a rendered mobile test.
- Shared page containers use a 1000px maximum width and 24px padding; sections have 30px vertical padding.

## Reusable pattern: anchored service-journey menu

**Pattern:** A short header menu mirrors the page’s decision path: offer (`Services`) → method (`How it works`) → action (`Contact`). Each item links to a clearly identified same-page section.

- **Why it may help:** For a short, single-service page, it lets a visitor skip directly to the question they have without adding extra page loads or a complex menu.
- **Best fit:** A focused local service offer with a small amount of supporting content and one main contact action.
- **Limits:** It does not suit a content-heavy site or multiple service lines. On this fixture, hiding the whole menu at 600px or below without a replacement would remove that shortcut for mobile visitors.
- **Adapt, do not copy:** Reuse the offer → process → contact sequence, but use the actual service labels and approved brand language for the destination site.

## Practical experiment

For a future single-service landing page, test a mobile menu button that reveals the same three anchored links. Compare the percentage of mobile visitors who reach the contact section or start the form with the current baseline. **Baseline and business impact are unmeasured in this fixture.**

## Source pointers

- [Fixture source](./index.html): document structure, CSS, anchored links, form handler, and demo-delivery notice.
- [Analysis workflow](../skills/z-website-analysis/SKILL.md): learning-only scope and evidence requirements.

