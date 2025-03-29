import textwrap

class DynamicCodeGenerator:
    @staticmethod
    def generate_function_code(function_name):
        function_map = {
            'open_chrome': '''
from system_functions import SystemFunctions

def main():
    try:
        SystemFunctions.open_chrome()
        print("Chrome opened successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")
''',
            'open_calculator': '''
from system_functions import SystemFunctions

def main():
    try:
        SystemFunctions.open_calculator()
        print("Calculator opened successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")
''',
            'open_notepad': '''
from system_functions import SystemFunctions

def main():
    try:
        SystemFunctions.open_notepad()
        print("Notepad opened successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")
''',
            'open_file_explorer': '''
from system_functions import SystemFunctions

def main():
    try:
        SystemFunctions.open_file_explorer()
        print("File Explorer opened successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")
''',
            'open_task_manager': '''
from system_functions import SystemFunctions

def main():
    try:
        SystemFunctions.open_task_manager()
        print("Task Manager opened successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")
''',
            'get_system_info': '''
from system_functions import SystemFunctions

def main():
    try:
        system_info = SystemFunctions.get_system_info()
        print("System Information:", system_info)
    except Exception as e:
        print(f"Error retrieving system info: {e}")
''',
            'check_disk_usage': '''
from system_functions import SystemFunctions

def main():
    try:
        disk_info = SystemFunctions.check_disk_usage()
        print("Disk Usage Information:", disk_info)
    except Exception as e:
        print(f"Error retrieving disk usage: {e}")
''',
            'get_running_processes': '''
from system_functions import SystemFunctions

def main():
    try:
        processes = SystemFunctions.get_running_processes()
        print("Running Processes:", processes)
    except Exception as e:
        print(f"Error retrieving running processes: {e}")
''',
            'shutdown_system': '''
from system_functions import SystemFunctions

def main():
    try:
        SystemFunctions.shutdown_system()
        print("System is shutting down.")
    except Exception as e:
        print(f"Error executing shutdown: {e}")
''',
            'restart_system': '''
from system_functions import SystemFunctions

def main():
    try:
        SystemFunctions.restart_system()
        print("System is restarting.")
    except Exception as e:
        print(f"Error executing restart: {e}")
''',
            'get_network_info': '''
from system_functions import SystemFunctions

def main():
    try:
        network_info = SystemFunctions.get_network_info()
        print("Network Information:", network_info)
    except Exception as e:
        print(f"Error retrieving network info: {e}")
''',
            'run_shell_command': '''
from system_functions import SystemFunctions

def main(command=None):
    try:
        if not command:
            command = input("Enter shell command to execute: ")
        result = SystemFunctions.run_shell_command(command)
        print("Command Execution Result:")
        print(result)
    except Exception as e:
        print(f"Error executing shell command: {e}")
'''
        }

        code_template = function_map.get(function_name)
        
        if not code_template:
            raise ValueError(f"No code template found for function: {function_name}")
        
        return textwrap.dedent(code_template).strip()