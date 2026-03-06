# Medical-NLP-Chatbot-RAG-Local-LLM-
total working code with end to end apis
Medical NLP Chatbot– Documentation

1. System Architecture
The system follows a Retrieval-Augmented Generation (RAG) architecture where relevant medical data is retrieved from datasets and then passed to a local language model to generate an answer.
Architecture Flow
            User Query
                │
                ▼
        Query Processing Layer
                │
                ▼
         Dataset Loader (JSON)
                │
                ▼
        Context Retrieval Engine
                │
                ▼
        Chunked Medical Records
                │
                ▼
        Local LLM (Ollama - Phi3)
                │
                ▼
          Generated Response
                │
                ▼
              User
Components
1. User Query Interface
•	Accepts natural language queries from the user.
2. Dataset Loader
•	Loads multiple JSON datasets containing patient records.
3. Retrieval Engine
•	Searches relevant chunks of medical records related to the query.
4. Chunking Layer
•	Splits large medical reports into smaller meaningful sections.
5. Local Language Model
•	Uses Phi3 model via Ollama to generate answers.
________________________________________
2. Model Choice
The system uses the Phi-3 model running locally through Ollama.
Reasons for Choosing Phi3
Feature	Reason
Lightweight	Runs efficiently on local machines
Good reasoning ability	Handles question-answering tasks
Offline capability	Ensures data privacy
Fast inference	Faster responses compared to larger models
Why Local Model Instead of Cloud
•	Medical data privacy
•	No internet dependency
•	Reduced API cost
•	Secure data handling
________________________________________
3. Retrieval Strategy
The system uses a keyword-based contextual retrieval approach.
Steps
1.	User enters a natural language query.
2.	The query is scanned for keywords such as:
o	patient id
o	report type
o	diagnosis
o	medical terms
3.	The retrieval engine searches across all datasets.
4.	Relevant documents are extracted.
5.	Retrieved data is passed as context to the LLM.
Retrieval Flow
User Query
     ↓
Keyword Matching
     ↓
Search in JSON datasets
     ↓
Retrieve relevant records
     ↓
Send to LLM for answer generation
This approach ensures that the model only processes relevant medical data, improving response accuracy.
________________________________________
4. Chunking Logic
Medical documents can be large, so they are split into smaller chunks before processing.
Why Chunking is Needed
•	Large documents exceed model context size
•	Improves retrieval accuracy
•	Faster processing
Chunking Strategy
The dataset is divided based on:
•	Document type
•	Medical description
•	Radiology report sections
•	Investigation reports
Example:
Full Medical Record
       │
       ├── Patient Details
       ├── Diagnosis
       ├── Radiology Report
       ├── Investigation Results
       └── Doctor Notes
Each section becomes a separate chunk that can be retrieved independently.
Chunk Size
Typical chunk size:
300 – 500 words
This size balances context understanding and processing speed.
________________________________________
5. Prompt Design
Prompt engineering is used to guide the language model to generate accurate responses.
Prompt Template
You are a medical document assistant.

Use the provided patient medical records to answer the question.

Context:
{retrieved_data}

Question:
{user_query}

Answer clearly based only on the provided context.
Prompt Design Goals
•	Restrict model to dataset information
•	Avoid hallucinated answers
•	Ensure medically relevant responses
•	Generate concise answers
Example
Input Query:
What does the mammography report indicate?
Prompt sent to model:
Context:
Mammography shows both breasts are almost entirely fatty.
No focal mass or suspicious microcalcifications detected.

Question:
What does the mammography report indicate?
Output:
The mammography report indicates that both breasts are mostly fatty and no suspicious masses or calcifications were detected.
________________________________________
Conclusion
This system demonstrates how local LLMs can be integrated with structured healthcare datasets to build an intelligent medical query assistant while maintaining privacy, efficiency, and offline capability.

6 . API Demo

API Demo using curl
Start server
uvicorn app.main:app --reload

Send request
curl -X POST "http://127.0.0.1:8000/query" \
-H "Content-Type: application/json" \
-d '{
"mrd_number": "10109",
"query": "What medications is the patient taking?"
}'

Response
{
  "mrd_number": "10109",
  "answer": "Tab. Ciplox TZ 1-0-1 x 5 days after meals\nTab. Pan 40mg 1-0-1 x 5 days before meals\nTab. Combiflam 1-1-1 x 3 days then SOS for pain after meals\nCap. Becosules 0-1-0 x 15 days\nSyp. Cremaffin 30ml 0-0-1 x SOS for pain",
  "confidence": "High"
}



Explanation
•	The system retrieves relevant patient records using hybrid retrieval (vector search + SQL filtering).
•	The relevant clinical text is passed to the local LLM (Phi-3 via Ollama).
•	The LLM generates a structured clinical response using only the provided patient records.

