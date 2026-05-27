import platform
import psutil

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

if __name__ == "__main__":
    main()