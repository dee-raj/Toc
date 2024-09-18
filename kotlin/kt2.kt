fun main() {
    var p= accept();
    p.myFun();
	p.myFun(21);
	p.call();	
    p.call();
	p.call();
}

open class Person(val name: String) {
    fun myFun(){
        println("hey! Mr. $name.")
    }
}
open class calling() : Person("dee-raj"){
    fun myFun(age:Int){
        println("You said... you are $age old.\n")
    }
}
class accept : calling() {
    var not:Int=1
	fun call(){
        println("this function is called at $not times.")
        not++;
    }
}