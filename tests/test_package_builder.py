"""Exercise packaging boundaries in isolated temporary directories."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tempfile
root=Path(__file__).resolve().parents[1]
def run(folder):
    return subprocess.run([sys.executable,str(folder/"tools/build_package.py")],capture_output=True,text=True)
with tempfile.TemporaryDirectory(prefix="website-package-test-") as tmp:
    base=Path(tmp)/"repo"
    for item in ["SKILL.md","package-resources.txt","references","assets","tools"]:
        src=root/item; dest=base/item
        dest.parent.mkdir(parents=True,exist_ok=True)
        if src.is_dir(): shutil.copytree(src,dest)
        else: shutil.copyfile(src,dest)
    assert run(base).returncode==0
    assert run(base).returncode==0
    manifest=json.loads((base/"dist/manifest.json").read_text())
    assert all(p=="SKILL.md" or p.startswith(("references/","assets/")) for p in manifest["files"])
    original=(base/"package-resources.txt").read_text()
    (base/"package-resources.txt").write_text("../outside")
    assert run(base).returncode!=0
    (base/"package-resources.txt").write_text(original)
    outside=Path(tmp)/"outside"; outside.mkdir(); sentinel=outside/"keep.txt"; sentinel.write_text("protected")
    (base/"dist").rename(base/"previous-dist")
    try:
        (base/"dist").symlink_to(outside,target_is_directory=True)
    except OSError:
        print("SKIP: symlink test requires OS permission")
    else:
        assert run(base).returncode!=0
        assert sentinel.read_text()=="protected"
    print("PASS: repeat build, clean allowlist, path rejection; symlink result above if unavailable")
