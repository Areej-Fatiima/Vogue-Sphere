# import subprocess
# import time

# if __name__ == "__main__":
#     print("Starting both Flask apps...")

#     # Start fetch_and_match.py on port 5000
#     fetch_proc = subprocess.Popen(["python", "outfit_scraper/fetch_and_match.py"])
    
#     print("fetch_and_match.py started on http://127.0.0.1:5001")

#     # Give it a second to start
#     time.sleep(2)

#     # Start app.py (AI Feedback) on port 5001
#     ai_proc = subprocess.Popen(["python", "outfit_scraper/app.py"])
#     print("app.py (AI Feedback) started on http://127.0.0.1:5000")

#     print("Both apps are running. Press Ctrl+C to stop.")

#     try:
#         # Keep the script running to maintain subprocesses
#         fetch_proc.wait()
#         ai_proc.wait()
#     except KeyboardInterrupt:
#         print("Stopping both apps...")
#         fetch_proc.terminate()
#         ai_proc.terminate()
#         print("Both apps stopped.")





# import subprocess
# import time
# import os

# if __name__ == "__main__":
#     # Get the directory where run_both.py is located
#     current_dir = os.path.dirname(os.path.abspath(__file__))
    
#     print("Starting both Flask apps...")

#     # Start fetch_and_match.py on port 5001
#     # Using 'python' or 'python.exe' depending on environment
#     fetch_proc = subprocess.Popen(
#         ["python", "fetch_and_match.py"],
#         cwd=current_dir
#     )
#     print(f"fetch_and_match.py started on http://127.0.0.1:5001")

#     # Give it a couple of seconds to start
#     time.sleep(2)

#     # Start app.py (AI Feedback) on port 5000
#     ai_proc = subprocess.Popen(
#         ["python", "app.py"],
#         cwd=current_dir
#     )
#     print(f"app.py (AI Feedback) started on http://127.0.0.1:5000")

#     print("\nBoth apps are running. Press Ctrl+C to stop.")

#     try:
#         # Keep the script running to maintain subprocesses
#         while True:
#             # Check if processes are still running
#             if fetch_proc.poll() is not None:
#                 print("fetch_and_match.py has stopped unexpectedly.")
#                 break
#             if ai_proc.poll() is not None:
#                 print("app.py has stopped unexpectedly.")
#                 break
#             time.sleep(1)
            
#     except KeyboardInterrupt:
#         print("\nStopping both apps...")
#         fetch_proc.terminate()
#         ai_proc.terminate()
#         print("Both apps stopped.")




import subprocess
import time
import sys

if __name__ == "__main__":
    print("Starting both Flask apps...")

    python_executable = sys.executable

    # Start fetch_and_match.py on port 5001
    fetch_proc = subprocess.Popen(
        [python_executable, "outfit_scraper/fetch_and_match.py"]
    )
    print("fetch_and_match.py started on http://127.0.0.1:5001")

    # Give it a second to start
    time.sleep(2)

    # Start app.py (AI Feedback) on port 5000
    ai_proc = subprocess.Popen(
        [python_executable, "outfit_scraper/app.py"]
    )
    print("app.py (AI Feedback) started on http://127.0.0.1:5000")

    print("Both apps are running. Press Ctrl+C to stop.")

    try:
        fetch_proc.wait()
        ai_proc.wait()
    except KeyboardInterrupt:
        print("Stopping both apps...")
        fetch_proc.terminate()
        ai_proc.terminate()
        print("Both apps stopped.")
