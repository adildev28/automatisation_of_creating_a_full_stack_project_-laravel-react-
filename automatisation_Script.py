import os
import subprocess

def run_command(command):
    """Utility function to run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True)
        print(f"Executed command: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e}")
        exit(1)



def initialize_repo(directory):
    """Function to initialize a git repository in the given directory."""
    os.chdir(directory)
    run_command("git init")
    print(f"Initialized empty Git repository in {directory}")

def create_laravel_project():
    """Function to create a Laravel project."""
    print("creating laravel project...")
    run_command(f"composer create-project --prefer-dist laravel/laravel backend")
    print("Laravel project created successfully.")

def create_react_project(template):
    """Function to create a React project with Vite."""
     print(f"creating {template} project...")
    run_command(f"npm create vite@latest front-end -- --template {template}")
    print(f"React project with {template} template created successfully.")

def setup_laravel_env(db_name, db_user, db_password):
    """Function to set up Laravel .env file with MySQL database configuration."""
    env_file = "backend/.env"
    with open(env_file, 'r') as file:
        env_content = file.read()

    # Modify .env content for MySQL
    env_content = env_content.replace("DB_CONNECTION=mysqli", "DB_CONNECTION=mysql")
    env_content = env_content.replace("DB_DATABASE=laravel", f"DB_DATABASE={db_name}")
    env_content = env_content.replace("DB_USERNAME=root", f"DB_USERNAME={db_user}")
    env_content = env_content.replace("DB_PASSWORD=", f"DB_PASSWORD={db_password}")

    with open(env_file, 'w') as file:
        file.write(env_content)

    print(f"Laravel .env configured with MySQL database '{db_name}'")

def install_react_packages():
    """Function to install necessary React packages."""
    os.chdir("front-end")
    run_command("npm install react-router-dom")
    print("React Router DOM installed successfully.")
    os.chdir("..")

def main():
    print("Welcome to the Laravel-React project automation script!")

    # Step 1: Ask for MySQL database credentials
    db_name = input("Enter the name for the MySQL database: ").strip()
    db_user = input("Enter your MySQL username: ").strip()
    db_password = input("Enter your MySQL password: ").strip()

    # Step 2: Create the MySQL database


    # Step 3: Get project name
    project_name = input("Enter the project name: ").strip()

    # Step 4: Create project directory on Desktop
    # Define the path to the directory
    project_path = os.path.join(os.path.expanduser("~/Desktop"), project_name)

    # Check if the directory exists
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        print(f"Directory '{project_name}' created at {project_path}")
    else:
        print(f"Directory '{project_name}' already exists at {project_path}")

    # Now you can access the directory
    os.chdir(project_path)

    # Step 5: Initialize a local Git repository
    initialize_repo(project_path)

    # Step 6: Create Laravel project
    os.chdir(project_path)
    create_laravel_project()

    # Step 7: Ask for React template choice
    template = input("Enter the Vite template for React (e.g., react, react-ts): ").strip()

    # Step 8: Create React project with Vite
    os.chdir(project_path)
    create_react_project(template)

    # Step 9: Set up Laravel .env file with the MySQL database configuration
    setup_laravel_env(db_name, db_user, db_password)

    # Step 10: Install React Router DOM in the React project
    install_react_packages()

    print("Project setup complete! You're ready to start coding!")

if __name__ == "__main__":
    main()
