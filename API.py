import getpass
import os

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("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")