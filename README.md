        Recursive implementation of the Floyd Warshall Algorithm 

This project is to rewrite the Floyd Warshall Algorithm so it uses recursion; the function calls itself and updates the shortest paths between nodes. 
It is written in Python using Visual Code Studio, and source controled through GitHub:
https://github.com/jasonshhh/Mid-Module-Assessment

Unit tests and performance tests were conducted to ensure the functions did what they were supposed to, and comaprisons were made betweent imperative and recursive implementations of the algorithm.

            --------How to run the program--------

                 ---Running The Algorithm---

In the github url above, navigate to the 'code' tab and press the green code button. Hit 'download ZIP' and save the project into an appropriate directory and unzip the files.

Open command prompt (or other command line interface) and change directory to where the project is saved and move into the folder:
./floydWarshall

Enter the command:
py floyd_warshall_recursive.py

The above runs the recursive version of the algorithm, outputting a shortest path graph of the input matrix.

The output should be identical to the below matrix.

Following matrix shows the shortest distances between every pair of vertices
        0        7       12        8
  NO_PATH        0        5        7
  NO_PATH  NO_PATH        0        2
  NO_PATH  NO_PATH  NO_PATH        0

Enter the command:
py floyd_warshall_imperative.py

This runs the imperative version of the algorithm. Th output should be identical to the above.

The output should be identical to the below matrix.

Following matrix shows the shortest distances between every pair of vertices
        0        7       12        8
  NO_PATH        0        5        7
  NO_PATH  NO_PATH        0        2
  NO_PATH  NO_PATH  NO_PATH        0


            ---Running unit tests and performance tests---

You must insert the path to the root directory of the project into sys.path.insert()
at the top of the unittest_floyd.py and timeit_test.py

In the command line interface navigate to:

./tests

This folder contains unit tests and performance tests. 

Enter the command:
python -m unittest unittest_floyd.py

This runs various unit tests to confirm the functions are performing as expected.

Enter the command:
py timeit_test.py

This tests the time taken for the functions to run. It also compares the time between the 6 algorithm implentations.


                ---Changing the parameters---

The user is able to change the parameters by opening the files in an IDE and changing the 'graph'. Changing various parameters will lead to error messages or a successful operation. 

                    -------License-------

Copyright 2022 Jason Hadwen

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.