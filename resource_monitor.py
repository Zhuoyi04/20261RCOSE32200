import os
import platform
import psutil
from datetime import datetime

def save_report(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    print("System Resource Monitor")
    print("=" * 23)

    print("System:", platform.system())
    print("Release:", platform.release())
    print("Machine:", platform.machine())

    print("\nCPU Information")
    print("-" * 15)
    print("Physical Cores:", psutil.cpu_count(logical=False))
    print("Total Cores:", psutil.cpu_count(logical=True))
    # Measure the current CPU usage percentage over a 1-second interval (for a more accurate reading)
    print("CPU Usage (%):", psutil.cpu_percent(interval=1))

    memory = psutil.virtual_memory()

    print("\nMemory Information")
    print("-" * 18)
    print("Total Memory (GB):", round(memory.total / (1024 ** 3), 2))
    print("Used Memory (GB):", round(memory.used / (1024 ** 3), 2))
    print("Available Memory (GB):", round(memory.available / (1024 ** 3), 2))
    print("Memory Usage (%):", memory.percent)

    # Check disk usage of the main system drive
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    print("\nDisk Information")
    print("-" * 16)
    print("Total Disk Space (GB):", round(disk.total / (1024 ** 3), 2))
    print("Used Disk Space (GB):", round(disk.used / (1024 ** 3), 2))
    print("Free Disk Space (GB):", round(disk.free / (1024 ** 3), 2))
    print("Disk Usage (%):", disk.percent)

    report = f"""
        System Resource Monitor Report
        Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

        System: {platform.system()}
        Release: {platform.release()}
        Machine: {platform.machine()}

        CPU Usage: {psutil.cpu_percent(interval=1)}%
        Memory Usage: {memory.percent}%
        Disk Usage: {disk.percent}%
    """

    save_report("system_report.txt", report)
    print("\nReport saved as system_report.txt")

if __name__ == "__main__":
    main()