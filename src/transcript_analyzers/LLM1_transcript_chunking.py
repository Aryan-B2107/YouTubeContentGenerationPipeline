"""
1) entering API KEY:
headers = {
    'Authorization': 'AIzaSyCSeMpywZGvLDIgYi67_vvlm_S---Ioabg',
    'Content-Type': 'application/json'
}

2)Request Format:
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "Summarize this transcript: [your transcript here]"
    }
  ],
  "max_tokens": 500,
  "temperature": 0.7
}

3) Result Format
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Here's a summary of the transcript..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 50,
    "total_tokens": 150
  }

"""

SYSTEM_PROMPT = """You are an expert at identifying and extracting specific content types from video transcripts with timestamps.

Your job is to:
1. Read the transcript carefully
2. Identify all instances of the requested content type
3. Extract the exact timestamp boundaries 
4. Return the content chunks in structured JSON format

Be precise with timestamps and don't miss any instances."""

#Final Desired OUTPUT FORMAT EXAMPLE:

"""chunks: [
    {
      "start_time": "00:05:23",
      "end_time": "00:06:45",
      "type": "joke",
      "content": "So I went to the doctor..."
    },
    {
      "start_time": "00:12:10",
      "end_time": "00:13:02",
      "type": "joke",
      "content": "My wife told me to stop singing..."
    }
  ]
"""


### USE TAGS TO LLM TO BE ABLE TO READ RELEVANT EXAMPLES
def create_chunking_prompt(transcript_chunk, content_type="jokes"):
    return f"""
    TRANSCRIPT WITH TIMESTAMPS:
{transcript_chunk}

If no {content_type} found, return: {{"chunks": []}}

"""


def intelligent_llm_chunk_pass(transcript_with_timestamps, content_type="joke"):
    pass
