import os
from pathlib import Path

def fix_encoding():
    base_dir = Path(".")
    
    replacements = {
        "â€\"": "—",
        "â€œ": "\"",
        "â€": "\"",
        "â€™": "\"",
        "â€˜": "\"",
        "Â©": "©",
        "â€¦": "…",
        "Ã©": "é",
        "Ã¨": "è",
        "Ã ": "à",
    }
    
    count = 0
    for html_file in base_dir.glob("*.html"):
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        original = content
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        if content != original:
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"✓ 修复 {html_file.name}")
    
    print(f"总共修复了 {count} 个文件")

if __name__ == "__main__":
    fix_encoding()
