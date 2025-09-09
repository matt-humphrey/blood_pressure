import banksia as bk

from blood_pressure import DATA_TRANSFORMS, make_interim_datasets, transform_datasets
from blood_pressure.config import DATASETS, INTERIM_DATA, METADATA, PROCESSED_DATA


def main():
    # Perform interim changes - rename variables, and drop redundant variables
    make_interim_datasets(DATASETS)

    # Read datasets into memory
    dfs, metas = {}, {}

    for name, dset in DATASETS.items():
        df, meta = bk.read_sav(INTERIM_DATA / dset["file"])
        dfs[name] = df
        metas[name] = meta

    # Perform transformations on interim data
    transformed_dfs = transform_datasets(dfs, DATA_TRANSFORMS)
    transformed_metas = bk.transform_metadata(metas, METADATA)

    # Save processed data
    for name, dset in DATASETS.items():
        print(f"Writing {name}...")
        bk.write_sav(PROCESSED_DATA / dset["file"], transformed_dfs[name], transformed_metas[name])
        print(f"{name} saved.")


if __name__ == "__main__":
    main()
