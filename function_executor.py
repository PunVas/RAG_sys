from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import io
import contextlib
import traceback
from system_functions import SystemFunctions
from vector_registry import FunctionVectorRegistry
from dynamic_code_generator import DynamicCodeGenerator
from session_handler import session_manager

app = FastAPI(title="LLM RAG Function Executor with Session Management")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

function_registry = FunctionVectorRegistry()

class SessionCreateRequest(BaseModel):
    user_id: str = None

class ExecutionRequest(BaseModel):
    prompt: str
    session_id: str = None
    parameters: dict = {}  

class ExecutionResponse(BaseModel):
    function: str
    code: str
    output: dict | str = None  
    session_id: str

@app.post("/create-session")
async def create_session(request: SessionCreateRequest = None):
    """Create a new session"""
    try:
        user_id = request.user_id if request else None
        session_id = session_manager.create_session(user_id)
        return {"session_id": session_id}
    except Exception as e:
        print(f"Error creating session: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import io
import contextlib
import traceback
import subprocess
from system_functions import SystemFunctions
from vector_registry import FunctionVectorRegistry
from dynamic_code_generator import DynamicCodeGenerator
from session_handler import session_manager

app = FastAPI(title="LLM RAG Function Executor with Session Management")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


function_registry = FunctionVectorRegistry()

class SessionCreateRequest(BaseModel):
    user_id: str = None

class ExecutionRequest(BaseModel):
    prompt: str
    session_id: str = None
    parameters: dict = None  

class ExecutionResponse(BaseModel):
    function: str
    code: str
    output: str | dict  
    session_id: str


@app.post("/execute", response_model=ExecutionResponse)
async def execute_function(
    request: ExecutionRequest, 
    x_session_id: str = Header(None)
):
    try:
        
        session_id = request.session_id or x_session_id or session_manager.create_session()
        
        
        try:
            session_manager.get_session(session_id)
        except KeyError:
            session_id = session_manager.create_session()
        
        
        session_manager.update_session_context(session_id, request.prompt)
        
        
        function_name = function_registry.retrieve_function(request.prompt)
        if not function_name:
            raise HTTPException(status_code=404, detail="No matching function found")
        
        
        code = DynamicCodeGenerator.generate_function_code(function_name)
        
        output = None
        
        if function_name == "run_shell_command":
            command = request.parameters.get("command")
            if not command:
                raise HTTPException(status_code=400, detail="Missing shell command parameter")

            try:
                process = subprocess.run(command, shell=True, capture_output=True, text=True)
                output = process.stdout if process.stdout else process.stderr
            except Exception as e:
                output = str(e)

        elif function_name == "open_application":
            app_name = request.parameters.get("app")
            if not app_name:
                raise HTTPException(status_code=400, detail="Missing application name")

            try:
                subprocess.Popen(app_name, shell=True)
                output = f"Application '{app_name}' launched successfully"
            except Exception as e:
                output = str(e)

        else:
            
            with contextlib.redirect_stdout(io.StringIO()) as f:
                exec_locals = {}
                exec(code, globals(), exec_locals)
                main_func = exec_locals.get('main')

                if main_func:
                    main_func()
                    output = f.getvalue().strip()

        
        session_manager.update_function_history(session_id, function_name)
        
        return ExecutionResponse(
            function=function_name,
            code=code,
            output=output,
            session_id=session_id
        )
    
    except Exception as e:
        print(f"Error executing function: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/session-context/{session_id}")
async def get_session_context(session_id: str):
    try:
        session = session_manager.get_session(session_id)
        return {
            "context": session.get('context', []),
            "function_history": session.get('function_history', [])
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Session not found")

@app.delete("/session/{session_id}")
async def delete_session(session_id: str):
    try:
        session_manager.delete_session(session_id)
        return {"message": "Session deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def health_check():
    return {"status": "Service is running"}
