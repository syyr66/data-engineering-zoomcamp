from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in current dir ({current_dir}):")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue
    
    print(f"  - {filepath.name}")

    if filepath.is_file() and filepath.stat().st_size > 0:
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content:\n    {content}")