def generate_persona(prompt, generator):
    """
    Generate a persona using the provided LLM generator.
    """
    try:
        output = generator(
            prompt, 
            max_new_tokens=300,  # Reduced from 800 for faster generation
            temperature=0.7,
            do_sample=True,
            pad_token_id=generator.tokenizer.eos_token_id
        )[0]["generated_text"]
        
        # Extract only the generated part (remove the original prompt)
        if prompt in output:
            persona = output.replace(prompt, "").strip()
        else:
            persona = output.strip()
            
        return persona
        
    except Exception as e:
        print(f"❌ Error generating persona: {e}")
        return "Error: Could not generate persona. Please try again."
