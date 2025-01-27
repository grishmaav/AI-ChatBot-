import pyautogui
import time
import pyperclip
from openai import OpenAI




client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="alex"):
    
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

   
pyautogui.click(1639, 1412)

time.sleep(1)  
while True:
    time.sleep(5)
   
    pyautogui.moveTo(972,202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')  

    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  
    pyautogui.click(1994, 281)

    
    chat_history = pyperclip.paste()

    
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named alan.You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] alex: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1808, 1328)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')