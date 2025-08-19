# main.py (root folder)
import sys
from reddit.reddit_scraper import fetch_reddit_data
from reddit.utils import extract_username_from_url, format_user_data
from llm.model_loader import load_model
from llm.prompt_builder import build_prompt
from llm.persona_generator import generate_persona
from pathlib import Path

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python main.py <reddit_profile_url>")
            return

        url = sys.argv[1]
        username = extract_username_from_url(url)
        if not username:
            print("❌ Invalid Reddit profile URL")
            print("Expected format: https://reddit.com/user/username")
            return

        print(f"\n🔍 Scraping Reddit data for user: {username}...")
        data = fetch_reddit_data(username)
        
        if not data['posts'] and not data['comments']:
            print("❌ No data found for this user. They may have no public posts/comments.")
            return
            
        formatted = format_user_data(data['posts'], data['comments'])
        
        if not formatted.strip():
            print("❌ No usable content found after formatting.")
            return

        print("\n🤖 Loading language model...")
        generator = load_model()

        print("\n🧠 Building user persona...")
        prompt = build_prompt(formatted)
        persona = generate_persona(prompt, generator)

        output_path = Path(f"outputs/{username}_persona.txt")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(persona)

        print(f"\n✅ User persona saved to: {output_path}")
        
    except KeyboardInterrupt:
        print("\n⚠️ Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check your internet connection and Reddit API credentials.")

if __name__ == "__main__":
    main()
