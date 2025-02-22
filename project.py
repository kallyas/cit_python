# program to manage project creation

import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


def create_project(name, language, project_dir):
    language = language.lower()
    # move to project_dir folder
    os.chdir(project_dir)
    if language == 'nodejs' or language == 'node' or language == 'node.js':
        # execute nodejs project creation
        print('Creating a Node.js project called ' + name)
        os.system('npm init -y')
        os.system('yarn add express cors jsonwebtoken mongoose dotenv morgan')
        os.system('curl https://raw.githubusercontent.com/github/gitignore/main/Node.gitignore -o .gitignore')
        os.system('git init')
        os.system('echo ' + name + ' >> README.md' if not os.name == 'nt' else 'echo ' + name + ' >> README.md')
        os.system('git add .')
        os.system('git commit -m "first commit"')
        os.system('mkdir src && cd src && mkdir config controllers models routes utils helpers && cd ..')
        os.system('code .')
    elif language == 'react' or language == 'reactjs' or language == 'react.js':
        # execute react project creation
        print('Creating a React project called ' + name)
        os.system('npx create-react-app ' + name + ' .')
        os.system('git init')
        os.system('git add .')
        os.system('git commit -m "first commit"')
        # open project with vscode
        os.system('code .')
    elif language == 'python' or language == 'python3':
        # execute python project creation
        print('Creating a Python project called ' + name)
        os.system('python3 -m venv venv')
        os.system('source venv/bin/activate')
        os.system('git init')
        os.system('curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -o .gitignore')
        # create main.py file, check if system is windows or linux
        os.system('echo >> main.py' if not os.name == 'nt' else 'touch main.py')
        os.system('git add .')
        os.system('git commit -m "first commit"')
        os.system('code .')
    elif language == 'web' or language == 'html' or language == 'css' or language == 'javascript':
        # execute web project creation
        print('Creating a Web project called ' + name)
        os.system('git init')
        os.system('echo ' + name + ' >> README.md' if not os.name == 'nt' else 'echo ' + name + ' >> README.md')
        os.system('mkdir js css assets && echo ' + name + ' >> index.html' if not os.name == 'nt' else 'touch index.html')
        os.system('git add .')
        os.system('git commit -m "first commit"')
        os.system('code .')
    elif language == 'php':
        # execute php project creation
        print('Creating a PHP project called ' + name)
        os.system('git init')
        os.system('echo ' + name + ' >> README.md' if not os.name == 'nt' else 'echo ' + name + ' >> README.md')
        os.system('composer init')
        os.system('echo ' + name + ' >> index.php' if not os.name == 'nt' else 'touch index.php')
        os.system('curl https://gist.githubusercontent.com/Yousha/a5514afd6cda8afba800f5af9f7115b4/raw/a27554246db50778257d079a89705e79f8488151/.gitignore -o .gitignore')
        os.system('git add .')
        os.system('git commit -m "first commit"')
        os.system('code .')
    else:
        print('Language not supported')


def main():
    print('Welcome to the project creator')
    project_name = input('Enter project name: ')
    project_dir = input('Enter project directory: ')
    language = input('Enter language: ')

    if project_name == '' or project_dir == '' or language == '':
        print('Please enter all the fields')
        return

    create_project_dir(project_dir)
    create_project(project_name, language, project_dir)


if __name__ == '__main__':
    main()



