# CropCareAI
CropCareAI is a web application built using the Flask framework that aims to assist plant enthusiasts, farmers, and researchers in identifying and diagnosing plant diseases using AI.
CropCareAI is a web application built using the Flask framework that aims to assist plant enthusiasts, farmers, and researchers in identifying and diagnosing plant diseases using AI.
Installation guide for cropcare.ai

1. **Install Python**: 
Make sure Python is installed on your system. You can download the latest version of Python from the official Python website (https://www.python.org/) Choose the appropriate installer for your operating system and follow the installation instructions.
   - **Note for Windows users**: During the installation, make sure to check the box that says "Add Python to PATH" to ensure that Python is added to the system's environment variables.

2.  **Clone the GitHub repository**: 
Navigate to the GitHub repository page of the Flask application you want to install. Click on the "Code" button and choose the option to clone the repository. You can either download the ZIP file and extract it or use git to clone the repository to your local machine.
   - If you choose to download the ZIP file, extract it to a location of your choice.

3. **Open a terminal or command prompt**: 
Open a terminal or command prompt on your system or open us VS Code. The steps for opening a terminal or command prompt may vary depending on your operating system.

4. **Navigate to the project directory**: Use the `cd` command to navigate to the root directory of the downloaded Flask application. For example, if you extracted the ZIP file to a folder named "my-flask-app," you would use the following command to navigate to that folder:

   ```
   cd path/to/my-flask-app
   ```




5. **Create a virtual environment**: It's recommended to create a virtual environment to isolate the dependencies of the Flask application. In the terminal or command prompt, run the following command to create a virtual environment:
   ```
   python -m venv myenv
   ```
 This command will create a new directory named "myenv" that will contain the virtual environment.

6. **Activate the virtual environment**: Activate the virtual environment by running the appropriate command based on your operating system:
   - For Windows:
     ```
     myenv\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source myenv/bin/activate
     ```

   After activation, you should see "(myenv)" at the beginning of your command prompt, indicating that you are working inside the virtual environment.
7. **Install dependencies
Run the following command to install the dependencies:
   ```
   pip install -r requirements.txt
   ```
 This command will install all the required packages and libraries specified in the `requirements.txt` file.



8. **Run cropcare-ai application**: 
Once the dependencies are installed and any necessary environment variables are set, you can run the Flask application. In the terminal or command prompt, navigate to the directory where the main application file (`app.py` or similar) is located. Run the following command to start the Flask application:
   ```
   flask run
   ```
Or 
   ```
   python app.py
   ```

   The Flask application should now start running locally. You can access it by visiting `http://localhost:5000` in your web browser.

That's it! You have now successfully installed and set up the Cropcare-AI application from GitHub on your local machine. You can explore and use the application as needed.

You may encounter the following errors:
Click link to see how to solve them



“An attempt was made to access a socket in a way forbidden by its access permissions/ Permission denied: Unable to establish a connection to the socket/ Socket operation on non-socket: Access denied"
File not found errors/ Module not found
