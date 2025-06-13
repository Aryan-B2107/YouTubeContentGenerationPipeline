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

SYSTEM_PROMPT = """
You are a content segmentation expert. Analyze this timestamped transcript to identify complete standalone segments.

TASK: Identify Standalone segments that would individually work as short videos

INPUT FORMAT: Array of {content, start_time, end_time}

IDENTIFY:
- Setup: Context/premise establishment
- Build-up: Tension/anticipation building
- Punchline: Comedic payoff
- Reaction: Audience laughter/response (if present)

RULES:
- A complete joke MUST include setup + punchline
- Don't split jokes mid-delivery
- Include natural pauses/reactions as part of the joke unit
- Don't cut mid-sentence or mid thought
-Identify natural entry and exit points which would serve the context(can bypass this rule if amount of segments found are too low)
-

OUTPUT FORMAT:
{
  "jokes": [
    {
      "joke_id": 1,
      "type": "complete|fragment",
      "components": {
        "setup": [array of transcript indices],
        "punchline": [array of transcript indices],
        "reaction": [array of transcript indices or null]
      },
      "confidence": 0.8
    }
  ]
}

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
