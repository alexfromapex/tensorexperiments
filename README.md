# What is this repo?

- Quick start boilerplate for working with Tensorflow on Macbook Air M1 (ARM-64 architecture)
- Uses Metal to access the GPU capabilities within Tensorflow
- Doesn't require Conda / Miniforge
- Works with Python 3.8
- Dependencies installed via Pyenv and Poetry

# Before doing anything else

- Install Homebrew
- Run `brew install hdf5 pyenv pyenv-virtualenv`
- Run `export HDF5_DIR="$(brew --prefix hdf5)";`
- Add the following lines to your `~/.zprofile` file if using Zsh or `~/.bash_profile` file if using Bash (you can check Zsh vs Bash by typing `echo $SHELL` in your terminal):

```
    export PATH="$HOME/.poetry/bin:$PATH";
    export PYENV_VIRTUALENV_DISABLE_PROMPT=0;
    eval "$(pyenv init -)";
    eval "$(pyenv virtualenv-init -)";
```

- Restart your terminal or reload the profile, e.g. `source ~/.zprofile` or `source ~/.bash_profile`
- Install Poetry, by running `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
- Install Python 3.8 into Pyenv, by running `pyenv install 3.8.10`
- Create a Pyenv virtual environment to work in, by running `pyenv virtualenv 3.8.10 tfexperiment`
- Activate the Pyenv virtual environment, by running `pyenv activate 3.8.10/envs/tfexperiment`
- Check that `python --version` says `3.8.10` and `which python` says something like `/Users/.../.pyenv/shims/python`
- Finally, `cd` to the directory with the `pyproject.toml` file, then run `poetry install`

# Getting Started

- After following steps above in "Before anything else" section, running `poetry run tf` should execute the code in `src/tf.py`

# Troubleshooting

- H5Py
    - If you have an issue with H5Py, install with `pip install --no-binary=h5py h5py`