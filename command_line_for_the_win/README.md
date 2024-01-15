# Demonstration: Uploading Screenshots to Sandbox Environment Using SFTP

This section provides a step-by-step demonstration of using the SFTP command-line tool to move local screenshots to the sandbox environment.

## Steps

1. **Connect to the Sandbox Environment:**
   - Open a terminal and use the SFTP command to connect to the sandbox environment.

     ```bash
     sftp username@hostname
     ```

2. **Navigate to the Sandbox Directory:**
   - Use the `cd` command to navigate to the target directory in the sandbox environment.

     ```bash
     cd /root/alx-system_engineering-devops/command_line_for_the_win/
     ```

3. **List Current Files in Sandbox:**
   - Use the `ls` command to list the current files in the sandbox directory.

     ```bash
     ls
     ```

4. **Navigate to Local Directory with Screenshots:**
   - Use the `lcd` command to navigate to the local directory where screenshots are stored.

     ```bash
     lcd /path/to/local/screenshots/
     ```

5. **List Local Screenshots:**
   - Use the `!ls` command to list the screenshots in the local directory.

     ```bash
     !ls
     ```

6. **Upload Screenshots to Sandbox:**
   - Use the `put` command to upload screenshots from the local machine to the sandbox.

     ```bash
     put *.png
     ```

7. **Verify Upload in Sandbox:**
   - Use the `ls` command in the sandbox environment to verify that screenshots have been uploaded.

     ```bash
     ls
     ```

8. **Quit SFTP:**
   - After the demonstration, quit the SFTP session.

     ```bash
     quit
     ```

Adjust the commands and paths based on your specific environment.
