# How to Run SOT fAkePI

To run the Python script, you'll need to have Python installed on your computer. Follow the steps below to install Python:

## Step 1: Download Python

1. Visit the official Python website: [https://www.python.org](https://www.python.org)
2. Click on the "Downloads" tab.
3. Choose the appropriate installer for your operating system (Windows, macOS, or Linux).
4. Click on the download link for the latest version of Python (e.g., Python 3.9).

## Step 2: Run the Installer

1. Locate the downloaded installer file and double-click on it.
2. On the installation wizard, make sure to check the box that says "Add Python to PATH" (for Windows) or "Install command-line tools" (for macOS).
3. Click "Install Now" or "Next" to start the installation process.

Congratulations! You have successfully installed Python on your computer.

## Launch the Script

1. Run run.bat


## How to Use the Script

The script will generate a folder structure following your captaincy ships. At the bottom of these folders will be all the ship milestone values for each milestone that can be placed onto an obs scene using text and "read from file" option. 
Every time you run the script it will overwrite the previous values, and will auto fetch new data every 60 seconds (this can be changed in the script).

## Setting up curl.txt

1. Open curl.txt
2. Navigate to https://www.seaofthieves.com/profile/captaincy/your-ships and open the developer console (F12)
3. In the developer console, click on the "Network" tab.
4. In the filter box, type "captaincy" and press enter.
5. This should show a list of requests. Click on the one called "captaincy".
6. Right click this request and click "Copy as cURL".
7. Paste this into curl.txt and save the file.
8. Run run.bat