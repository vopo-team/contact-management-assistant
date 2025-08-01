import re
import subprocess
from collections import OrderedDict, defaultdict
from datetime import datetime

type_map = {
    "feat": "Features",
    "feature": "Features",
    "fix": "Bug Fixes",
    "hotfix": "Hotfixes",
    "docs": "Documentation",
    "doc": "Documentation",
    "chore": "Chores",
    "dev": "Development",
}

tags_output = subprocess.check_output(
    ["git", "tag", "--sort=-creatordate"]
).decode("utf-8")
tags = tags_output.strip().splitlines()

tags = ["UNRELEASED"] + tags

versions = OrderedDict()

for i in range(len(tags)):
    current_tag = tags[i]
    next_tag = tags[i + 1] if i + 1 < len(tags) else ""

    if current_tag == "UNRELEASED":
        rev_range = f"{tags[1]}..HEAD" if len(tags) > 1 else "HEAD"
    elif next_tag:
        rev_range = f"{next_tag}..{current_tag}"
    else:
        rev_range = current_tag

    log_format = "%ad|%an|%s"
    try:
        log_output = subprocess.check_output(
            [
                "git",
                "log",
                "--pretty=format:" + log_format,
                "--date=iso",
                rev_range,
            ]
        ).decode("utf-8")
    except subprocess.CalledProcessError:
        continue

    sections = defaultdict(list)

    for line in log_output.splitlines():
        try:
            date_str, author, message = line.split("|", 2)
            dt = datetime.fromisoformat(date_str.strip())
            formatted_date = dt.strftime("%d.%m.%Y %H:%M:%S")
        except Exception:
            continue

        match = re.match(r"^(\w+)(\([^)]+\))?:\s+(.+)", message)
        if not match:
            continue

        raw_type, _, msg = match.groups()
        normalized_type = raw_type.lower()
        section = type_map.get(normalized_type)
        if section:
            entry = f"- {msg} - ({formatted_date}, {author.strip()})"
            sections[section].append(entry)

    versions[current_tag] = sections

with open("docs/CHANGELOG.md", "w") as f:
    for version, sections in versions.items():
        f.write(f"## {version}\n\n")
        for section_name in sorted(sections):
            f.write(f"### {section_name}\n\n")
            for entry in sections[section_name]:
                f.write(entry + "\n")
            f.write("\n")
