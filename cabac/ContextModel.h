#pragma once
#include <cstdint>
#include "CABACTables.h"

class ContextModel
{
private:
	uint8_t ucState;
	uint32_t binsCoded;

	static const uint8_t TransLPSTable[64 << 1];
	static const uint8_t TransMPSTable[64 << 1];
	static const int entropyBits[64 << 1];

public:
	ContextModel() { ucState = 0; binsCoded = 0; }
	~ContextModel() {}

	void init(int qp, int initValue);
	uint8_t getState() { return (ucState >> 1); }
	uint8_t getMps() { return (ucState & 1); }
	void setStateAndMps(uint8_t state, uint8_t MPS) { ucState = (state << 1) + MPS; }

	void updateMPS() { ucState = TransMPSTable[ucState]; }
	void updateLPS() { ucState = TransLPSTable[ucState]; }

	static int getEntropyBitsTrm(int val) { return entropyBits[126 ^ val]; }

	void setBinsCoded(uint32_t val) { binsCoded = val; }
};
