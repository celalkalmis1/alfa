using System;
using System.Linq;
using System.Collections.Generic;
using System.IO; // Dosya yazma işlemleri için eklendi

// LINQ Query Syntax examples

public class Program
{
    public static void Main()
    {
        // Student collection
        List<Student> students = new List<Student>() { 
                new Student() { Name = "Zbych", Marks = 13, Faculty = "Informatics"} ,
                new Student() { Name = "John", Marks = 11, Faculty = "Informatics"} ,
                new Student() { Name = "Ala", Marks = 12, Faculty = "Mathematics" } ,
                new Student() { Name = "Ola", Marks = 9, Faculty = "Informatics" } ,
                new Student() { Name = "Ela", Marks = 4, Faculty = "Mathematics"} ,
                new Student() { Name = "Ula", Marks = 10, Faculty = "Informatics" }, 
                new Student() { Name = "Rick", Marks = 12, Faculty = "Medicine" },
                new Student() { Name = "Henek", Marks = 10, Faculty = "Mathematics" },
                new Student() { Name = "Basia", Marks = 14, Faculty = "Medicine" },
                new Student() { Name = "Anna", Marks = 11, Faculty = "Mathematics" },
                new Student() { Name = "Fred", Marks = 5, Faculty = "Informatics" },
                new Student() { Name = "Beata", Marks = 9, Faculty = "Psychology" }
            };
        
        string filePath = "StudentReport.txt"; // Oluşturulacak dosyanın adı

        // StreamWriter kullanarak dosyayı oluşturup içine yazıyoruz
        using (StreamWriter writer = new StreamWriter(filePath))
        {
            var result = from s in students
                         where s.Marks < 9 
                         select s;
                         
            writer.WriteLine("(Ex 1.) Candidates that can not be enrolled (too few scores):");
                          
            foreach(Student stud in result){            
                writer.WriteLine(stud.Name + " - " + stud.Marks + " - " + stud.Faculty );
            }
            
            var result1 = from s in students
                          where s.Marks > 9 && s.Faculty == "Informatics" 
                          orderby s.Name 
                          select s;
            
            writer.WriteLine("----------------------------------------");
            writer.WriteLine("(Ex 2.) Candidates enrolled to Informatics:");                    
            foreach(Student stud1 in result1){          
                writer.WriteLine(stud1.Name + " - " + stud1.Marks + " - " + stud1.Faculty );
            }
            
            writer.WriteLine("----------------------------------------");
            var avgMarks = students.Average(s => s.Marks);  
            writer.WriteLine($"(Ex 3.) Average for all Candidates is {avgMarks}. ");  
            
            writer.WriteLine("----------------------------------------");
            writer.WriteLine("(Ex 4.) Candidates by faculties:");
            
            var result2 = from s in students
                          orderby s.Marks descending
                          group s by s.Faculty;

            //iterate each group        
            foreach (var faculty in result2)
            {
                writer.WriteLine("");   
                writer.WriteLine("{0}:", faculty.Key); //Each group has a key 
                
                foreach(Student s in faculty) // Each group has inner collection
                    writer.WriteLine("{0} \t  {1}", s.Name, s.Marks);
            }
            
            writer.WriteLine("----------------------------------------");
            writer.WriteLine("(Ex 5.) Average for all faculties:");
            
            var result3 = 
                from s in students 
                group s by s.Faculty into groups 
                select new 
                { 
                    Faculty = groups.Key, 
                    AverageMarks = groups.Average(s => s.Marks), 
                };
                
            foreach (var faculty in result3)
             {
                 writer.WriteLine("{0} \t  {1}", faculty.Faculty, faculty.AverageMarks);
             }
        } // using bloğu burada biter, dosya otomatik olarak kapatılır ve kaydedilir.

        // İşlem bittiğinde konsola bilgi veriyoruz
        Console.WriteLine($"İşlem tamamlandı! Sonuçlar '{filePath}' adlı dosyaya yazdırıldı.");
    }
}

public class Student{
    public int ID { get; set; }
    public string Name { get; set; }
    public int Marks { get; set; }
    public string Faculty { get; set; }
}