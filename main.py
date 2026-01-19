from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()


def main():
    print("Hello from langchain-course!")


    summary_template = """
    given the LinkedIn information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="llama3.2:1b")
    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json")
    response = chain.invoke(input={"information": linkedin_data})
    print(response.content)

if __name__ == "__main__":
    main()
