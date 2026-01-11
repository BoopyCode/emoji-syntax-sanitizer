#!/usr/bin/env python3
# Emoji Syntax Sanitizer - Because your code shouldn't be more expressive than your love life

import sys
import os
import re
from pathlib import Path

# Emoji regex - catches those sneaky little Unicode troublemakers
# Yes, this is simplified. No, it won't catch every emoji. Yes, that's your problem.
EMOJI_PATTERN = re.compile(
    r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]'
)

def sanitize_file(filepath):
    """Removes emojis from a file. Returns True if any were found (so you can feel special)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all emojis (for dramatic effect)
        emojis_found = EMOJI_PATTERN.findall(content)
        
        if not emojis_found:
            return False  # Your code is boring and safe
        
        # Remove the little devils
        clean_content = EMOJI_PATTERN.sub('', content)
        
        # Write back (make backup? LOL no, live dangerously)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        
        print(f"🚨 SANITIZED: {filepath} - Removed {len(emojis_found)} emoji(s): {''.join(set(emojis_found))}")
        return True
        
    except Exception as e:
        print(f"💥 Failed to process {filepath}: {e}")
        return False

def main():
    """Main function - because every script needs one, apparently."""
    if len(sys.argv) < 2:
        print("Usage: python emoji_sanitizer.py <file_or_directory>")
        print("Example: python emoji_sanitizer.py ./src  # Because your src folder is probably infected")
        sys.exit(1)
    
    target = sys.argv[1]
    path = Path(target)
    
    files_processed = 0
    emojis_removed = 0
    
    if path.is_file():
        # Single file - the simple life
        if sanitize_file(str(path)):
            emojis_removed += 1
        files_processed = 1
    elif path.is_dir():
        # Directory - because you're ambitious (or messy)
        for file_path in path.rglob('*.py'):  # Only Python files, because we're not animals
            if sanitize_file(str(file_path)):
                emojis_removed += 1
            files_processed += 1
    else:
        print(f"❓ '{target}' is neither a file nor directory. Are you trying to be clever?")
        sys.exit(1)
    
    # Dramatic conclusion
    print(f"\n📊 Summary: Processed {files_processed} file(s), sanitized {emojis_removed} file(s) with emojis")
    print("✅ Your code is now 100% less expressive but 100% more functional!")

if __name__ == "__main__":
    main()
