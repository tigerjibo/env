$(info ******************************************)
$(info *****Auto Install and Configure software***)
$(info **Author :JiBo Email:jibo.tiger@gmail.com**)

all: agency_update install env

agency_update:
	@echo "Add nework agency and update..."
	sudo python prepare.py
install:
	@echo "Install all software..."
	sudo python sudo.py
env:
	@echo "Configure Software Environment.."
	python do.py
	sudo python sudo_env.py
clean:
	rm -rf *.pyc
