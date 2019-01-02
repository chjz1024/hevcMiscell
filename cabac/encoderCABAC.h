#pragma once
#include <cstdint>
#include <fstream>
#include "ContextModel.h"

class encoderCABAC
{
private:
  uint32_t uiLow;
  uint32_t uiRange;
  uint32_t bufferedByte;

  uint32_t uiBinsCoded;
  int32_t binCountIncrement;
  int32_t bitsLeft;
  int32_t numBufferedBytes;

public:
  encoderCABAC(const char *in = "in.dat", const char *out = "out.dat") :fin(in, std::fstream::in | std::fstream::binary
  ), fout(out, std::fstream::out | std::fstream::binary) {}
  virtual ~encoderCABAC() {}
  void init() {}
  void start();
  void finish();
  void encodeBin(uint32_t binValue, ContextModel &rcCtxModel);
  void testAndWriteOut();

  //user defined section
private:
  void writeOut();
  std::ifstream fin;
  std::ofstream fout;
public:
  void run(int32_t qp, int32_t initValue);
};
