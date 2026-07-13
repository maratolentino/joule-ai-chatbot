# joule-ai-chatbot
An interactive, mobile-responsive energy chatbot ecosystem built for Filipino households. Powered by a FastAPI backend and Google Gemini AI, it features strict contextual guardrails ensuring the model strictly addresses electricity optimization, appliance efficiency, and utility billing inquiries while politely declining unrelated requests.

# Joule AI - Virtual Energy Assistant (Conversational Prototype)

This module serves as the conversational intelligence component of the **Joule AI** ecosystem—a hardware-free household energy manager designed to help consumers reduce electricity consumption. It translates complex billing statistics into highly actionable, easy-to-understand energy efficiency guidance.

##  Key Features
* **Strict Contextual Guardrails**: System-level prompt filtering confines the Large Language Model (LLM) strictly to power utilities, appliances, and energy safety bounds, forcing automatic refusal on out-of-scope topics.
* **Localized Context & Tone**: Programmed to communicate fluently in English, Filipino, and Taglish to render advice natural, empathetic, and highly accessible to local consumers.
* **Hot-Prompt Simulation Chips**: A custom sliding row of quick-select button presets allows judges and users to test critical billing queries instantly.
* **Cross-Origin Configuration**: Equipped with decoupled CORS middleware architecture, providing secure and optimized local network bridge connections between the web client interface and the Python runtime server.

##  Tech Stack & Architecture

### Frontend (Mobile App Shell Mockup)
* **Languages**: HTML5, CSS3, JavaScript (Vanilla ES6+)
* **UI Features**: Responsive mobile device mockup wrapper, dedicated color matching palette, and inline event listeners for instant interaction state loops.

### Backend & AI Inference (Computation Server)
* **Language**: Python 3.10+
* **Framework**: FastAPI (Asynchronous Web Framework)
* **AI Integration**: Google GenAI SDK (Interfacing the Gemini 1.5 Flash Model)
* **Data Validation**: Pydantic (For structural data payload serialization and incoming types parsing)

##  Core Setup Requirements
* Python 3.10 or higher
* Google AI Studio Developer Account (For the `GEMINI_API_KEY` provisioning)
* Dependency libraries: `fastapi`, `uvicorn`, `google-genai`, `pydantic`
