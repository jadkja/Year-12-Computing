import os
import subprocess
import sys

def install_pip():
    """Ensures pip is installed and up to date."""
    try:
        subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    except subprocess.CalledProcessError:
        print("Failed to install or upgrade pip. Check your Python installation.")

def install_requirements():
    """Installs the necessary Python packages, including tkinter."""
    required_packages = ["pillow"] # Add any other packages here.

    try:
        # Check if tkinter is already installed (usually part of standard library)
        try:
            import tkinter
            print("tkinter is already installed.")
        except ImportError:
            print("tkinter not found, attempting to verify...")
            # Tkinter is usually part of the standard library, but on some systems
            # it might have been removed or have issues.
            if sys.platform.startswith('darwin'):
                # Tkinter should be included with Python on macOS
                print("tkinter should be included with Python on macOS. If you're having issues, please reinstall Python.")
            elif sys.platform.startswith('win'):
                # Tkinter is included with Python on Windows
                print("tkinter is included with Python on Windows. If you're having issues, please reinstall Python.")
            else:
                print(f"Unknown operating system: {sys.platform}. Please ensure tkinter is installed or reinstall Python.")

        # Install other pip packages
        subprocess.run([sys.executable, "-m", "pip", "install"] + required_packages, check=True)
        print("All dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install required packages.")

if __name__ == "__main__":
    install_pip()
    install_requirements()
