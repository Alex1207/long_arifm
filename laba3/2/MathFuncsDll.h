#ifdef MATHFUNCSDLL_EXPORTS
#define MATHFUNCSDLL_API __declspec(dllexport) 
#else
#define MATHFUNCSDLL_API __declspec(dllimport) 
#endif

namespace MathFuncs
{
    class LongInt
    {
	private:
		long size;
		bool minus;
		int *digits;
		bool TakeSize (char *flag, char *fname);
		bool ReadFile(char *flag, char *fname);
		void DelNull();
		bool More (LongInt a, LongInt b);
		bool Equally(LongInt a, LongInt b);
		LongInt Sum(LongInt a, LongInt b, LongInt &c);
		LongInt Sub(LongInt a, LongInt b, LongInt &c);
		LongInt Addition(LongInt a, LongInt b, LongInt &c);
		LongInt Mul(LongInt a, LongInt b, LongInt &c);
		void LightDiv(LongInt a, int b, LongInt q, int &r);
		void Div(LongInt a, LongInt b, LongInt &q, LongInt &r, LongInt c, LongInt m);
		void Division(LongInt a, LongInt b, LongInt &q, LongInt &r, LongInt c, LongInt m);
		LongInt DecToBin(LongInt a);
    public: 		
		LongInt();
		~LongInt();
		bool Read(char *flag, char *fname);
		bool operator>(const LongInt& B);
		bool operator<(const LongInt& B);
		bool operator>=(const LongInt& B);
		bool operator<=(const LongInt& B);
		bool operator==(const LongInt& B);
		bool operator!=(const LongInt& B);
		LongInt operator+(const LongInt& a);
		LongInt operator-(const LongInt& a);
		LongInt operator*(const LongInt& a);
		LongInt operator/(const LongInt& a);
		LongInt operator%(const LongInt& a);
		LongInt Pow (LongInt a, LongInt b, LongInt mod);
		void Print();
		bool CheckMinus();
		bool CheckSize();
		bool WriteFile (char *flag, char *fname);
    };
}