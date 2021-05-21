import os

import mlrun.feature_store as fs
from dotenv import load_dotenv
from mlrun import set_environment


def main():
    # Load environment variables
    load_dotenv()

    # Setup project
    project_name, artifact_path = set_environment(
        project="remote-model-deployment",
        artifact_path=os.getenv("MLRUN_ARTIFACT_PATH"),
        api_path=os.getenv("MLRUN_DBPATH"),
        access_key=os.getenv("V3IO_ACCESS_KEY"),
    )
    print(f"Setting project environment for '{project_name}'")

    print(
        fs.get_offline_features("level-3-demo/heart-disease-train")
        .to_dataframe()
        .head()
    )


if __name__ == "__main__":
    main()
