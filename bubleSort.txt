def createRandomArray = {size ->
  (0..<size).collect {
    (Math.floor(Math.random() * 10) + 1) as int
  }
}

def bubbleSort = {array ->
  (array.size()-1).times {
    ((array.size()-1)-it).times {
      array[it] < array[it+1] ?: Collections.swap(array, it,it+1)
    }
  }
  array
}

def array = createRandomArray(10)

println "start : ${array}"
def bk = array.clone()
def afterArray = bubbleSort(array)
println "end : ${afterArray}"
assert bk.sort() == afterArray