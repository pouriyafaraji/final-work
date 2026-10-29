# Persian Emotional TTS

## Conda setup on Windows and Linux

On Windows, run these commands in **Anaconda Prompt** or **Miniconda Prompt**.
On Linux, use a terminal where Conda is initialized.

### 1. Create the environment with Python 3.10

```bash
conda create --name emotional_tts python=3.10 -y
```

### 2. Activate the environment

```bash
conda activate emotional_tts
```

The following installation and verification commands must be run while this
environment is active.

### 3. Install PyTorch, Torchaudio, and Torchvision with CUDA 12.1

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia -y
```

A compatible NVIDIA driver is required. Installing the full CUDA Toolkit
separately is not necessary for these Conda packages.

### 4. Install the other required libraries

```bash
conda install -c conda-forge transformers datasets librosa soundfile numpy matplotlib tensorboard -y
```

### 5. Create the project directories

From the project root, run:

```bash
python scripts/create_project_dirs.py
```

The script uses the project root rather than the current working directory, so
it can also be invoked from another directory. It creates:

```text
data/raw/
data/processed/
models/acoustic/
models/emotion_extractor/
models/vocoder/
configs/
```

It is safe to run the script more than once; existing directories are kept.

### 6. Verify PyTorch and GPU detection

```bash
python -c "import torch; print('PyTorch:', torch.__version__); print('PyTorch CUDA:', torch.version.cuda); print('CUDA available:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'Not detected')"
```

For the RTX 4060, `CUDA available` should print `True` and the GPU line should
show the graphics card name.

To deactivate the environment when finished:

```bash
conda deactivate
```
