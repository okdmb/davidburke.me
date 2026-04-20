# Publish Accessibility Posts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish two accessibility-themed posts by updating their publication dates to the current time.

**Architecture:** Hugo posts with future dates are not built by default. Changing the `date` in front matter to a past or current time makes them visible.

**Tech Stack:** Hugo (Markdown/Front Matter)

---

### Task 1: Update "From Specialty to Standard" post date

**Files:**
- Modify: `content/post/specialized-features-gone-mainstream/index.md`

- [ ] **Step 1: Read current file to ensure exact match**

- [ ] **Step 2: Update date to 2026-04-20T03:00:00Z**

```markdown
date = 2026-04-20T11:00:00Z
```
to
```markdown
date = 2026-04-20T03:00:00Z
```

### Task 2: Update "The Digital Curb Cut Effect" post date

**Files:**
- Modify: `content/post/the-digital-curb-cut-effect/index.md`

- [ ] **Step 1: Read current file to ensure exact match**

- [ ] **Step 2: Update date to 2026-04-20T03:00:00Z**

```markdown
date = 2026-04-20T10:00:00Z
```
to
```markdown
date = 2026-04-20T03:00:00Z
```

### Task 3: Verification

- [ ] **Step 1: Run Hugo to build the site and check for errors**

Run: `hugo`
Expected: Success, no "future" warnings.

- [ ] **Step 2: Verify both posts are in the generated index.json**

Run: `grep -E "From Specialty to Standard|The Digital Curb Cut Effect" public/index.json`
Expected: Matches found.
