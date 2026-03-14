from ..controllers.speech_controller import call_gemini

async def humanize_text(text, ):
    """Rewrites text to sound more conversational and 'human-speakable'."""
    prompt = f"""
    Rewrite the following text to sound more natural and conversational. 
    Avoid robotic phrasing or overly formal jargon while maintaining the original content.

    Input: {text}
    """
    result = await call_gemini(prompt)
    return result


print(humanize_text("Ryan says: Today i went to the gym and saw my friends in the cinema. Milan says: Today i did revision until the afternoon, then went to the gym and made dinner with my mum."))