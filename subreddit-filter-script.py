import zstandard as zstd
import json
import io
import os

def filter_subreddit(input_filepath, output_filepath, target_subreddit):
    dctx = zstd.ZstdDecompressor(max_window_size=2147483648)
    cctx = zstd.ZstdCompressor()

    target_subreddit = target_subreddit.lower()
    matched_count = 0
    processed_count = 0

    print(f"Opening {input_filepath}...")
    
    with open(input_filepath, 'rb') as in_file, open(output_filepath, 'wb') as out_file:
        
        with dctx.stream_reader(in_file) as reader, cctx.stream_writer(out_file) as writer:
            
            text_stream = io.TextIOWrapper(reader, encoding='utf-8')
            
            print(f"Scanning for r/{target_subreddit} (This may take a while...)")
            
            for line in text_stream:
                processed_count += 1
                
                if processed_count % 100000 == 0:
                    print(f"Processed {processed_count:,} lines. Found {matched_count:,} matches.")

                if not line.strip():
                    continue

                try:
                    data = json.loads(line)
                    
                    subreddit = data.get("subreddit", "")
                    
                    if subreddit.lower() == target_subreddit:
                        writer.write(line.encode('utf-8'))
                        matched_count += 1
                        
                except json.JSONDecodeError:
                    continue
                except Exception as e:
                    print(f"Unexpected error on line {processed_count}: {e}")
                    continue

    print("-" * 30)
    print("Filtering Complete!")
    print(f"Total lines processed: {processed_count:,}")
    print(f"Total matches saved to {output_filepath}: {matched_count:,}")

if __name__ == "__main__":
    input_zst = input("Enter the path to your source .zst file: ").strip()
    
    if not os.path.exists(input_zst):
        print(f"Error: Could not find file at '{input_zst}'")
        exit(1)

    target_sub = input("Enter the subreddit to filter by: ").strip()
    
    output_zst = f"filtered_{target_sub}.zst"
    
    filter_subreddit(input_zst, output_zst, target_sub)