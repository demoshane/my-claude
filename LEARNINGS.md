# Global Learnings

Cross-project rules from past bugs. Strict filter: only truly universal patterns. Keep under 40 lines.

---

## SQL Migrations — Verify Column Exists

When adding columns to UPDATE/INSERT statements, verify the column exists in both CREATE TABLE schema AND the migration chain. Test with a fresh DB.

---
