import ast
from pathlib import Path


def test_core_does_not_import_transport_models_or_platform():
    core = Path(__file__).resolve().parents[1] / "src/vietais_sentinel/core"
    forbidden = {"fastapi", "starlette", "ultralytics", "torch", "sqlalchemy", "vietais_platform"}
    for file in core.rglob("*.py"):
        tree = ast.parse(file.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                imports = [node.module or ""]
            else:
                continue
            for module in imports:
                assert module.split(".")[0] not in forbidden, f"{file}: {module}"


def test_package_does_not_depend_on_legacy_checkout():
    root = Path(__file__).resolve().parents[1] / "src"
    for file in root.rglob("*.py"):
        assert "academic-integrity-system" not in file.read_text()
        assert "Eureka-AIS-Framework" not in file.read_text()
