use std::path::Path;

use anyhow::{Context, anyhow};
use hoomd_workspace::Entry;
use log::info;

use crate::StatePoint;

pub fn simulate_one(directory: &Path) -> anyhow::Result<()> {
    let state_point: StatePoint = hoomd_workspace::state_point(directory)
        .context("could not read state point")?
        .ok_or(anyhow!("state point not found"))?;

    let job_directory = state_point.path()?;

    info!(
        "Loaded `{}`: n={}, temperature={}",
        job_directory.display(),
        state_point.n,
        state_point.temperature,
    );

    // Initialize and run your simulation using state_point.
    // Write job-specific files under job_directory.
    //
    // The tutorial's full simulate.rs also handles checkpointing,
    // wall time, trajectories, and property logging.

    Ok(())
}
