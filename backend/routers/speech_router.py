from ..controllers.speech_controller import call_gemini
from fastapi import APIRouter

router = APIRouter()

@router.post("/categorize")
async def categorize_text(request):
    """Generalizes text into a specific set of categories."""
    prompt = f"""
    Analyze the following text and categorize it into EXACTLY ONE of these categories: {', '.join("")}.
    Return only the category name.

    Text: {request}
    """
    result = await call_gemini(prompt)
    return {"processed_text": result}


@router.post("/humanize")
async def humanize_text(text):
    """Rewrites text to sound more conversational and 'human-speakable'."""
    prompt = f"""
    Rewrite the following text to sound more natural and conversational. 
    Avoid robotic phrasing or overly formal jargon while maintaining the original content.

    Input: {text}
    """
    result = await call_gemini(prompt)
    return result


