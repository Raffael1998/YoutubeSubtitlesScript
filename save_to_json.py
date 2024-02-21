import json
import os
from get_transcript import fetch_transcripts, sanitize_filename, format_filename


def save_transcripts_to_json(transcripts, filename):
    """
    Function to save the transcript as json file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([{title: transcript} for title, transcript in transcripts], file, ensure_ascii=False, indent=4)
    print(f"Transcripts saved to {filename}")

def main():
    """Saving the transcripts"""
    saving_folder = "json_transcripts"
    # Ensure saving folders exist
    os.makedirs(saving_folder, exist_ok=True)
    for index, url in enumerate(playlist_urls):
        transcripts = fetch_transcripts(url)
        if transcripts:
            first_video_title = transcripts[0][0]  # Get the title of the first video
            base_filename = format_filename(first_video_title)
            json_filename = f"{index:02d}_transcript_{sanitize_filename(base_filename)}.json"
            
            save_transcripts_to_json(transcripts, os.path.join(saving_folder, json_filename))
        else:
            print(f"No transcripts fetched for playlist: {url}")


if __name__=="__main__":

    playlist_urls = [
    'https://www.youtube.com/watch?v=Ab-1wMFj3DA&list=PLMcG1Hs2JbcsGGJ84BtG2fClp7SF7K9jU',
    'https://www.youtube.com/watch?v=xoJ6vmK9m3Q&list=PLMcG1Hs2JbcsyDndXARl6TVtBRCal0VHD',
    'https://www.youtube.com/watch?v=CFRyQZbmJ-M&list=PLMcG1Hs2Jbcu_RpgG0VSuWC4ZcIpUxD8F',
    'https://www.youtube.com/watch?v=Q-nS88HWA40&list=PLMcG1Hs2JbcucfbPvfAa6jA_y1RpRxhp5',
    'https://www.youtube.com/watch?v=Gm1tVIQyTC0&list=PLMcG1Hs2JbcsUeHH2MMX4YvGPQ8Khe4Uy',
    'https://www.youtube.com/watch?v=VMXCMulRtyM&list=PLMcG1Hs2JbcsgmDMZhvsUzm8f7o5qaN3d',
    'https://www.youtube.com/watch?v=yJgPct6gAtg&list=PLMcG1Hs2JbcsfCFBHTlRjrK_CHLHlGLRE',
    'https://www.youtube.com/watch?v=OE1YKqwD5i8&list=PLMcG1Hs2Jbcshbr_qSsVrwEbrsRs03_7-',
    'https://www.youtube.com/watch?v=1LYG2xono0g&list=PLMcG1Hs2JbcvOXwi4y9kDRRYd8xnNKDbV',
    'https://www.youtube.com/watch?v=uIc4eSxm1oI&list=PLMcG1Hs2JbcsACzF2loiQuH1mcagq8br3'
]

    main()