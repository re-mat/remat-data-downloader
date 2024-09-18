from __future__ import annotations

import importlib.metadata

import remat_data_downloader as m


def test_version():
    assert importlib.metadata.version("remat_data_downloader") == m.__version__
