use clap::Parser;
use std::fs::{self, File};
use std::io::Write;
use std::path::PathBuf;
use std::process::Command;
use std::time::SystemTime;

/// Concatenate GoPro footage in a directory into one file using ffmpeg
#[derive(Parser)]
#[command(author, version, about)]
struct Args {
    /// Path to the directory containing GoPro clips
    input_dir: PathBuf,

    /// Output file name
    #[arg(short, long, default_value = "output.mp4")]
    output: PathBuf,

    /// Print the order of files before concatenating
    #[arg(short, long)]
    verbose: bool,

    /// List the order only; do not run ffmpeg
    #[arg(short = 'n', long = "dry-run")]
    dry_run: bool,
}

fn main() -> anyhow::Result<()> {
    let args = Args::parse();

    let mut files_with_times: Vec<(PathBuf, SystemTime)> = fs::read_dir(&args.input_dir)?
        .filter_map(|e| e.ok())
        .map(|e| e.path())
        .filter(|p| {
            p.extension()
                .map(|ext| ext.to_ascii_lowercase() == "mp4")
                .unwrap_or(false)
        })
        .filter_map(|p| fs::metadata(&p).and_then(|m| m.modified()).ok().map(|t| (p, t)))
        .collect();

    files_with_times.sort_by_key(|(_, t)| *t);

    if files_with_times.is_empty() {
        anyhow::bail!("No .mp4 files found in {:?}", args.input_dir);
    }

    // Always print a concise order in dry-run; in non-dry-run only if verbose.
    if args.dry_run || args.verbose {
        println!("Files will be concatenated earliest → latest:");
        for (i, (path, time)) in files_with_times.iter().enumerate() {
            let dt: chrono::DateTime<chrono::Local> = (*time).into();
            println!("{:>2}. {} ({})", i + 1, path.display(), dt);
        }
        println!();
    }

    // If dry-run, stop here successfully.
    if args.dry_run {
        println!("(dry-run) Not invoking ffmpeg. Exiting.");
        return Ok(());
    }

    // Create concat list for ffmpeg
    let list_path = args.input_dir.join("files.txt");
    let mut list_file = File::create(&list_path)?;
    for (path, _) in &files_with_times {
        // ffmpeg concat demuxer wants single quotes and -safe 0 allows abs paths
        writeln!(list_file, "file '{}'", path.display())?;
    }

    // Run ffmpeg concat without re-encoding
    let status = Command::new("ffmpeg")
        .args([
            "-f", "concat",
            "-safe", "0",
            "-i", list_path.to_str().unwrap(),
            "-c", "copy",
            args.output.to_str().unwrap(),
        ])
        .status()?;

    if !status.success() {
        anyhow::bail!("ffmpeg failed");
    }

    println!(
        "✅ Concatenated {} clips into {}",
        files_with_times.len(),
        args.output.display()
    );
    Ok(())
}
