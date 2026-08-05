# Domain Docs

This is a single-context repository. Engineering skills should use the following domain documentation when exploring the codebase.

## Before exploring

- Read `CONTEXT.md` at the repository root when it exists.
- Read relevant architecture decision records under `docs/adr/` when they exist.
- If either location is absent, proceed silently. Do not create placeholder documents.

The `/domain-modeling` skill creates these files lazily when terminology or architectural decisions are actually resolved.

## Expected structure

```text
/
|-- CONTEXT.md
|-- docs/adr/
`-- source directories
```

## Vocabulary

When output names a domain concept in an issue, proposal, hypothesis, or test, use the term defined in `CONTEXT.md`. Avoid synonyms that the glossary explicitly rejects.

If a needed concept is absent, reconsider whether the term belongs to the project or note the gap for `/domain-modeling`.

## ADR conflicts

If proposed work contradicts an existing ADR, call out the conflict explicitly instead of silently overriding the decision.
