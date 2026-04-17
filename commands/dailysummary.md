# Daily Summary

Produce a concise, well-formatted daily briefing covering Jira, Gmail, and Calendar.

## Execution

Run these fetches **in parallel** (single message, multiple tool calls):

### 1. Jira — active tickets assigned to me
1. `mcp__claude_ai_Atlassian__getAccessibleAtlassianResources` → pick the cloudId
2. `mcp__claude_ai_Atlassian__searchJiraIssuesUsingJql` with:
   - `cloudId`: from step 1
   - `jql`: `assignee = currentUser() AND statusCategory != Done ORDER BY updated DESC`
   - `fields`: `["summary","status","priority","updated","issuetype"]`

For each issue, build the URL as `https://<site-url>/browse/<ISSUE-KEY>` using the site URL from `getAccessibleAtlassianResources`.

### 2. Gmail — last 24h, inbox minus noise
`mcp__claude_ai_Gmail__search_threads` with:
- `q`: `in:inbox newer_than:1d -category:promotions -category:social`
- `max_results`: 25

For each thread, build the link as `https://mail.google.com/mail/u/0/#inbox/<threadId>`.

### 3. Calendar — today's events (primary)
`mcp__claude_ai_Google_Calendar__list_events` with:
- `calendar_id`: `primary`
- `time_min` / `time_max`: today 00:00 → tomorrow 00:00 in the user's local timezone (Europe/Helsinki)
- `single_events`: true
- `order_by`: `startTime`

## Output format

Render as clean markdown. **No emojis.** Use this exact structure:

```
# Daily Summary — <YYYY-MM-DD, Weekday>

## Today's Calendar
- **HH:MM–HH:MM** — Event title _(location if any)_
  <one-line description if useful>
...
_(or "No events scheduled." if empty)_

## Active Jira Tickets (<count>)
Grouped by status. Within each group, sorted by priority then updated desc.

### <Status name>
- **[KEY-123](https://…/browse/KEY-123)** — Summary line _(Priority · updated <relative>)_
...

## Inbox — Last 24h (<count>)
Grouped by sender when 2+ from same sender; otherwise flat list. Newest first.

- **[Subject line](https://mail.google.com/…)** — _Sender_ · <relative time>
  <snippet, 1 line, truncated to ~120 chars>
...
```

## Rules
- Parallelise all three fetches.
- If a section is empty, state that explicitly — don't omit the heading.
- Relative times: "2h ago", "yesterday 14:30", etc.
- Keep snippets to one line. Strip quoted reply chains.
- If any fetch fails, show the failure inline under its section and continue with the others.
- Do not ask follow-up questions. Just output the summary.
