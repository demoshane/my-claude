# Global Learnings

Cross-project rules from past bugs. Strict filter: only truly universal patterns. Keep under 40 lines.

---

## SQL Migrations — Verify Column Exists

When adding columns to UPDATE/INSERT statements, verify the column exists in both CREATE TABLE schema AND the migration chain. Test with a fresh DB.

---

## Electron printToPDF — Unlock Height Chain

`printToPDF` clips at scroll containers. Any `body { height: 100vh }` + `main { overflow-y: auto }` layout produces a viewport-sized PDF. Always include in `@media print`: `html, body { height: auto; overflow: visible }` and the same on every scrollable ancestor down to the content element.

---
