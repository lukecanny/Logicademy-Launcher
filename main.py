import os
import subprocess
import sys

class ProjectLauncher:
    def __init__(self, projects_config):
        """
        projects_config: Dictionary of project names to their absolute paths
        Example: {
            'hdlgen'     :   './HDLGen-ChatGPT/',
            'socbuilder' :   './PYNQ-SoC-Builder/'
        }
        """
        self.projects = projects_config

    def run_project(self, project_name):
        """
        Run a specific project's main.py
        """
        if project_name not in self.projects:
            raise ValueError(f"Project {project_name} not found")
        
        project_path = self.projects[project_name]
        
        try:
            # Run main.py in the project's directory
            result = subprocess.run(
                [sys.executable, 'main.py'], 
                cwd=project_path, 
                capture_output=True, 
                text=True
            )
            
            # Optional: print output
            print(result.stdout)
            
            if result.stderr:
                print("Errors:", result.stderr)
            
            return result.returncode
        
        except Exception as e:
            print(f"Error running {project_name}: {e}")
            return -1

def main():

    # Get the absolute path of the current script
    current_script_path = os.path.abspath(__file__)
    print(current_script_path)
    # Get the directory containing the current script
    current_directory   = os.path.dirname(current_script_path)
    print(current_directory)
    # Construct paths to dir containing main.py for each project
    hdlgen_dir          = os.path.join(current_directory, 'HDLGen-ChatGPT/Application')
    socbuilder_dir      = os.path.join(current_directory, 'PYNQ-SoC-Builder')

    print(hdlgen_dir)
    print(socbuilder_dir)

    # Configure projects
    launcher = ProjectLauncher({
        'hdlgen':       hdlgen_dir,
        'socbuilder':   socbuilder_dir
    })

    # Run a specific project
    x = input("Press 1 for HDLGen, and 2 for PYNQ SoC Builder: ")
    if (x=="1"):
        launcher.run_project('hdlgen')
    elif (x=="2"):
        launcher.run_project('socbuilder')
    else:
        print("Invalid Option Selected")
        main()

if __name__ == '__main__':
    main()