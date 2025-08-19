from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

def load_model(model_name="distilgpt2"):
    """
    Loads DistilGPT2 model from Hugging Face using transformers.
    This model is very lightweight (~350MB) and fast for low-memory systems.
    """
    try:
        print(f"🔄 Loading model: {model_name} ...")

        # Check if CUDA is available
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Add padding token if not present
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            device_map="auto" if device == "cuda" else None,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            low_cpu_mem_usage=True  # Optimize for low memory systems
        )

        text_gen_pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device=0 if device == "cuda" else -1
        )

        print("✅ Model loaded successfully.")
        return text_gen_pipeline
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        print("Please ensure you have sufficient memory and the model is available.")
        raise
