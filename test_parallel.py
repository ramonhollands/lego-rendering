import subprocess

processes = []

blender_path = "/home/ramon/blender/blender"  # Update this to your exact path

for i in range(1):
    for j in range(1):  # parallel processes
        p = subprocess.Popen(
            [blender_path, "--background", "--python", "test.py"])
        processes.append(p)
    for p in processes:
        p.wait()


# p = subprocess.Popen(
#             ["python3", "upload.py"])

# p.wait()