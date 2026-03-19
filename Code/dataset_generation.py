import pandas as pd
import openai
import json
import time

client = openai.OpenAI(api_key="")

def generate_examples(seed_nl, seed_fol, num_examples=5):
    
    system_instruction = """
    You are an expert logician and computational linguist. 
    Your task is to expand a high-quality dataset of NL-to-FOL pairs.
    
    STRICT RULES:
    1. STRUCTURAL INVARIANCE: The logical skeleton of the FOL must remain exactly the same as the seed. Do not change the quantifiers, the logical connectives, the negation placement, or the parenthetical nesting.

    2. LEXICAL DIVERGENCE: Replace all predicate names (e.g., human, mammal) and proper names/constants (e.g., john) with entirely new ones. Use diverse domains (e.g., science, sports, technology, ethics, fantasy).

    3. VARIABLE CONSISTENCY: Ensure that variable binding (x, y, z) remains consistent with the original structure.

    4. NATURAL LANGUAGE ALIGNMENT: The new NL sentence must be a fluent, natural-sounding English translation of the new FOL expression, matching the tone and phrasing style of the seed NL.
    
    5. OUTPUT FORMAT: You must return a JSON object with the following structure:
       {"pairs": [{"nl": "...", "fol": "..."}, ...]}
    """

    user_content = f"""
    Generate {num_examples} new, unique pairs structurally isomorphic to this seed:
    NL: {seed_nl}
    FOL: {seed_fol}
    """

    try:
        response = client.chat.completions.create(
            model="",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_content}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )
        
        data = json.loads(response.choices[0].message.content)
        return data.get("pairs", [])
    
    except Exception as e:
        print(f"API Error: {e}")
        return []

input_file = ""
output_file = ""
df = pd.read_excel(input_file)

all_generated_pairs = []

for index, row in df.iterrows():
    seed_nl = row['NL_sentence']
    seed_fol = row['FOL_expression']
    
    print(f"[{index+1}/{len(df)}] Expanding: {seed_nl}")
    
    batch = generate_examples(seed_nl, seed_fol, num_examples=5)
    all_generated_pairs.extend(batch)
    
    if (index + 1) % 5 == 0:
        pd.DataFrame(all_generated_pairs).to_excel(output_file, index=False)
        print(f"--- Progress saved ({len(all_generated_pairs)} pairs total) ---")

    time.sleep(0.5)

final_df = pd.DataFrame(all_generated_pairs)
final_df.to_excel(output_file, index=False)
print(f"Processing complete. {len(final_df)} pairs saved to {output_file}.")