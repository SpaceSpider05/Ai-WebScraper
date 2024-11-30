import openai
import os

openaikey = "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"
openai.api_key = openaikey


template_gpt = (
    "You are tasked with extracting specific information from the following text content:\n"
    "{dom_content}\n\n"
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}.\n"
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response.\n"
    "3. **No Inferences:** Do not infer or generate information beyond the provided description.\n"
    "4. **Empty Response:** If no information matches the description, return an empty string ('').\n"
    "5. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no additional details, assumptions, or interpretations."
)

def parse_with_openai(dom_chunks, parse_description):
    parsed_results = []
    
    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = template_gpt.format(dom_content=chunk, parse_description=parse_description)
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are an AI assistant that extracts specific data."},
                {"role": "user", "content": prompt}
            ]
        )
        result_text = response.choices[0].message["content"].strip() 
        print(f"Parse batch {i} of {len(dom_chunks)}")
        parsed_results.append(result_text)
        
    return "\n".join(parsed_results)
