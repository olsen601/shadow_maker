# shadow_maker
Generates sudo shadow files to test john the ripper.

First
  Clone the repo to a local repository.
  Create a virtual environment outside the repository.
  Navigate to inside the local repository.
  Using "pip install -r requirements.txt" install the required python modules.
  
Second
  From a command prompt enter "python shadow.py"
  
  
Loose ends
  If your using this on a unix system, pcrypt needs to be replaced with crypt in the import statement on line 1 of shadow.py.
