# Workflow

Commands below are run from `workflow/`.

## Initialize

```bash
python scripts/populate_workspace.py
```

Jobs are stored in `../data/workspace/`.

```bash
row show status
row show jobs
row show directories
```

## Submit Jobs

Always check the generated job scripts:

```bash
row submit --dry-run -n 1
```

Only submit if the job scripts are correct:

```bash
row submit --action <ACTION_NAME>
```

## Dashboard

The dashboard requires `signac-dashboard`.

Serve the dashboard using:

```bash
python scripts/dashboard.py run --port 8888
```

Access a remote dashboard using:

```bash
ssh -N -L 8888:127.0.0.1:8888 user@host
```
