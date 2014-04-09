$(info ******************************************)
$(info *****Auto Install and Configure software***)
$(info **Author :JiBo Email:jibo.tiger@gmail.com**)
PASSWD:=88249218

all: agency_update install env

agency_update:
	@echo "Add nework agency and update..."
	echo ${PASSWD} | sudo -S python prepare.py
install:
	@echo "Install all software..."
	sudo python sudo.py
env:
	@echo "Configure Software Environment.."
	python do.py
	echo ${PASSWD} | sudo -S python sudo_env.py
clean:
	rm -rf *.pyc
