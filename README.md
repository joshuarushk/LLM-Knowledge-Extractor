This is a pipeline text analysis prototype wherei every step runs in sequence to transform raw text into structured metadata. The modular pattern is easy to extend, swap, or unit test individual steps independently and ensuring a clean/readable flow.


Setup:

git clone <repo>
cd llm-analyzer
pip install -r requirements.txt
export OPENAI_API_KEY="your_key"
uvicorn app.main:app --reload

I structured the code as a pipeline of steps rather than just utilities, to keep the system modular and composable. Each step is isolated, testable, and can be swapped or added to without changing the rest of the code, this is a dataflow approach rather than a monolithic service. I employed FastAPI for speedy JSON APIs, OpenAI for LLM summarization/metadata, and NLTK for simple noun-based keyword extraction. SQLite was added as a lightweight persistence option to demonstrate extensibility.

Concerning tradeoffs, because of the timebox, I refrained from using a trained model and used rule-based, lightweight sentiment analysis instead of relying on a trained model. Both error handling, validation of LLM JSON responses, and more comprehensive NLPwere toned down for performance. The pipeline is now running sequentially; in production, I'd consider async or parallel processing for scalability.
