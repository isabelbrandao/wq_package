#!/usr/bin/env python3
"""
Script to clean Jupyter notebooks before committing to git.
This removes cell outputs to keep the repository clean and reduces file size.
"""

import json
import sys
from pathlib import Path


def clean_notebook(notebook_path):
    """
    Remove all outputs from a Jupyter notebook.
    
    Args:
        notebook_path: Path to the notebook file
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Track if any changes were made
    changes_made = False
    
    # Clear outputs from all cells
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            if cell.get('outputs'):
                cell['outputs'] = []
                changes_made = True
            if cell.get('execution_count'):
                cell['execution_count'] = None
                changes_made = True
    
    # Write back the cleaned notebook
    if changes_made:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
            f.write('\n')  # Add newline at end of file
        print(f"✓ Cleaned {notebook_path}")
        return True
    else:
        print(f"○ No changes needed for {notebook_path}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python export_clean_notebook.py <notebook1.ipynb> [notebook2.ipynb ...]")
        print("   or: python export_clean_notebook.py notebooks/")
        sys.exit(1)
    
    paths = sys.argv[1:]
    cleaned_count = 0
    
    for path_str in paths:
        path = Path(path_str)
        
        if path.is_dir():
            # Process all notebooks in directory
            notebooks = list(path.glob('**/*.ipynb'))
            # Exclude .ipynb_checkpoints
            notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
            
            if not notebooks:
                print(f"No notebooks found in {path}")
                continue
                
            print(f"Found {len(notebooks)} notebook(s) in {path}")
            for notebook in notebooks:
                if clean_notebook(notebook):
                    cleaned_count += 1
        
        elif path.is_file() and path.suffix == '.ipynb':
            if clean_notebook(path):
                cleaned_count += 1
        else:
            print(f"⚠ Skipping {path} (not a notebook or directory)")
    
    print(f"\n✓ Cleaned {cleaned_count} notebook(s)")


if __name__ == '__main__':
    main()
