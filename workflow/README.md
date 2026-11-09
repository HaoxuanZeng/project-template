# Workflow

Commands below are run from `workflow/`.

## Initialize

```bash
(cd ../data && ../target/release/populate_workspace)
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
