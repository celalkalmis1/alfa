using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace SchoolSystemApp
{
    abstract class Person
    {
        private string fullName;
        private int age;

        public string FullName
        {
            get { return fullName; }
            set { fullName = value; }
        }

        public int Age
        {
            get { return age; }
            set { age = value; }
        }

        public abstract string Info();
    }

    class Student : Person
    {
        private string studentId;
        private string department;
        private int score;
        private static int totalStudents = 0;
        private static Random randomGenerator = new Random();

        public Student(string name, int age, string id, string dept)
        {
            FullName = name;
            Age = age;
            studentId = id;
            department = dept;
            score = randomGenerator.Next(4, 16);
            totalStudents++;
        }

        public Student()
        {
            this.department = GetRandomDepartment();
            this.score = randomGenerator.Next(4, 16);
            this.Age = randomGenerator.Next(18, 30);
            totalStudents++;
        }

        public static int GetStudentCount()
        {
            return totalStudents;
        }

        public string StudentId
        {
            get { return studentId; }
            set { studentId = value; }
        }

        public string Department
        {
            get { return department; }
            set { department = value; }
        }

        public int Score
        {
            get { return score; }
            set { score = value; }
        }

        public override string Info()
        {
            return $"name {FullName} , age {Age} , faculty {Department}";
        }

        public static string GenerateIdSuffix()
        {
            return randomGenerator.Next(100, 999).ToString();
        }

        public void CreateIdPool(List<string> pool, int size)
        {
            while (pool.Count < size)
            {
                string suffix = GenerateIdSuffix();
                if (!pool.Contains(suffix))
                {
                    pool.Add(suffix);
                }
            }
        }

        private string GetRandomDepartment()
        {
            string[] departments = { "Engineering", "Cloud Computing", "Business Admin", "Architecture" };
            int index = randomGenerator.Next(departments.Length);
            return departments[index];
        }
    }

    class Graduate : Student
    {
        private string degreeType;

        public Graduate(string name, int age, string id, string dept, string degree) : base(name, age, id, dept)
        {
            this.degreeType = degree;
        }

        public Graduate() : base()
        {
            this.degreeType = GetRandomDegree();
        }

        public string DegreeType
        {
            get { return degreeType; }
            set { degreeType = value; }
        }

        public override string Info()
        {
            return $"name {FullName} , age {Age} , faculty {Department} , graduated {DegreeType}";
        }

        private string GetRandomDegree()
        {
            string[] degrees = { "Master", "PhD" };
            Random rnd = new Random();
            int index = rnd.Next(degrees.Length);
            return degrees[index];
        }
    }

    class Program
    {
        public static void Main(string[] args)
        {
            List<Student> studentList = new List<Student>();

            Graduate serverNode = new Graduate();
            serverNode.FullName = "Graduate_Admin";
            serverNode.Age = 26;
            serverNode.StudentId = "k00000";
            serverNode.Department = "Computer Science";
            serverNode.Score = 15;

            int maxDevices = 10;
            List<string> idPool = new List<string>();

            serverNode.CreateIdPool(idPool, maxDevices - 1);
            studentList.Add(serverNode);

            for (int k = 1; k < maxDevices; k++)
            {
                Student temp = new Student();
                temp.FullName = "User_" + k;
                studentList.Add(temp);
            }

            for (int m = 1; m < studentList.Count; m++)
            {
                int lastIdx = idPool.Count - 1;
                string pickedValue = idPool[lastIdx];
                studentList[m].StudentId = "k00" + pickedValue;
                idPool.RemoveAt(lastIdx);
            }

            Console.WriteLine("--- School System Status ---");
            foreach (var s in studentList)
            {
                Console.WriteLine(s.Info());
            }
            Console.WriteLine("\nTotal Registered: " + Student.GetStudentCount());
            Console.WriteLine("\n======================================================\n");

            string filePath = "StudentReport.txt";

            using (StreamWriter writer = new StreamWriter(filePath))
            {
                writer.WriteLine("--- LINQ QUERIES REPORT ---");
                writer.WriteLine($"Date Generated: {DateTime.Now}\n");

                writer.WriteLine("(Ex 1.) Candidates that can not be enrolled (Score < 10):");
                var failedStudents = studentList.Where(s => s.Score < 10);
                foreach (var s in failedStudents)
                {
                    writer.WriteLine($"{s.FullName} - {s.Score} - {s.Department}");
                }
                writer.WriteLine("----------------------------------------");

                writer.WriteLine("(Ex 2.) Candidates enrolled in Engineering (Score >= 10):");
                var engineeringStudents = studentList.Where(s => s.Department == "Engineering" && s.Score >= 10);
                foreach (var s in engineeringStudents)
                {
                    writer.WriteLine($"{s.FullName} - {s.Score} - {s.Department}");
                }
                writer.WriteLine("----------------------------------------");

                double totalAverage = studentList.Average(s => s.Score);
                writer.WriteLine($"(Ex 3.) Average score for all Candidates is: {totalAverage:F2}");
                writer.WriteLine("----------------------------------------");

                writer.WriteLine("(Ex 4.) Candidates by departments (Highest score first):");
                var orderedStudents = studentList.OrderBy(s => s.Department).ThenByDescending(s => s.Score);
                foreach (var s in orderedStudents)
                {
                    writer.WriteLine($"{s.FullName,-15} {s.Score,-4} Department: {s.Department}");
                }
                writer.WriteLine("----------------------------------------");

                writer.WriteLine("(Ex 5.) Average for all departments:");
                var averageByDept = studentList
                    .GroupBy(s => s.Department)
                    .Select(group => new
                    {
                        Department = group.Key,
                        AverageScore = group.Average(s => s.Score)
                    });

                foreach (var group in averageByDept)
                {
                    writer.WriteLine($"{group.Department,-18} {group.AverageScore:F2}");
                }
                writer.WriteLine("----------------------------------------");

                writer.WriteLine("(Ex 6.) Specific Query: Name, Faculty, Age, Grades:");
                var specificInfoQuery = studentList.Select(s => new { s.FullName, s.Department, s.Age, s.Score });
                foreach (var info in specificInfoQuery)
                {
                    writer.WriteLine($"Name: {info.FullName,-15} | Faculty: {info.Department,-18} | Age: {info.Age} | Grade: {info.Score}");
                }
            }

            Console.WriteLine($"SUCCESS: LINQ report has been successfully written to '{filePath}'!");
        }
    }
}