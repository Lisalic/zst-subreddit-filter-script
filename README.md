# Subreddit Filter Script

A Python script to filter Reddit data dumps by subreddit. This tool processes compressed Reddit data files (in Zstandard format) and extracts posts/comments from a specific subreddit.

# Subreddit Filter Script

A Python script to filter Reddit data dumps by subreddit. This tool processes compressed Reddit data files (in Zstandard format) and extracts posts/comments from a specific subreddit.

## Installation

### 1. Install Python

- [Windows Installation Guide](https://www.youtube.com/watch?v=e70ykVBazAg)
- [MacOS Installation Guide](https://www.youtube.com/watch?v=VYmYKeY65nk)

### 2. Install Required Library

Open your terminal/command prompt and run:

```bash
pip install zstandard
```

**Windows:** Open Command Prompt or PowerShell  
**MacOS:** Open Terminal

## Usage

### 3. Download Reddit Data

Download a Reddit data dump in Zstandard format.

### 4. Run the Script

1. Open this repository page in your web browser.
2. Click the green **Code** button and choose **Download ZIP**.
3. Unzip the downloaded file and copy `subreddit-filter-script.py` to a folder you can find easily.

After you have the file, run the script as shown below.

```bash
python subreddit-filter-script.py
```

When prompted:

- Enter the path to your input .zst file
- Enter the subreddit name to filter (without the 'r/' prefix)

The script will create a new file `filtered_{subreddit}.zst` containing only posts/comments from that subreddit.

## Example

```
Enter the path to your source .zst file: /Users/abc/Documents/reddit_data.zst
Enter the subreddit to filter by: bullying
```

This will create `filtered_bullying.zst` containing all posts/comments from r/python.
