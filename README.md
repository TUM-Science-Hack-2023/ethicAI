# ethicAI

## Installation

```
pip3 install streamlit
pip3 install streamlit-chat
pip3 install streamlit-extras

pip3 install pandas
pip3 install plotly

pip3 install --upgrade openai
pip3 install cohere
```


## Secrets

Secrets are the API keys needed to access the LLM APIs. To use them locally, create a `.streamlit/secrets.toml` file under the project root and add the following contents:

```toml
# Everything in this section will be available as an environment variable
# Use thse secret keys with st.secrets["OPEN_AI_KEY"]

COHERE_KEY = "YOUR KEY GOES HERE"
OPEN_AI_KEY = "YOUR KEY GOES HERE" 
OPEN_AI_KEY2 = "YOUR KEY GOES HERE" # Second key to deal with rate limits
```

When hosting on the Streamlit community platform, secrets can be added manually.