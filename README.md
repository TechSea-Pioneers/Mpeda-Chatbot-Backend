# Mpeda-backend

To install llama_index for mac user :
CMAKE_ARGS="-DLLAMA_METAL=on" pip install -U llama-cpp-python --no-cache-dir
pip install 'llama-cpp-python[server]'

<br>
 To install llama_index for linux/mac user :

CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python

please run the main.py file to run the server. the api will be there, the api is not dynamic as it is tunneled. 
