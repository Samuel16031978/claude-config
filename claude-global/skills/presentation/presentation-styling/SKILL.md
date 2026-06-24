---
name: presentation-styling
description: Knowledge about CSS classes, component patterns, and syntax highlighting in the presentation
---

# Presentation Styling Skill

CSS classes and HTML patterns used in `presentation/index.html`.

## CSS Component Classes

### Layout

- `.two-col` ÔÇö 2-column grid layout with 24px gap
- `.info-grid` ÔÇö 2-column grid for info cards
- `.col-card` ÔÇö Card inside a column (add `.good` for green border, `.bad` for red border)
- `.info-card` ÔÇö Card in an info grid

### Content Blocks

- `.trigger-box` ÔÇö Gray box with dark left border (for key concepts, prerequisites)
- `.how-to-trigger` ÔÇö Green box with green border (for "Try This" actions)
- `.warning-box` ÔÇö Orange box with warning border (for important warnings)
- `.code-block` ÔÇö Dark code display block with monospace font

### Lists

- `.use-cases` ÔÇö Container for icon+text list items
- `.use-case-item` ÔÇö Individual item with icon and text
- `.feature-list` ÔÇö Simple bordered list

### Tags & Badges

- `.matcher-tag` ÔÇö Gray inline pill tag
- `.weight-badge` ÔÇö Green pill badge (auto-injected by JS for weighted slides)

## Code Block Syntax Highlighting

Inside `.code-block`, use these spans for syntax coloring:

```html
<div class="code-block">
<span class="comment"># This is a comment</span>
<span class="key">field_name</span>: <span class="string">value</span>
<span class="cmd">&gt;</span> command to run
</div>
```

- `.comment` ÔÇö Green (#6a9955) for comments
- `.key` ÔÇö Blue (#9cdcfe) for property names/keys
- `.string` ÔÇö Orange (#ce9178) for string values
- `.cmd` ÔÇö Yellow (#dcdcaa) for commands/prompts

## Slide Type Patterns

### Content Slide with Two Columns (Good vs Bad)
```html
<div class="slide" data-slide="N" data-weight="5">
    <h1>Title</h1>
    <div class="two-col">
        <div class="col-card bad">
            <h4>Before (Vibe Coding)</h4>
            <!-- bad example -->
        </div>
        <div class="col-card good">
            <h4>After (Agentic)</h4>
            <!-- good example -->
        </div>
    </div>
</div>
```

Do not hardcode `<span class="weight-badge">` in slide HTML. The presentation JavaScript injects and removes weight badges automatically.

### Content Slide with Code Example
```html
<div class="slide" data-slide="N">
    <h1>Title</h1>
    <div class="trigger-box">
        <h4>Key Concept</h4>
        <p>Description</p>
    </div>
    <div class="code-block"><span class="comment"># Example</span>
<span class="key">field</span>: <span class="string">value</span></div>
</div>
```

### Icon List Pattern
```html
<div class="use-cases">
    <div class="use-case-item">
        <span class="use-case-icon">EMOJI</span>
        <div class="use-case-text">
            <strong>Title</strong>
            <span>Description text</span>
        </div>
    </div>
</div>
```

## Journey Bar Specific

- `.journey-bar` ÔÇö Fixed bar below progress bar
- `.journey-bar.hidden` ÔÇö Hidden on title slide
- Journey bar color transitions from red (0%) to green (100%) via HSL interpolation
- Weight badges are auto-injected by JS into `h1` elements of weighted slides
