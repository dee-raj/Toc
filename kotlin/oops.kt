fun main(){
    //create a class
    class Car{
        var brand=""
        var year=0
    }
    //create an object 
    var c1=Car()
    c1.brand="Ford "
    c1.year=1975
    print(c1.brand)
    println(c1.year)

    //multiple object
    val c2=Car()
    c2.brand="BMW "
    c2.year=2000
    print(c2.brand)
    println(c2.year)

    // class Car(var brand3:String='', var year2:Int=0)

    // var c3=Car("tesla",2010)
    // println(c3)
}