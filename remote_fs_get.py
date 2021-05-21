import os
import yaml
import mlrun.feature_store as fs
from mlrun import set_environment


def main():
    # Load config
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    # Set remote credentials
    os.environ["MLRUN_DBPATH"] = config["MLRUN_DBPATH"]
    os.environ["MLRUN_ARTIFACT_PATH"] = config["MLRUN_ARTIFACT_PATH"]
    os.environ["V3IO_USERNAME"] = config["V3IO_USERNAME"]
    os.environ["V3IO_API"] = config["V3IO_API"]
    os.environ["V3IO_ACCESS_KEY"] = config["V3IO_ACCESS_KEY"]

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
