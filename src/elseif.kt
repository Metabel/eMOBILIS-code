fun main() {
    print("please enter your age")
    var age = readLine()?.toIntOrNull()
    if (age != null) {
        if (age < 13) {
            print("you are a child")
        } else if (age  < 18) {
            println("you are a teenager")
        } else if (age < 25) {
            print("you are a young adult")
        } else if (age < 59) {
            print("you are an adult")
        } else if(age <70){
            print("you are a senior citizen")
        }
        } else {
            println("enter a valid number")
        }
    println("enter your marks(0-100): ")
    val marks=readLine()?.toIntOrNull()
    if(marks!=null ){
        if(marks>=80){
            println("Grade A")
        }else if(marks >=70){
            println("Grade B")
        }else if(marks>=60){
            println("Grade C")

        }else if(marks>=50){
            println("Grade D")

        }
    }
}

//a program that asks user for marks and prints the results











