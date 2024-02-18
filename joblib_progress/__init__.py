import contextlib
from typing import Optional

import joblib
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

__version__ = "1.0.4"


@contextlib.contextmanager
def joblib_progress(description: Optional[str] = None, total: Optional[int] = None):
    if description is None:
        description = "Processing..."

    progress = Progress(
        SpinnerColumn(),
        TaskProgressColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        "<",
        TimeRemainingColumn(),
    )
    task_id = progress.add_task(f"[cyan]{description}", total=total)

    print_progress = joblib.parallel.Parallel.print_progress

    def update_progress(self: joblib.parallel.Parallel):
        progress.update(task_id, completed=self.n_completed_tasks, refresh=True)
        return print_progress(self)

    try:
        joblib.parallel.Parallel.print_progress = update_progress
        progress.start()

        yield progress
    finally:
        progress.stop()
        joblib.parallel.Parallel.print_progress = print_progress
