import ReplicatorSender
import ReplicatorReceiver
import threading


def main():
    thread_sender = threading.Thread(target=ReplicatorSender.main, daemon=True)
    thread_receiver = threading.Thread(target=ReplicatorReceiver.main, daemon=True)
    thread_sender.start()
    thread_receiver.start()

    while True:
        print("Enter 'exit' or 'quit' to stop the program")
        user_input = input()
        if user_input == "exit" or user_input == "quit":
            break
    return


if __name__ == "__main__":
    main()
