import random
import subprocess
from MiniCalculatorInterpreter import calculator
def handle_response(message) -> str:
    content = str(message.content).lower()
    if content.startswith("roll"):
        return str(random.randint(0,100))

    if "hi" in content:
        return f"Hi {message.author}! How are you?"

    if "friend" in content:
        return f"yes! {message.author} :)"

    if "money" in content:
        return "🤑"
    
    if "how are you" in content or "how r u" in content \
       or "hru" in content or "how u" in content:
        return f"I am good!"
    if "i am good" in content or "i am okay" in content or "i am great" in content:
        return "That's great!"
    
    if "i am feeling sad" in content or "i am angry" in content or "i am not feelimg well" in content:
        return "Oh no, why is that?"
    
    if content.startswith("reverse"):
        return content.replace("reverse","")[::-1]

    if content.startswith("calculate"):
        value = subprocess.check_output(["python3","MiniCalculatorInterpreter/calculator.py", content.replace("calculate ","")  ], text=True)
        return value.strip()
    
    if "?" in content:
        return "Yes!" if random.randint(1,10) < 6 else "No!"

    if content.startswith("choose "):
        options = content.replace("choose ","").split(",")
        return options[random.randint(0,len(options)-1)]
     
    return "." * random.randint(1,10)


class TestMessage():
    def __init__(self, content):
        self.content = content

def test_handle_response():
    message = TestMessage("calculate 2+3")
    response = handle_response(message)
    assert("5" == response)

if __name__ == "__main__":
    test_handle_response()