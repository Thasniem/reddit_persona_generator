def build_prompt(formatted_text):
    return f"""Analyze this Reddit user and create a personality profile:

USER ANALYSIS:
Based on the posts and comments below, this Reddit user appears to be:

AGE: 
INTERESTS: 
PERSONALITY: 
WRITING STYLE: 

EVIDENCE FROM POSTS:
{formatted_text}

DETAILED PERSONA:"""