This package has two modules.

•transcript fetcher - fetches the transcript of selected YouTube video and generates 
the transcript using YouTubeAnalytics API.
                    - fetches watch time data, of highly watched timestamps.

•transcript transmitter - takes raw transcript data,converts to valid json format
                          which is going to be called by transcript_analyser package

                        - json format will have following data:
                            ->high watchtime time stamp ranges
                            ->per line trasncript time stamps:
ex:[
  {
    "text": "Hey everyone, welcome back to the channel!",
    "start": 0.0,
    "duration": 4.5
  },
  ...
]