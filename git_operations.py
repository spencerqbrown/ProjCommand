import subprocess

def git_local(name):
    username = "USER"
    password = "PASSWORD"
    subprocess.call(["cd", "cd " + name]) # go to directory
    subprocess.call(["git init", "git commit -m 'first commit'"])
    # TODO load username, password properly
    git_web(username, password, name) # may need to adjust name variable
    url = "github.com" #placeholder
    subprocess.call(["git clone " + url, "git push"])

def git_web(username, password, name):