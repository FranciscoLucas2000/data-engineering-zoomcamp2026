from pathlib import Path

# Returns the current working directory
current_dir = Path.cwd()

# Returns only the file name
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

# filepath is a Path object
# if the file is the same as the script we skip it as we don't want to show the content of it
for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")