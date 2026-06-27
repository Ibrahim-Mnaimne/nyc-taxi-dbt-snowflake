import json
from pathlib import Path

target = Path("target")
out = Path("docs")
out.mkdir(exist_ok=True)

with open(target / "index.html", "r", encoding="utf-8") as f:
    content = f.read()

with open(target / "manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(target / "catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

search_str = 'n=[o("manifest","manifest.json"+t),o("catalog","catalog.json"+t)]'
replace_str = (
    "n=[{label: 'manifest', data: "
    + json.dumps(manifest)
    + "},{label: 'catalog', data: "
    + json.dumps(catalog)
    + "}]"
)

new_content = content.replace(search_str, replace_str)

if new_content == content:
    print("WARNING: injection string not found. dbt version may differ.")
else:
    print("Injection successful.")

with open(out / "index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Self-contained docs written to docs/index.html")