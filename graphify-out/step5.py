import sys, json
from graphify.build import build_from_json
from graphify.cluster import score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from pathlib import Path

extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text())
detection  = json.loads(Path('graphify-out/.graphify_detect.json').read_text())
analysis   = json.loads(Path('graphify-out/.graphify_analysis.json').read_text())

G = build_from_json(extraction)
communities = {int(k): v for k, v in analysis['communities'].items()}
cohesion = {int(k): v for k, v in analysis['cohesion'].items()}
tokens = {'input': extraction.get('input_tokens', 0), 'output': extraction.get('output_tokens', 0)}

labels = {
  0: "Hugo Theme Features",
  1: "Universal Design Concepts",
  2: "Hugo Markdown Support",
  3: "Vintage Typewriter Mechanism",
  4: "Mechanical Typewriter Keyboard",
  5: "Notebook Writing",
  6: "Vintage Tech Close-up",
  7: "Abstract 3D Shapes",
  8: "Closed Captions Player",
  9: "Voice Assistant UI",
  10: "Dark Mode Interface",
  11: "Search Autocomplete",
  12: "Audiobook Player",
  13: "Closed Captioning Icon",
  14: "AI Autocomplete UI",
  15: "TypeScript Logo",
  16: "Laptop Typing Theme"
}

questions = suggest_questions(G, communities, labels)

report = generate(G, communities, cohesion, labels, analysis['gods'], analysis['surprises'], detection, tokens, 'content/', suggested_questions=questions)
Path('graphify-out/GRAPH_REPORT.md').write_text(report)
Path('graphify-out/.graphify_labels.json').write_text(json.dumps({str(k): v for k, v in labels.items()}))
print('Report updated with community labels')