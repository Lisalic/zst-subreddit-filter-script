# Subreddit Filter Script

A Python script to filter Reddit data dumps by subreddit. This tool processes compressed Reddit data files (in Zstandard format) and extracts posts/comments from a specific subreddit.

## Requirements

- Python 3.6+
- zstandard library (`pip install zstandard`)

## Usage

1. Download a Reddit data dump in Zstandard compressed format
2. Run the script:
   ```bash
   python subreddit-filter-script.py
   ```
3. Enter the path to your input .zst file when prompted
4. Enter the subreddit name to filter (without the 'r/' prefix)
5. The script will create a new file `filtered_{subreddit}.zst` containing only posts/comments from that subreddit

## Example

```
Enter the path to your source .zst file: /Users/abc/Documents/subreddit-filterreddit_data.zst
Enter the subreddit to filter by: bullying
```

This will create `filtered_bullying.zst` containing all posts/comments from r/python.
