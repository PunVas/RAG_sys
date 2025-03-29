import os
import psutil
import subprocess
import platform

class SystemFunctions:
    @staticmethod
    def open_chrome():
        if platform.system() == 'Darwin':  
            subprocess.Popen(['open', '-a', 'Google Chrome'])
        elif platform.system() == 'Windows':
            os.startfile('chrome')
        else:  
            subprocess.Popen(['google-chrome'])

    @staticmethod
    def open_calculator():
        if platform.system() == 'Windows':
            os.system('calc')
        elif platform.system() == 'Darwin':  
            subprocess.Popen(['open', '-a', 'Calculator'])
        else:  
            subprocess.Popen(['gnome-calculator'])

    @staticmethod
    def open_notepad():
        if platform.system() == 'Windows':
            os.system('notepad')
        elif platform.system() == 'Darwin':  
            subprocess.Popen(['open', '-a', 'TextEdit'])
        else:  
            subprocess.Popen(['gedit'])

    @staticmethod
    def open_file_explorer():
        if platform.system() == 'Windows':
            os.system('explorer')
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', '.'])
        else:
            subprocess.Popen(['xdg-open', '.'])

    @staticmethod
    def open_terminal():
        if platform.system() == 'Windows':
            os.system('start cmd')
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', '-a', 'Terminal'])
        else:
            subprocess.Popen(['gnome-terminal'])

    @staticmethod
    def open_task_manager():
        if platform.system() == 'Windows':
            os.system('taskmgr')
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', '-a', 'Activity Monitor'])
        else:
            subprocess.Popen(['gnome-system-monitor'])

    @staticmethod
    def get_system_info():
        return {
            'cpu_usage': psutil.cpu_percent(),
            'memory_usage': psutil.virtual_memory().percent,
            'total_memory': psutil.virtual_memory().total / (1024 * 1024),  
            'available_memory': psutil.virtual_memory().available / (1024 * 1024)  
        }

    @staticmethod
    def get_disk_usage():
        disk = psutil.disk_usage('/')
        return {
            'total_space': disk.total / (1024 ** 3),  
            'used_space': disk.used / (1024 ** 3),
            'free_space': disk.free / (1024 ** 3),
            'usage_percent': disk.percent
        }
    
    @staticmethod
    def check_disk_usage(threshold=80):
        disk = psutil.disk_usage('/')
        return {
            'usage_percent': disk.percent,
            'exceeds_threshold': disk.percent > threshold
        }

    @staticmethod
    def check_internet():
        try:
            subprocess.check_call(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def system_shutdown():
        if platform.system() == 'Windows':
            os.system('shutdown /s /t 0')
        elif platform.system() == 'Darwin' or platform.system() == 'Linux':
            os.system('shutdown now')

    @staticmethod
    def system_restart():
        if platform.system() == 'Windows':
            os.system('shutdown /r /t 0')
        elif platform.system() == 'Darwin' or platform.system() == 'Linux':
            os.system('reboot')

    @staticmethod
    def system_logoff():
        if platform.system() == 'Windows':
            os.system('shutdown /l')
        elif platform.system() == 'Darwin' or platform.system() == 'Linux':
            os.system('pkill -KILL -u $USER')

    @staticmethod
    def run_shell_command(command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'return_code': result.returncode
            }
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def get_running_processes():
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            processes.append(proc.info)
        return processes

    @staticmethod
    def get_network_info():
        try:
            import socket
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            return {'hostname': hostname, 'ip_address': ip_address}
        except Exception as e:
            return {'error': str(e)}
