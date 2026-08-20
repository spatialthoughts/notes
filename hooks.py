import re
from pathlib import Path


def on_config(config):
    docs_dir = Path(config['docs_dir'])

    def count_items(filepath):
        path = docs_dir / filepath
        if path.exists():
            content = path.read_text()
            return len(re.findall(r'^- \[', content, re.MULTILINE))
        return 0

    def update_nav(nav_items):
        result = []
        for item in nav_items:
            if isinstance(item, str):
                result.append(item)
            elif isinstance(item, dict):
                new_dict = {}
                for title, value in item.items():
                    if isinstance(value, str) and value.endswith('.md') and value not in ('index.md', 'log.md'):
                        n = count_items(value)
                        new_dict[f"{title} ({n})"] = value
                    elif isinstance(value, list):
                        new_dict[title] = update_nav(value)
                    else:
                        new_dict[title] = value
                result.append(new_dict)
        return result

    config['nav'] = update_nav(config['nav'])
    return config
