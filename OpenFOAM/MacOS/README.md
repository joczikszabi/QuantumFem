# Docker for Mac
* Click on the Docker.app to start Docker. The Docker whale in the top status bar indicates Docker is running.
* Download the following scripts and put them in a local directory, e.g. your home directory
  - [installMacOpenFOAM](https://sourceforg.net/projects/openfoam/files/v2012/installMacOpenFOAM)
  - [startMacOpenFOAM](https://sourceforge.net/projects/openfoam/files/v2012/startMacOpenFOAM)
* Open the command line terminal and make the scripts executable
```bash
chmod +x installMacOpenFOAM
chmod +x startMacOpenFOAM
```
* Install OpenFOAM using:
```bash
./startMacOpenFOAM
```
* This will open a new terminal with OpenFOAM environment fully installed. Note the script allows you to login as user called ofuser and mount your home directory.
```bash
cd /home/ofuser/workingDir
cp -r $FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity .
cd cavity
blockMesh
icoFoam
```
