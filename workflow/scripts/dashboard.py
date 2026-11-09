from pathlib import Path

import signac
from signac_dashboard import Dashboard
from signac_dashboard.modules import (
    DocumentList,
    FileList,
    ImageViewer,
    Schema,
    StatepointList,
)

ROOT = Path(__file__).resolve().parents[2]


class CustomDashboard(Dashboard):
    pass


if __name__ == "__main__":
    project = signac.get_project(str(ROOT / "data"))

    modules = [
        StatepointList(),
        DocumentList(context="JobContext"),
        DocumentList(context="ProjectContext"),
        FileList(),
        ImageViewer(context="JobContext", img_globs=["figures/*.png"]),
        Schema(),
    ]

    dashboard = CustomDashboard(
        project=project,
        modules=modules,
    )
    dashboard.main()
