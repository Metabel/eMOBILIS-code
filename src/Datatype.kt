fun main(){
    //strings
    val course="Kotlin"
    var lname :String="Joy"
    println("I am learning " + course)
    println(lname)
    //numeric datatypes-int
    val age=20
    val marks: Int =57
    val mynum:Byte=120
    val mynewnum:Long=2333799988888655
    println(marks)
    println(mynum::class)
    println(mynewnum)
    //floating point double,float
    val tax=10.65
    val rate:Float=10.67f
    print("the tax rate is" +tax+ "and the tax rate is" +rate)
    //boolean:true or false
    val isstudent=true
    println(isstudent)
    //char:stores a single character
    val grade="A"
    println(grade::class)
    //type conversion
    val x:Float=10.65f
    val y=x.toInt()
    print(y)
}