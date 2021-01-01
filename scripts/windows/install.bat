@REM You must have Anaconda installed and activated for this to work

cd ../../ && conda env create -f environment.yml python=3.7
conda activate credential-saver && cd scripts/windows && setup.bat