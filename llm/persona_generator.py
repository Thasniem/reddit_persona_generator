def generate_persona(prompt, generator):
    output = generator(prompt, max_new_tokens=800, temperature=0.7)[0]["generated_text"]
    return output
