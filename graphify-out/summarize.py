import json
from pathlib import Path

detect = json.loads(Path('graphify-out/.graphify_detect.json').read_text())
files = detect.get('files', {})
code = len(files.get('code', []))
docs = len(files.get('document', []))
papers = len(files.get('paper', []))
images = len(files.get('image', []))
videos = len(files.get('video', []))

print(f"Corpus: {detect.get('total_files', 0)} files · ~{detect.get('total_words', 0)} words")
if code: print(f"  code:     {code} files")
if docs: print(f"  docs:     {docs} files")
if papers: print(f"  papers:   {papers} files")
if images: print(f"  images:   {images} files")
if videos: print(f"  video:    {videos} files")

skipped = detect.get('skipped_sensitive', [])
if skipped: print(f"Skipped {len(skipped)} sensitive files.")
print(f"TOTAL_FILES: {detect.get('total_files', 0)}")
print(f"TOTAL_WORDS: {detect.get('total_words', 0)}")
