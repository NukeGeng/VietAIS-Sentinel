"""Small deterministic repository gates; not a security scanner."""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_SUFFIXES = {
    ".pt",
    ".pth",
    ".onnx",
    ".engine",
    ".safetensors",
    ".mp4",
    ".mov",
    ".webm",
    ".pem",
    ".key",
}


def main() -> int:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    paths = sorted(set(result.stdout.decode().split("\0")) - {""})
    errors = []
    for name in paths:
        path = ROOT / name
        if not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"Forbidden artifact: {name}")
        if path.name == ".env" or (
            path.name.startswith(".env.") and not path.name.endswith(".example")
        ):
            errors.append(f"Real environment file: {name}")
        if path.stat().st_size > 1_000_000:
            errors.append(f"Large file requires artifact storage: {name}")
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        if name.startswith("docs/") and not name.startswith("docs/templates/"):
            for marker in ("Owner:", "Status:", "Last verified:"):
                if marker not in text:
                    errors.append(f"{name}: missing {marker}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            destination = target.split("#", 1)[0]
            if destination and not (path.parent / destination).exists():
                errors.append(f"{name}: broken local link {target}")
    for error in errors:
        print(error)
    if errors:
        return 1
    print(f"Repository gates passed ({len(paths)} files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
