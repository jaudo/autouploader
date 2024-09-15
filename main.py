'''import threading
import subprocess
import os
proc = subprocess.Popen(os.getcwd() + r'\runInf.bat',
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            stdin=subprocess.PIPE,
                            cwd=os.getcwd(),
                            env=os.environ)
proc.stdin.close()

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    script1_thread = threading.Thread(target=run_script, args=("dut1.py",))
    script2_thread = threading.Thread(target=run_script, args=("dut2.py",))
    script3_thread = threading.Thread(target=run_script, args=("dut3.py",))
    script4_thread = threading.Thread(target=run_script, args=("dut4.py",))
    script5_thread = threading.Thread(target=run_script, args=("dut5.py",))
    script6_thread = threading.Thread(target=run_script, args=("dut6.py",))

    script1_thread.start()
    script2_thread.start()
    script3_thread.start()
    script4_thread.start()
    script5_thread.start()
    script6_thread.start()

    script1_thread.join()
    script2_thread.join()
    script3_thread.join()
    script4_thread.join()
    script5_thread.join()
    script6_thread.join()

    print("Both scripts have finished executing.")'''

import subprocess

# Path to the Tkinter application script
script_path = "dut1.py"

# Number of instances to launch
num_instances = 6

processes = []

# Launch multiple instances
for _ in range(num_instances):
    process = subprocess.Popen(["python", script_path])
    processes.append(process)

# Optionally wait for all processes to complete
for process in processes:
    process.wait()