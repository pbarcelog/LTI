# Data Model – LTI App

The **canonical data model specification** (entities, fields, relationships, validation notes, and technical detail used alongside Django) is maintained in the AI specs repository path:

**→ [Data model specification](../ai-specs/ai-specs/specs/data-model.md)**

Use that file as the **single source of truth** when evolving models, migrations, or API resources. Update this `docs/` tree only for high-level product context (e.g. [product-context.md](./product-context.md), [architecture.md](./architecture.md)) unless you intentionally duplicate a short summary for stakeholders.

## Why a wrapper?

- **`docs/`** stays aligned with product and onboarding material.
- **`ai-specs/ai-specs/specs/data-model.md`** holds the detailed model documentation that agents and implementers should follow.

When the domain model changes, update **`../ai-specs/ai-specs/specs/data-model.md`** first, then adjust **`api-spec.yml`** and Django models accordingly.
