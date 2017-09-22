# Build btk (linux only)

1. download [btk source code](https://github.com/Biomechanical-ToolKit/BTKCore)
2. Modify the file b-tk.core/Wrapping/Python/CMakeLists.txt
    In line 23 it says: SET(CMAKE_SWIG_FLAGS "")
    and should read SET(CMAKE_SWIG_FLAGS "-py3")
3. configure and generate with cmake-gui (*without bindings*)
4. install with `sudo make install`
5. return in cmake-gui and add the following entries:
  1. `NUMPY_VERSION` (string): current version
  2. `NUMPY_INCLUDE_DIR` (path): poiting to `/home/romain/anaconda3/lib/python3.6/site-packages/numpy/core/include`
6. build again
7. copy all the files in bin directory to  `/home/romain/anaconda3/lib/python3.6/site-packages/btk`
8. rename `btk.py` to `init.py`
