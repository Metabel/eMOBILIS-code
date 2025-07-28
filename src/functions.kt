fun main() {
    //function is block of reusable code
    //that performs a specific task
    greet()
    greatuser("Jane")
    userinfo("Lucy",27)
    userinfo("Mark",21)
    val result=addtwonumbers(20,30)
    println(result)
    println(addtwonumbers(67, 34))

}

fun greet(){
    println("Hello Goodmorning")
}
//function with parameter
fun greatuser(name:String){
    println("hello, how are you $name")
}
//function with multiple parameters
fun userinfo(fname: String,age:Int){
    println("hello my name is $fname and I am $age years old")
}
fun addtwonumbers(x:Int,y:Int):Int{
    return x+y
}