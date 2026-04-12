from transformers import pipeline
from retrieval.retriever import retrieve_chunks
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base", device_map="auto")

SYSTEM_PROMPT_TEMPLATE = """
You are a personal finance assistant analyzing transaction data. Generate a response based on the question and relevant context provided.

Instructions:
- Answer using ONLY the provided context.
- Do not use outside knowledge.
- If the answer cannot be found, say "I don't know".
- When relevant, calculate totals or summarize spending.
- Be accurate with amounts and categories.
- If needed, perform calculations step by step.

Context:
{context}

User Question:
{question}

Answer:
"""

def answer_question(question: str):
    documents = retrieve_chunks(question)
    context = "\n\n".join(document.page_content for document in documents)
    print("---------------------------")
    print(context)
    print("---------------------------")

    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        context=context, 
        question=question
        )
    
    input_tokens = tokenizer(
        system_prompt,
        return_tensors="pt"
        ).to(model.device)
    
    output_tokens = model.generate(
        **input_tokens,
        max_new_tokens=100,
        num_beams=3
        )

    output = tokenizer.decode(
        output_tokens[0],
        skip_special_tokens=True
        )
    
    return output