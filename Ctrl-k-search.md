# Ctrl+K Search Feature for Hugo

## Overview

This document outlines how to implement a Ctrl/Cmd + K search feature
(command palette style) in a Hugo-based static website using client-side
search.

## Step 1: Configure Hugo to Output JSON

Add to config.toml:

\[outputs\] home = \["HTML", "JSON"\]

Create: layouts/\_default/index.json.json

Add:

{{- \$pages := where .Site.RegularPages "Type" "in"
site.Params.mainSections -}} \[ {{- range \$index, \$page := \$pages -}}
{{- if \$index }},{{ end }} { "title": {{ \$page.Title \| jsonify }},
"content": {{ \$page.Plain \| jsonify }}, "permalink": {{
\$page.Permalink \| jsonify }}, "summary": {{ \$page.Summary \| jsonify
}} } {{- end -}}\]

## Step 2: Add Search Modal

Create: layouts/partials/search-modal.html

::: {#search-modal hidden="" role="dialog"}
::: search-backdrop
:::

::: search-box
    <input id="search-input" type="text" placeholder="Search..." />
    <div id="search-results"></div>
:::
:::

Include in baseof.html: {{ partial "search-modal.html" . }}

## Step 3: Keyboard Shortcut

document.addEventListener('keydown', (e) =\> { const isMac =
navigator.platform.toUpperCase().includes('MAC'); if ((isMac ? e.metaKey
: e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault();
openSearch(); } });

function openSearch() { const modal =
document.getElementById('search-modal'); modal.hidden = false;
document.getElementById('search-input').focus(); }

function closeSearch() { document.getElementById('search-modal').hidden
= true; }

document.addEventListener('keydown', (e) =\> { if (e.key === 'Escape')
closeSearch(); });

## Step 4: Load Search Index

let fuse;

fetch('/index.json') .then(res =\> res.json()) .then(data =\> { fuse =
new Fuse(data, { keys: \['title', 'content', 'summary'\], threshold: 0.3
}); });

## Step 5: Handle Input

const input = document.getElementById('search-input'); const
resultsContainer = document.getElementById('search-results');

let debounceTimer;

input.addEventListener('input', (e) =\> { clearTimeout(debounceTimer);
debounceTimer = setTimeout(() =\> { const query = e.target.value; if
(!query \|\| !fuse) return;

    const results = fuse.search(query).slice(0, 10);
    renderResults(results);

}, 150); });

## Step 6: Render Results

function renderResults(results) { resultsContainer.innerHTML =
results.map(r =\>
`<a href="${r.item.permalink}" class="result">       <div class="title">${r.item.title}</div>       <div class="summary">${r.item.summary}</div>     </a>`).join('');
}

## Step 7: Keyboard Navigation

-   Arrow keys to move selection
-   Enter to open result
-   Escape to close modal

## Step 8: Accessibility

-   role="dialog"
-   Focus trap
-   aria-label for input
-   Keyboard navigation support

## Step 9: Performance

-   Limit indexed fields
-   Use .Plain content
-   Compress index.json
-   Lazy-load script if needed

## Result

A fast, client-side Ctrl/Cmd + K search experience for Hugo sites
without requiring a backend.
