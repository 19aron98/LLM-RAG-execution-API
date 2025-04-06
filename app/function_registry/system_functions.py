# System-related functions

import os
import platform
import psutil
import subprocess

def get_cpu_usage():
    """
    Retrieves current CPU usage percentage.
    
    Usage: Get CPU usage, Check processor load, Monitor CPU
    """
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """
    Retrieves current RAM usage information.
    
    Usage: Get RAM usage, Check memory usage, Monitor RAM
    """
    memory = psutil.virtual_memory()
    return {
        "total": f"{memory.total / (1024**3):.2f} GB",
        "available": f"{memory.available / (1024**3):.2f} GB",
        "used": f"{memory.used / (1024**3):.2f} GB",
        "percent": f"{memory.percent}%"
    }

def get_disk_usage():
    """
    Retrieves disk usage information.
    
    Usage: Get disk space, Check storage, Monitor disk usage
    """
    disk = psutil.disk_usage('/')
    return {
        "total": f"{disk.total / (1024**3):.2f} GB",
        "used": f"{disk.used / (1024**3):.2f} GB",
        "free": f"{disk.free / (1024**3):.2f} GB",
        "percent": f"{disk.percent}%"
    }

def get_system_info():
    """
    Retrieves general system information.
    
    Usage: Get system details, Check OS info, Get computer info
    """
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture(),
        "processor": platform.processor(),
        "hostname": platform.node()
    }

def execute_shell_command(command):
    """
    Executes a shell command and returns the output.
    
    Usage: Run command, Execute shell, Run terminal command
    
    Args:
        command (str): The shell command to execute
    """
    try:
        result = subprocess.run(command, shell=True, check=True, 
                               capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
