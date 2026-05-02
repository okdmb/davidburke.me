import sys, json
from graphify.cache import save_semantic_cache
from pathlib import Path

all_nodes, all_edges, all_hyperedges = [], [], []
for i in range(1, 5):
    p = Path(f'graphify-out/.graphify_chunk_0{i}.json')
    if p.exists():
        try:
            d = json.loads(p.read_text())
            all_nodes.extend(d.get('nodes', []))
            all_edges.extend(d.get('edges', []))
            all_hyperedges.extend(d.get('hyperedges', []))
        except Exception as e:
            print(f"Error parsing chunk {i}: {e}")
    else:
        print(f"Missing chunk {i}")

Path('graphify-out/.graphify_semantic_new.json').write_text(json.dumps({'nodes': all_nodes, 'edges': all_edges, 'hyperedges': all_hyperedges}))

new = json.loads(Path('graphify-out/.graphify_semantic_new.json').read_text())
saved = save_semantic_cache(new.get('nodes', []), new.get('edges', []), new.get('hyperedges', []))
print(f'Cached {saved} files')

cached = json.loads(Path('graphify-out/.graphify_cached.json').read_text()) if Path('graphify-out/.graphify_cached.json').exists() else {'nodes':[],'edges':[],'hyperedges':[]}
combined_nodes = cached['nodes'] + new.get('nodes', [])
combined_edges = cached['edges'] + new.get('edges', [])
combined_hyperedges = cached.get('hyperedges', []) + new.get('hyperedges', [])
seen = set()
deduped = []
for n in combined_nodes:
    if n['id'] not in seen:
        seen.add(n['id'])
        deduped.append(n)

merged = {
    'nodes': deduped,
    'edges': combined_edges,
    'hyperedges': combined_hyperedges,
}
Path('graphify-out/.graphify_semantic.json').write_text(json.dumps(merged, indent=2))
print(f'Semantic: {len(deduped)} nodes, {len(combined_edges)} edges')

ast = json.loads(Path('graphify-out/.graphify_ast.json').read_text())
sem = json.loads(Path('graphify-out/.graphify_semantic.json').read_text())
seen = {n['id'] for n in ast['nodes']}
merged_nodes = list(ast['nodes'])
for n in sem['nodes']:
    if n['id'] not in seen:
        merged_nodes.append(n)
        seen.add(n['id'])
merged_edges = ast['edges'] + sem['edges']
merged_hyperedges = sem.get('hyperedges', [])
merged_final = {
    'nodes': merged_nodes,
    'edges': merged_edges,
    'hyperedges': merged_hyperedges,
}
Path('graphify-out/.graphify_extract.json').write_text(json.dumps(merged_final, indent=2))
print(f'Merged final: {len(merged_nodes)} nodes, {len(merged_edges)} edges')
