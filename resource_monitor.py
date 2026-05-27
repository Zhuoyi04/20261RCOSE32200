import platform

def main():
    print("System Resource Monitor")
    print("=" * 23)
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Machine:", platform.machine())


if __name__ == "__main__":
    main()