import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <options>")
        sys.exit(1)

    selected_tasks = sys.argv[1:]
    print("You can do anything based on user choices:\n")
    print("Selection:")
    for task in selected_tasks:
        print(task)


if __name__ == "__main__":
    main()
