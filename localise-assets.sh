#!/usr/bin/env bash
# Pull all remote images (current WordPress site + Unsplash) into
# assets/img/remote/, then rebuild so pages reference the local copies.
# Run this ONCE before DNS cutover — after the old WordPress site goes away,
# its image URLs die, and this makes the new site fully self-contained.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p assets/img/remote

python3 - <<'PY'
import build, subprocess, pathlib
for key, (url, local) in build.IMAGES.items():
    out = pathlib.Path("assets/img/remote") / local
    if out.exists():
        print(f"skip  {local}")
        continue
    print(f"fetch {local}")
    subprocess.run(["curl", "-fsSL", "-o", str(out), url], check=True)
PY

echo "Rebuilding with local assets…"
python3 build.py
echo "Done. Optional: compress with  'npx @squoosh/cli' or  'magick mogrify -quality 82'  over assets/img/remote/"
