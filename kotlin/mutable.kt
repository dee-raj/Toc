// mutable collection 
fun main(){
    //list allows duplicate values
    var mlist= mutableListOf("Apple","banana","Orange") //mutableArrayOf()
    println(mlist)
    //changing the value of mlist at index 1
    mlist[1]="graps"
    println(mlist)
    //add new value to the list
    mlist.add("Apple")
    println(mlist)


    //set not allowed duplicate values
    var mset= mutableSetOf(6,10)
    mset.add(2)
    mset.add(6) //duplicate value may add but not be printed
    mset.add(9)
    print("\n\nMutable set")
    for (item in mset){
        println(item)
    }

    //map have 'key to value' pair
    val mmap=mutableMapOf<Int,String>(1 to " one", 2 to " two", 3 to " three")
    mmap.put(2," second") //duplicate key and diff value so the value will replce
    mmap.put(4," four")
    println("\n\nMutable map")
    for (key in mmap.keys){
        print(key)
        println(mmap[key])
    }
}