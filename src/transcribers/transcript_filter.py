#This Filter Converts  raw transcript Data to JSON FORMAT

import re

"""#Our regex pattern: (\d{1,2}:\d{2})\s+(.+?)(?=\d{1,2}:\d{2}|$)

	
1) (\d{1,2}:\d{2}): Captures the time stamp.
\d:
Returns a match where the string contains digits (numbers from 0-9)
{}:
Exactly the specified number of occurrences

"""


def convert_script_to_json(raw_transcript):
    # Split transcript into lines:
    lines = raw_transcript.splitlines()

    transcript_json = []
    start_time = None
    end_time = None
    content = ""

    for line in lines:
        # Extracting time stamps:
        # r ensures string format, \d{1, 2} => 1 or two digits expected || \d{2} => two digits expected
        # Correcting the regex by closing the parentheses for time match
        time_match = re.match(r'(\d{1,2}:\d{2})', line.strip())

        # Handling valid time matches, and appending when a time is found:
        if time_match:
            # If we already have a start time, save the previous segment
            if start_time is not None:
                transcript_json.append({
                    "content": content.strip(),
                    "start_time": start_time,
                    "end_time": time_match.group(1  )  # The end time is the last known start time
                })

            # Now, update the start time
            start_time = time_match.group(1)

            # Reset content for the new segment
            content = ""

        else:
            # Accumulate content in the current segment
            content += " " + line.strip()

    # After the loop, save the last segment (since it won't be saved inside the loop)
    if start_time and content:
        transcript_json.append({
            "content": content.strip(),
            "start_time": start_time,
            "end_time": end_time  # End time for the last segment
        })

    return transcript_json

if __name__ == "__main__":
    try:
        with open("raw_transcript.txt", "r", encoding="utf-8") as file:
            sample_raw_transcript = file.read()
    except FileNotFoundError:
        print("raw_transcript.txt not found.")

    json_output = convert_script_to_json(sample_raw_transcript)

    import json
    print(json.dumps(json_output, indent=4))



