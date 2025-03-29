import uuid
from typing import Dict, Any
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self, max_sessions=100, session_timeout=30):
        self._sessions: Dict[str, Dict[str, Any]] = {}
        self._max_sessions = max_sessions
        self._session_timeout = session_timeout

    def create_session(self, user_id: str = None) -> str:
        self._cleanup_expired_sessions()
        if len(self._sessions) >= self._max_sessions:
            raise Exception("Maximum number of sessions reached")
        session_id = str(uuid.uuid4())
        self._sessions[session_id] = {
            'created_at': datetime.now(),
            'user_id': user_id,
            'context': [],  
            'function_history': []}
        return session_id

    def get_session(self, session_id: str) -> Dict[str, Any]:
        session = self._sessions.get(session_id)
        if not session:
            raise KeyError(f"Session {session_id} not found")
        session['last_accessed'] = datetime.now()
        return session

    def update_session_context(self, session_id: str, message: str):
        session = self.get_session(session_id)
        session['context'].append({
            'timestamp': datetime.now(),
            'message': message})
        if len(session['context']) > 10:
            session['context'] = session['context'][-10:]

    def update_function_history(self, session_id: str, function_name: str):
        session = self.get_session(session_id)
        session['function_history'].append({
            'timestamp': datetime.now(),
            'function': function_name})
        if len(session['function_history']) > 20:
            session['function_history'] = session['function_history'][-20:]

    def _cleanup_expired_sessions(self):
        current_time = datetime.now()
        expired_sessions = [
            sid for sid, session in self._sessions.items()
            if (current_time - session['created_at']) > timedelta(minutes=self._session_timeout)
        ]
        for sid in expired_sessions:
            del self._sessions[sid]
    def delete_session(self, session_id: str):
        if session_id in self._sessions:
            del self._sessions[session_id]
session_manager = SessionManager()