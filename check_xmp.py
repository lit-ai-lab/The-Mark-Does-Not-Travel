import os
import csv
import argparse
from pathlib import Path

def check_xmp_existence(file_path, chunk_size=65536):
    """
    Checks for the existence of XMP (Extensible Metadata Platform) data within an image file.
    
    [Detection Principle]
    XMP is embedded into image file binaries in XML format according to the ISO 16684-1 standard.
    This script reads the binary data of the file and searches for the following key identifiers:
    1. 'http://ns.adobe.com/xap/1.0/': The standard namespace URI for XMP metadata.
    2. '<?xpacket': The header indicating the start of an XMP packet.
    
    This method provides a fast and accurate way to determine if XMP is included in most 
    image formats (JPEG, PNG, WebP, etc.) without relying on external libraries.
    """
    # Define binary patterns to search for
    patterns = [
        b'http://ns.adobe.com/xap/1.0/',
        b'<?xpacket'
    ]
    
    try:
        with open(file_path, 'rb') as f:
            # Read the file in chunks for memory efficiency
            overlap = max(len(p) for p in patterns) - 1
            buffer = b""
            
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                
                # Combine the end of the previous chunk with the current chunk 
                # to prevent patterns from being split across chunk boundaries
                search_target = buffer + chunk
                if any(p in search_target for p in patterns):
                    return "O"
                
                # Keep the end of the current chunk for the next search iteration
                buffer = chunk[-overlap:] if len(chunk) > overlap else chunk
                
            return "X"
    except Exception as e:
        return f"Error: {e}"

def main():
    # Configure command-line arguments
    parser = argparse.ArgumentParser(description="Checks image files for XMP metadata and saves the results to a CSV file.")
    parser.add_argument("input_dir", help="The target directory path to inspect")
    parser.add_argument("-o", "--output", default="xmp_report.csv", help="The output CSV filename (default: xmp_report.csv)")
    parser.add_argument("-e", "--extensions", nargs="+", 
                        default=[".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"],
                        help="List of image extensions to check (e.g., .jpg .png)")
    
    args = parser.parse_args()

    input_path = Path(args.input_dir)
    if not input_path.exists():
        print(f"Error: The path '{args.input_dir}' could not be found.")
        return

    image_extensions = {ext.lower() for ext in args.extensions}
    data_list = []

    print(f"Starting inspection: {input_path.absolute()}")
    print(f"Target extensions: {', '.join(image_extensions)}")
    
    # Recursively search all subdirectories
    files_to_check = [f for f in input_path.rglob('*') if f.suffix.lower() in image_extensions]
    total_files = len(files_to_check)

    if total_files == 0:
        print("No image files to inspect.")
        return

    for i, file in enumerate(files_to_check, 1):
        has_xmp = check_xmp_existence(file)
        
        # Calculate relative path (for better readability in the report)
        try:
            display_path = file.relative_to(input_path)
        except ValueError:
            display_path = file
            
        data_list.append({
            'File Name': file.name,
            'Relative Path': str(display_path),
            'XMP Exists': has_xmp,
            'Absolute Path': str(file.absolute())
        })
        
        if i % 10 == 0 or i == total_files:
            print(f"In progress: {i}/{total_files} completed...", end='\r')

    # Save to CSV file
    print(f"\nSaving results to: {args.output}")
    try:
        if data_list:
            keys = data_list[0].keys()
            with open(args.output, 'w', newline='', encoding='utf-8-sig') as f:
                dict_writer = csv.DictWriter(f, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(data_list)
            print(f"Success: Inspection complete. (Total {total_files} files checked)")
    except Exception as e:
        print(f"CSV save error: {e}")

if __name__ == "__main__":
    main()
