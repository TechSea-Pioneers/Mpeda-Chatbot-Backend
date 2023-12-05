from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt

def setup_llama_cpp():
    llm = LlamaCPP(
        model_url='',
        model_path="./model/openhermes-2.5-neural-chat-7b-v3-2-7b.Q4_K_M.gguf",
        temperature=0.1,
        max_new_tokens=3024,
        context_window=3900,
        generate_kwargs={},
        model_kwargs={"n_gpu_layers": 90},
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        verbose=True,
    )
    print('LlamaCPP is ready to use.')
    return llm
