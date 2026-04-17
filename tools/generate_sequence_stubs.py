#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

USECASE_PATTERN = re.compile(
    r'usecase\s+"([^"]+)"(?:\s+as\s+([A-Za-z0-9_]+))?'
)


def parse_usecase_names(use_case_path: Path) -> list[tuple[str, str | None]]:
    text = use_case_path.read_text(encoding="utf-8")
    return USECASE_PATTERN.findall(text)


def sanitize_filename(usecase_name: str) -> str:
    return usecase_name.replace(" ", "_").replace("/", "_")


def render_stub(usecase_name: str) -> str:
    return f'''@startuml
skinparam style strictuml

title {usecase_name}

actor "User" as user
boundary "UI Boundary" as ui
control "Application Control" as app
entity "Domain Entity" as entity

user -> ui: Request {usecase_name}
ui -> app: Forward request
app -> entity: Execute business operation
entity --> app: Return operation result

opt Optional related flow
  ref over ui, app : Included/extended use case interaction
end

app --> ui: Build response
ui --> user: Present response
@enduml
'''


def expected_paths(root: Path) -> list[tuple[str, Path]]:
    use_case_path = root / "_refs" / "diagrams-new" / "use_case.puml"
    sequence_dir = root / "_refs" / "diagrams-new" / "sequence"
    usecases = parse_usecase_names(use_case_path)

    path_counts: dict[str, int] = {}
    targets: list[tuple[str, Path]] = []
    for display_name, alias in usecases:
        base_name = sanitize_filename(display_name)
        count = path_counts.get(base_name, 0)

        if count == 0:
            filename = f"{base_name}.puml"
        elif alias:
            filename = f"{base_name}__{sanitize_filename(alias)}.puml"
        else:
            filename = f"{base_name}__{count + 1}.puml"

        path_counts[base_name] = count + 1
        targets.append((display_name, sequence_dir / filename))

    return targets


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    targets = expected_paths(root)

    if args.check:
        missing_count = sum(1 for _, path in targets if not path.exists())
        if missing_count:
            print(f"missing:{missing_count}")
            return 1
        print(f"ok:{len(targets)}")
        return 0

    for usecase_name, path in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_stub(usecase_name), encoding="utf-8")

    print(f"ok:{len(targets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
