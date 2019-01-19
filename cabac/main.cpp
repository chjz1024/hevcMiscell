#include <iostream>
#include <fstream>
#include "encoderCABAC.h"
#include <ctime>
int main(int argc, char const *argv[])
{
  encoderCABAC enc;
  auto start = clock();
  enc.run(0,0);
  auto end = clock();
  double dur = (double)(end-start)/CLOCKS_PER_SEC;
  std::cout << "Total time:" << dur << std::endl;
  return 0;
}