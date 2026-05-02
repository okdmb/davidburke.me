import json
from pathlib import Path

analysis = json.loads(Path('graphify-out/.graphify_analysis.json').read_text())
extract = json.loads(Path('graphify-out/.graphify_extract.json').read_text())

node_names = {n['id']: n.get('label', n['id']) for n in extract['nodes']}

for cid, nodes in analysis['communities'].items():
    labels = [node_names.get(n, n) for n in nodes[:5]] # print top 5 nodes
    print(f"Community {cid}: {labels}")