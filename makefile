Path = 

Install_Dir = /opt

Pkg_Config := /usr/lib/pkgconfig

.PHONY= install uninstall all

all:
	echo ${PKG_CONFIG}

install:
	python3 python/generatePkgConfig.py -i ${Path} -o .
	sudo cp libtorch.pc $(Pkg_Config)
	sudo cp ${Path}/libtorch ${Install_Dir}
	sudo  echo "/opt/libtorch/lib" >> /etc/ld.so.conf
	sudo ldconfig -v

uninstall:
	sudo rm $(Pkg_Config)/libtorch.pc
	sudo rm -rf ${Install_Dir}/libtorch
	sudo sed -i '/libtorch/d' /etc/ld.so.conf
	sudo ldconfig -v
