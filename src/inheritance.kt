open class Animal {
    fun eat(){
        println("The animal eats food")
    }
}
//child class
class Dog(val color:String, val breed: String,val age:Int):Animal(){
    //overriding the eat method
    override fun eat(){
        println("Dog is eating")
    }
    //method specific to dog
    fun bark(){
        println("the dog is$breed aged $age in colour $color")
    }
}
fun main(){
    //create an object dog
    val mydog=Dog("brown",  "german shephered",  4)
        //calling an inherited method from animal
    mydog.eat()
    //calling its own method
    mydog.bark()
    mydog.displayinfo()


}