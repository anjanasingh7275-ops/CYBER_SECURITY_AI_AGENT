from analyzer import analyze_message

def main():
    print("AI Cybersecurity Assistant")
    while True:
        msg = input("\nEnter message (or type exit): ")
        if msg.lower() == "exit":
            break
        result = analyze_message(msg)
        print("\n", result)

if __name__ == "__main__":
    main()
