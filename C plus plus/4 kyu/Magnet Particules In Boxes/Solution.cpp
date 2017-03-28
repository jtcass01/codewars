#include <cmath>

class Magnets
{
public:
    static double doubles(const int &, const int &);
    static double boxForce(const int &, const int &);
};

double Magnets::doubles(const int &maxk, const int &maxn){
  double sum = 0;
  
  for(unsigned int k = 1; k <= maxk; k++){
    for(unsigned int n = 1; n <= maxn; n++){
      sum += boxForce(k,n);
    }
  }
  
  return sum;
}

double Magnets::boxForce(const int &k, const int &n){
  return 1 / (double(k)*pow(double(n)+1, 2*double(k)));
}
