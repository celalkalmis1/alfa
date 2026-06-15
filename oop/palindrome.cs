using System;
class PrimeFactors {
    
    static bool poli(int num)
    {
    string textNum = num.ToString();
    bool is_poli = true;
    for (int i=0; i<textNum.Length/2;i++)
        if (textNum[i] != textNum[textNum.Length-1-i])
        {
            is_poli = false;
            break;
        }    
    return is_poli;
    }

      static void Main() {
       
       for(int i =1; i<1000;i++)
       {
           for(int j=1; j<1000; j++ )
           {
              int num = i*j;
               if(poli(num))
               {
               Console.WriteLine(num +"   "+ poli(num));               
               }
           }           
       }
       
     }
    
}