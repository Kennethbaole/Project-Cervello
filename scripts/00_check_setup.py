import sys
import platform

print("Python:", sys.version.split()[0], "| OS:", platform.system())

try:
    import mne
    print("MNE:", mne.__version__)
    print("\n--- mne.sys_info() ---")
    mne.sys_info()
except Exception as e:
    print("MNE import failed:", e)

try:
    import matplotlib
    print("\nMatplotlib backend:", matplotlib.get_backend())
except Exception as e:
    print("Matplotlib import failed:", e)