all:
	@python logistic_regression.py
	@gcc main.c logistic_regression.c
	@echo Done !

clean:
    @rm -rf *.c *.exe