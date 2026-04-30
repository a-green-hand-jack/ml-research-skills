# Citation Audit Report Template

Use this template for saved reports or substantial chat reports.

```markdown
# Citation Audit Report

Date: YYYY-MM-DD
Paper root:
Main TeX:
BibTeX files:
Target venue:

## Summary
- Overall status:
- Blocking issues:
- Important issues:
- Warnings:
- Unverified items:

## Files Checked

## Deterministic TeX/BibTeX Graph Check

### Passed

### Blocking Issues

### Warnings

## Metadata Verification

| Key | Status | Source checked | Issue | Action |
|---|---|---|---|---|

## Citation Claim Audit

| Location | Citation | Local claim | Role | Support | Action |
|---|---|---|---|---|---|

## Reference and Label Hygiene

## Recommended Fix Plan
1. Fix blocking TeX/BibTeX graph issues.
2. Fix blocking metadata mismatches.
3. Resolve unsupported high-risk claims.
4. Clean warnings if time permits.

## Unresolved Author Decisions

## Commands Run
```

## Status Labels

Overall status:

- `READY`: no blocking or important issues remain
- `READY_WITH_WARNINGS`: no blocking or important issues remain, but cleanup is recommended
- `NEEDS_FIXES`: blocking or important issues remain
- `INCOMPLETE_AUDIT`: required sources could not be accessed or the user asked for a partial audit

## Final Chat Summary

When replying in chat, keep it short:

```markdown
Citation audit status: NEEDS_FIXES

Blocking:
- ...

Important:
- ...

Verified:
- ...

Report saved to: ...
```
```
