"""
Initially for the sake of working, I'm going to fetch the transcript using YouTubeTranscriptApi.

But Eventually the following will be implemented:
1)Use Beautiful soup to get html of a give YouTube URL
2)scrape the relevant transcript part through analysing css formats, getting all the relevant data like
time stamps and the transcript for that time stamp
3) write in a clean json file and return the json file

"""

"""
OKAY..  so youtube transcript API doesn't work anymore

It's cause AI companies were putting too much load on youtube's servers
by millions of requests, so youtube fought back and now we can't use it

Guess the user will have to manually copy paste transcripts,
which is still faster

ALSO:
Many requests can cause IP bans, so this method is generally risky

Though we can work around that using multiple proxy servers.


"""


