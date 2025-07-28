fun main() {
    val courses= arrayOf("kotlin","css","python","html")
    println(courses.contentToString())
    println(courses[0])
    println(courses[2])
    courses[0]="Javascript"
    println(courses[0])
    println(courses.contentToString())
    //getting the array size
    println(courses.size)
    //looping through the array
    for (x in courses)
        println(x)
    //intarray
    val mynums=arrayOf(10,56,9,7,54,23,19)
    //accessing the elements
    println(mynums[1])
    for(mynum in mynums){
        println(mynum)
    }
    //array methods.sort()
    mynums.sort()
    println(mynums.contentToString())
    courses.forEach{ x ->
        println(x)
    }
    mynums.forEach{ num ->
        println(num)
    }
    //forEach Indexed
    val students=arrayOf("Luke","Mary","James",)
    students.forEachIndexed { index,y->
        println("index $index:$y")
    }
}