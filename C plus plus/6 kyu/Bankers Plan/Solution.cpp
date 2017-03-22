using namespace std;

#include <string>

class BankerPlan
{
public:
    static bool fortune(int f0, double p, int c0, int n, double i);
    static int calculateFortune(const int &, const double &, const int &);
    static int calculateYearlyWithdraw(const int &, const double &);
};

bool BankerPlan::fortune(int f0, double p, int c0, int n, double i){
  int count = 0, fortune = f0, yearlyWithdraw = c0;
  double interestRate = (p/100), inflation = (i/100);  

  while(fortune > 0){
    fortune = calculateFortune(fortune, interestRate, yearlyWithdraw);
    yearlyWithdraw = calculateYearlyWithdraw(yearlyWithdraw, inflation);
    count++;
    if(count == n){
      return true;
    }
  }
  
  return false;
}

int BankerPlan::calculateFortune(const int &previousFortune, const double &interestRate, const int &yearlyWithdraw){
  return previousFortune + interestRate*previousFortune - yearlyWithdraw;
}

int BankerPlan::calculateYearlyWithdraw(const int &previousYearlyWithdraw, const double &inflation){
  return previousYearlyWithdraw + previousYearlyWithdraw*inflation;
}
