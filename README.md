# url_lookup_service
This is a test project. The purpose of all the files in the repository is mentioned below:

URLLookupSvc.py - The service tags the URL as malware based on a list of existing malware list in the database.
db_setup.py - The script helps set up a SQLite db for use by the application. It creates the table, inserts a list of malware URLs, displays the contents of the table.
malware_list.txt - A sample list of URLs obtained from the internet.
malware_url.db - A sample database
requirements.txt - Packages to be installed on the system in order to run the application successfully
url_lookup.app - A simple flask application which allows the users to enter a URL and responds back with a True/False flag for the Malware field

"HOW TO USE THE CODE"

1. Clone the respository.
2. Create a Python virtual environment and run the "pip install -r requirements.txt" command to install the dependencies.
3. Run the "db_setup.py" script to create a local database.
4. Run the url_lookup.app. It should run on flask default port 5000. Enter the URL in the field and click on Submit.
5. 
