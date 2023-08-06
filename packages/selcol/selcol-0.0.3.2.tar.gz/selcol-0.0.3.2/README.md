## cpp
Build `onnxruntime` following the instruction in https://onnxruntime.ai/docs/build/inferencing.html
For example, if you use Linux,
```bash
git clone --recursive https://github.com/Microsoft/onnxruntime.git
cd onnxruntime
./build.sh --config RelWithDebInfo --build_shared_lib --parallel
cd build/Linux/RelWithDebInfo
sudo make install
```


Then build the example
```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib  # if /usr/local/lib is not in search path
g++ cpp_example/main.cpp $(pkg-config --cflags --libs libonnxruntime)
```
