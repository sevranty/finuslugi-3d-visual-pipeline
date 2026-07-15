# PR Ready Gates

The initial architecture PR may move from Draft to Ready only after all gates pass on one unchanged HEAD:

- deterministic validator: pass;
- valid fixtures: pass;
- invalid fixtures: rejected;
- relative links: pass;
- asset checksum verification: pass;
- owner review: no unresolved P1 or P2 findings;
- known limitations: documented;
- rights review blockers: explicitly retained for release;
- separate owner instruction: received.
