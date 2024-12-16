import os

def create_project_structure_with_descriptions(base_dir):
    """
    Creates a project folder structure with descriptions for each folder.
    """
    structure = {
        "data": {
            "subfolders": ["raw/", "processed/", "results/"],
            "description": "This folder contains all the data for the project. "
                           "Raw data goes in 'raw/', processed data in 'processed/', and results in 'results/'."
        },
        "notebooks": {
            "subfolders": [
                "1_data_collection.ipynb",
                "2_data_engineering.ipynb",
                "3_modeling.ipynb",
                "4_visualization.ipynb",
            ],
            "description": "This folder contains Jupyter notebooks for data collection, cleaning, modeling, and visualization."
        },
        "scripts": {
            "subfolders": [
                "scrape_alibaba.py",
                "scrape_resale.py",
                "data_cleaning.py",
                "clustering.py",
                "profitability_model.py",
                "sentiment_analysis.py",
                "run_pipeline.py",
            ],
            "description": "This folder contains Python scripts for scraping data, cleaning it, performing analysis, "
                           "and running the pipeline."
        },
        "tests": {
            "subfolders": ["test_scraping.py", "test_data_cleaning.py", "test_models.py"],
            "description": "This folder contains unit tests for different parts of the project, "
                           "including data scraping, cleaning, and model testing."
        },
        "results": {
            "subfolders": ["insights.pdf", "visualizations/"],
            "description": "This folder contains the results of the analysis, such as insights and visualizations."
        },
    }

    # Root files
    root_files = [".gitignore", "README.md", "requirements.txt", "LICENSE"]
    root_description = (
        "This is the root directory for the project. It contains global files like the README, "
        "requirements.txt for dependencies, and LICENSE for the project."
    )

    # Create base directory
    os.makedirs(base_dir, exist_ok=True)

    # Add root-level description
    with open(os.path.join(base_dir, "description.txt"), "w") as f:
        f.write(root_description)

    # Create folders, subfolders, and descriptions
    for folder, details in structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Add folder-specific description
        description_path = os.path.join(folder_path, "description.txt")
        with open(description_path, "w") as f:
            f.write(details["description"])

        # Create subfolders and files
        for item in details["subfolders"]:
            item_path = os.path.join(folder_path, item)
            if item.endswith("/"):  # It's a folder
                os.makedirs(item_path, exist_ok=True)
            else:  # It's a file
                with open(item_path, "w") as f:
                    f.write("")  # Create an empty file

    # Create root-level files
    for file in root_files:
        file_path = os.path.join(base_dir, file)
        with open(file_path, "w") as f:
            f.write("")  # Create an empty file

    print(f"Project structure successfully created at {base_dir}!")
# Specify the base directory
base_directory = r"C:\Users\amine\Desktop\Gestion des Projets\Projets en Développement\E-Commerce Product Pricing & Sentiment Study"
create_project_structure_with_descriptions(base_directory)
