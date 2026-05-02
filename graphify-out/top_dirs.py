import json
from pathlib import Path
from collections import Counter

detect = json.loads(Path('graphify-out/.graphify_detect.json').read_text())
files = detect.get('files', {})

root = Path('.').resolve()
counts = Counter()
for ftype, flist in files.items():
    for f in flist:
        p = Path(f)
        if p.is_absolute():
            try:
                p = p.relative_to(root)
            except ValueError:
                continue
        if len(p.parts) > 1:
            # We want to show top-level subdirectories
            counts[str(p.parts[0])] += 1

print("Top 5 subdirectories by file count:")
for k, v in counts.most_common(5):
    print(f"  {k}/: {v} files")
