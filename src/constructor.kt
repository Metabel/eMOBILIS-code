class Person (val name:String,val age:Int,val height:Int,val occupation:String){

        //function to display the persons info
        fun displayinfo(){
            println("Name:$name,Age:$age,occupation:$occupation")
        }
}
fun main(){
    //creating an object
    val person1=Person(name = "Mary", age = 22, height = 180, occupation = "Data Scientist")
    person1.displayinfo()

    val person2=Person(name = "Luke", age = 30, height = 180, occupation = "Lawyer")
    person2.displayinfo()
}
