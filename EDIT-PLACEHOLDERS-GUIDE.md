# 📝 How to Edit Blog Post Placeholders

## Quick Start: Open All Posts in VS Code

```bash
# Option 1: Open all posts at once in VS Code
code /Users/edikan/Documents/PROJECT\ FORGE/edikan-ai/posts/

# Option 2: Open specific post
code /Users/edikan/Documents/PROJECT\ FORGE/edikan-ai/posts/2025-09-10-transpose-button-confession.html
```

## Finding All Placeholders

### In VS Code:
1. Press `Cmd+Shift+F` (Mac) or `Ctrl+Shift+F` (Windows) for global search
2. Search for: `PLACEHOLDER`
3. You'll see all placeholders across all files
4. Click any result to jump to that location

### From Terminal:
```bash
# See all placeholders with context
cd /Users/edikan/Documents/PROJECT\ FORGE/edikan-ai/posts
grep -n "PLACEHOLDER" *.html

# Count total placeholders
grep -c "PLACEHOLDER" *.html | grep -v ":0"

# See placeholders with 2 lines of context
grep -B2 -A2 "PLACEHOLDER" *.html
```

## Types of Placeholders to Fill

### 1. Personal Story Placeholders
Look for: `[YOUR STORY - ... PLACEHOLDER]`

Example:
```html
<!-- BEFORE -->
<div class="personal-story">
    <strong>[YOUR STORY - LOOPS PLACEHOLDER]</strong>
    <p>Add your personal experience with loops...</p>
</div>

<!-- AFTER -->
<div class="personal-story">
    <p>It was my third week at the steel mill. I deployed what I thought was a simple temperature monitoring loop. By 3 AM, the entire production line had stopped. The monitoring system had consumed all available memory and crashed. My manager called it "the most expensive while loop in company history" - it cost us $50,000 in downtime.</p>
</div>
```

### 2. Specific Incident Placeholders
Look for: `[SPECIFIC INCIDENT PLACEHOLDER]`

Fill with:
- Exact date/time
- System affected
- People involved
- Cost/impact
- Your emotional state

### 3. Learning Moment Placeholders
Look for: `[YOUR LEARNING MOMENT PLACEHOLDER]`

Fill with:
- When it clicked
- What resource helped
- Who explained it
- The "aha" moment

### 4. Code Placeholders
Look for: `[CODE PLACEHOLDER - ...]`

Replace with actual code you wrote that had bugs

## Batch Editing Strategy

### Step 1: Create a tracking file
```bash
# Create a checklist of all placeholders
cd /Users/edikan/Documents/PROJECT\ FORGE/edikan-ai
grep -l "PLACEHOLDER" posts/*.html > placeholders-checklist.txt
```

### Step 2: Edit systematically
1. Start with Month 00 posts (most personal/vulnerable)
2. Add real incidents from your experience
3. Include actual code that failed
4. Be specific about costs/impacts

### Step 3: Preview your edits
```bash
# Open edited post in browser to preview
open /Users/edikan/Documents/PROJECT\ FORGE/edikan-ai/posts/2025-09-10-transpose-button-confession.html
```

## Quick Replace Examples

### For Confession Posts (Month 00):
- Replace `[YOUR DEBUGGING NIGHTMARE PLACEHOLDER]` with actual 2 AM debugging session
- Replace `[YOUR INFINITE LOOP STORY PLACEHOLDER]` with production incident
- Replace `[YOUR WAKE-UP CALL PLACEHOLDER]` with moment you realized you didn't understand

### For Competence Posts (Month 0):
- Replace `[YOUR EXCEL TRANSITION PLACEHOLDER]` with why you left Excel
- Replace `[YOUR SQL DISASTER PLACEHOLDER]` with actual query that crashed DB
- Replace `[YOUR GIT CONFUSION PLACEHOLDER]` with lost work incident

### For Math Posts (Month 1):
- Replace `[YOUR MATRIX CONFUSION PLACEHOLDER]` with why you didn't understand
- Replace `[YOUR STATISTICS MISUNDERSTANDING PLACEHOLDER]` with wrong assumptions
- Replace `[YOUR CALCULUS APPLICATION PLACEHOLDER]` with real optimization problem

### For Python Posts (Month 2):
- Replace `[YOUR NUMPY MISTAKE PLACEHOLDER]` with vectorization fail
- Replace `[YOUR PANDAS STRUGGLE PLACEHOLDER]` with data manipulation disaster
- Replace `[YOUR OVERFITTING STORY PLACEHOLDER]` with model that memorized noise

## VS Code Multi-Cursor Editing

To edit similar placeholders quickly:
1. Select a placeholder text
2. Press `Cmd+D` (Mac) repeatedly to select next occurrences
3. Type replacement text once, updates all selected

## Validation Check

After editing, verify no placeholders remain:
```bash
# Should return nothing if all placeholders are replaced
grep "PLACEHOLDER" posts/*.html

# Check specific post
grep "PLACEHOLDER" posts/2025-09-10-transpose-button-confession.html
```

## Remember:
- Be vulnerable and specific
- Include real numbers (costs, time, impact)
- Name actual systems/tools you used
- Describe your emotional state
- Share what actually helped you learn

Your authenticity is what will connect with readers!