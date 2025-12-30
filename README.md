## Agentic RAG System

This project implements an **agentic Retrieval-Augmented Generation (RAG)** pipeline designed to produce **grounded, self-evaluated answers** rather than free-form LLM responses.

Instead of answering questions in a single pass, the system treats question answering as a **multi-step reasoning process**:
1. Retrieve relevant documents from a vector database
2. Grade the retrieved evidence for relevance and sufficiency
3. Escalate to web search when local knowledge is insufficient
4. Generate an answer constrained by supporting evidence
5. Evaluate the final answer for usefulness and factual support before returning it

The workflow is orchestrated as a **graph of modular reasoning nodes**, allowing the system to dynamically route, retry, or halt based on quality checks. This design reduces hallucinations, improves factual grounding, and mirrors how a human researcher searches, evaluates, and synthesizes information.

### Key Features
- **Vector-based retrieval** using embeddings and a persistent Chroma database
- **Agentic control flow** with conditional routing and feedback loops
- **Document and answer grading** to detect low-quality or unsupported responses
- **Evidence-constrained generation** to reduce hallucination risk
- **Modular, extensible architecture** built with LangChain

### Use Cases
- Knowledge-grounded chatbots and assistants
- Research and documentation Q&A systems
- Safer, more reliable LLM applications that require evidence awareness
