from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_model(model_name="microsoft/phi-2"):
    """
    Loads the Phi-2 model from Hugging Face using transformers.
    This model is small and fast, making it ideal for lightweight use cases.
    """
    print(f"🔄 Loading model: {model_name} ...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

    text_gen_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device_map="auto",
        torch_dtype="auto"
    )

    print("✅ Model loaded successfully.")
    return text_gen_pipeline
