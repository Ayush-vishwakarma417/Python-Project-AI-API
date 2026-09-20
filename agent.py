import os
import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Set PERMANENT Database
db_client = chromadb.PersistentClient(path="./agent_brain")
collection = db_client.get_or_create_collection(name="personal_memory")

# Set Gemini 
ai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def chat_with_memory(user_message):
    past_context = ""
    
    if collection.count() > 0:
        results = collection.query(query_texts=[user_message], n_results=2)
        if results['documents'][0]:
            past_context = "\n".join(results['documents'][0])
    
    system_instruction = f"""You are a helpful, conversational AI assistant. 
    Here are relevant facts the user has told you in the past. Use them to answer naturally!
    PAST MEMORIES:\n{past_context}"""
    
    response = ai_client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_message,
        config={"system_instruction": system_instruction}
    )
    
    # Save the new memory
    msg_id = f"msg_{collection.count() + 1}"
    collection.add(documents=[user_message], ids=[msg_id])
    
    return response.text, past_context

# RUNNING THE ENGINE 

print("🧠 Memory Agent is online! (Type 'quit' to exit, or 'show memory' to look inside)")

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == 'quit':
        print("Shutting down...")
        break
        
 # The  Command to look inside the database ---
    if user_input.lower() == 'show memory':
        all_data = collection.get() # will get the info from database.
        print("\n--- 🗄️ LOOKING INSIDE THE VAULT ---")
        if not all_data['documents']:
            print("Memory is totally empty!")
        else:
            for i in range(len(all_data['ids'])):
                print(f"[{all_data['ids'][i]}] -> {all_data['documents'][i]}")
        continue
    # -----------------------------------------------------------

    answer, memory_pulled = chat_with_memory(user_input)
    
    if memory_pulled:
        print(f"\n[System Secretly Pulled: '{memory_pulled}']")
        
    print(f"Agent: {answer}")