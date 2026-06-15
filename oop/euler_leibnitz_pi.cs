using System;
class FindingPi {
     static double leibnitz(int rep)
   {
    double term = 1;   
    double total = 0;
    int sign = -1;
    
    for(int i=1; i<rep; i+=2 )
    {
        sign*=-1;
        term= 1.0*sign*1/i;
        total += term;
    }    
     
     return 4*total;
   }
   
   
    static double euler(int rep)
   {
    double term = 1;   
    double total = 0;
    
    for(int i=1; i<rep; i++ )
    {
        term= 1.0*1/(i*i);
        total += term;
    }    
     return Math.Sqrt(total * 6);
   }
    static void Main() {
        int rep = 10000;
        double pi = 3.141592653589793238;
    
    Console.WriteLine("rep {0} Leibnitz  {1} the difference {2}", rep , leibnitz(rep), pi - leibnitz(rep));
    Console.WriteLine("rep {0} Euler  {1} the difference {2}", rep , euler(rep), pi - euler(rep));
  }
}