import json
import shutil
from pathlib import Path

target = Path("target")
out = Path("docs-site")
out.mkdir(exist_ok=True)

# Read the generated files
index = (target / "index.html").read_text(encoding="utf-8")

# dbt 1.11 already embeds manifest+catalog in index.html for the docs site.
# Copy index.html directly as the standalone site.
shutil.copy(target / "index.html", out / "index.html")

print("Docs site written to docs-site/index.html")