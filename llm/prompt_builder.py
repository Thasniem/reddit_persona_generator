def build_prompt(formatted_text):
    return f"""
You are an expert in personality profiling. Analyze this Reddit user's activity and create a detailed user persona including:

- Age group
- Occupation or status
- Interests/hobbies
- Personality traits
- Mood trends
- Subreddits they visit
- Writing style
- Notable quotes (with post/comment snippets)

Cite the source (post title or comment) for each trait.

User Activity:
{formatted_text}
"""