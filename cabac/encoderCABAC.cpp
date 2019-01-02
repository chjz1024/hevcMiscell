#include "encoderCABAC.h"
#include "CABACTables.h"

void encoderCABAC::start()
{
  uiLow = 0;
  uiRange = 510;
  bufferedByte = 0xff;

  bitsLeft = 23;
  numBufferedBytes = 0;
}

void encoderCABAC::finish()
{
  uint32_t interVar;
  if (uiLow >> (32 - bitsLeft))
  {
    interVar = bufferedByte + 1;
    fout.write((char *)&interVar, 1);
    interVar = 0;
    while (numBufferedBytes > 1)
    {
      fout.write((char *)&interVar, 1);
      numBufferedBytes--;
    }
    uiLow -= 1 << (32 - bitsLeft);
  }
  else
  {
    if(numBufferedBytes>0)
    {
      fout.write((char *)&bufferedByte, 1);
    }
    interVar = 0xff;
    while(numBufferedBytes>1)
    {
      fout.write((char *)&interVar, 1);
      numBufferedBytes--;
    }
  }
  interVar = uiLow >> 8;
  fout.write((char *)&interVar, (24 - bitsLeft) / 8);
}


void encoderCABAC::encodeBin(uint32_t binValue, ContextModel &rcCtxModel)
{
  uiBinsCoded += binCountIncrement;
  rcCtxModel.setBinsCoded(1);

  uint32_t uiLPS = CABACTables::LPSTable[rcCtxModel.getState()][(uiRange >> 6) & 3];
  uiRange -= uiLPS;

  if (binValue != rcCtxModel.getMps())
  {
    int numBits = CABACTables::RenormTable[uiLPS >> 3];
    uiLow = (uiLow + uiRange) << numBits;
    uiRange = uiLPS << numBits;
    rcCtxModel.updateLPS();
    bitsLeft -= numBits;
    testAndWriteOut();
  }
  else
  {
    rcCtxModel.updateMPS();
    if (uiRange < 256)
    {
      uiLow <<= 1;
      uiRange <<= 1;
      bitsLeft--;
      testAndWriteOut();
    }
  }
}

void encoderCABAC::testAndWriteOut()
{
  if (bitsLeft < 12)
  {
    writeOut();
  }
}


void encoderCABAC::writeOut()
{
  uint32_t leadByte = uiLow >> (24 - bitsLeft);
  bitsLeft += 8;
  uiLow &= 0xffffffffu >> bitsLeft;

  if (leadByte == 0xff)
  {
    numBufferedBytes++;
  }
  else
  {
    if (numBufferedBytes > 0)
    {
      uint32_t carry = leadByte >> 8;
      uint32_t byte = bufferedByte + carry;
      bufferedByte = leadByte & 0xff;
      fout.write((char *)&byte, 1);

      byte = (0xff + carry) & 0xff;
      while (numBufferedBytes > 1)
      {
        fout.write((char*)&byte, 1);
        numBufferedBytes--;
      }
    }
    else
    {
      numBufferedBytes = 1;
      bufferedByte = leadByte;
    }
  }
}

void encoderCABAC::run(int32_t qp, int32_t initValue)
{
  char buff;
  ContextModel ctx;
  ctx.init(qp, initValue);
  start();
  while(fin.read(&buff,1))
  {
    for(int i = 0; i < 8; i++)
    {
      encodeBin((buff >> (7 - i)) & 1, ctx);
     // encodeBin(0, ctx);
    }
  }
  finish();
}