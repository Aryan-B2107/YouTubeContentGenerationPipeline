This package takes in raw transcript data, redirects it to:

1)LLM1 (Chunker LLM):
which chunks the transcripts as per jokes start and end time stamps

2)LLM2 (Scorer LLM):
this call to the gemini API service takes the chunked transcripts and scores all
the transcripts and sorts it as per score

Scoring metrics:
1)humour score
2)relatibility score(to audience)
3)shock value
4)tone summary
5)virality score-(fine tune on other metrics)

3. LLM3 (multiple Sound effects assigned  as per time stamp)

This LLM pass takes in the input individually chunked input transcripted chunks, analyses audience pauses, laughs,
highs and lows to eventually selects from 100s of audio sound effects from

url = examplemp3s.com  assign sound effects to timestamps

after entire pass, audio files associated to correct timestamps will be 
stitched using the compositing module(ffmpeg)
