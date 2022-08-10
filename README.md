# InstallLibtorch
This is a tool that can seteup libtorch. Libtorch is C++ interface of Pytorch that is a machine learning framework for Python. We can use libtorch to develop machine learning applications in C++, like using Pytorch in Python.

## Usage
This repository uses makefile to generate `.pc` file and install libtorch. The libtorch will be install to `/opt`. The `.pc` file offers some information for the command `pkg-config` to get the include path and the path of the library files. Therefore, you must install `pkg-config` before using the makefile of this repository.

You can use these commands to install `pkg-config`:
```bash
sudo apt-get updatte
sudo apt-get upgrade
sudo apt-get install pkg-config
```

The command `pkg-config` need the enviroment variable `PKG_CONFIG` to get `.pc` file. You can use command to test:
```bash
echo ${PKG_CONFIG}
```

If you don't get any response, you must use the command to add the enviroment variable into `.bashrc`:
```bash
echo "PKG_CONFIG=/usr/lib/pkgconfig" >> ~/.bashrc
```

Now, we discuss the usage of the makefile for this repository. If you want to install libtorch, you can use this command:
```bash
sudo make install Path=~
```
where `Path` is to set the path that is the location for the directory `libtorch`.

You can use the command to uninstall libtorch:
```bash
sudo make uninstall
```

## Setup
You can follow bellow to setup libtorch:
1. If you want to use GPU, you must install GPU driver, CUDA and cuDNN. If you don't want to use GPU, skip this step.
2. Download [libtorch](https://pytorch.org/get-started/locally/) according to your requirement. Note, You must select `Libtorch` in the Package and `C++/Java` to get libtorch for C++. For example, we want to get CPU version libtorch, and then download to `~`:
    ```bash
    cd ~
    wget https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-1.12.1%2Bcpu.zip 
    ```
3. Unzip the compressed file.
    ```bash
    unzip libtorch-cxx11-abi-shared-with-deps-1.12.1+cpu.zip
    ```
4. Change the current dirctory to this repository, and then use the commad to setup libtorch:
    ```bash
    sudo make install Path=~
    ```

You can use this command to get the include path:
```bash
pkg-config --cflags libtorch
```

You can get the library files via the command:
```bash
pkg-config --libs libtorch
```

If the two command can return information, You succeed to install libtorch. Now, you can use the command `pkg-config` and makefile to develop machine learning applications with libtorch. Good luck!