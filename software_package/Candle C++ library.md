# CANdle C++ library 

CANdle C++ library is the base module of software that all other modules are based on. It takes care of low-level communication between the host and the MD80 controllers. Using the CANdle C++ library directly is the best option to reach the full performance of the drives when it comes to communication frequency between the host and MD80 controllers. 

## Quick start

The quick startup guide includes cloning the repo, building and running the examples. First, you should clone the candle repo from the MAB Robotics GitHub page to your local machine. Then, make sure you're in the main directory candle/ and run the following commands:
```
mkdir build
cd build
cmake ..
make 
```
starting from the top one these commands: create a build directory, go into the build directory, generate makefiles using CMake and compile the source code using make. After executing these commands you should be able to see the compiled examples in the candle/build/ directory. To run one of them use the following command:
```
./exampleX 
```
where X is the number of the example. 

## Building as a static lib

Candle C++ library can be built as a static or shared object library. In the quick startup guide, we used the default settings, thus the library was compiled to a shared object file. In case you’d like to build it for a static lib you should pass additional arguments to the cmake .. command:
```
cmake .. -DCANDLE_BUILD_STATIC=TRUE
```
After executing this command you should be able to see the following CMake output:

```{figure} ./images/candle_build_static.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```

In case you’d like to go back to shared lib just call: 
```
cmake .. -DCANDLE_BUILD_STATIC=FALSE
```
or delete the build directory contents and call cmake .. again (the default library type is shared). This is what the cmake output looks like when reconfiguring for shared lib: 
```{figure} ./images/candle_build_shared.png
:alt: candle
:class: bg-primary mb-1
:align: center
:class: no-scaled-link
```