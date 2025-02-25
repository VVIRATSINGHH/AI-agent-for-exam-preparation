def __init__(self, offline_mode=False):
    """Initialize the AI agent with specific models"""
    self.offline_mode = offline_mode
    self.study_materials = {}

    if not offline_mode:
        try:
            print("Initializing models...")
            device_type = None
            if torch.cuda.is_available():
                device_type = "cuda"
            elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
                device_type = "mps"
            else:
                device_type = -1
            self.summarizer = pipeline(
                "summarization",
                model="facebook/bart-large-cnn",
                device=device_type
            )
            self.qa_model = pipeline(
                "question-answering",
                model="distilbert/distilbert-base-cased-distilled-squad",
                device=device_type
            )
            print("Models loaded successfully!")

        except Exception as e:
            print(f"Error initializing models: {str(e)}")
            print("Falling back to basic functionality...")
            self.summarizer = None
            self.qa_model = None
    else:
        print("Running in offline mode with basic functionality")
        self.summarizer = None
        self.qa_model = None
