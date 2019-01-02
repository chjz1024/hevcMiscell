#pragma once
#include <cstdint>

class CABACTables
{
public:
	const static uint8_t LPSTable[64][4];
	const static uint8_t RenormTable[32];
};
