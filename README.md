# Hands-on Gravitational-Wave Data Analysis 

**Please complete Steps 1–5 *before* the workshop.** In particular, download the strain data in advance. You will need an internet connection for initial software installation and data download, but Notebook 1 reads the downloaded data locally. The hands-on exercises will be provided as Jupyter notebooks (`.ipynb` files).

## 1. Install Miniconda

Conda manages the Python version and scientific software needed for this workshop. If you already have **Miniconda, Anaconda, or Miniforge**, you can use your existing installation and skip this step.

1. Check whether Conda is installed by opening a terminal and running:

   ```bash
   conda --version
   ```

2. If the command is not found, download **Miniconda** from the [official Miniconda installation page](https://www.anaconda.com/docs/getting-started/miniconda/install). Select the installer for your operating system (Windows, macOS Intel/Apple Silicon, or Linux) and follow its instructions.
3. Restart the terminal after installation, then check `conda --version` again.

**Which terminal?** On Windows, open *Anaconda Prompt* (or *Miniconda Prompt*) from the Start menu. On macOS or Linux, open your normal *Terminal*.

> **Windows compatibility note:** PyCBC and its low-level gravitational-wave frame dependencies are generally easier to install under Linux. If environment creation fails on native Windows, use [Windows Subsystem for Linux (WSL2)](https://learn.microsoft.com/en-us/windows/wsl/install) with an Ubuntu distribution and install Miniconda **inside WSL**; then follow the Linux instructions here. VS Code can connect to WSL through its [WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl).

## 2. Clone the repository

```bash
git clone https://github.com/abhishek-sharma9/GWDA_workshop.git
cd GWDA_workshop
```

## 3. Create and activate the Conda environment

Run the following commands **from the repository folder**, where `environment.yaml` is located:

```bash
conda env create -f environment.yaml
```
Activate the env:

```bash
conda activate gw-workshop
```

This installs Python, PyCBC, LALSuite, GWpy, GWOSC tools, NumPy, SciPy, Matplotlib, and Jupyter. The initial installation may take some time, depending on internet speed and your platform.

Verify the installation:

```bash
python -c "import pycbc, gwpy, lal, lalsimulation, numpy, scipy, matplotlib; from pycbc.frame import read_frame, write_frame; print('GW workshop environment: OK')"
```

If you see `GW workshop environment: OK`, the key Python imports succeeded.

## 4. Build a jupyter kernel following the command:

```bash
python -m ipykernel install --user --name gw-workshop --display-name "gw-workshop"
```

## 5. Download the required GW frame files

With `gw-workshop` activated and while in the repository root, run:

```bash
python download_data.py
```

## 6. Start the jupyter lab/notebook server

From the repository root, with the environment activated, run:

```bash
jupyter lab
```

A browser window should open. Browse to `notebooks/` and open `.ipynb` files. Run cells from top to bottom with **Shift+Enter**. If you are asked to choose a Python kernel, select the **gw-workshop** environment.

For the classic Notebook interface, you can instead run:

```bash
jupyter notebook
```
To stop JupyterLab or Jupyter Notebook, return to the terminal and press **Ctrl+C**.

**Using VS Code:** Open the repository folder in VS Code, open the `.ipynb` file, click **Select Kernel** (upper right), and choose the Python interpreter from the `gw-workshop` Conda environment. Install the Python and Jupyter VS Code extensions if prompted.

## Additional resources

- [Gravitational Wave Open Science Center (GWOSC)](https://gwosc.org/)
- [PyCBC documentation](https://pycbc.org/pycbc/latest/html/)
- [GWpy documentation](https://gwpy.github.io/docs/stable/)
- [GW Open Data Workshop](https://github.com/rishn/GW-Open-Data-Workshop)
- [PyCBC tutorials](https://github.com/gwastro/PyCBC-Tutorials)

**For participants:** Please complete the installation, environment creation, and download the data before the session. Bring your laptop and charger.
