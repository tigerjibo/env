$(info ******************************************)
$(info *****Auto Install and Configure software***)
$(info **Author :JiBo Email:jibo.tiger@gmail.com**)

all:
	@echo "Add nework agency and update..."
	sudo python prepare.py
	@echo "Install all software..."
	sudo python sudo.py
	@echo "Configure Software Environment.."
	python do.py
	sudo python sudo_env.py

