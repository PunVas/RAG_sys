import chromadb
from sentence_transformers import SentenceTransformer
import numpy as np

class FunctionVectorRegistry:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.embedding_model = SentenceTransformer(model_name)
        self.chroma_client = chromadb.Client()
        try:
            self.chroma_client.delete_collection("function_registry")
        except:
            pass
        self.collection = self.chroma_client.create_collection(name="function_registry")
        self.function_descriptions = {
            'open_chrome': 'Open the Google Chrome web browser',
            'open_calculator': 'Launch the system calculator application',
            'open_notepad': 'Open the default text editor',
            'get_system_info': 'Retrieve current system performance metrics',
            'run_shell_command': 'Execute a shell or command prompt command',
            'open_file_explorer': 'Open the system file explorer (Finder on Mac, Nautilus on Linux)',
            'open_task_manager': 'Open Task Manager or equivalent system monitoring tool',
            'check_disk_usage': 'Retrieve total, used, and free disk space on the system',
            'get_running_processes': 'Fetch a list of currently running system processes',
            'shutdown_system': 'Shutdown the computer immediately',
            'restart_system': 'Restart the computer immediately',
            'get_network_info': 'Retrieve system IP address and network interface details'
        }
        self._populate_registry()

    def _populate_registry(self):
        function_ids = list(self.function_descriptions.keys())
        descriptions = list(self.function_descriptions.values())
        embeddings = self.embedding_model.encode(descriptions)
        self.collection.add(
            embeddings=embeddings.tolist(),
            documents=descriptions,
            ids=function_ids
        )

    def retrieve_function(self, query, top_k=1):        
        query_embedding = self.embedding_model.encode([query])[0].tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        if results['ids'] and results['ids'][0]:
            return results['ids'][0][0]
        return None