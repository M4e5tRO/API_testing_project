# API_testing_project
This project automates API tests using **Python** & **Requests**.

* `Requests` docs - https://requests.readthedocs.io/en/latest/
* `pytest` docs - https://docs.pytest.org/en/stable/contents.html
* `Allure` docs - https://allurereport.org/docs/

## Setup

1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   ```
   a. Activate the virtual environment:
      - For **Windows**:
         ```bash
         venv\Scripts\activate
      - For **macOS/Linux**:
         ```bash
         source venv/bin/activate
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Install `Allure`:

   - Follow the official installation guide: [guide](https://allurereport.org/docs/install/)

     - For **Windows**:
       1. Make sure [**Java 11** / **Java 17**](https://learn.microsoft.com/en-us/java/openjdk/download) installed, and its directory is specified in the `JAVA_HOME` environment variable.
       2. Allow changes via PowerShell:
            ```
            Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
            ```
       3. Install Scoop package manager if not already installed:
          ```bash
          iwr get.scoop.sh | iex
          ```
       4. Use Scoop to install Allure:
          ```bash
          scoop install allure
          ```
       5. Verify the installation:
          ```bash
          allure --version
          ```
     - For **macOS/Linux**:
       1. Install using Homebrew:
          ```bash
          brew install allure
          ```
4. Run tests:
    ```bash
    pytest
   
5. Open Allure Report:
    ```bash
    allure serve
    ```