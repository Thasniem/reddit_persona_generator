import praw
import json
from pathlib import Path

def fetch_reddit_data(username, save_path='data/raw_posts_comments.json'):
    """
    Fetch Reddit user data using PRAW (Python Reddit API Wrapper)
    Note: Requires Reddit API credentials in environment variables or praw.ini
    """
    try:
        # Initialize Reddit instance (read-only)
        reddit = praw.Reddit(
            client_id="your_client_id",  # Replace with your Reddit app client ID
            client_secret="your_client_secret",  # Replace with your Reddit app secret
            user_agent="reddit_persona_generator/1.0 by your_username"
        )
        
        # Get user instance
        user = reddit.redditor(username)
        
        # Fetch posts (submissions)
        posts = []
        try:
            for submission in user.submissions.new(limit=50):
                posts.append({
                    'title': submission.title,
                    'selftext': submission.selftext,
                    'score': submission.score,
                    'created_utc': submission.created_utc,
                    'subreddit': str(submission.subreddit),
                    'url': submission.url
                })
        except Exception as e:
            print(f"Error fetching posts: {e}")
            posts = []
        
        # Fetch comments
        comments = []
        try:
            for comment in user.comments.new(limit=100):
                if hasattr(comment, 'body') and comment.body != '[deleted]':
                    comments.append({
                        'body': comment.body,
                        'score': comment.score,
                        'created_utc': comment.created_utc,
                        'subreddit': str(comment.subreddit)
                    })
        except Exception as e:
            print(f"Error fetching comments: {e}")
            comments = []
        
        data = {"posts": posts, "comments": comments}
        
        # Save data
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        
        return data
        
    except Exception as e:
        print(f"Error connecting to Reddit API: {e}")
        print("Please ensure you have valid Reddit API credentials configured.")
        return {"posts": [], "comments": []}