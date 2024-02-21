import os
import re

def format_text(text):
    """Remove unnecessary line breaks, adjust capitalization, and ensure single spaces."""
    # Join lines into a single block of text
    text = ' '.join(text.split('\n'))
    # Adjust capitalization after full stops
    text = re.sub(r'\. ([a-z])', lambda x: '. ' + x.group(1).upper(), text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    return text

def compile_transcripts_to_txt(transcripts_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as txt_file:
        for filename in sorted(os.listdir(transcripts_folder), key=lambda x: int(x.split('_')[0])):
            if filename.endswith('.txt'):
                # Extract playlist title from filename, assuming format "transcript_{Playlist Title}.txt"
                playlist_title = filename.split('_', 2)[-1].replace('transcript_', '').replace('.txt', '')
                txt_file.write(f"*{playlist_title}*\n\n")  # Write playlist title
                
                with open(os.path.join(transcripts_folder, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    # Split content by asterisks lines, assuming each title is surrounded by asterisks
                    parts = re.split(r'\n\*(.*?)\*\n', content)
                    for i in range(1, len(parts), 2):
                        video_title = parts[i]
                        video_transcript = parts[i+1]
                        formatted_text = format_text(video_transcript)
                        txt_file.write(f"**{video_title}**\n\n")  # Write video title
                        txt_file.write(f"{formatted_text}\n\n")  # Write formatted transcript
    
    print(f"Compiled text document saved as: {output_file}")

if __name__ == "__main__":
    transcripts_folder = "txt_transcripts"  # Folder containing the .txt files
    output_file = "Playlist_Transcripts.txt"  # Output text file name
    compile_transcripts_to_txt(transcripts_folder, output_file)
