"""
Script to auto-update navigation sections in main documentation files with links to all .md modules in docs/implementation/ and its subfolders.
Links are grouped by subfolder (category).
"""
import os

NAV_SECTION = '\n---\n\n## Related Modules\n'
MAIN_DOCS = [
    'universal_communication.md',
    'agriculture.md',
    'conservation.md',
    'bioacoustics.md',
]
EXCLUDE = set(MAIN_DOCS + [
    'system_enhancement_strategies.md',
    'robotic_systems_integration.md',
    'animal_environmental_protection.md',
])

MODULES_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../docs/implementation'))

def collect_md_files():
    grouped = {}
    for root, dirs, files in os.walk(MODULES_ROOT):
        rel_dir = os.path.relpath(root, MODULES_ROOT)
        if rel_dir == '.':
            category = 'General'
        else:
            category = rel_dir.replace('\\', '/').title()
        for file in files:
            if file.endswith('.md') and file not in EXCLUDE:
                if file in MAIN_DOCS and rel_dir == '.':
                    continue
                grouped.setdefault(category, []).append(os.path.join(rel_dir, file) if rel_dir != '.' else file)
    return grouped

def make_nav_links(grouped):
    nav = NAV_SECTION
    for category, files in sorted(grouped.items()):
        nav += f'\n### {category}\n'
        for f in sorted(files):
            name = os.path.splitext(os.path.basename(f))[0].replace('_', ' ').title()
            nav += f'- [{name}]({f.replace(os.sep, "/")})\n'
    return nav

def update_nav_in_file(filepath, nav_links):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if NAV_SECTION in content:
        pre, _ = content.split(NAV_SECTION, 1)
        new_content = pre + nav_links
    else:
        new_content = content.strip() + nav_links
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    grouped = collect_md_files()
    nav_links = make_nav_links(grouped)
    for doc in MAIN_DOCS:
        path = os.path.join(MODULES_ROOT, doc)
        if os.path.exists(path):
            update_nav_in_file(path, nav_links)
    print("Navigation updated in main docs.")
