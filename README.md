# 🧠 AI Icebreaker Generator (LangChain + Ollama)

This project is a **Generative AI application built with LangChain** that generates a concise **summary of a person** using their name. It also provides **interesting facts, ice breakers, and topics of interest** by leveraging LinkedIn and Twitter-style data.

---

## 🚀 Features

- Generates professional summaries from personal data  
- Creates ice breakers & conversation topics  
- Built with **LangChain**  
- Supports **Ollama (local LLMs)** and **OpenAI-compatible models**  
- Uses **sample JSON data from GitHub Gist** for testing  
- Ready for live scraping with tools like **Scrapin**

---

## 🛠 Tech Stack

- Python  
- RAG  
- LangChain  
- Ollama  
- OpenAI API (optional)  
- GitHub Gist (mock data)

---

## 🧪 Data Source

- **Testing**: Static LinkedIn & Twitter JSON data hosted on GitHub Gist  
- **Production**: Can be extended to scrape live data from LinkedIn & Twitter

## ⚙️ Environment Setup

Create a `.env` file or set environment variables before running the app:

```env
# OpenAI API Key (from https://openai.com)
OPENAI_API_KEY=sk-xxxxx

# SerpAPI (for Google search)
SERPAPI_API_KEY=xxxxxx

# ProxCurl API (for LinkedIn data)
PROXYCURL_API_KEY=xxxxxx

# Twitter API keys (from https://developer.twitter.com)
TWITTER_API_KEY=xxxx
TWITTER_API_SECRET=xxxxxx
TWITTER_ACCESS_TOKEN=xx-xx
TWITTER_ACCESS_SECRET=xxxx

# Optional: Use sample Twitter data to skip API call
TWITTER_SAMPLE=1

