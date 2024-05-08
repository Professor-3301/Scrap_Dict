import subprocess

def dirb_enum(url, threads=10):
    try:
        # Command to execute DirBuster with specified URL and number of threads
        command = f"dirb {url} /home/adwaith/Documents/PROJECT_X/static/wordlist.txt -r {threads}"
        
        direc = []
        # Execute the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        # Read the output line by line
        for line in process.stdout:
            # Check if the line contains a directory name (assuming it starts with '[+]')
            if line.startswith('==>'):
                direc.append(line.strip()[15:])  # Print the directory name
        
        # Wait for the process to finish
        process.wait()
        return direc
    except subprocess.CalledProcessError as e:
        # If an error occurs, print the error message
        print("Error:", e.output)

# Example usage with 20 threads
url_to_scan = "http://www.cek.ac.in/"
dirb_enum(url_to_scan, threads=100)
