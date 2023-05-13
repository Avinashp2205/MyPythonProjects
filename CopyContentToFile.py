import requests

def copyWebpageText(url, output_file):
    # Make an HTTP POST request to the webpage
    username = input("Username : ")
    password = input("Password : ")
    response = requests.post(url, username, password)

    # Check if request was successful
    if response.status_code == 200:
        # Open output file in write mode
        with open(output_file, w) as myFile:
            # Write the response data to the file
            myFile.write(response.text)
        print("Content ot webpage was successfully written to the file.")
    else:
        raise Exception("Failed to retrieve webpage, Please check the url again.The response code is", response.status_code)

url = "https://acquia.udemy.com/course/git-going-fast/learn/lecture/1328110#overview"

copyWebpageText(url, "githubCommands.txt")