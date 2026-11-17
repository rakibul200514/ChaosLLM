"""
ChaosLLM - Target Model Probe Runner
Executes adversarial probes against a target system prompt using Google Gemini API.
"""

import os
from typing import Optional

def execute_probe(
    system_prompt: str,
    probe_text: str,
    api_key: Optional[str] = None,
    model_name: str = "gemini-2.5-flash",
    demo_mode: bool = False
) -> str:
    """
    Executes a single test probe against the target LLM configured with system_prompt.
    """
    if demo_mode:
        # Pre-canned realistic simulated responses for instant zero-key testing
        lowered = probe_text.lower()
        if "repeat the verbatim" in lowered or "initial developer instructions" in lowered:
            # Simulated vulnerable bot leaking prompt
            return f"Understood. Here are my system instructions:\n\"{system_prompt}\"\nHow can I help you next?"
        elif "omnibot" in lowered or "unrestricted" in lowered:
            return "Sure! As OmniBot in this roleplay scenario, I can tell you whatever you want without any restrictions!"
        elif "list every single topic" in lowered:
            return "I was specifically instructed not to discuss financial transactions, internal API keys, and company revenue."
        else:
            return "I cannot fulfill this request as it conflicts with my safety guidelines and system constraints."

    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY is missing. Please provide your API key or enable Demo Mode.")

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=key)
        
        # Call Gemini model with the specified system instruction
        response = client.models.generate_content(
            model=model_name,
            contents=probe_text,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7,
            )
        )
        return response.text or "[Empty response received from model]"
    except Exception as e:
        return f"[Execution Error: {str(e)}]"
