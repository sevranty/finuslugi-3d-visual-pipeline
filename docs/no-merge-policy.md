# No-Merge Policy

The initial architecture pull request is review-only until the owner explicitly changes lifecycle state.

- Do not mark Ready automatically.
- Do not enable auto-merge.
- Do not merge after a successful validator run without separate owner instruction.
- Any commit after validation invalidates the previous validation report.
- Any commit after owner review invalidates the previous review evidence.
- Rights review and visual regression remain independent release gates even after architecture acceptance.
