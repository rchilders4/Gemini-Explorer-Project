Gemini Explorer Project

This code demonstrated my creation of a Streamlit chat interface integrating Google's advanced language model, Gemini.
I send an inital prompt to Google's Vertexai as a query to the llm_function def setting it to the user role and getting the output as the model's response for the model role.

For the Gemini_Explorer.py to work first you need to download the Google Cloud CLI installer.

To run Gemini_Explorer.py, you use the following lines of code in powershell:
gcloud init
gcloud auth login
streamlit run Gemini_Explorer.py

Once the localhost launches in your defult browser, you will have the chance to enter a name, age, race, and pronouns to give Rex as it initaly talks to the Vertexai.
Otherwise it will default to an generic initial prompt, afterworks a chat input will appear and you can directly create messages yourself.
