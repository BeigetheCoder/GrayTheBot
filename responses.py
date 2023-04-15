import random

def handle_response(message) -> str:
    content = str(message.content).lower()
    if content.startswith("/number"):
        return str(random.randint(0,100))

    if "hi" in content:
        return f"Hi {message.author}! How are you?"

    if "friend" in content:
        return f"yes! {message.author} :)"

    if "money" in content:
        return "🤑"
    
    if "how are you" in content or "how r u" in content \
       or "hru" in content:
        return f"I am good!"
    
    return "." * random.randint(1,10)
