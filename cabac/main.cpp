#include <iostream>
#include <fstream>
#include "encoderCABAC.h"
int main(int argc, char const *argv[])
{
  encoderCABAC enc,enc2("in.dat","out2.dat");
  enc.run(0,0);
  enc2.run(30, 60);

  std::ifstream fin1("out.dat");
  std::ifstream fin2("out2.dat");
  char in1, in2;
  while (fin1.read(&in1, 1) && fin2.read(&in2, 1))
  {
    if(in1!=in2)
    {
      std::cout << "not equal" << std::endl; // right
      break;
    }
  }
  std::cin.get();
  return 0;
}