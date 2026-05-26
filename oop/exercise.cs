using System;
using System.Collections.Generic;

namespace OOP_in_Csharp
{
    class Student
    {
        private string _name;
        private string _idnumber;
        private string _faculty;
        private static int _counter = 0;
        
        public Student(string bn, string id, string fa)
        {
            this._name = bn;
            this._idnumber = id;
            this._faculty = fa;

            _counter++;
        }
        public Student()
        {
            _counter++;
        }
        public static int getStudNum()
        {
            return _counter;
        }
        
        // Properties
        public string Name
        {
            get { return this._name; }
            set { this._name = value; }
        }
        public string IDNumber
        {
            get { return this._idnumber; }
            set { this._idnumber = value; }
        }

        public string Faculty
        {
            get { return this._faculty; }
            set { this._faculty = value; }
        }

        public static string getNum()
        {
            Random random = new Random();
            int num;
            num = random.Next(2, 99);
            return num.ToString();
        }
        
        public void StartStudent()
        {
            IDNumber = "k000" + getNum();
        }

        public virtual void StartRegistration(string addr1, string addr2)
        {
            IDNumber = "k000" + addr1 + addr2;
        }

        public void generateIdSuffixes(List<string> id2, int N)
        {
            int count = 0;
            string piece = "";
            
            while(count < N) 
            {
                piece = getNum();
                if(id2.Contains(piece) == false)
                {
                    id2.Add(piece);
                    count++;
                }
            }
        }
    }
    
    // Mezun / Yüksek Lisans Öğrencisi Sınıfı
    class GraduateStudent : Student 
    {
        public GraduateStudent(string bn, string id, string fa, string graduateStatus) : base(bn, id, fa)
        {
            this.Graduate = graduateStatus;
        }

        public GraduateStudent() { }
       
        protected string graduate;
        public string Graduate
		{
			get { return graduate;  }
			set { graduate = value; }
		}

        public override void StartRegistration(string addr1, string addr2)
        {
            IDNumber = "k00300" + addr1 + "." + addr2;
        }
    }
    
    class Program
    {
        static void StudentFinish(List<Student> myClass, string studentName)
        {
            for (int i = 0; i < myClass.Count; i++)
            {
                if (myClass[i].Name == studentName)
                {
                    myClass.RemoveAt(i);
                }
            }
        }

        public static void Main(string[] args)
        {
            List<Student> studentList = new List<Student>();
            
            // 1. MEZUN ÖĞRENCİ: Listenin başına gelmesi için ilk sırada oluşturup ekliyoruz
            Student gradStudent = new GraduateStudent();
            gradStudent.Name = "MezunOgrenci";
            gradStudent.IDNumber = "k00300"; // Mezun özel numarası
            gradStudent.Faculty = "Engineering"; 

            const int numStudents = 5;

            List<string> id2 = new List<string>();
            gradStudent.generateIdSuffixes(id2, numStudents - 1);
            
            foreach(string id in id2)
            {
                Console.Write(id + ", ");
            }
            Console.WriteLine("");
            
            // Mezun öğrenciyi listeye 0. indeksten (en baştan) ekledik
            studentList.Add(gradStudent);

            // 2. LİSANS ÖĞRENCİLERİ: Döngüyle listeye arkasından ekleniyorlar
            for (int i = 1; i < numStudents; i++)
            {
                Student stud = new Student("Lisans" + i.ToString(), "", "Engineering");
                studentList.Add(stud);
            }

            int last;
            string piece;
            // Diğer lisans öğrencilerine numara atama döngüsü
            for (int i = 1; i < studentList.Count; i++)
            {
                last = id2.Count - 1;
                piece = id2[last];
                
                // İSTEDİĞİN DEĞİŞİKLİK: Diğer öğrenciler k000 formatında oluyor
                studentList[i].IDNumber = "k000" + piece; 
                
                id2.RemoveAt(last);
                Console.WriteLine("{0} {1}", studentList[i].Name, studentList[i].IDNumber);
            }

            Console.WriteLine("------------");
            Console.WriteLine("TÜM SINIF LİSTESİ (Mezun En Başta):");
            Console.WriteLine("------------");

            // Çıktıda Mezun en başta, lisanslar k000 ile arkasında listelenir
            foreach (Student stud in studentList)
            {
                Console.WriteLine("{0} {1}", stud.Name, stud.IDNumber);
            }
            Console.WriteLine("\nWe have {0} Students.", Student.getStudNum());
        }
    }
}