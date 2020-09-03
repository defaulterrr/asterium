all: 
	g++-10 main.cpp -o ./app.out
	./app.out

clean: 
	rm -rf ./app.out