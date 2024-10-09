from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
    You are tasked with extracting specific information from the following text content: {dom_content}.
    Please follow these instructions carefully: \n\n
    1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}.
    2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. 
    3. **Empty Response:** If no information matches the description, return an empty string ('').
    4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.
"""

model = OllamaLLM(model="llama3")

def parse_with_ollama(dom_chunks, parse_description):
    # Create a prompt template to use with our model.
    prompt = ChatPromptTemplate.from_template(template)
    # Create a chain: First go to the prompt, then go to the model.
    chain = prompt | model
    
    parsed_results = []
    
    # For each of the chunks...
    for i, chunk in enumerate(dom_chunks, start = 1):
        # ...Call the LLM and pass it to it with the parse_description.
        response = chain.invoke(
            {
                "dom_content": chunk, 
                "parse_description": parse_description
            }
        )
        
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        # Append the response from the LLM.
        parsed_results.append(response)
        
    # Join all the results with a new line character and return them.    
    return "\n".join(parsed_results)