"""Build a clean runtime package without including authoring or test records."""
from pathlib import Path
import hashlib, json, shutil, subprocess, os, stat
ROOT = Path(__file__).resolve().parents[1]
name = next(l.split(": ", 1)[1] for l in (ROOT / "SKILL.md").read_text().splitlines() if l.startswith("name: "))
if name not in {"z-website-analysis", "z-website-critique", "z-website-production"}:
    raise SystemExit("Unexpected skill name")
resources = (ROOT / "package-resources.txt").read_text().split()
if resources != ["references", "assets"]:
    raise SystemExit("Unexpected runtime allowlist")
dest = ROOT / "dist" / name
if (ROOT / "dist").is_symlink() or (ROOT / "SKILL.md").is_symlink():
    raise SystemExit("Symlinked package roots are not allowed")
if any((ROOT / folder).is_symlink() for folder in resources):
    raise SystemExit("Symlinked resource roots are not allowed")
if dest.resolve().parent != (ROOT / "dist").resolve() or dest.is_symlink():
    raise SystemExit("Unsafe package target")
if dest.exists():
    for directory in [dest, *dest.rglob("*")]:
        if directory.is_dir() and not directory.is_symlink():
            os.chmod(directory, directory.stat().st_mode | stat.S_IRWXU)
    def retry_readonly(function, path, error_info):
        error = error_info[1]
        if not isinstance(error, PermissionError):
            raise error
        os.chmod(path, stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
        function(path)
    shutil.rmtree(dest, onerror=retry_readonly)
dest.mkdir(parents=True)
shutil.copyfile(ROOT / "SKILL.md", dest / "SKILL.md")
for folder in resources:
    for src in (ROOT / folder).rglob("*"):
        if src.is_symlink():
            raise SystemExit("Symlinks are not runtime inputs")
    shutil.copytree(ROOT / folder, dest / folder)
hashes = {str(f.relative_to(dest)).replace(chr(92), "/"): hashlib.sha256(f.read_bytes()).hexdigest()
          for f in sorted(dest.rglob("*")) if f.is_file()}
sha = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
(ROOT / "dist" / "manifest.json").write_text(json.dumps({"source_commit":sha or "uncommitted","files":hashes},indent=2)+"\n")
print(f"Built {name}: {len(hashes)} runtime files")
