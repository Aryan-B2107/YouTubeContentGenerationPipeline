import json


def convert_to_seconds(t):
    parts_time = t.split(":")
    print(parts_time)
    # hour = int(parts_time[0]) * 3600 if len(parts_time)==3 else 0
    minute = int(parts_time[0]) * 60 if len(parts_time)>=2 else 0
    seconds = int(parts_time[1])
    return minute + seconds

def joke_joiner(start_time, end_time):
    with open('Converted_json_transcript.json', 'r') as f:
        jokes = json.load(f)
        filtered_output = []
        for j in jokes:
            # print(j['start_time'], j['end_time'])
            if convert_to_seconds(j['start_time']) >= start_time and convert_to_seconds(j['end_time']) <= end_time:
                filtered_output.append(j['content'])
    return filtered_output


if __name__ == "__main__":
    jokes_list = []
    with open(r'C:\Users\omkul\ProjectsCoding\YoutubeContentGenerationPipeline\YouTubeContentGenerationPipeline\src\transcript_analyzers\jokes_segments.json', 'r') as file:
        data = json.load(file)
        for chunk in data["chunks"]:
            start = convert_to_seconds(chunk["start_time"])
            end = convert_to_seconds(chunk["end_time"])
            print(f"Start: {start}, End: {end}")
            # You can now call your function here
            joke_sentences = joke_joiner(start, end)
            full_paragraph = " ".join(joke_sentences)
            jokes_list.append(full_paragraph)

            with open('joined_jokes.json', 'w') as outfile:
                json.dump(jokes_list, outfile,)