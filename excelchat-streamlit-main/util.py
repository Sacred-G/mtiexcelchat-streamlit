from langchain.chat_models import ErnieBotChat
from langchain.llms.ollama import Ollama
from pandasai.llm import OpenAI, LangchainLLM
from pandasai.prompts import GeneratePythonCodePrompt

from llm.ais_erniebot import AIStudioErnieBot


def get_open_ai_model(api_key):
    return OpenAI(api_token=api_key)


def get_ollama_model(model_key, base_url):
    llm = Ollama(model=model_key, base_url=base_url, verbose=True)
    return LangchainLLM(langchain_llm=llm)


def get_baidu_as_model(access_token):
    llm_core = AIStudioErnieBot(access_token=access_token, verbose=True)
    return LangchainLLM(llm_core)


def get_baidu_qianfan_model(client_id, client_secret):
    llm_core = ErnieBotChat(
        model_name="ERNIE-Bot",
        temperature=0.1,
        ernie_client_id=client_id,
        ernie_client_secret=client_secret
    )
    return LangchainLLM(llm_core)


# Function to get a custom prompt template
def get_prompt_template():
    instruction_template = """
    Using the provided dataframes ('dfs'), analyze this data, and avoid calling dataframe set_index to sort the data during the process.
    1. Preparation: If necessary, preprocess and clean the data.
    2. Execution: Perform data analysis operations on the data (grouping, filtering, aggregating, etc.).
    3. Analysis: Conduct actual analysis (if the user requests a plot chart, please add the following two lines of code in the script to set the font, save and display the result as an image file 'temp_chart.png').
    plt.rcParams['font.sans-serif']
    plt.rcParams['axes.unicode_minus']=False
    4. Use original dataframe ('dfs') for additional questions.
    """
    custom_template = GeneratePythonCodePrompt(custom_instructions=instruction_template)
    return custom_template

# Main function
