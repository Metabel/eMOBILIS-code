
class Student {
    //properties
    var name:String=""
    var age: Int=0
    var course:String=""
    var studentid: String=""
    //a method
    fun displayinfo(){
        println("Student details:name $name,Age: $age,Course: $course,ID: $studentid")
    }

}
fun main(){
    //object is an instance of a class
    val student1=Student()
    //initializing properties of student object
    student1.name="Aggy"
    student1.age=22
    student1.course="MIT"
    student1.studentid="mt101"
    //call the function displayinfo
    student1.displayinfo()
    //create another object
    val student2=Student()
    student2.name="James"
    student2.age=18
    student2.course="AI"
    student2.studentid="mt102"
    student2.displayinfo()

}



