# LLM RAG Function Executor API

## Overview
This project is a **Function Execution API** powered by **LLM(all-MiniLM-L6-v2)** and **session management**. It takes a **prompt**, finds which function to run, generates the code dynamically, executes it, and returns the output. It can also execute **shell commands** and **launch  some apps**.

*I have tried my best to make it work on both linux and windows but currently tested only on windows.*

*I have use an LLM to generate some dummy functions like open_chrome, open_task_manager, etc.*
It supports:
- **Session Management** (track previous prompts and executions)
- **Dynamic Function Execution** (run generated code securely)
- **Executing Shell Commands** (run terminal commands via API)
- **Opening Applications** (launch apps from a prompt)
- And many more...

---

## Installation & Setup
### Prerequisites
- Python 3.9+
- FastAPI
- Uvicorn
- Required dependencies from `requirements.txt`

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/PunVas/RAG_sys.git
   cd RAG_sys
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
4. The API will be available at `http://127.0.0.1:8000/`

5. Want to try apis in browser itself? go to `http://127.0.0.1:8000/docs`
   
---

## How to Use

### Screenshots

### 1. Session creation and open chrome 
<div align="center">
  <img src="./ss/Screenshot_1.png" alt="Execution Example" width="45%">
  <img src="./ss/Screenshot_2.png" alt="Session Creation" width="45%">
</div>

### 2. Show system stats and custom command execution
<div align="center">
  <img src="./ss/Screenshot_3.png" alt="Function Execution" width="45%">
  <img src="./ss/Screenshot_4.png" alt="Shell Command" width="45%">
</div>

### 3. NetworkInfo  & Session Context  
<div align="center">
  <img src="./ss/Screenshot_5.png" alt="Application Launch" width="45%">
  <img src="./ss/Screenshot_6.png" alt="Session Context" width="45%">
</div>

### 4. Session deletion 
<div align="center">
  <img src="./ss/Screenshot_7.png" alt="Health Check" width="45%">
</div>
